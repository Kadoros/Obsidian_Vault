#!/usr/bin/env python3
"""
TCO controlled ablation — change ONE thing in DeepONet: the branch.

All models learn the evolution operator  u -> u_t  (sensor grid in, field out):
    u_t(y) = sum_k b_k * t_k(y)        trunk t_k: SAME network, QR-orthonormalised
    loss   = ||u_t - b Phi^T||^2 + ||u - c Phi^T||^2   (same for every model)
Only the branch (how the coefficients b are produced) differs:
    deeponet  : b = MLP(sensor values u)                      (vanilla DeepONet)
    coeffmlp  : b = MLP(c),  c = <u, Phi>                     (same input coordinates as tensor)
    tensor    : b = A c + T(c, c)                             (TCO: 3rd-order tensor, nothing else)
Same data, trunk, loss, optimiser, steps, seeds.

Evaluation for EVERY model, identically:
  accuracy   test error of u_t, short-horizon rollout error, spectrum error (grid, RK4)
  physics    the model's generator is mapped to real Fourier coordinates and its Taylor
             coefficients at 0 are extracted (Richardson finite differences): linear part A
             and quadratic tensor T. These are compared with the exact Galerkin truth
             (T_rel_err, on selection rule, selection mass) — for the MLP branches this is the
             "implied tensor" of a black-box operator.
             Also: constant term f(0) (truth: 0) and purity of the eigenbasis of A.

Needs tco_pde.py, tco_pod.py, tco_trunk.py in the same folder; torch (GPU if available).
  python tco_ablation.py --pde burgers --quick --out runs/AB_smoke
"""
import argparse
import json
import os
import time

import numpy as np
import torch

from tco_pde import PDE, Blocks, model_rhs, DEFAULTS
from tco_pod import simulate_grid, real_fourier_basis, extract_linear_quadratic, b_to_z, z_to_b, pod_basis
from tco_trunk import Trunk

SURFACE, INK, INK2 = "#fcfcfb", "#0b0b0b", "#52514e"
SEQ = ["#fcfcfb", "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]


class MLP(torch.nn.Module):
    def __init__(self, d_in, d_out, width, depth):
        super().__init__()
        layers, d = [], d_in
        for _ in range(depth):
            layers += [torch.nn.Linear(d, width), torch.nn.Tanh()]; d = width
        layers += [torch.nn.Linear(d, d_out)]
        self.net = torch.nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x)


class Model(torch.nn.Module):
    def __init__(self, kind, n_grid, r, width, depth, Phi_fixed=None, stats=None):
        super().__init__()
        self.kind, self.n, self.r = kind, n_grid, r
        self.fixed = Phi_fixed is not None
        if self.fixed:
            self.register_buffer("Phi_f", torch.tensor(Phi_fixed))
        else:
            self.trunk = Trunk(r, width, depth)
        # standardisation (same recipe for every model): branch sees c / sc, predicts b / sb;
        # deeponet's sensor input is standardised with a global mean / std
        st = stats or {"sc": np.ones(r), "sb": np.ones(r), "um": 0.0, "us": 1.0}
        self.register_buffer("sc", torch.tensor(st["sc"])); self.register_buffer("sb", torch.tensor(st["sb"]))
        self.um, self.us = float(st["um"]), float(st["us"])
        self.register_buffer("x", torch.linspace(0, 2 * np.pi, n_grid + 1, dtype=torch.float64)[:-1])
        P, Q = np.triu_indices(r)
        self.register_buffer("P", torch.tensor(P)); self.register_buffer("Q", torch.tensor(Q))
        if kind == "deeponet":
            self.branch = MLP(n_grid, r, width, depth)
        elif kind == "coeffmlp":
            self.branch = MLP(r, r, width, depth)
        elif kind == "tensor":
            self.A = torch.nn.Parameter(1e-3 * torch.randn(r, r, dtype=torch.float64))
            self.T = torch.nn.Parameter(torch.zeros(r, P.size, dtype=torch.float64))
        else:
            raise ValueError(kind)

    def basis(self):
        if self.fixed:
            return self.Phi_f
        Qm, _ = torch.linalg.qr(self.trunk(self.x))
        return Qm * np.sqrt(self.n)

    def coeff_map_std(self, c, Phi, U=None):
        """standardised branch output b / sb as a function of trunk coordinates c."""
        if self.kind == "deeponet":
            Uin = c @ Phi.T if U is None else U
            return self.branch((Uin - self.um) / self.us)
        cs = c / self.sc
        if self.kind == "coeffmlp":
            return self.branch(cs)
        return cs @ self.A.T + (cs[:, self.P] * cs[:, self.Q]) @ self.T.T

    def coeff_map(self, c, Phi):
        """b = g(c) in physical units (used for evaluation / implied tensor)."""
        return self.coeff_map_std(c, Phi) * self.sb

    def forward(self, U, return_std=False):
        Phi = self.basis()
        c = U @ Phi / self.n
        bs = self.coeff_map_std(c, Phi, U)
        if return_std:
            return bs, c
        return (bs * self.sb) @ Phi.T, c @ Phi.T


