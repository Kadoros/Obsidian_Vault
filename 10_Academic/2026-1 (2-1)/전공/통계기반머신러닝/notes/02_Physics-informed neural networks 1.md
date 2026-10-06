---
tags:
  - note
  - SciML
  - PINN
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Physics-informed neural networks 1 (4주차, 03/25)
paper: "Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear PDEs (J. Comput. Phys., 2019)"
---

# Physics-Informed Neural Networks (PINN) 1

> **한 줄 요약:** 신경망이 직접 해 $u(t,x)$ 를 표현하고, **PDE를 손실 함수의 정규화(regularization) 항(physics loss)** 으로 명시적으로 강제한다. 미분은 **자동미분(Automatic Differentiation)** 으로 정확히 계산. Forward(해 구하기)와 Inverse(PDE 계수 추정) 문제를 동시에 다룰 수 있다.

논문: *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations* (Journal of Computational Physics, 2019). — Raissi, Perdikaris, Karniadakis.

---

## 1. PDE using DL (Deep BSDE) vs. PINN — 핵심 대비

| | **PDE using DL (Deep BSDE)** | **PINN** |
|---|------|------|
| 물리 법칙 반영 | **Implicit** (BSDE 구조 안에 암묵적으로) | **Explicit** (손실에 PDE residual을 직접 넣음) |
| 신경망 출력 | gradient $\nabla u$ → $u$ 를 전파해 갱신 | $u(t,x)$ 직접 출력 |
| 손실 | $\mathcal{L} = |u_{GT} - u(T,x)|_2$ (종단조건만, data) | $\mathcal{L} = \underbrace{|u_{GT}-u(t,x)|_2}_{\text{data}} + \underbrace{|\text{PDE}|_2}_{\text{physics}}$ |
| 신경망 구조 | 시간 단계별 서브넷 NN$_1$, NN$_2$, …, NN$_T$ | 단일 NN$(\theta)$ |

- **Deep BSDE**: `Physical Law (Implicit)`. 손실 = 종단 조건 데이터항만, $l(\theta)=\mathbb{E}[|g(X_{t_N}) - \hat u|^2]$.
- **PINN**: 입력 $(t,x)$ → NN → $u(t,x)$. 손실 = **Data loss** ($MSE_u$, 초기/경계조건) + **Physics loss** ($MSE_f$, PDE residual을 정규화로). 물리법칙이 explicit한 regularization.

→ 참조: [[01_PDE using Deep Learning]]

---

## 2. Problem Statement — 왜 PINN인가

**Physics-informed Neural Networks (PINN)**: 주어진 물리 법칙(일반적인 비선형 PDE로 기술됨)을 **존중(respect)** 하면서 지도학습(supervised learning) 과제를 푸는 신경망.

### Strong Inductive Bias (강한 귀납 편향)
- 현대 ML이 아직 활용하지 못한 막대한 **사전 지식(prior knowledge = 물리 법칙)** 이 존재한다.
- 이 사전 정보는 **정규화 에이전트(regularization agent)** 로 작용해 **허용 가능한 해의 공간(space of admissible solutions)** 을 다룰 수 있는 크기로 **제약(constrain)** 한다.
- 효과: **빠르게 올바른 해로 수렴**하고, **훈련 예제가 적어도(few training examples) 일반화가 잘 됨**.
- 그림 직관: `Prior Information` → (Regularization Agent) → `Constrained Space of Admissible Solutions`. 이 공간은 data term + physics term으로 좁혀진다.

---

## 3. Problem Setup (Forward 문제)

### 3.1 대상 PDE
$$
u_t + \mathcal{N}[u;\lambda] = 0, \qquad x \in \Omega,\; t \in [0,T]
$$
- $u(t,x)$: 미지의 해
- $\mathcal{N}[\cdot]$: 비선형 미분 연산자(nonlinear differential operator)
- $\Omega$: 공간 영역(spatial domain), $[0,T]$: 시간 구간
- 예: $\mathcal{N}[u;\lambda] = \lambda_1 u u_x - \lambda_2 u_{xx}$ (Burgers류)

**Goal (Forward):** **고정된 모델 파라미터 $\lambda$** 가 주어졌을 때, 시스템의 미지 은닉 상태 $u(t,x)$ 를 찾는다.

### 3.2 Initial & Boundary Conditions (well-posed 만들기)
1. **초기 조건(Initial condition):** $u(0,x) = u_0(x)$
2. **경계 조건(Boundary condition):** $u(t,x) = g(t,x),\; x\in\partial\Omega$

### 3.3 Training Data
- 제한된 관측 집합 $\{(t_i, x_i, u_i)\}$ — 입력 $(t_i,x_i)$, 출력 라벨 $u_i$ (= $u_{GT}$)
- 이 데이터는 보통 **초기/경계 조건**에서 나온다 → data loss → 지도학습(supervised).

