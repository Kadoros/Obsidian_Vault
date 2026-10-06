"""
진짜 GNR LOSO: 13명 학습 → 1명 unseen 테스트.
Pure Neural vs GNR 비교 (cross-subject generalization).
"""
import numpy as np, torch, torch.nn as nn, pickle, time, json
from pathlib import Path

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Device: {DEVICE}")

HOME = Path.home()
DATA_DIR = HOME / "Hyeon/research/EEG/gnr_data"
RES_DIR  = HOME / "Hyeon/research/EEG/results"

# Load all subjects
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
            np.concatenate(Y_sph_list, axis=0))

print("\nLoading 14명...")
all_data = {}
for sub in subjects:
    with open(DATA_DIR / f"{sub}.pkl", 'rb') as f:
        d = pickle.load(f)
    X, Y_bem, Y_sph = build_features(d)
    all_data[sub] = {'X': X, 'Y_bem': Y_bem, 'Y_sph': Y_sph}
    print(f"  {sub}: X={X.shape}, Y={Y_bem.shape}")

class MLP(nn.Module):
    def __init__(self, in_dim, out_dim, hidden=256, depth=3):
        super().__init__()
        layers = [nn.Linear(in_dim, hidden), nn.SiLU()]
        for _ in range(depth-1):
            layers += [nn.Linear(hidden, hidden), nn.SiLU()]
        layers += [nn.Linear(hidden, out_dim)]
        self.net = nn.Sequential(*layers)
    def forward(self, x): return self.net(x)

def train_one(X_tr, Y_tr, X_va, Y_va, epochs=500, hidden=256, depth=3):
    model = MLP(X_tr.shape[1], Y_tr.shape[1], hidden, depth).to(DEVICE)
    opt = torch.optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-5)
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
        if (ep+1) % 100 == 0:
            model.eval()
            with torch.no_grad():
                vl = ((model(Xv) - Yv)**2).mean().item()
            if vl < best:
                best = vl
                best_state = {k:v.cpu().clone() for k,v in model.state_dict().items()}
    if best_state: model.load_state_dict(best_state)
    return model

# LOSO
results = []
print(f"\n[LOSO]")
print(f"{'test':10s} | {'Sphere%':>8} | {'Pure%':>8} | {'GNR%':>8} | {'Pure->GNR':>10}")
print("-"*60)
t_total = time.time()

for test_sub in subjects:
    train_subs = [s for s in subjects if s != test_sub]
    
    # Aggregate train data
    X_tr = np.concatenate([all_data[s]['X'] for s in train_subs], axis=0)
    Y_bem_tr = np.concatenate([all_data[s]['Y_bem'] for s in train_subs], axis=0)
    Y_sph_tr = np.concatenate([all_data[s]['Y_sph'] for s in train_subs], axis=0)
    
    X_te = all_data[test_sub]['X']
    Y_bem_te = all_data[test_sub]['Y_bem']
    Y_sph_te = all_data[test_sub]['Y_sph']
    
    # Sphere
    err_sph = np.linalg.norm(Y_sph_te - Y_bem_te) / np.linalg.norm(Y_bem_te)
    
    # Pure Neural
    m_pure = train_one(X_tr, Y_bem_tr, X_te, Y_bem_te)
    m_pure.eval()
    with torch.no_grad():
        pred = m_pure(torch.tensor(X_te, dtype=torch.float32).to(DEVICE)).cpu().numpy()
    err_pure = np.linalg.norm(pred - Y_bem_te) / np.linalg.norm(Y_bem_te)
    
    # GNR
    res_tr = Y_bem_tr - Y_sph_tr
    res_te = Y_bem_te - Y_sph_te
    m_gnr = train_one(X_tr, res_tr, X_te, res_te)
    m_gnr.eval()
    with torch.no_grad():
        pred_res = m_gnr(torch.tensor(X_te, dtype=torch.float32).to(DEVICE)).cpu().numpy()
    pred_full = Y_sph_te + pred_res
    err_gnr = np.linalg.norm(pred_full - Y_bem_te) / np.linalg.norm(Y_bem_te)
    
    ratio = err_pure / max(err_gnr, 1e-4)
    print(f"{test_sub:10s} | {err_sph*100:>7.2f}% | {err_pure*100:>7.2f}% | {err_gnr*100:>7.2f}% | {ratio:>9.2f}×")
    
    results.append({"sub": test_sub, "sphere": float(err_sph*100), 
                    "pure": float(err_pure*100), "gnr": float(err_gnr*100)})

print(f"\n총 시간: {(time.time()-t_total)/60:.1f}분")

sph_m  = np.mean([r['sphere'] for r in results])
pure_m = np.mean([r['pure']   for r in results])
gnr_m  = np.mean([r['gnr']    for r in results])
print("\n" + "="*60)
print(f"  LOSO Mean (N=14):")
print(f"  Sphere only:  {sph_m:.2f}%")
print(f"  Pure Neural:  {pure_m:.2f}%   ({sph_m/pure_m:.2f}× vs sphere)")
print(f"  GNR:          {gnr_m:.2f}%   ({sph_m/gnr_m:.2f}× vs sphere, {pure_m/gnr_m:.2f}× vs pure)")
print("="*60)

json.dump(results, open(RES_DIR / "loso_gnr_real.json", 'w'), indent=2)
print(f"\n저장: {RES_DIR / 'loso_gnr_real.json'}")
