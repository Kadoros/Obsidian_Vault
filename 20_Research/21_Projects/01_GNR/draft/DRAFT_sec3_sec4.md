# §3 Method / §4 Plug-and-play — 본문 초안

> 포지셔닝: DeltaPhi 형태. §4 가 헤드라인, §3 은 "누구나 붙일 수 있다"를 증명하는 뒷받침.
> 모든 수치는 `make_iclr_tables.py` 가 캐시에서 재생성. (T1/T4/T8)

---

# §3 Method: an analytic prior you can attach in a few lines

## 3.1 Setup

We are given a physical model that is **known to be incomplete**. Write the true operator as

$$\mathcal A_{\text{true}} \;=\; \underbrace{\mathcal A_0}_{\text{known physics}} \;+\; \underbrace{\Delta\mathcal A}_{\text{unmodelled}},$$

and assume high-fidelity data is expensive, so only $n \lesssim 50$ input–output pairs are available.
A base operator learner $M$ (DeepONet, FNO, GNOT, POD-DON, a GP, …) is trained on those pairs.

Our proposal is one line:

$$\hat u \;=\; \underbrace{P(f)}_{\text{analytic prior, zero training}} \;+\; \underbrace{M(f)(x)}_{\text{base model, trained on the residual}} .$$

$P$ solves $\mathcal A_0$ **in closed form**. The base model is unchanged; only its target changes from
$u$ to $u - P(f)$. Nothing else in the pipeline moves, which is what makes this plug-and-play.

## 3.2 The prior is always two steps

**(i) Lift.** Sensor values $\mathbf f_s\in\mathbb R^{m}$ become a continuous function by least squares in a
Chebyshev basis (degree $\min(m{-}1,8)$). This step is numerical hygiene, not a contribution: the fitted
polynomial is basis-independent, and Chebyshev is used only because its design matrix has condition
number $O(10)$ against $O(10^6)$ for the monomial basis at $m{=}11$, $d{=}8$.

**(ii) Apply $\mathcal A_0^{-1}$ in closed form.** This is the physics, and it takes one of three routes.

## 3.3 Three routes, and what each costs to write

**Tier 1 — separable / constant coefficient.** If the eigenpairs $(\phi_k,\lambda_k)$ of $\mathcal A_0$ on the
domain are known, the solution is a single formula

$$u \;=\; \sum_k \frac{\langle \hat f,\phi_k\rangle}{\|\phi_k\|^2}\; g(\lambda_k)\;\phi_k ,$$

and **the only thing a new PDE contributes is the spectral multiplier $g$**: $1/\lambda$ for Poisson,
$e^{-\lambda t}$ for heat at time $t$, $1/(\lambda-\kappa^2)$ for Helmholtz. Changing the *domain* changes
only the eigenpair and the inner-product weight — the surrounding code is untouched.

**Tier 2 — variable coefficient, layered, or weakly nonlinear.** Three short templates: a Born/Neumann
series (split $a = a_0 + \delta a$ and iterate against the constant-coefficient inverse), a fixed-point
iteration for weak nonlinearity, and a **transfer matrix** for layered media. The last is the important
one for engineering: inside each layer the coefficient is constant, so the solution is closed-form, and
matching displacement and flux at the interfaces determines the constants from a $2L\times 2L$ system
whose size is the **number of layers, not the number of grid points**. There is no spatial
discretisation, hence no $O(h^2)$ error, at any contrast.

**Tier 3 — no closed form.** Fall back to a mean-field/homogenised prior and let the operator learner do
the work. We report this route as inert (§8): it costs nothing and buys nothing.

> **Table 8** gives the measured cost of each route. Tier 1 is one line; swapping to a sphere is 6 lines
> and to a disk 23; the layered transfer matrix is 18 lines and extends to 3D by reusing the same routine
> per transverse Fourier mode; Born and the nonlinear fixed point are 18 and 10 lines. Verified prior
> errors range from $10^{-7}$ to exact.

## 3.4 Training

Only the target changes. Writing $M_\theta$ for the base model,

$$\text{Direct:}\quad \min_\theta\ \mathcal L\big(M_\theta(f)(x),\ u\big)
\qquad\longrightarrow\qquad
\text{+Prior:}\quad \min_\theta\ \mathcal L\big(M_\theta(f)(x),\ u - P(f)\big),$$

