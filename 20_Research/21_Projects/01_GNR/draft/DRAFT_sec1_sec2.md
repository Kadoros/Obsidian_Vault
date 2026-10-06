# §1 Introduction / §2 Related work — 본문 초안

> 포지셔닝: DeltaPhi 형태. 헤드라인은 §4(plug-and-play), §3 은 "몇 줄이면 붙는다",
> §3.5 는 "왜 잔차에 상한이 필요한가"(GP 진단 -> zero-init 스케일).

---

# §1 Introduction

Engineering models are almost never complete. A thermal model of a chip stack omits interface
resistance; a battery model omits a transport pathway; a thin-film design model treats every material
as having a single refractive index. Practitioners know these gaps exist, and they also know that
closing them by measurement or high-fidelity simulation is expensive — often tens of samples, not
thousands.

Operator learning is the natural tool for that setting, and it has a natural difficulty: with $n\le 50$
input–output pairs a neural operator must rediscover, from data, physics that is already written down.

This paper takes the obvious step and asks what it costs to take it well. **Compute the known physics in
closed form, and let the network learn only what the model is missing:**

$$\hat u \;=\; \underbrace{P(f)}_{\text{analytic, zero training}} \;+\; \underbrace{M_\theta(f)(x)}_{\text{base model, trained on the residual}} .$$

Nothing about $M_\theta$ changes — not its architecture, its size, its optimiser, or its budget. Only its
target moves from $u$ to $u-P(f)$. That makes the construction genuinely plug-and-play, and it is why we
can report it against five different base models rather than one.

**Contributions.**

1. **It attaches to anything, and it always helps.** Across seven benchmarks spanning 1D to 3D and a
   stack built from *measured* optical constants, training any of five base models (DeepONet,
   POD-DeepONet, FNO, GNOT-Lite, a Matérn GP) on the analytic residual beats training it directly —
   **35 of 35 cells, none negative**, mean gains +73/+65/+66/+70/+62 % (§4).

2. **Why the prior must be analytic, measured.** A prior's own error becomes a floor that the residual
   removes only about a fifth of. A *learned* prior retains 16.0 % / 8.9 % self-error even with 200
   auxiliary simulations and loses 1.3–2.5$\times$; a *coarse solver* pays $O(h^2)$ and loses
   4.5–27.6$\times$, while in 3D the analytic route is simultaneously 27.6$\times$ more accurate and
   29$\times$ faster (§5).

3. **A trained residual is unsafe on an accurate prior, and one parameter fixes it.** Where the prior is
   already near-exact the residual does not sit at zero — it overshoots by up to 107$\times$ and turns a
   $0.0009$ error into $0.110$. A GP in the same slot never does this, because its posterior mean is a
   linear smoother bounded by its training targets. Giving the network the same bound — a single
   zero-initialised scale on the residual head, no loss term, no hyper-parameter — reduces the cells
   where the prior alone would have been better from **21/45 to 7/35**, clearing every benchmark whose
   model is genuinely incomplete, at no cost in accuracy (§3.5, §4.4).

4. **A map of where this works.** Closed-form priors exist for far more than textbook geometries — one
   spectral multiplier per operator, a basis swap per domain, a transfer matrix for layered media that
   extends to 3D by reuse — and we report the boundary as carefully as the successes: turbulence sits
   outside the convergence radius of any perturbative prior, and we show where that boundary falls
   (§3.3, §6, §8).

---

# §2 Related work

**Residual and delta learning for operators.** The closest work in shape is DeltaPhi [NeurIPS 2025],
which trains
neural operators on residuals formed *between training samples* and reports consistent gains across
architectures. We share the architecture-agnostic framing and the four-column protocol, and differ in
what supplies the reference: theirs is assembled from data, so it requires offline pairs and inherits
their error, while ours is computed in closed form, requires none, and is exact for the physics it
encodes. §5 turns that difference into a measurement rather than an argument.

**Physics-guided correction.** A second family learns *both* the reference and the correction as neural
operators. In the low-data regime this spends scarce data twice, and the reference's residual
approximation error is not removed by the correction — we measure 16.0 % and 8.9 % of it surviving into
the final answer.

**Coarse-solver correction.** A third family uses a cheap numerical solve as the reference. This shares
our "do not learn the known physics" instinct and differs in the error it carries: discretisation.
On smooth problems the two are indistinguishable, which we state plainly; on layered, discontinuous or
three-dimensional problems a coarse grid cannot be both cheap and accurate, and that is exactly where
the analytic route separates.

**Differentiable simulation and hybrid calibration.** Learning parameters inside a differentiable
physical model is an established area, and our §7 (correcting in parameter space rather than output
space) lives next to it. Three things differ: the goal is low-data operator learning rather than the
parameters themselves; the choice of *where* to place the correction is made automatically rather than
by the modeller; and a closed-form prior makes the derivative free and the parameter count small enough
to work at $n=10$. We also chart where parameter-space correction fails, which that literature has
little reason to do.

**Gaussian processes and kernel methods.** GPs remain strong baselines at this data scale, and we
include one as a base model throughout. §3.5 uses it as more than a baseline: the fact that a GP residual
never harms an accurate prior, while every network does, is what identifies the missing property and
motivates the fix.

**Zero-initialised residual branches.** The mechanism we adopt — scaling a residual branch by a learnable
parameter initialised at zero — is the ReZero [Bachlechner et al., UAI 2021] / LayerScale
[Touvron et al., ICCV 2021] construction, also used to graft adapters onto frozen backbones
[Zhang et al., ICCV 2023]. Our contribution is not the construction but the diagnosis: hybrid
physics-plus-residual models have a specific failure mode when the physics is nearly right, and this is
what removes it.

> **인용 확인 필요 (내부 메모)**: DeltaPhi 는 팀 메일에서 NeurIPS 2025 로 언급됨 — 제출 전 arXiv
> 번호와 정확한 서지 확인할 것. ReZero(arXiv:2003.04887), LayerScale(arXiv:2103.17239),
> ControlNet(arXiv:2302.05543) 도 최종본에서 대조할 것. physics-guided correction 은
> 2606.03469 로 저장소 노트에 기록돼 있으나 서지 미확인.
