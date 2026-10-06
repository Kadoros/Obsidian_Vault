---
tags:
  - note
  - SciML
  - NeuralOperator
  - DeepONet
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Neural Operator 3 (9주차, 04/29) — DeepONet & Physics-Informed DeepONet
paper: "DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators (Nature Machine Intelligence, 2021)"
---

# Neural Operator 3 — DeepONet & Physics-Informed DeepONet (PIDoN)

> **한 줄 요약:** DeepONet은 연산자 출력을 **기저함수(basis)의 선형결합 $G(u)(y) = \sum_k b_k(u)\,t_k(y)$** 로 표현한다. **Branch net**이 입력 함수로부터 계수 $b_k$ 를, **Trunk net**이 출력 위치로부터 기저 $t_k$ 를 만들어 내적으로 결합. 연산자에 대한 **Universal Approximation Theorem**의 보장을 받으며, 부분적 해석가능성을 가진다. PINN과 결합하면 **PIDoN (= NO + PINN)**.

논문: *DeepONet: Learning nonlinear operators for identifying differential equations based on the universal approximation theorem of operators* (Nature Machine Intelligence, 2021). — Lu, Jin, Karniadakis.

---

## 1. 복습 — PINN vs. Neural Operator

| | PINN | Neural Operator |
|---|---|---|
| 입력→출력 | $a(x) \to \tilde u(x)$, 손실 $\mathcal{L} = \|\mathcal{N}[u_\theta](x)\|^2$ (PDE residual) | $G: a(x) \to u(x)$ (함수→함수, **implicit physics**) |
| 결과 | PDE residual 최소화 → **개별 해 하나** | 입력 함수를 해 함수로 **사상** |
| 일반화 | — | **다양한 초기조건/경계조건/계수/grid 해상도** |

→ 배경 이론: [[05_Neural Operator 1]], 변형들: [[06_Neural Operator 2]]

---

## 2. Application of Neural Operators

**중심 응용:** parametric PDE가 정의하는 **solution operator를 학습**.
모든 문제가 공통 구조:
$$
G^{\dagger} : \text{input function} \to \text{solution function}
$$
- coefficient $a(x) \to$ solution $u(x)$
- initial condition $u_0(x) \to$ solution $u(x,t)$

**General PDE Setup:** $L_a u = f$. 학습할 사상: $a \mapsto u$, $f \mapsto u$, $x \mapsto u$.

### 2.1 Test Problems (어떤 함수가 입력인가)

| 문제 | 입력 | 변하는 요소 | 고정 요소 |
|------|------|-------------|-----------|
| **Poisson** $-\frac{d^2}{dx^2}u(x) = f(x)$ | $f(x)$ (source) | $f(x)$ (forcing) | PDE 구조, 경계조건 |
| **Darcy Flow** $-\nabla\cdot(a(x)\nabla u(x)) = f(x)$ | $a(x)$ (coefficient field) | $a(x)$ (material/permeability) | PDE 구조, source $f(x)$ |
| **Burgers** $\partial_t u + u\partial_x u = \nu\partial_{xx}u$ | $u_0(x)$ (initial cond.) | $u_0(x)$ | PDE 구조, 계수 $a(x)$ |

- **Poisson:** 소스(전하/열) $f(x)$ → 효과가 공간에 어떻게 퍼지나 $u(x)$. (정전기, 중력 퍼텐셜, 정상상태 열, Poisson image editing)
- **Darcy Flow:** 공간에 따라 변하는 물질 특성 $a(x)$ 를 통과하는 유체 흐름 $u(x)$. (지하수, 석유/가스 저류층, 다공성 매질, 오염물 이동)
- **Burgers:** 초기조건 $u_0(x)$ 에서 시작해 수송·확산으로 진화. ($u(x) \to u(x,t)$; 충격파, 교통 흐름, 단순 유체, 난류 toy model)

---

## 3. Disadvantages of Neural Operator

| | PINN | Neural Operator |
|---|---|---|
| **Data requirement** | Low (physics-based loss) | **High (data-driven)** |
| **Interpretability** | Low (black box) | Low (implicit physical law) |

1. **High Data Requirement:** Neural Operator는 보통 **대량의 훈련 데이터** 필요.
2. **Limited Interpretability:** 많은 딥러닝 모델처럼 **해석가능성이 낮음**.

→ DeepONet은 이 중 **해석가능성**을 (부분적으로) 개선하고, PINN과 결합해 데이터 요구량도 낮춘다.

