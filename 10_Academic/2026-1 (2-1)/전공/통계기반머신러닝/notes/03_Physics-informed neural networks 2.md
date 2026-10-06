---
tags:
  - note
  - SciML
  - PINN
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Physics-informed neural networks 2 — Variants of PINN / B-PINN (5주차, 04/01)
paper: "B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data (J. Comput. Phys., 2021)"
---

# Physics-Informed Neural Networks 2 — Variants of PINN & Bayesian PINN

> **한 줄 요약:** Vanilla PINN의 여러 약점을 보완하는 변형들을 개관하고, 그중 **Bayesian PINN (B-PINN)** 을 집중적으로 다룬다. B-PINN = **물리 법칙(PINN) + 불확실성 정량화(BNN)** → 잡음(noise)에 강하고 과적합을 줄이며 **예측값과 불확실성을 함께** 출력하는 PDE solver.

논문: *B-PINNs: Bayesian physics-informed neural networks for forward and inverse PDE problems with noisy data* (Journal of Computational Physics, 2021).

---

## 1. Vanilla PINN의 문제점과 변형(Variants)

| # | Vanilla PINN의 문제 | 대안(Alternative) | 핵심 키워드 |
|---|---------------------|-------------------|------------|
| 1 | **Instance-wise retraining** (인스턴스마다 재학습 필요) | **Neural Operator** | Operator learning |
| 2 | **Noisy environments** (gradient가 noise에 약함) | **Bayesian PINN** | Uncertainty |
| 3 | **Loss/gradient imbalance** (손실 항 간 불균형) | **Self-adaptive PINN** | Self-adaptive weighting |
| 4 | **Unstable training** (불안정한 학습) | **X-PINN** | Domain decomposition |

- 문제 3 보충: 일반 PINN 손실 $\mathcal{L} = \mathcal{L}_u + \mathcal{L}_i + \mathcal{L}_b + \mathcal{L}_p$ 에서 각 항의 스케일/gradient가 불균형 → self-adaptive weighting으로 $\lambda_1\mathcal{L}_u + \lambda_2\mathcal{L}_i + \lambda_3\mathcal{L}_b + \lambda_4\mathcal{L}_p$ 처럼 가중치를 학습.
- 이 강의는 **#2 (Bayesian PINN)** 에 집중. (Neural Operator는 [[05_Neural Operator 1]] 이후, X-PINN/operator는 [[04_Physics-informed neural networks 3]])

---

## 2. PINN vs. Bayesian PINN

### 2.1 구조 비교
- **PINN:** 데이터 $D$ → PINN($\theta$, 단일 결정론적 파라미터) → $\tilde u(x,\theta)$. 손실 = data + physics.
- **Bayesian-PINN:** 데이터 $D$ → **BNN** → 파라미터 표본 $\{\theta^{\{i\}}\} \sim P(\theta\mid D)$ (posterior) → PINN → 여러 예측 $\tilde u(x,\theta^{\{i\}})$
  - **Prior** $P(\theta)$, **Likelihood (data + physics)** $P(D\mid\theta)$, **Posterior** $P(\theta\mid D)$
  - 출력: **평균 $\mathbb{E}[\tilde u(x)]$ → Prediction**, **분산 $\mathrm{var}(\tilde u(x))$ → Uncertainty**

### 2.2 특성 비교표
| | Vanilla PINN | Bayesian-PINN |
|---|---|---|
| Output | Deterministic | Probabilistic |
| Uncertainty | Not available | **Available** |
| Noise 강건성 | Weak | **Strong** |
| Overfitting | Possible | **Reduced** |

- **직관 (Noise 강건성):** 단일 gradient($\nabla, \Delta$)는 error에 민감하지만, 표본 평균/분산은 $\mathrm{var} = \dfrac{\text{error}}{\sqrt{n}}$ ($n$ = 표본 수 $M$)로 잡음이 평균화되어 줄어든다.
- **Bayesian-PINN = "일정 수준의 불확실성을 동반한 가장 그럴듯한(most likely) 해".**

---

## 3. Problem Statement

**Bayesian-PINN : Uncertainty-aware PDE solver = Physical laws (PINN) + Uncertainty (BNN)**

- **Vanilla PINN의 단점:** 잡음 데이터에 민감, 불확실성 정량화 불가, 과적합 위험.
- **BNN:** Bayesian framework에서 잡음 데이터로부터 생기는 불확실성을 정량화.
- **Bayesian-PINN:** 과적합을 피하는 능력 덕분에 **잡음이 큰 시나리오에서 더 정확한 예측**.

**Core Idea**
- **BNNs:** 파라미터의 불확실성을 모델링.
- **PINNs:** 물리적 일관성(physical consistency)을 강제.

---

## 4. General PDE System (B-PINN 설정)

$$
\mathcal{N}_x(u;\lambda) = f, \quad x \in D \qquad (\text{PDE constraint})
$$
$$
\mathcal{B}_x(u;\lambda) = b, \quad x \in \partial D \qquad (\text{Boundary condition})
$$
- **PDE constraint:** 시스템을 지배하는 물리 법칙을 인코딩.
- **Boundary condition:** 영역 경계에서의 제약을 강제.
- 해는 신경망으로 근사: $u(x) \approx \tilde u(x;\theta)$