with $P$ treated as a constant (no gradient flows into it) and the prediction reassembled as
$\hat u = P(f) + M_\theta(f)(x)$. Optimiser, schedule, epochs, sensors, query points and seeds are
identical between the two columns; nothing but the target moves, which is what lets the prior attach to
an unmodified architecture.

We use a sample-wise relative $L_2$ loss,
$\mathcal L = \frac1n\sum_b \lVert \hat u_b - u_b\rVert^2 / \lVert u_b\rVert^2$, throughout.
Plain MSE is unusable on benchmarks whose solution magnitude varies by two orders across samples — a
layered stack with randomly drawn materials spans $130\times$ — where it lets the largest samples
dominate and the direct baseline fails to fit even its training set.

## 3.5 Why the residual needs a bound, and how to give it one

A prior that is already accurate leaves nothing to learn, and there a trained residual does not sit
quietly at zero: it *amplifies*. Measuring the size of the predicted residual against the true one,
a DeepONet overshoots by **107$\times$** on clean Poisson and **9.7$\times$** on the weak nonlinearity,
which turns a prior error of $0.0009$ into a combined error of $0.110$.

A GP in the same slot does not do this — not because it learns better, but because its posterior mean
$k(x_*,X)[K+\sigma^2 I]^{-1}\mathbf y$ is a linear smoother over the observed training residuals, so its
output magnitude is tied to theirs and cannot blow up. A network carries no such bound.

We give the network the same property with one parameter:

$$\hat u \;=\; P(f) \;+\; a\cdot M_\theta(f)(x), \qquad a\in\mathbb R,\quad a_{\text{init}} = 0 .$$

No term is added to the loss and no hyper-parameter is introduced. The gradient
$\partial\mathcal L/\partial a \propto \langle M_\theta(f),\, r\rangle$ is the correlation between the
head's output and the true residual, so $a$ stays near zero when the residual is noise and grows when
there is signal — the model decides for itself how much correction to apply, continuously rather than
by a binary switch. (This is the ReZero/LayerScale construction; the contribution here is the diagnosis
that hybrid prior–residual models need it, and the measurement that it suffices.)

---

# §4 The prior attaches to any base model

## 4.1 Protocol

For every (benchmark, base model) pair we report four columns under one recipe:

| column | meaning |
|---|---|
| **Direct** | base model trained on $u$, no prior |
| **+Prior** | **the same base model, same size, same budget**, trained on $u - P(f)$ |
| Prior-only | $P$ alone, zero training (reference) |
| +Prior (gated) | the CV gate additionally decides whether to keep the residual |

The headline comparison is **Direct vs +Prior**, and both train the base model — only the target
changes from $u$ to $u-P(f)$. This is the same comparison DeltaPhi reports, and it is the fair one:
neither column is allowed to discard the network.

Everything except the presence of the prior is held fixed: same sensors, same query points, same
epochs, same optimiser, same seeds. Five base models — DeepONet, POD-DON, FNO, GNOT-Lite, a
Matérn-5/2 GP — and eight benchmarks spanning 1D, 2D, variable coefficients, and **measured material
data**.

## 4.2 Main result

> **Table 1.** At $n{=}50$, training on the analytic residual beats training directly for *every* base
> model on *every* benchmark — **35 of 35 cells positive, none negative** — with mean gains of
> **+73 % (DeepONet), +65 % (POD-DON), +66 % (FNO), +70 % (GNOT), +62 % (GP)**.

Two features matter more than the headline number. First, the gains are **architecture-agnostic**: no
base model is favoured, which is what one expects if the prior is supplying physics rather than
compensating for a particular inductive bias. Second, they persist on the benchmark whose missing
physics is *not* synthetic — an optical thin-film stack where the ground truth uses measured dispersion
and absorption from a public database and the prior is the constant-index model an engineer actually
starts from.

## 4.3 The combination is not always the right answer

Table 1 also carries a prior-only column, and it is not decoration. In **7 of the 35 cells** the prior
*by itself* is still better than the prior plus a trained residual (marked $\dagger$) — down from
21 of 45 before the bounded head of §3.5. What remains is concentrated rather than scattered:

- **Four of the seven are the 3D stack**, where no residual placement helps at all — a limitation we
  report separately (§8): the analytic prior extends to three dimensions but the learned part does not
  at this data budget.
- Two are ties at a floor of $0.0009$ on clean Poisson, where there is nothing left to learn and the
  difference is in the fourth decimal.
- Where the model is genuinely incomplete — HBM ($0.540$), the battery ($0.501$), the weak
  nonlinearity, the convection layer — **no cell is daggered**: the combination wins outright.
- One base model is the exception: **the GP residual never hurts**, beating prior-only on all nine
  benchmarks. The reason is not that the GP learns better — it is that it cannot overshoot. Measuring
  the size of each predicted residual against the true one, both a GP and a DeepONet are accurate when
  the missing physics is real (ratios $0.98$ and $0.93$ on HBM). When the prior is already near-exact
  and there is nothing to learn, the GP stays bounded ($0.73$ on clean Poisson, $0.54$ on the weak
  nonlinearity) while the DeepONet predicts a residual **107$\times$** and **9.7$\times$ too large.
  A GP posterior mean is a linear smoother over observed training residuals, so its magnitude is tied
  to theirs; a network carries no such bound and amplifies numerical noise into its test predictions.

  In other words the GP already does implicitly what our gate does explicitly, which is why it is the
  one column that never needs it.

We report this rather than selecting benchmarks around it, because it is the fact that makes the next
subsection necessary. A plug-and-play method that is worse than its own prior on half the cells is not
usable without a rule for when to stop.

## 4.4 The bounded residual closes most of that gap

Re-running the same protocol with the zero-initialised scale of §3.5 — four architectures, five
benchmarks, everything else fixed — removes most of the harm:

> Cells where prior-only wins fall from **21/45 to 7/35**, and every benchmark whose model is genuinely
> incomplete clears entirely. Clean Poisson goes from $0.110/0.122/0.040/0.060$ to
> $0.0006/0.0006/0.0009/0.0010$, and the weak nonlinearity from $0.111/0.124/0.041/0.060$ to
> $0.0061/0.0063/0.0068/0.0073$.

Crucially it costs nothing where the missing physics is real: on HBM and the battery the scaled head is
better in six of eight cells (battery DeepONet $0.1164\to0.0596$, HBM GNOT $0.2920\to0.2592$). The bound
suppresses noise, not capacity.

The CV gate remains available as a belt-and-braces check and is what we use when *choosing between
correction spaces* (§7), but it is no longer what makes the method safe.

> **Table 4.** With the gate, the worst case across the whole table is $1.00\times$ against prior-only:
> the method never underperforms its own prior. The gate is a **guarantee added on top of** Table 1,
> not the source of its gains.

The gate is not a formality. On the optical benchmark POD-DON's residual hurts at every $n$ and the gate
switches it off every time (0 % on), while DeepONet's gate tracks the data budget, turning on for 20 %,
60 % and 100 % of seeds at $n = 10, 20, 50$. The decision is made from training folds alone.

## 4.5 Relation to DeltaPhi

DeltaPhi attaches residual learning to several neural operators and reports consistent gains, which is
the same shape as Table 1. The difference is what supplies the reference: DeltaPhi forms residuals
**between training samples**, so it needs offline data and its reference inherits that data's error; our
reference is computed in closed form, needs no data at all, and is exact for the physics it encodes.
Section 5 turns this into a measurement — a prior's own error becomes a floor the residual cannot remove,
so a learned reference (16.0 % / 8.9 % self-error) loses 1.3–2.5$\times$ and a coarse solver loses
4.5–27.6$\times$.

---

## 쓸 때 주의 (내부 메모)

- §4.2 의 "every base model on every benchmark" 는 **T1 을 실제로 확인하고** 쓸 것. 한 칸이라도
  음수 gain 이면 문장을 약화해야 한다.
- §3.3 의 줄 수는 **코드에서 센 값**(T8). 코드가 바뀌면 다시 세야 한다.
- Tier-3 를 성능 주장에 절대 넣지 말 것. §8 에 무기여로 기재.
- DeltaPhi 비교는 §2 에서 인용을 달고 §4.4 에서 숫자로 받는 구조.
