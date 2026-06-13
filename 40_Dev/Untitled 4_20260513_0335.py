"""
Few-shot adaptation experiment.
Pre-trained GNR (LOSO) + fine-tune with K source from new subject.
Compare: Sphere, LOSO GNR, From-scratch, Pre-trained+fine-tune.
"""
import numpy as np, torch, torch.nn as nn, pickle, time, json, copy
from pathlib import Path
from sklearn.cluster import KMeans

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device: {DEVICE}")

HOME = Path.home()
DATA_DIR = HOME / "Hyeon/research/EEG/gnr_data"
RES_DIR  = HOME / "Hyeon/research/EEG/results"

subjects = sorted([f.stem for f in DATA_DIR.glob("sub-*.pkl")])
print(f"Subjects: {len(subjects)}")

def build_features(data):
    L_bem = data['L_bem']; L_sph = data['L_sph']
    src_rr = data['src_rr']; r0 = data['sphere_r0']; rad = data['sphere_rad']
    n_src, n_ch = data['n_src'], data['n_ch']
    L_bem_3d = L_bem.T.reshape(n_src, 3, n_ch)
    L_sph_3d = L_sph.T.reshape(n_src, 3, n_ch)
    r_s_rel = src_rr - r0
    r_s_norm = np.linalg.norm(r_s_rel, axis=1, keepdims=True)
    r_s_normalized = r_s_rel / rad
    X_list, Y_bem_list, Y_sph_list = [], [], []
    for d in range(3):
        feat = np.concatenate([r_s_normalized, np.tile(np.eye(3)[d], (n_src,1)),
                              r_s_norm/rad], axis=1)
        X_list.append(feat); Y_bem_list.append(L_bem_3d[:,d,:])
        Y_sph_list.append(L_sph_3d[:,d,:])
    return (np.concatenate(X_list, axis=0),
            np.concatenate(Y_bem_list, axis=0),
            np.concatenate(Y_sph_list, axis=0),
            src_rr, n_src)

print("\nLoading 14명...")
all_data = {}
for sub in subjects:
    with open(DATA_DIR / f"{sub}.pkl", 'rb') as f:
        d = pickle.load(f)
    X, Y_bem, Y_sph, src_rr, n_src = build_features(d)
    all_data[sub] = {'X': X, 'Y_bem': Y_bem, 'Y_sph': Y_sph,
                     'src_rr': src_rr, 'n_src': n_src}

class MLP(nn.Module):
    def __init__(self, in_dim=7, out_dim=74, hidden=256, depth=3):
        super().__init__()
        layers = [nn.Linear(in_dim, hidden), nn.SiLU()]
        for _ in range(depth-1):
            layers += [nn.Linear(hidden, hidden), nn.SiLU()]
        layers += [nn.Linear(hidden, out_dim)]
        self.net = nn.Sequential(*layers)
    def forward(self, x): return self.net(x)

def train_one(X_tr, Y_tr, X_va, Y_va, epochs=500, lr=1e-3, init_model=None):
    """Train MLP. If init_model given, fine-tune from it."""
    if init_model is None:
        model = MLP().to(DEVICE)
    else:
        model = copy.deepcopy(init_model).to(DEVICE)
    opt = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-5)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, epochs)
    Xt = torch.tensor(X_tr, dtype=torch.float32).to(DEVICE)
    Yt = torch.tensor(Y_tr, dtype=torch.float32).to(DEVICE)
    Xv = torch.tensor(X_va, dtype=torch.float32).to(DEVICE)
    Yv = torch.tensor(Y_va, dtype=torch.float32).to(DEVICE)
    best = 1e9; best_state = None
    for ep in range(epochs):
        model.train()
        loss = ((model(Xt) - Yt)**2).mean()
        opt.zero_grad(); loss.backward(); opt.step(); sched.step()
        if (ep+1) % 50 == 0:
            model.eval()
            with torch.no_grad():
                vl = ((model(Xv) - Yv)**2).mean().item()
            if vl < best:
                best = vl
                best_state = {k:v.cpu().clone() for k,v in model.state_dict().items()}
    if best_state: model.load_state_dict(best_state)
    return model

def eval_err(model, X, Y_bem, Y_sph_for_gnr=None):
    """If Y_sph given → GNR (sphere + residual). Else direct prediction."""
    model.eval()
    Xt = torch.tensor(X, dtype=torch.float32).to(DEVICE)
    with torch.no_grad():
        pred = model(Xt).cpu().numpy()
    if Y_sph_for_gnr is not None:
        pred = Y_sph_for_gnr + pred
    return np.linalg.norm(pred - Y_bem) / np.linalg.norm(Y_bem)

def spatial_k_select(src_rr, n_src, K, seed=0):
    """Select K source indices via k-means cluster centers, expand to all 3 orientations."""
    if K >= n_src: 
        src_idx = np.arange(n_src)
    else:
        # cluster sources, pick closest to each centroid
        km = KMeans(n_clusters=K, random_state=seed, n_init=3).fit(src_rr)
        # for each cluster center, pick closest source
        from scipy.spatial import cKDTree
        tree = cKDTree(src_rr)
        _, src_idx = tree.query(km.cluster_centers_, k=1)
        src_idx = np.unique(src_idx)  # remove duplicates if any
    # expand to (src, direction) indices
    idx_3d = np.concatenate([src_idx + d*n_src for d in range(3)])
    return idx_3d, src_idx