| 기호 | 의미 | 기호 | 의미 |
|------|------|------|------|
| $\mathcal{N}_x$ | 미분 연산자 | $\mathcal{B}_x$ | 경계 연산자 |
| $u(x)$ | 미지 해 | $b(x)$ | 경계 조건 |
| $\lambda$ | PDE 파라미터 | $D$ | 영역(Domain) |
| $f(x)$ | 강제/소스항(forcing/source) | $\partial D$ | 영역 경계 |

- **관측(Observation):** $u, f, b$ 의 측정값.

---

## 5. Noisy Environments (잡음 관측 모델)

데이터 $D$ 는 센서로부터 얻은 $u, f, b$ 의 산재된 **잡음 측정값**. 측정값은 서로 독립인 **Gaussian** 분포(숨은 실제값 중심):
$$
\bar u^{(i)} = u(x_u^{(i)}) + \epsilon_u^{(i)}, \quad i=1,\dots,N_u
$$
$$
\bar f^{(i)} = f(x_f^{(i)}) + \epsilon_f^{(i)}, \quad i=1,\dots,N_f
$$
$$
\bar b^{(i)} = b(x_b^{(i)}) + \epsilon_b^{(i)}, \quad i=1,\dots,N_b
$$
즉, **noisy data = clean data + error**.

---

## 6. Bayesian Formulation

### 6.1 Likelihood (Physics + Data)
세 가지를 결합: 데이터 불일치, PDE 잔차, 경계 조건
$$
P(\mathcal{D}\mid\theta) = \underbrace{P(\mathcal{D}_u\mid\theta)}_{\text{data}} \cdot \underbrace{P(\mathcal{D}_f\mid\theta)}_{\text{physics}} \cdot \underbrace{P(\mathcal{D}_b\mid\theta)}_{\text{boundary}}
$$
$$
P(\mathcal{D}_u\mid\theta) = \prod_{i=1}^{N_u}\frac{1}{\sqrt{2\pi\sigma_u^{(i)2}}}\exp\!\Big(-\frac{(\tilde u(x_u^{(i)};\theta)-\bar u^{(i)})^2}{2\sigma_u^{(i)2}}\Big) \quad(\text{Data mismatch: estimated }u - u_{GT})
$$
$$
P(\mathcal{D}_f\mid\theta) = \prod_{i=1}^{N_f}\frac{1}{\sqrt{2\pi\sigma_f^{(i)2}}}\exp\!\Big(-\frac{(\tilde f(x_f^{(i)};\theta)-\bar f^{(i)})^2}{2\sigma_f^{(i)2}}\Big) \quad(\text{PDE residual})
$$
$$
P(\mathcal{D}_b\mid\theta) = \prod_{i=1}^{N_b}\frac{1}{\sqrt{2\pi\sigma_b^{(i)2}}}\exp\!\Big(-\frac{(\tilde b(x_b^{(i)};\theta)-\bar b^{(i)})^2}{2\sigma_b^{(i)2}}\Big) \quad(\text{Boundary conditions})
$$

### 6.2 Prior (BNN)
신경망 파라미터 $\theta$ 를 확률변수로 취급: $P(\theta)$ (Gaussian prior).

### 6.3 Posterior (Bayes' theorem)
$$
P(\theta\mid D) \propto P(D\mid\theta)\,P(\theta) \qquad (\text{posterior} \propto \text{likelihood} \times \text{prior})
$$

### 6.4 Posterior Sampling
- $\{\theta^{\{i\}}\} \sim P(\theta\mid D)$ 를 샘플링.
- 여러 예측(예측의 확률분포) $\tilde u(x,\theta^{\{i\}})$.
- **평균 $\mathbb{E}[\tilde u(x)]$ → Prediction**, **분산 $\mathrm{var}(\tilde u(x))$ → Uncertainty**.

---

## 7. Pipeline

```
[Input: Noisy data (u, f, b)]   D_u: solution, D_f: forcing, D_b: boundary
        ↓
[Neural Network]   ũ(x, θ)
        ↓
[Bayesian Formulation]
   Prior P(θ): Gaussian prior
   Likelihood P(D|θ): Exponential (Gaussian) function
   P(θ|D) ∝ P(D|θ) × P(θ): Bayes' Theorem
        ↓
[Sampling]   HMC / VI:  {θ^{i}} ~ P(θ|D)   →  θ1→u1(x), θ2→u2(x), θ3→u3(x), ...
        ↓
[Prediction]   E[ũ(x)] (예측)  +  var(ũ(x)) (불확실성)
```

**구조 그림 (Pipeline 2/2):** 좌측 **Bayesian neural network** (가중치가 분포, $x_1..x_n$ 입력 → $\tilde u$) + 우측 **physics-informed network** (편미분 $\partial_{x_1},\dots$ 으로 $\tilde f = \mathcal{N}_x(\tilde u;\lambda)$, $\tilde b = \mathcal{B}_x(\tilde u;\lambda)$, 그리고 $u,b,f$ 관측). Prior + Likelihood → Posterior (HMC, VI로 추정).

