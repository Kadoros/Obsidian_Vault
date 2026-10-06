# §6 Generality / §7 Correction space / §9 Conclusion / Appendix — 본문 초안

> §6 은 "직사각형 1D 장난감" 공격, §7 은 부차 기여(예측 진단 실패로 '방법'이 아닌 '관찰'),
> Appendix 는 §8-11(벤치 선정) 이 성립하려면 반드시 있어야 하는 부분.

---

# §6 Generality: geometry, dimension, and what it costs

## 6.1 A new domain is a new eigenpair, not new derivations

Tier-1 is a single formula, so moving to another domain means writing down its eigenpair and inner
product and nothing else. We verify this on three geometries with the same code path:

| domain | $(\phi_k,\lambda_k)$ | inner product | prior error | code |
|---|---|---|---|---|
| interval, Dirichlet | $\sin(k\pi x)$, $(k\pi)^2$ | $\int_0^1$ | $10^{-7}$ | — |
| **disk**, axisymmetric | $J_0(\alpha_k r)$, $\alpha_k^2$ | $\int_0^1 \cdot\,r\,dr$ | $1.5\times10^{-5}$ | 23 lines |
| **sphere**, radial | $\sin(k\pi r)/r$, $(k\pi)^2$ | $\int_0^1 \cdot\,r^2 dr$ | $3.8\times10^{-5}$ | 6 lines |

The sphere follows from the substitution $v=ru$, which turns the radial Laplacian into a
one-dimensional one — six lines, and the prior is exact to five digits. With missing physics added
(ambient loss $\mu=3$, matched to give the same $\approx0.54$ floor as the HBM stack), the residual
recovers it: at $n{=}50$ the disk goes $0.127\to0.075$ and the sphere $0.132\to0.079$ against the
direct model.

## 6.2 Layered media extend to 3D by reuse, not by rewriting

For a box that is layered in $z$, the transverse directions separate exactly, so
$u=\sum_{p,q}\hat u_{pq}(z)\sin(p\pi x)\sin(q\pi y)$ and each mode obeys a one-dimensional problem
with $\gamma=\pi\sqrt{p^2+q^2}$. Inside a layer the coefficient is constant, the homogeneous solutions
are $\cosh,\sinh$, and a polynomial source has a closed-form particular solution by recursion — so the
**1D transfer matrix routine is called once per mode** and nothing is re-derived.

The consequence is the strongest single number in the paper. Against converged truth, the analytic
prior is exact while a structure-aware coarse $z$-solver sits at $0.074$ and a plain 3D grid at
$0.340$; end-to-end at $n{=}50$ that is $6.0\times$ and $27.6\times$, and the analytic route costs
**2.4 ms per sample against 70.8 ms** — 29$\times$ faster and 27.6$\times$ more accurate at the same
time. Matching accuracy on a grid costs $N^3$; matching it in closed form costs one extra loop.

We verified the prior is exact rather than merely close: refining the FDM grid makes it converge *to*
the transfer-matrix solution at first order, which is what one expects when the latter is the limit.

## 6.3 Where it stops

The same section should say where the construction runs out, and §8 does so in full. In brief: Born
requires low contrast and diverges at $285\times$; the transfer matrix requires layering; and for
problems with no closed form the Tier-3 fallback is honest but inert.

---

# §7 Where to put the correction

*(Secondary contribution: we map the behaviour, we do not yet predict it.)*

## 7.1 Output space is not the only option

Everything so far corrects the *output*: $\hat u = P(f) + M_\theta(f)$. But a prior is a function of
physical parameters and of a source, and the model error need not live in the output. Two other
placements are available when the prior is analytic and therefore differentiable:

$$\underbrace{P(f)+M_\theta(f)}_{\text{output}} \qquad
\underbrace{\mathrm{Solve}\big(f;\ \theta_0+\delta\theta\big)}_{\text{parameter}} \qquad
\underbrace{\mathrm{Solve}\big(f+M_\theta(f)\big)}_{\text{inside the solver}}$$

The comparison is controlled: same network, same capacity, same budget; only the placement moves.

## 7.2 Placement is worth up to 10$\times$ at fixed capacity

- **Parameter space** wins when the error is a parameter error. On optics — where the prior uses one
  constant index per material and the truth uses measured dispersion — learning $\delta n_m(\lambda)$
  instead of a spectral correction gives $0.214\to0.061$, and on thermal benchmarks it reaches at
  $n{=}10$ what output-space needs $n\approx200$–$400$ to reach (**20–40$\times$ data efficiency**),
  because it fits two to six physical scalars rather than a network.
- **Inside the solver** wins when the missing physics is smooth: $0.211\to0.021$ on a missing reaction
  term and $0.302\to0.095$ on missing convection, purely from placement, because the solver imposes the
  boundary conditions and smoothness for free.