# === Main experiment ===
K_VALUES = [10, 50, 100, 200, 500, 1000, 2000]
TEST_SUBS = subjects  # 14명 모두

print(f"\nK values: {K_VALUES}")
print(f"Test subjects: {len(TEST_SUBS)}")
print(f"\n{'='*90}")

results = []
t_total = time.time()

for ti, test_sub in enumerate(TEST_SUBS):
    print(f"\n[{ti+1}/{len(TEST_SUBS)}] Test = {test_sub}")
    train_subs = [s for s in subjects if s != test_sub]
    
    # Pre-train GNR on 13 subs
    X_tr_all = np.concatenate([all_data[s]['X'] for s in train_subs], axis=0)
    Y_bem_tr_all = np.concatenate([all_data[s]['Y_bem'] for s in train_subs], axis=0)
    Y_sph_tr_all = np.concatenate([all_data[s]['Y_sph'] for s in train_subs], axis=0)
    res_tr_all = Y_bem_tr_all - Y_sph_tr_all
    
    X_te = all_data[test_sub]['X']
    Y_bem_te = all_data[test_sub]['Y_bem']
    Y_sph_te = all_data[test_sub]['Y_sph']
    src_rr = all_data[test_sub]['src_rr']
    n_src = all_data[test_sub]['n_src']
    
    print(f"  Pre-training LOSO GNR (13 subs)...", end=" ", flush=True)
    t0 = time.time()
    gnr_pretrained = train_one(X_tr_all, res_tr_all, X_te, Y_bem_te - Y_sph_te, epochs=500)
    print(f"{time.time()-t0:.1f}s")
    
    # K=0 baselines
    err_sphere = np.linalg.norm(Y_sph_te - Y_bem_te) / np.linalg.norm(Y_bem_te)
    err_loso = eval_err(gnr_pretrained, X_te, Y_bem_te, Y_sph_te)
    print(f"  Sphere: {err_sphere*100:.2f}%  |  LOSO GNR (K=0): {err_loso*100:.2f}%")
    
    sub_results = {
        'sub': test_sub,
        'sphere': float(err_sphere*100),
        'loso_gnr': float(err_loso*100),
        'K_values': K_VALUES,
        'from_scratch': [],
        'fine_tune': [],
    }
    
    print(f"  {'K':>5} | {'Scratch':>8} | {'Fine-tune':>10}")
    print(f"  {'-'*30}")
    for K in K_VALUES:
        adapt_idx_3d, _ = spatial_k_select(src_rr, n_src, K)
        # remaining for eval
        all_idx = np.arange(n_src*3)
        eval_idx = np.setdiff1d(all_idx, adapt_idx_3d)
        
        X_ad = X_te[adapt_idx_3d]
        res_ad = (Y_bem_te - Y_sph_te)[adapt_idx_3d]
        X_ev = X_te[eval_idx]
        Y_bem_ev = Y_bem_te[eval_idx]
        Y_sph_ev = Y_sph_te[eval_idx]
        res_ev = Y_bem_ev - Y_sph_ev
        
        # From-scratch GNR (on K source residuals)
        gnr_scratch = train_one(X_ad, res_ad, X_ev, res_ev, epochs=300)
        err_scratch = eval_err(gnr_scratch, X_ev, Y_bem_ev, Y_sph_ev)
        
        # Fine-tune from pre-trained
        gnr_ft = train_one(X_ad, res_ad, X_ev, res_ev, epochs=200, 
                          lr=1e-4, init_model=gnr_pretrained)
        err_ft = eval_err(gnr_ft, X_ev, Y_bem_ev, Y_sph_ev)
        
        print(f"  {K:>5} | {err_scratch*100:>7.2f}% | {err_ft*100:>9.2f}%")
        sub_results['from_scratch'].append(float(err_scratch*100))
        sub_results['fine_tune'].append(float(err_ft*100))
    
    results.append(sub_results)

print(f"\n총 시간: {(time.time()-t_total)/60:.1f}분")

# Aggregate
print("\n" + "="*90)
print("Few-shot adaptation: Mean over 14 subjects")
print("="*90)
sph_m = np.mean([r['sphere'] for r in results])
loso_m = np.mean([r['loso_gnr'] for r in results])
print(f"  Sphere only:         {sph_m:.2f}%")
print(f"  LOSO GNR (K=0):      {loso_m:.2f}%")
print()
print(f"  {'K':>5} | {'From-scratch':>14} | {'Fine-tune':>14} | {'Gap':>8}")
print(f"  {'-'*50}")
for i, K in enumerate(K_VALUES):
    sc_m = np.mean([r['from_scratch'][i] for r in results])
    ft_m = np.mean([r['fine_tune'][i] for r in results])
    print(f"  {K:>5} | {sc_m:>12.2f}% | {ft_m:>12.2f}% | {sc_m-ft_m:>7.2f}%")
print("="*90)

json.dump(results, open(RES_DIR / "few_shot_results.json", 'w'), indent=2)
print(f"\n저장: {RES_DIR / 'few_shot_results.json'}")
