# §5 Why *analytic* / §8 Limitations — 본문 초안

> §4(plug-and-play)가 "붙으면 좋아진다"를 보였다면, §5 는 **"왜 하필 해석적 prior 인가"** 에 답한다.
> §8 은 리뷰어가 찾기 전에 우리가 먼저 쓴다. 수치는 T2 / 캐시에서 재생성.

---

# §5 Why the prior must be analytic

## 5.1 A prior's own error becomes a floor

Any hybrid of the form $\hat u = P(f) + M(f)$ inherits whatever $P$ gets wrong. Write the prior as
$P = P^\star + \varepsilon$, where $P^\star$ is exact for the known physics. The residual learner is then
trained on

$$u - P(f) \;=\; \underbrace{r}_{\text{missing physics}} \;-\; \underbrace{\varepsilon}_{\text{the prior's own error}},$$

so it must absorb **both**. One might hope the network simply learns $\varepsilon$ away. It does not.
Across our benchmarks the residual removes only about **20 %** of a prior's self-error; the rest survives
into the final answer. Concretely, moving the prior's grid from $n_g{=}80$ to $n_g{=}800$ cuts its own
error from 0.145 to 0.015 and cuts the *end-to-end* error from 0.178 to 0.045 at $n{=}5$ — the final
error tracks the prior's error, not the network's capacity.

This gives a single statement that explains every alternative at once:

> **The final error is bounded below by the prior's own error.** Choosing a prior is therefore choosing
> a floor, and an analytic prior is the only construction that sets that floor to zero at no cost.

## 5.2 The two alternatives, measured

**A learned prior** (the physics-guided-correction family) approximates the known physics with a network.
Trained generously — 200 cheap auxiliary simulations, more than the 10–50 high-fidelity pairs the task
allows — it still retains **16.0 %** self-error on the layered-conductivity case and **8.9 %** on the
battery case. Its correction must then absorb the genuine discrepancy *and* that residue, and it loses
**1.3–2.5$\times$** end-to-end.

**A coarse solver** (the coarse-solver-correction family) has a physical parameterisation but pays
$O(h^2)$ discretisation error. On a layered stack against converged truth, the transfer matrix is exact
while coarse FDM sits at 0.149 ($n_g{=}80$) and 0.053 ($n_g{=}200$), and loses **12.4$\times$** and
**4.5$\times$** end-to-end. The gap is not a fair-setup artefact: both priors receive the same
coefficient field, and the analytic one wins because it has no grid.

**In 3D the gap compounds.** Matching accuracy on a grid costs $N^3$, so at $n{=}50$ our transfer-matrix
prior beats a structure-aware coarse solver 6.0$\times$, and a plain 3D grid **27.6$\times$ while running
29$\times$ faster** (2.4 ms vs 70.8 ms per sample). The analytic route is simultaneously cheaper and more
accurate, which is unusual enough to be worth stating plainly.

> **Table 2** collects these. **Table 8** answers the natural follow-up — what it costs to obtain such a
> prior for a new problem.

## 5.3 What this does *not* claim

On smooth benchmarks a coarse FDM prior is already accurate enough that its floor sits far below what the
residual can achieve at $n\le 50$, and there the two are indistinguishable (D.17 in the earlier version of
this work). The advantage appears exactly when a coarse grid cannot resolve the physics — discontinuous
coefficients, layering, multiscale structure, 3D — which is also where a grid stops being cheap. We state
the decision rule directly:

> **A prior's form matters only when its self-error is not small compared with the residual error
> achievable at that data budget.** Otherwise the gate will find no difference, and neither will you.

---

# §8 Limitations

We state these up front because several of them are the boundary of the contribution rather than
incidental weaknesses.

1. **Applicability requires four things** of the prior: it must output a field on the target domain, be
   much cheaper than the truth, be non-learned, and have small self-error. The first excludes lumped
   (0-D) engineering models — thermal resistance networks, equivalent circuits — which do not produce a
   field without a lifting step.

2. **Turbulence and Navier–Stokes at long horizons are out of scope.** Dropping the nonlinear term gives
   a closed-form Stokes/diffusion prior, so a prior *exists*; what fails is its usefulness. On steady 2D
   NS the perturbative prior degrades as the nonlinear-to-viscous ratio grows (0.074 at 0.06, 0.402 at
   0.35) and the series **diverges** near ratio 1. On time-dependent 2D NS the prior improves FNO
   1.80$\times$ at $T{=}0.25$ but 0.99$\times$ at $T{=}1.0$, at both 32$^2$ and 64$^2$. This is the same
   failure as Born diverging on a 285$\times$-contrast stack — both are Neumann series with a convergence
   radius — and standard NS benchmarks use horizons well beyond it.

3. **On smooth problems we tie with a coarse solver** (§5.3).

4. **Tier-3 contributes nothing.** With no closed form, the mean-field prior leaves FNO within $\pm2.5\%$
   of running alone. We report it as a graceful fallback, not as a gain.

5. **Born is low-contrast only**; the transfer matrix is **layered only**. High-contrast non-layered media
   have neither.

6. **The learned residual does not scale.** When the configuration itself varies widely the correction
   becomes configuration-dependent and output-space residual learning fails at $n{=}50$ *and* $n{=}200$;
   an FNO residual recovers about 10 % of it and then saturates. In 3D no residual placement helps at all
   — every base model sits at the prior's floor and the gate declines all five. The prior scales to 3D;
   the learned part does not, at this data budget.

7. **Most of our missing physics is synthetic.** The optical benchmark is the exception: its ground truth
   uses measured dispersion and absorption, and the prior is the constant-index model engineers actually
   use. We could not find a public benchmark of *measured* multilayer spectra — this field's ML work is
   itself largely simulated — so a fully measured input–output benchmark remains open.

8. **The gate must train its candidates.** We tried to predict the best correction space from cheap
   diagnostics and failed: an indicator that correlated perfectly on one dial (rank correlation $+1.00$
   against the defect width) raised false alarms on a noise dial, and no crossing appeared on an
   observation-density dial at all. Selecting the space still costs cross-validation.

9. **Correction-space results are exploratory.** Parameter-space correction gives 20–40$\times$ data
   efficiency where the error lies in the parameters, and placing the network inside the solver gives
   2.7–10$\times$ where the missing physics is smooth — but the same placement is *worse* where recovering
   the correction is an ill-posed deconvolution. We map the behaviour; we do not yet predict it (§8.8).

10. **Benchmarks remain modest in scale** relative to the operator-learning literature: nine benchmarks
    spanning 1D–3D, with $n\le 50$ by design, at resolutions up to $64^2$ (time-dependent NS) and $12^3$
    (Darcy).

11. **Degenerate benchmarks were excluded** rather than reported: several candidate scenarios had priors
    that were near-exact or missing physics too weak to measure, and including them would have inflated
    the averages. Selection criteria are in the appendix.

---

## 내부 메모

- §5.1 의 "약 20%" 는 coarse FDM 두 격자(ng=80: .149→.116, ng=200: .053→.042)에서 나온 값.
  본문에 쓸 때 **어느 실험에서 나온 수치인지 각주**를 달 것.
- §8.2 의 NS 수치는 `bench_navier_stokes.json`(정상) + `bench_ns_time_{A,B,C}.json`(시간발달).
  T=0.5, 2.0 은 **미측정**이므로 "0.25 와 1.0 에서" 로만 쓸 것.
- §8.11 은 정직하지만 **appendix 에 실제 선정기준을 써야** 성립한다. 아직 안 썼음.
- §5.2 의 "both priors receive the same coefficient field" 는 `bench_analytic_vs_fdm.py` 셋업 사실.
  리뷰어 mDio 의 'unfair setup' 지적에 대한 직접 답이므로 문장을 지우지 말 것.