## 7.3 Two properties decide which, and we can measure both

**Subspace containment.** A parameter family spans only what its parameters generate. Fixed-region
$\delta k(x)$ cannot move a defect whose position follows the input, and it never beats the prior
($0.554\to0.544$); replacing it with a movable term — a sink centred on the observed source peak, two
scalars — gives $0.554\to0.075$. Fewer parameters, better result: what matters is the subspace, not the
count. On Navier–Stokes the same logic explains a failure: an eddy viscosity is real and diagonal, and
an oracle over that whole family removes only 24–30 % of the error, while allowing complex diagonal and
rank-8 mode coupling still reaches only 17 % — because the true correction is *nonlinear in the input*
(a superposition test violates by 44 %) and no linear family can express it.

**Conditioning.** Moving inward buys physical structure and costs invertibility. Source-space
placement fails on the localized defect (worse than output space) because recovering a sharp source
from smooth observations is a deconvolution; the learned correction never finds the sink (correlation
$+0.17$).

## 7.4 What we could not do

We tried to predict the best placement without training the candidates. An indicator built from the
observation operator correlates perfectly with the outcome along one dial (rank correlation $+1.00$
across defect width) but raises false alarms on a noise dial and finds no crossing at all on an
observation-density dial. With one crossing observed, no threshold can be validated. Selecting the
placement therefore still costs cross-validation, and we report the diagnosis rather than a method.

---

# §9 Conclusion

Given a physical model that is known to be incomplete and a data budget that will not support learning
it from scratch, computing the known physics in closed form and learning only the discrepancy improves
every base model we tried, on every benchmark we ran. The gains are not an artefact of the residual
formulation: a prior's own error becomes a floor the residual barely removes, which is why a learned
prior and a coarse solver both lose to an analytic one, by 1.3–2.5$\times$ and 4.5–27.6$\times$
respectively, and by more in three dimensions where a grid must pay $N^3$ for the accuracy a closed
form gives away.

The construction is also unsafe in a specific and fixable way. On an already-accurate prior a trained
residual overshoots rather than vanishing, by up to two orders of magnitude; a Gaussian process in the
same slot never does, because its posterior mean is bounded by its training targets. Giving a network
the same bound takes one zero-initialised scalar, no loss term and no hyper-parameter, and removes
almost all of the harm.

What remains open is where to put the correction. Placement is worth up to an order of magnitude at
fixed capacity and the best choice is problem-dependent in ways we can measure but not yet predict.
And the boundary of the whole approach is sharp: perturbative priors have a convergence radius, and
turbulence lies outside it.

---

# Appendix A — Benchmark selection

Several candidate scenarios were examined and excluded. We list them because averages over a
hand-picked benchmark set are otherwise uninterpretable, and because the exclusion criteria are the
same diagnostics used in the main text.

**Criterion 1 — the missing physics must be measurable.** A scenario is excluded if the prior's own
error is so small that no method could distinguish itself. Rejected: a weak nonlinear reaction with
floor $0.011$ at the source amplitudes used elsewhere (it enters the main table only after the
amplitude is raised to give floor $0.35$), and the composite-plasticity variant whose prior is
near-exact ($0.0003$).

**Criterion 2 — the prior must be a prior, not a broken model.** Excluded if the prior's error exceeds
order one, since the setting is then "no usable model" rather than "incomplete model". Rejected: the
convection-dominated case with a diffusion-only prior (floor $16.4$), and Born applied to a
$285\times$-contrast stack, where the perturbation series diverges outright ($44.9$, then $10^4$, then
$10^9$ with more terms).

**Criterion 3 — the baseline must be trainable.** Excluded if the direct model fails to fit its own
training data, since a comparison against a broken baseline is meaningless. Rejected: an early OOD
design drawing materials independently per layer, which gave a solution-magnitude spread of $137\times$
and a direct model with training error $0.89$ — worse than predicting the mean ($0.81$). The published
version restricts the material sequence, giving spread $24\times$ and a direct model at $0.52$, in line
with the $0.61$ reported for the same benchmark in the earlier version of this work.

**Criterion 4 — sweeps must be representative.** For the qualitative field figure, a source sweep is
used only if its prior floor matches that of the standard training distribution. Rejected on this test:
the localized-defect scenario, whose defect position is tied to the source peak and therefore jumps
discontinuously along a frequency sweep, and the averaged-stiffness composite, whose prior is an order
of magnitude smaller than the truth and reads as a blank panel.

**Not excluded, reported as failures.** Tier-3 Darcy (prior inert), 3D missing physics (no residual
placement helps), and long-horizon Navier–Stokes (prior collapses) are all in the paper. Excluding them
would have been the same operation as the above, and we did not.