---

## 4. DeepONet — 핵심 아이디어

**DeepONet : 비선형 연산자를 근사** — 입력 함수를 출력(해) 함수로 사상:
$$
u(x) \to G(u)(y)
$$
- **input function** $u(x)$ (= $u_0, a, f$ 중 하나), **output function** $G(u)$, **output location** $y$.

### 4.1 Partial Interpretability — 함수 공간 표현
출력은 **기저함수의 선형결합(composition)** 으로 표현되는 연속 함수:
$$
\boxed{G(u)(y) = \sum_{k=1}^{p} b_k(u)\,t_k(y)}
$$
- $t_k(y)$: **기저함수(basis functions)**
- $b_k(u)$: 입력 함수에 의존하는 **계수(coefficients)**
- ($u(x) = \sum_p b_k t_k$ 형태 — 해를 기저의 합으로 본다.)

### 4.2 경계조건/물리를 기저에 인코딩 (1) — Dirichlet BC
임의 기저 대신, **경계조건을 만족하도록 기저를 설계**.
**예: Dirichlet BC** $u(0)=0$, $u(1)=0$ 가 주어지면:
$$
t_k(x) = x(1-x)\,\phi_k(x)
$$
- $x=0 \Rightarrow t=0 \Rightarrow u=0$, $x=1 \Rightarrow t=0 \Rightarrow u=0$ — 어떤 $\phi_k$ 여도 경계조건 자동 만족.

### 4.3 경계조건/물리를 기저에 인코딩 (2) — Fourier Features
Trunk 입력/구조를 설계해 해의 물리적 성질을 인코딩.
**예: Fourier Features**
$$
x \to \sin(kx),\ \cos(kx)
$$
- $t_k(y)$: 공간 패턴(spatial pattern), $b_k(u)$: 주어진 입력에 대한 그 패턴의 중요도.

### 4.4 Strong Generalization & 이론 보장
- **Input-Dependent Adaptation:** 기저함수는 **공유(shared)**, **계수 $b_k(u)$ 만 입력에 따라 변함**.
  - 표현 구조는 동일, 계수만 변화 → **함수 수준(function-level) 일반화**.
- **Theoretical Guarantee — Universal Approximation Theorem (연산자 버전):** 기저함수가 충분히 많으면 ($p\to\infty$) DeepONet은 **임의의 연속 연산자를 근사**할 수 있다.

---

## 5. Architecture — Branch & Trunk

### 5.1 두 네트워크
1. **Branch Network**
   - 입력: 함수 $u$ 의 샘플값 $[u(x_1), u(x_2), \dots, u(x_m)]$
   - 목표: 입력 계수 $b_k(u)$ 인코딩. (입력 $u(x)$ → $b_k$ coefficient)
2. **Trunk Network**
   - 입력: 출력 위치 $y$
   - 목표: 출력을 평가할 기저함수 $t_k(y)$ 인코딩. ($y$ → $t_k$ basis function)

**Final Output (내적):**
$$
G(u)(y) \approx \sum_{k=1}^{p} b_k \cdot t_k
$$
- branch 출력 $b_k$, trunk 출력 $t_k$ 를 **내적(inner product)** 으로 결합.

### 5.2 Stacked vs. Unstacked DeepONet
- **Stacked:** 각 $b_k$ 마다 독립 branch net (Branch net$_1$…Branch net$_p$).
- **Unstacked:** 단일 Branch net이 $b_1..b_p$ 출력, 단일 Trunk net이 $t_1..t_p$ 출력 → $\otimes$ (내적) → $G(u)(y)$.
- $p\to\infty$ 일수록 universal approximation theorem에 가까워짐.

(훈련 데이터 구조: 입력 함수 $u$ 를 **고정 센서 $x_1,\dots,x_m$** 에서 측정, 출력 함수 $G(u)$ 를 **임의 위치 $y$** 에서 평가.)

---

## 6. Training Process

### 6.1 Objective
연산자 $G(u)(y)$ 를 parametric model로 근사:
$$
G_\theta(u)(y) \approx G(u)(y) \qquad (u_\theta(y) \approx u(y))
$$

### 6.2 Training Data
$$
\{(u^{(i)}, y^{(j)}, G(u^{(i)})(y^{(j)}))\}
$$
- $u^{(i)}$: 입력 함수(센서값으로 표현), $y^{(j)}$: 평가 위치, $G(u^{(i)})(y^{(j)})$: ground-truth 출력(solution).