### 3.4 Objective & Key Idea
**목표:** 다음을 만족하는 함수 $u(t,x)$ 를 찾기
1. 초기/경계 조건(관측 데이터)을 존중
2. 지배 PDE를 만족

**Key Idea:** PDE를 수치적으로 푸는 대신,
- $u(t,x)$ 를 신경망으로 표현: $u(t,x) \approx u_\theta(t,x)$ (즉 $u_{GT}\approx \hat u$)
- **PDE를 훈련 중 제약(constraint)으로 강제**.

---

## 4. PINN 정식화

### 4.1 PDE → Residual Form
PDE $u_t + \mathcal{N}[u] = 0$ 를 **잔차(residual)** 형태로:
$$
f(t,x) := u_t + \mathcal{N}[u]
$$
- 목표는 $f(t,x) = 0$ 을 강제하는 것. 즉 $\hat u_t + \mathcal{N}[\hat u_t] = f(t,x) \to 0$ (residual → 0).
- PDE를 직접 풀지 않고, 모델이 **이 잔차를 최소화**하도록 학습.

### 4.2 Loss Function
$$
\mathcal{L} = \mathcal{L}_u + \mathcal{L}_f
$$
- **Data Loss** $\mathcal{L}_u$ (fidelity term): 초기/경계 조건 강제
$$
\mathcal{L}_u = \frac{1}{N_u}\sum_{i=1}^{N_u} |u(t_u^i,x_u^i) - u^i|^2 \quad (= |u_{GT} - \hat u|)
$$
- **Physics Loss** $\mathcal{L}_f$ (regularization term): PDE 만족 강제
$$
\mathcal{L}_f = \frac{1}{N_f}\sum_{i=1}^{N_f} |f(t_f^i,x_f^i)|^2 \quad (\text{PDE} \to 0)
$$

### 4.3 Pipeline (Forward)
1. **입력** $(t,x)$ → NN$_\theta$ → **출력** $u(t,x)$
2. **훈련 데이터**
   - 초기/경계 조건 $\{(t_u^i,x_u^i,u^i)\}_{i=1}^{N_u}$ — **라벨 있음 → Supervised** (data loss)
   - 물리 제약점 $\{(t_f^i,x_f^i)\}_{i=1}^{N_f}$ — **라벨 없음 → Unsupervised** (physics loss)
     - 이 샘플 지점들을 **collocation points** 라 부름. 라벨 불필요 → **제한된 감독(limited supervision)** 으로도 학습 가능.
3. **자동미분(Automatic Differentiation, AD)** 으로 도함수 정확히 계산:
   - $u_t = \mathrm{grad}(u,t)$, $u_x = \mathrm{grad}(u,x)$, $u_{xx} = \mathrm{grad}(u_x,x)$
   - AD = 코드로 정의된 함수의 **정확한 도함수(exact derivatives)** 를 계산하는 기법.
4. **PDE 잔차 $f(t,x)$ 평가**
5. **손실 계산** $\mathcal{L} = \mathcal{L}_u + \mathcal{L}_f$
6. **역전파(Backpropagation)로 파라미터 $\theta$ 갱신**

---

## 5. Example — Schrödinger Equation (Forward)

양자 세계에서 시스템 상태의 시간 진화를 기술:
$$
i h_t + 0.5\,h_{xx} + |h|^2 h = 0
$$
- $h(t,x)$: 복소값 파동함수, $i$: 허수 단위
- **목표:** $h(t,x)$ 를 공간·시간에 걸쳐 학습. 복소수를 실/허로 분리:
$$
h(t,x) = u(t,x) + i\,v(t,x)
$$
- 신경망: 입력 $(t,x)$ → 출력 $(u(t,x), v(t,x))$

**PDE Reformulation (두 잔차 모두 0이어야):**
$$
f_u = u_t + 0.5\,v_{xx} + (u^2+v^2)v \quad(\text{real part})
$$
$$
f_v = v_t - 0.5\,u_{xx} - (u^2+v^2)u \quad(\text{imaginary part})
$$
- 도함수 $u_t, u_{xx}, v_t, v_{xx}$ 는 AD로 계산.

**설정:** $x \in [-5,5]$, $t \in [0,\pi/2]$
- 초기조건: $h(0,x) = 2\,\mathrm{sech}(x)$
- 주기적 경계조건: $h(t,-5)=h(t,5)$, $h_x(t,-5)=h_x(t,5)$