---

## 8. Hamiltonian Monte Carlo (HMC) — Posterior Sampling

### 8.1 목표
신경망 파라미터의 posterior에서 샘플링: $\{\theta^{\{i\}}\} \sim P(\theta\mid D)$.

### 8.2 Idea — 확률을 에너지로
$$
P(\theta\mid\mathcal{D}) \simeq \exp(-U(\theta)), \quad U(\theta) = -\ln P(\mathcal{D}\mid\theta) - \ln P(\theta)
$$
- **energy ↓ ⇒ probability ↑** (낮은 에너지 = 높은 확률).
- 보조 운동량 변수 $r$ 도입, Hamiltonian:
$$
H(\theta, r) = \underbrace{U(\theta)}_{\text{Potential Energy (exploitation)}} + \underbrace{\tfrac{1}{2}r^T M^{-1} r}_{\text{Kinetic Energy (exploration)}}
$$
- 에너지 지형(landscape)에서 골짜기(낮은 에너지)를 따라가되(exploitation), 운동량으로 다른 골짜기로 넘어가며 탐색(exploration).

### 8.3 Hamiltonian dynamics
$$
d\theta = M^{-1} r\, dt \qquad (\theta \text{ 는 운동량에 따라 변함})
$$
$$
dr = -\nabla U(\theta)\, dt \qquad (r \text{ 은 } U(\theta) \text{ 의 gradient에 따라 변함})
$$
- $\nabla U(\theta)$: 에너지 증가 방향, $-\nabla U(\theta)$: 더 낮은 에너지로 향하는 힘.
- **Metropolis 수용(accept) 단계:**
$$
\alpha \leftarrow \min\{1,\ \exp(H(\theta_L, r_L) - H(\theta^{t_{k-1}}, r^{t_{k-1}}))\}
$$
  - $p \ge \alpha$ 면 $\theta^{t_k} \leftarrow \theta_L$ (수용), 아니면 $\theta^{t_k} \leftarrow \theta^{t_{k-1}}$ (기각).
- 이 dynamics는 **총 에너지를 근사적으로 보존** → exploitation과 exploration의 균형.

---

## 9. Experiments

### 9.1 Function Regression
$u(x) = \sin^3(6x)$, $x \in [-1,1]$, 32개 훈련점 + 관측 잡음 $\epsilon_u \sim \mathcal{N}(0, 0.1^2)$.
- **BNN-GPR / BNN-HMC / BNN-VI** 비교: 평균(Mean)·2std(불확실성 밴드)·Exact. 데이터가 적은 구간에서 불확실성 밴드가 넓어짐.

### 9.2 1D Poisson Equation
$\lambda \partial_x^2 u = f$, $x \in [-0.7, 0.7]$. $f$ 16 센서, $u$ 2 센서.
- **잡음 작을 때**(B-PINN-HMC): 예측이 Exact에 거의 일치, 밴드 좁음.
- **잡음 클 때**: 예측이 틀어지고 불확실성 밴드가 크게 넓어짐.

### 9.3 1D Poisson — 센서 수 효과
$N=8, 12, 16, 18$ 로 늘릴수록 불확실성 밴드(2std) 축소, 평균이 Exact에 수렴. ($\mathrm{var} = \text{error}/\sqrt{N}$)

### 9.4 1D nonlinear Poisson
$\lambda \partial_x^2 u + k\tanh(u) = f$, $x\in[-0.7,0.7]$. 비선형이어도 잡음 작을 때 정확, 클 때 밴드 확대.

### 9.5 2D nonlinear Allen–Cahn
$\lambda(\partial_x^2 u + \partial_y^2 u) + u(u^2 - 1) = f$, $x,y\in[-1,1]$. $f$ 500 센서, $u$ 25 센서.
- error map과 2std map: 잡음이 클수록 error/uncertainty 모두 증가 (불확실성이 실제 error를 잘 추적).

---

## 10. 요약

- **B-PINN = PINN(물리) + BNN(불확실성).** 출력이 확률적이라 **예측 + 불확실성**을 함께 제공.
- Likelihood는 **data + PDE residual + boundary** 세 Gaussian 항의 곱; Prior는 가중치 Gaussian; Posterior는 Bayes 정리로.
- Posterior 샘플링은 **HMC**(확률→에너지, Hamiltonian dynamics) 또는 **VI**.
- 효과: **잡음에 강건, 과적합 감소**, 데이터/센서가 많을수록 불확실성 감소.

---

## 관련 노트

**강의 노트**
- [[02_Physics-informed neural networks 1]]
- [[04_Physics-informed neural networks 3]]
- [[05_Neural Operator 1]]

**개념 노트 (50_Concepts)**
- [[PINN]]
- [[Inverse Problem Ill-posedness]] — noisy data / inverse 문제와 불확실성