def train(model, U, Ut, steps, lr, batch, device, log, tag):
    U_, Ut_ = torch.tensor(U, device=device), torch.tensor(Ut, device=device)
    su, st = (U_ ** 2).mean(), (Ut_ ** 2).mean()
    opt = torch.optim.Adam(model.parameters(), lr=lr)
    sch = torch.optim.lr_scheduler.CosineAnnealingLR(opt, steps)
    g = torch.Generator(device="cpu").manual_seed(0)
    for t in range(steps):
        idx = torch.randint(0, U_.shape[0], (min(batch, U_.shape[0]),), generator=g).to(device)
        if model.fixed:   # same field-space loss for every model; basis is fixed
            pt, _ = model(U_[idx])
            loss = ((pt - Ut_[idx]) ** 2).mean() / st
            opt.zero_grad(); loss.backward(); opt.step(); sch.step()
            if t % max(1, steps // 5) == 0 or t == steps - 1:
                log(f"    [{tag}] step {t}: field loss {loss.item():.3e}")
            continue
        pt, pu = model(U_[idx])
        lt, lu = ((pt - Ut_[idx]) ** 2).mean() / st, ((pu - U_[idx]) ** 2).mean() / su
        loss = lt + lu
        opt.zero_grad(); loss.backward(); opt.step(); sch.step()
        if t % max(1, steps // 5) == 0 or t == steps - 1:
            log(f"    [{tag}] step {t}: dyn {lt.item():.3e}  recon {lu.item():.3e}")


def fit_tensor_lstsq(model, U, Ut):
    """Exact minimiser of the same field loss for the tensor branch on a fixed orthonormal
    basis (it is linear in A, T). Standardisation is switched off for this model."""
    Phi = model.Phi_f.cpu().numpy()
    n = model.n
    C, D = U @ Phi / n, Ut @ Phi / n
    P, Q = np.triu_indices(model.r)
    X = np.concatenate([C, C[:, P] * C[:, Q]], 1)
    sc = np.sqrt((X ** 2).mean(0)) + 1e-14
    W = np.linalg.lstsq(X / sc, D, rcond=1e-12)[0] / sc[:, None]
    with torch.no_grad():
        model.sc.fill_(1.0); model.sb.fill_(1.0)
        model.A.copy_(torch.tensor(W[:model.r].T)); model.T.copy_(torch.tensor(W[model.r:].T))


def taylor_linear_quadratic(f, r, eps):
    """Linear part A and canonical quadratic T of a smooth vector field f at 0 (Richardson)."""
    I = np.eye(r)
    f0 = f(np.zeros((1, r)))[0]
    Lin = lambda e: (f(e * I) - f(-e * I)) / (2 * e)
    A = ((4 * Lin(eps / 2) - Lin(eps)) / 3).T
    def Qf(V, e):
        return (0.5 * (f(e * V) + f(-e * V)) - f0) / e ** 2
    Qr = lambda V: (4 * Qf(V, eps / 2) - Qf(V, eps)) / 3
    P, Q = np.triu_indices(r)
    single = Qr(I)
    pair = Qr(I[P] + I[Q]) - single[P] - single[Q]
    T = np.where((P == Q)[:, None], single[P], pair).T
    return A, T, f0


def eig_purity(A, R, n_grid):
    lam, V = np.linalg.eig(A)
    G = R @ V
    sp = np.abs(np.fft.fft(G, axis=0)) ** 2
    kk = np.minimum(np.arange(n_grid), n_grid - np.arange(n_grid))
    spk = np.array([sp[kk == j].sum(0) for j in range(n_grid // 2 + 1)])
    spk = spk / spk.sum(0, keepdims=True)
    return float(spk.max(0).mean())


def rollout_grid(model, U0, Uref, dt_save, n_sub, device):
    """Explicit RK4 in grid space with the learned u -> u_t; batch of trajectories."""
    with torch.no_grad():
        u = torch.tensor(U0, device=device)
        h = dt_save / n_sub
        out = [u.clone()]
        f = lambda v: model(v)[0]
        for _ in range(1, Uref.shape[1]):
            for _ in range(n_sub):
                k1 = f(u); k2 = f(u + h / 2 * k1); k3 = f(u + h / 2 * k2); k4 = f(u + h * k3)
                u = u + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
            out.append(u.clone())
        traj = torch.stack(out, 1).cpu().numpy()
    if not np.all(np.isfinite(traj)):
        return np.inf, np.inf
    nT = Uref.shape[1]
    t_s = max(1, (nT - 1) // 10)
    short = np.median(np.linalg.norm(traj[:, t_s] - Uref[:, t_s], axis=1) / np.linalg.norm(Uref[:, t_s], axis=1))
    sm = np.mean(np.abs(np.fft.rfft(traj[:, nT // 2:], axis=2)) ** 2, axis=(0, 1))
    sr = np.mean(np.abs(np.fft.rfft(Uref[:, nT // 2:], axis=2)) ** 2, axis=(0, 1))
    return float(short), float(np.linalg.norm(sm - sr) / np.linalg.norm(sr))


def fig_slices(T_tb, Ts, names, kl, r, out_mode, path, title):
    import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
    from matplotlib.colors import LinearSegmentedColormap
    cmap = LinearSegmentedColormap.from_list("seq", SEQ); cmap.set_bad(SURFACE)
    P, Q = np.triu_indices(r)
    def sl(T):
        S = np.full((r, r), np.nan)
        S[P, Q] = np.abs(T[out_mode])
        return S
    mats = [sl(T_tb)] + [sl(T) for T in Ts]
    vmax = np.nanmax(mats[0])
    fig, axes = plt.subplots(1, len(mats), figsize=(4.2 * len(mats), 4.2), facecolor=SURFACE)
    for ax, M, t in zip(axes, mats, ["True (Galerkin)"] + names):
        im = ax.imshow(M, cmap=cmap, vmin=0, vmax=vmax, origin="lower")
        ax.set_title(t, color=INK, fontsize=10)
        ax.set_xticks(range(r)); ax.set_xticklabels(kl, fontsize=6, color=INK2)
        ax.set_yticks(range(r)); ax.set_yticklabels(kl, fontsize=6, color=INK2)
        ax.set_xlabel("q (|k| of real Fourier mode)", color=INK2, fontsize=8)
        ax.set_ylabel("p", color=INK2, fontsize=8)
        for s in ax.spines.values():
            s.set_visible(False)
    cb = fig.colorbar(im, ax=axes, shrink=0.8); cb.outline.set_visible(False)
    cb.ax.tick_params(colors=INK2, labelsize=8)
    fig.suptitle(title, color=INK, fontsize=11, x=0.01, ha="left")
    fig.savefig(path, dpi=150, facecolor=SURFACE, bbox_inches="tight"); plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pde", choices=["burgers", "kdv", "fisher", "ks"], default="burgers")
    ap.add_argument("--param", type=float, default=None, help="default: 2nd value of the PDE's list")
    ap.add_argument("--regimes", nargs="+", default=["closed", "full"])
    ap.add_argument("--models", nargs="+", default=["deeponet", "coeffmlp", "tensor"])
    ap.add_argument("--tensor_solver", choices=["lstsq", "adam"], default="adam",
                    help="adam (default): tensor branch trained exactly like the MLPs (same optimiser, lr, steps). "
                         "lstsq: exact minimiser of the same loss (the branch is linear in its parameters), "
                         "a reference for what adam should reach")
    ap.add_argument("--trunk", choices=["pod", "joint"], default="pod",
                    help="pod: all models share the same fixed POD basis (isolates the branch); "
                         "joint: trunk network trained jointly (harder optimisation)")
    ap.add_argument("--K", type=int, default=8)
    ap.add_argument("--n_grid", type=int, default=64)
    ap.add_argument("--kmax_full", type=int, default=128)
    ap.add_argument("--n_traj", type=int, default=200)
    ap.add_argument("--n_test", type=int, default=20)
    ap.add_argument("--steps", type=int, default=None, help="default 20000 (quick: 800)")
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--batch", type=int, default=2048)
    ap.add_argument("--width", type=int, default=128)
    ap.add_argument("--depth", type=int, default=3)
    ap.add_argument("--seeds", type=int, nargs="+", default=[0, 1, 2])
    ap.add_argument("--n_sub", type=int, default=20, help="RK4 substeps per saved step in rollouts")
    ap.add_argument("--device", default="cuda" if torch.cuda.is_available() else "cpu")
    ap.add_argument("--quick", action="store_true")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    dp, dT, ddt, dsv, damp, dmean = DEFAULTS[a.pde]
    prm = a.param if a.param is not None else dp[min(1, len(dp) - 1)]
    t_final = dT
    if a.quick:
        # quick = code check only: 40 trajectories are too few for adam to pin down the tensor
        a.n_traj, a.n_test, a.kmax_full, a.seeds = 40, 6, 48, a.seeds[:1]
        a.steps = a.steps or 800
        t_final = dT / 4
    a.steps = a.steps or 20000
    torch.set_default_dtype(torch.float64)
    out = a.out or f"runs/AB_{a.pde}_{prm}_{a.trunk}"
    os.makedirs(out, exist_ok=True)
    logf = open(os.path.join(out, "log.txt"), "w")

    def log(*m):
        s = " ".join(str(x) for x in m); print(s, flush=True); logf.write(s + "\n")

    log("args:", json.dumps({**vars(a), "param": prm}))
    r = 2 * a.K + 1
    R, kl = real_fourier_basis(a.n_grid, a.K)
    blF = Blocks(a.K, 0, "none", False)
    pde = PDE(a.pde, prm)
    A_z, T_z, _ = blF.truth(pde)
    f_true_b = lambda B: z_to_b(model_rhs(b_to_z(B, a.K), None, {"A": A_z, "T": T_z, "C": np.zeros((r, 0)),
                                                                 "L": np.zeros((r, 0))}, blF), a.K)
    A_tb, T_tb, P, Q = extract_linear_quadratic(f_true_b, r)
    rule = np.zeros_like(T_tb, bool)
    for o in range(r):
        rule[o] = (kl[o] == kl[P] + kl[Q]) | (kl[o] == np.abs(kl[P] - kl[Q]))
    results = []
    for regime in a.regimes:
        ks = a.K if regime == "closed" else a.kmax_full
        sim = lambda n, seed: simulate_grid(pde, ks, a.n_grid, n, t_final, ddt, dsv, np.random.default_rng(seed),
                                            damp, dmean, a.K)
        U, Ut, _ = sim(a.n_traj, 0)
        Ute, Utte, tid = sim(a.n_test, 10_000)
        Uref = np.stack([Ute[tid == t] for t in np.unique(tid)])     # (n_test, nT, n_grid)
        c_scale = float(np.sqrt(np.mean((U @ R / a.n_grid) ** 2)))
        Phi_pod, _ = pod_basis(U, r)
        cP, dP = U @ Phi_pod / a.n_grid, Ut @ Phi_pod / a.n_grid
        stats = {"sc": cP.std(0) + 1e-12, "sb": dP.std(0) + 1e-12, "um": float(U.mean()), "us": float(U.std())}
        slices, names = [], []
        for kind in a.models:
            for seed in a.seeds:
                torch.manual_seed(seed)
                model = Model(kind, a.n_grid, r, a.width, a.depth,
                              Phi_fixed=Phi_pod if a.trunk == "pod" else None, stats=stats).to(a.device)
                t0 = time.time()
                if kind == "tensor" and a.trunk == "pod" and a.tensor_solver == "lstsq":
                    fit_tensor_lstsq(model, U, Ut)
                    log(f"    [{regime} tensor s{seed}] solved by least squares (exact minimiser of the field loss)")
                else:
                    train(model, U, Ut, a.steps, a.lr, a.batch, a.device, log, f"{regime} {kind} s{seed}")
                model.eval()
                with torch.no_grad():
                    Phi_t = model.basis()
                    pt, pu = model(torch.tensor(Ute, device=a.device))
                    Phi = Phi_t.cpu().numpy()
                dz = float(np.linalg.norm(pt.cpu().numpy() - Utte) / np.linalg.norm(Utte))
                rec = float(np.linalg.norm(pu.cpu().numpy() - Ute) / np.linalg.norm(Ute))
                Qm = R.T @ Phi / a.n_grid

                def g(C):
                    with torch.no_grad():
                        return model.coeff_map(torch.tensor(C, device=a.device), Phi_t).cpu().numpy()
                f = lambda BF: g(BF @ Qm) @ Qm.T
                A_l, T_l, f0 = taylor_linear_quadratic(f, r, 1e-2 * c_scale)
                absT = np.abs(T_l)
                short, spec = rollout_grid(model, Uref[:, 0], Uref, ddt * dsv, a.n_sub, a.device)
                m = {"T_rel_err": float(np.linalg.norm(T_l - T_tb) / np.linalg.norm(T_tb)),
                     "T_rel_err_on_rule": float(np.linalg.norm((T_l - T_tb)[rule]) / np.linalg.norm(T_tb[rule])),
                     "T_selection_mass": float(absT[rule].sum() / (absT.sum() + 1e-30)),
                     "A_rel_err": float(np.linalg.norm(A_l - A_tb) / np.linalg.norm(A_tb)),
                     "const_term_rel": float(np.linalg.norm(f0) / (np.linalg.norm(A_tb) * c_scale)),
                     "eig_purity_mean": eig_purity(A_l, R, a.n_grid),
                     "span_mismatch": float(np.linalg.norm(Qm.T @ Qm - np.eye(r)) / np.sqrt(r)),
                     "test_rel_err_dzdt": dz, "recon_rel_err_test": rec,
                     "rollout_short_rel_err_median": short, "spectrum_rel_err": spec,
                     "n_params": int(sum(p.numel() for p in model.parameters())),
                     "train_time_s": round(time.time() - t0, 1)}
                log(f"[{a.pde} p={prm} {regime:<6} {kind:<8} s{seed}] dz={dz:.2e} roll_short={short:.1e} spec={spec:.1e} | "
                    f"Trel={m['T_rel_err']:.2e} Trule={m['T_rel_err_on_rule']:.2e} Tsel={m['T_selection_mass']:.3f} "
                    f"Arel={m['A_rel_err']:.2e} f0={m['const_term_rel']:.1e} eig_purity={m['eig_purity_mean']:.3f} "
                    f"span={m['span_mismatch']:.1e} params={m['n_params']} ({m['train_time_s']}s)")
                results.append({"regime": regime, "model": kind, "seed": seed, "metrics": m})
                if seed == a.seeds[0]:
                    slices.append(T_l); names.append(kind)
        o = list(kl).index(3) if 3 in kl else 1
        fig_slices(T_tb, slices, names, kl, r, o, os.path.join(out, f"fig_implied_tensor_{regime}.png"),
                   f"{a.pde} (param={prm}, {regime}): implied quadratic tensor, output mode cos 3x")
    # summary table (mean over seeds)
    lines = ["| regime | model | dz | roll_short | T_rel_err | T_on_rule | T_sel_mass | A_rel_err | eig_purity |",
             "|---|---|---|---|---|---|---|---|---|"]
    for regime in a.regimes:
        for kind in a.models:
            ms = [x["metrics"] for x in results if x["regime"] == regime and x["model"] == kind]
            mean = lambda k: np.mean([m[k] for m in ms])
            lines.append(f"| {regime} | {kind} | {mean('test_rel_err_dzdt'):.2e} | {mean('rollout_short_rel_err_median'):.1e} | "
                         f"{mean('T_rel_err'):.2e} | {mean('T_rel_err_on_rule'):.2e} | {mean('T_selection_mass'):.3f} | "
                         f"{mean('A_rel_err'):.2e} | {mean('eig_purity_mean'):.3f} |")
    open(os.path.join(out, "summary.md"), "w").write("\n".join(lines) + "\n")
    log("\n".join(lines))
    with open(os.path.join(out, "results.json"), "w") as fjs:
        json.dump({"args": vars(a), "pde": a.pde, "param": prm, "results": results}, fjs, indent=2)
    log("saved to", out)


if __name__ == "__main__":
    main()