### 6.3 Loss (Supervised Learning)
$$
L = \frac{1}{N}\sum_{i,j} \big|G(u^{(i)})(y^{(j)}) - G_\theta(u^{(i)})(y^{(j)})\big|^2 \qquad (= \|\hat u(y) - u_{GT}(y)\|^2)
$$

### 6.4 Training Procedure
1. 입력 함수 $u(x)$ 를 샘플하고 센서점($m$개)에서 평가
2. 샘플값을 **branch network** 통과 → $b_k$
3. 위치 $y$ 를 **trunk network** 입력 → $t_k$
4. 두 출력을 **내적**으로 결합 → $b_k\cdot t_k = u(y)$
5. 손실 계산 후 **backpropagation**으로 파라미터 갱신

---

## 7. Physics-Informed DeepONet (PIDoN)

**PIDoN = Neural Operator(DeepONet) + PINN**
$$
L = L_{\text{data}} + L_{\text{physics}}
$$
- **장점:** 낮은 데이터 요구량(강한 inductive bias) + **높은 해석가능성**(기저함수 합성 구조).

### 구조
- **DeepONet 부분:** Branch net($u$ → $b_k$) + Trunk net($y$ → $t_k$) → $\otimes$ → $G_\theta(u)(y)$ ($= \sum_k b_k t_k$).
- **Physics 부분:** $G_\theta(u)(y)$ 에 대해
  - **PDE residual** $\mathcal{N}[G_\theta(u)](y)$ → $\mathcal{L}_{\text{physics}}$
  - **BC & IC** $\mathcal{B}[G_\theta(u)](y)$ → $\mathcal{L}_{\text{BC}}, \mathcal{L}_{\text{IC}}$
- 전체 Loss 최소화 → $\theta^*$.

> 즉, DeepONet의 **함수→함수 사상(mapping, 해석가능한 기저 합성)** 에 PINN의 **물리 손실(explicit)** 을 더해, 데이터 효율과 해석가능성을 모두 얻는다.
> PINN의 advanced 변형(B-PINN, SA-PINN)과 같은 "Vanilla PINN 보완" 흐름의 연산자 버전. ← [[02_Physics-informed neural networks 1]]

---

## 8. 요약

- **DeepONet:** $G(u)(y) = \sum_k b_k(u)\,t_k(y)$. **Branch**(입력함수→계수 $b_k$) + **Trunk**(출력위치→기저 $t_k$) → 내적.
- **부분 해석가능성:** 출력이 기저 합성. 기저를 설계해 BC(예: $x(1-x)\phi_k$)나 물리(Fourier features)를 인코딩 가능.
- **일반화:** 기저 공유, 계수만 입력에 따라 변함 → 함수 수준 일반화. **Universal Approximation Theorem** (연산자) 보장.
- **학습:** $\{(u^{(i)}, y^{(j)}, G(u^{(i)})(y^{(j)}))\}$ 으로 supervised, $L_2$ 손실.
- **PIDoN:** DeepONet + PINN ($L_{\text{data}} + L_{\text{physics}}$) → 낮은 데이터 요구 + 높은 해석가능성.

---

## 관련 노트

**강의 노트**
- [[05_Neural Operator 1]]
- [[06_Neural Operator 2]]
- [[02_Physics-informed neural networks 1]]
- [[08_Kolmogorov-Arnold Networks 1]]

**개념 노트 (50_Concepts)**
- [[Neural Operator]]
- [[Operator_Math_Theory]] — 기저함수 선형결합 / 연산자 근사

**연구 노트 (20_Research)**
- [[../../../../../20_Research/24_Idea_proposal/pino slam]] — Physics-Informed Neural Operator 기반 SLAM 아이디어
- [[../../../../../20_Research/25_Research_log/PINO_3DGS_Notes]] — PINO + 3DGS 결합 노트
- [[../../../../../20_Research/24_Idea_proposal/Neural Operator slam]]

**함수해석 관점 (50_Concepts)**
- [[DeepONet]] — trunk = 기저, branch = 계수, 비선형 한계
- [[Orthonormal Basis Expansion]] — 계수 = 내적
- [[Kolmogorov n-width]] — $p$차원 선형공간의 하한
- [[HyperDeepONet]]
- [[계수 구조에 물리 주입]] — §4.2의 "BC를 기저에 인코딩"을 계수 구조로 확장한 아이디어