**Loss (세 항):**
$$
MSE_0 = \frac{1}{N_0}\sum |h(0,x_0^i) - h_0^i|^2 \quad(\text{Initial Condition})
$$
$$
MSE_b = \frac{1}{N_b}\sum \big(|h^i(t_b^i,-5)-h^i(t_b^i,5)|^2 + |h_x^i(t_b^i,-5)-h_x^i(t_b^i,5)|^2\big) \quad(\text{Boundary})
$$
$$
MSE_f = \frac{1}{N_f}\sum |f(t_f^i,x_f^i)|^2 \quad(\text{Physics term})
$$
$$
\boxed{MSE = MSE_0 + MSE_b + MSE_f}
$$
**결과:** 20,000개 collocation points로, 예측 $|h(t,x)|$ 가 $t=0.59, 0.79, 0.98$ 단면에서 Exact와 거의 일치.

(추가 예시: **Allen–Cahn equation** — $t=0.1$ 초기 스냅샷에서 $t=0.9$ 최종 예측까지 정확히 재현.)

---

## 6. Data-driven Discovery of PDE (Inverse 문제)

### 6.1 Problem Definition
$$
u_t + \mathcal{N}[u;\lambda] = 0
$$
- $u(t,x)$: 미지의 해 (**데이터로 관측됨**)
- $\mathcal{N}$: 비선형 미분 연산자
- $\lambda$: Forward에서는 **Fixed** 였지만, 여기서는 **발견해야 할 미지 파라미터(unknown parameters to be discovered)**.

**Goal (Inverse):** (잡음 섞일 수 있는) 관측 데이터가 주어졌을 때 **지배 PDE를 식별** — 즉 $\lambda$ 를 추정.

### 6.2 Core Idea: PDE 파라미터를 NN과 함께 학습
- **Step 1:** 해 근사 $u(t,x) \approx \text{NN}(t,x)$ (즉 $u_{GT}\approx \text{NN}(t,x)$)
- **Step 2:** PDE 잔차 정의 $f = u_t + \mathcal{N}[u;\lambda]$
  - **파라미터 $\lambda$ 가 trainable variable 이 됨** ($\hat u_t, \hat\lambda$ 함께 학습)
- 손실: $\mathcal{L} = \mathcal{L}_{data} + \mathcal{L}_f$

### 6.3 Example — 2D Navier–Stokes Equation
유체 흐름(fluid flow) 물리를 기술:
$$
u_t + \lambda_1(u u_x + v u_y) = -p_x + \lambda_2(u_{xx} + u_{yy})
$$
$$
v_t + \lambda_1(u v_x + v v_y) = -p_y + \lambda_2(v_{xx} + v_{yy})
$$
- $u,v$: 속도 성분(velocity), $p$: 압력(pressure), $\lambda_1,\lambda_2$: **미지 파라미터**
- 신경망: $(t,x)$ → NN → $(u,v,\lambda_1,\lambda_2)$

**PDE residuals:**
$$
f := u_t + \lambda_1(u u_x + v u_y) + p_x - \lambda_2(u_{xx}+u_{yy})
$$
$$
g := v_t + \lambda_1(u v_x + v v_y) + p_y - \lambda_2(v_{xx}+v_{yy})
$$

**Loss function** = velocity data loss (관측 적합) + PDE residual loss (물리 강제):
$$
MSE := \frac{1}{N}\sum_{i=1}^{N}\big(|u(\cdot)-u^i|^2 + |v(\cdot)-v^i|^2\big) + \frac{1}{N}\sum_{i=1}^{N}\big(|f(\cdot)|^2 + |g(\cdot)|^2\big)
$$

**결과:** $\lambda_1$ 오차 ≈ **0.078%**, $\lambda_2$ 오차 ≈ **4.67%** — 와류(vorticity) 유동에서 속도장 $u,v$ 와 PDE 계수를 데이터만으로 정확히 복원.

---

## 7. 요약 (핵심 정리)

- PINN = **신경망이 해 $u$ 를 표현** + **PDE를 손실의 explicit 정규화로 강제** + **AD로 정확한 미분**.
- 손실 = **Data loss (초기/경계, supervised)** + **Physics loss (collocation points, unsupervised)**.
- **Forward:** $\lambda$ 고정, $u$ 를 구함. **Inverse(Discovery):** 데이터로 $u$ 와 PDE 계수 $\lambda$ 를 함께 추정.
- 장점: 적은 데이터로도 강한 inductive bias 덕분에 일반화·수렴이 좋다.

---

## 관련 노트

**강의 노트**
- [[00_Course Overview]]
- [[01_PDE using Deep Learning]]
- [[03_Physics-informed neural networks 2]]

**개념 노트 (50_Concepts)**
- [[PINN]] — PINN 핵심 정의 (data + physics loss)
- [[AutoDiff]] — PDE residual 미분을 자동미분으로
- [[Inverse Problem Ill-posedness]] — inverse 문제(PDE 계수 추정)의 ill-posedness
