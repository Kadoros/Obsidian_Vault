---
tags:
  - note
  - SciML
  - NeuralOperator
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Neural Operator 1 (6주차, 04/08) — Operator learning theory
paper: "Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs (JMLR, 2021/2024)"
---

# Neural Operator 1 — Operator Learning Theory

> **한 줄 요약:** PINN이 *하나의 특정 PDE 해*를 푸는 반면, Neural Operator는 **함수 공간 사이의 사상(operator) $G: a(x) \mapsto u(x)$** 를 학습한다. 즉 **PDE solver 자체를 학습**해, 한 번 훈련하면 다양한 초기/경계조건에 대해 재학습 없이 빠르게 해를 낸다. 핵심 연산은 **kernel integral**, 핵심 성질은 **discretization invariance**.

논문: *Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs* (Journal of Machine Learning Research, 2021/2024). — Kovachki, Li, et al.

---

## 1. 위치 — Vanilla PINN 문제 중 #1 (Instance-wise retraining)

| Vanilla PINN의 문제 | 대안 | 키워드 |
|---|---|---|
| **Instance-wise retraining** (인스턴스마다 재학습) | **Neural Operator** | **Operator learning** (= mapping function) |
| Noisy environments | Bayesian PINN | Uncertainty |
| Loss/gradient imbalance | Self-adaptive PINN | Self-adaptive weighting |
| Unstable training | X-PINN | Domain decomposition |

- PINN은 PDE/조건이 바뀔 때마다 재학습 필요 → Neural Operator는 **함수→함수 사상**을 배워 일반화.

---

## 2. PINN vs. Neural Operator

### 2.1 구조 대비
- **PINN:** 입력 $a(x)$ (좌표 $x$, 초기/경계) → PINN → $\tilde u(x)$ (solution). 손실 $\mathcal{L} = \|\mathcal{N}[u_\theta](x)\|^2$ = **PDE residual (explicit)** 을 최소화.
- **Neural Operator:** 입력 $a(x)$ → (network, **PDE는 implicit, NO PDE in loss**) → $\tilde u(x)$. **입력 함수를 해 함수로 사상**: $G: a(x) \to u(x)$. PDE는 데이터 안에 암묵적으로.

### 2.2 특성 비교
| | PINN | Neural Operator |
|---|---|---|
| 목적 | **특정 PDE 하나** 풀기 | **PDE solver 학습** |
| 학습 방식 | Physics-based loss | **Data-driven** |
| 일반화 | Limited | **Strong** |
| 속도 | Slow (문제마다 학습) | **Fast (한 번 학습 후)** |
| 데이터 요구량 | Low | **High** |

→ **Neural Operator:** 함수 사이의 mapping(operator learning)을 배우고, PDE의 **solution operator를 근사**.

### 2.3 언제 무엇을 쓰나
| PINN 적합             | Neural Operator 적합       |
| ------------------- | ------------------------ |
| 데이터 부족              | 충분한 훈련 데이터               |
| 물리가 잘 정의됨           | **빠른 추론**이 중요 (수천 배 빠름)  |
| 단일 정확한 해            | **유사한 PDE를 여러 개** 풀기     |
| Inverse 문제, 파라미터 추정 | CFD, 날씨 예측 (다양한 초기/경계조건) |

---

## 3. Problem Statement — Discretization Invariance

**Neural operators :** 무한차원(infinite-dimensional) 함수 공간 사이의 연산자(mapping).
- 다양한 방법으로 **이산화(discretized)** 가능, **여러 해상도(resolution)** 에서, **재학습 없이(without re-training)**.

### Discretization Invariance (이산화 불변성)
- **(Input) any grid:** 어떤 점 집합으로 정의된 입력도 받음 (vs. CNN — 고정 grid 필요).
- **(Output) any grid:** **임의의 점**에서 출력 생성 가능.
- **수렴성:** 이산화가 세밀해질수록(mesh refinement, $\Delta x \to 0$) 예측이 **연속 연산자(continuous operator)로 수렴** (vs. GNN, Transformer — 보장 없음).

> **Key Advantages**
> - 임의 해상도/메시에서 작동
> - 이산화가 달라도 **같은 파라미터** 사용 (discretization invariance)
> - 함수 공간에서 일관적(consistent)
> - PDE 문제에 자연스럽게 적합

### Implementation Variants (Kernel)
- **Graph Neural Operator (GNO)**
- **Low-Rank Neural Operator (LNO)**
- **Multipole Neural Operator (MGNO)**
- **Fourier Neural Operator (FNO)**

---

## 4. Generic Parametric PDEs — PDE를 사상으로 보기

**Key Idea:** PDE는 **입력 함수 → 해 함수**의 사상으로 볼 수 있다.
$$
(L_a u)(x) = f(x), \quad x \in D \qquad u(x) = 0,\ x \in \partial D
$$
- $L_a$: 초기+경계 조건을 포함한 (파라미터 $a$ 에 의존하는) 연산자, $f(x)$: physics(소스항)
- $a \in A$: 파라미터(입력 함수), $u \in U$: 해(출력 함수)

**예: Poisson equation**
$$
-\nabla\cdot(a(x)\nabla u(x)) = f(x), \qquad (L_a u)(x) = -\nabla\cdot(a(x)\nabla u(x))
$$

---

## 5. Neural Operator — Key Operator Definition

PDE를 풀기 = 연산자 $L_a^{-1}$ 를 적용:
$$
L_a^{-1}(L_a u)(x) = L_a^{-1} f(x), \qquad u(x) = L_a^{-1} f \quad(\text{output} = L_a^{-1}(\text{input physics}))
$$
$$
\boxed{G^{\dagger} := L_a^{-1} f : A \to U}
$$
- **PDE를 푸는 것 = 연산자 $G^{\dagger}$ 를 적용하는 것.**
- PDE를 매번 푸는 대신, **입력 함수를 해로 사상하는 연산자를 학습**: $a \mapsto u$.

---

## 6. Problem Setting — 학습 목표

### Goal
- **두 무한차원 공간 사이의 사상**을, 그 사상의 입력-출력 쌍 유한 관측으로부터 학습.
- 참 연산자(true operator) $G^{\dagger}$ 의 **근사(approximation)** $G_\theta$ 학습:
$$
G_\theta : A \to U, \quad \theta \in \mathbb{R}^p, \qquad G_\theta \approx G^{\dagger}
$$
$$
\min \mathcal{L} = \min \|G_\theta - G^{\dagger}\|_2
$$

### Data
$$
\{(a^{(i)}, u^{(i)})\}_{i=1}^{N}
$$
- $a^{(i)} \sim \mu$: 분포에서 샘플된 입력 함수, $u^{(i)} = G^{\dagger}(a^{(i)})$: 대응 출력.

### Loss Function
- **기대 오차(expected error):**
$$
\|G^{\dagger} - G_\theta\|_{L^2_\mu}^2 = \mathbb{E}_{a\sim\mu}\|G^{\dagger}(a) - G_\theta(a)\|_U^2
$$
- **경험적 위험 최소화(Empirical-Risk Minimization, ERM):**
$$
\min_\theta \frac{1}{N}\sum_{i=1}^{N}\|u^{(i)} - G_\theta(a^{(i)})\|_U^2 \qquad (= |u_{GT} - G_\theta(a)|_2)
$$

---

## 7. Formulation — Neural Operator 아키텍처

### 7.1 Overall Idea
Neural Operator = 함수 사이 사상을 배우는 신경망: $G_\theta : a(x) \to u(x)$.
모든 연산이 **함수 공간(function space)** 에서 정의됨 (grid 위가 아님).

### 7.2 Architecture Overview (3단계)
1. **Lifting** $a(x) \to v_0(x)$
   - 점별(pointwise) 변환, 입력을 **고차원 feature space로 embedding**.
2. **Iterative Kernel Integration** $v_t \to v_{t+1}$
$$
v_{t+1}(x) = \sigma\Big(W v_t(x) + \int \kappa(x,y)\,v_t(y)\,dy + b(x)\Big)
$$
3. **Projection** $v_T(x) \to u(x)$
   - feature를 다시 출력 함수로 사상.

### 7.3 Iterative Kernel Integration 분해
$$
v_{t+1}(x) = \sigma\Big(\underbrace{W v_t(x)}_{\text{local linear}} + \underbrace{\int \kappa(x,y)\,v_t(y)\,dy}_{\text{non-local integral}} + \underbrace{b(x)}_{\text{bias}}\Big)
$$
- **Local linear term $W v_t(x)$:** 표준 신경망의 행렬곱과 유사.
- **Non-local integral operator $\int \kappa(x,y) v_t(y)\,dy$:** **모든 점 $y$** 의 정보를 모아 점 $x$ 에 영향 → 전역(global) 상호작용.
- **Bias + activation $b(x)$, $\sigma$:** 표준 신경망 구성요소.

---

## 8. Full Model

### 8.1 Composition
$$
G_\theta = Q \circ \sigma(W + K + b) \circ \cdots \circ P
$$
- $P$ = Lifting(Encoder), 중간 = kernel(integral) 층, $Q$ = Projection(Decoder).
- 층이 쌓이지만, **각 층은 행렬이 아니라 연산자(operator)**.
- **Key Difference:** 행렬 곱(matrix multiplication)을 **적분 연산자(integral operator, 무한차원 선형 연산자)** 로 대체.

### 8.2 변형별 kernel 층 (Instantiations)
| 변형 | kernel 층 형태 |
|------|----------------|
| **GNO** | $\frac{1}{|B(x,r)|}\sum_{l\in B(x,r)} \kappa(x,y)\,v(y_l) + b(x)$ (국소 그래프 합) |
| **LNO** | $\sum_{j=1}^r \langle \psi^{(j)}, v\rangle\,\varphi^{(j)}(x) + b(x)$ (저랭크 분해) |
| **FNO** | $\mathcal{F}^{-1}(R\cdot\mathcal{F}(v))(x) + b(x)$ (Fourier 공간 곱) |

(공통: $v \to$ kernel층 + $W v$ → 합 → $\sigma$)

---

## 9. Parameterization — kernel integral의 계산

### 9.1 Core Problem
핵심 연산:
$$
u(x) = \int_D \kappa(x,y)\,v(y)\,dy
$$
- $u(x)$ 계산에 **모든 점 $y$** 의 정보가 필요 → 전역 상호작용 → **계산이 intractable**.

### 9.2 Discretization (Riemann Sum)
정확도를 유지하며 비용 줄이기 — 적분을 **Riemann 합**으로 근사:
$$
u(x_j) \approx \sum_{l=1}^{J} \kappa(x_j, x_l)\,v(x_l)\,\Delta x_l
$$
- **이산화가 세밀해질수록 ($J \to \infty$, $\Delta x \to 0$): 연속 적분 연산자로 수렴** (Riemann sum → true integral). → **discretization invariance의 근거**.

### 9.3 CNN Convolution과의 대비 (왜 Neural Operator인가)
CNN convolution은 이산 합(discrete sum):
$$
u(x_j) = \sum_{l\in\text{local}} \kappa(x_j - x_l)\,v(x_l)
$$
- 고정된 연속 연산자의 Riemann 근사로 취급되지 **않음** → $J \to \infty$ 가 **의미 없음(no meaning)**.
- **결론: 의미 있는 연속 연산자로의 수렴 보장이 없다.** Neural Operator는 이 점에서 본질적으로 다르다 (해상도 불변, 연속 연산자 수렴).

---

## 10. 요약

- Neural Operator = **함수 공간 사이 사상 $G_\theta: a \mapsto u$** 을 학습 → PDE solver 자체를 학습.
- 구조: **Lifting → (Iterative) Kernel Integration → Projection**. 행렬곱 대신 **적분 연산자**.
- 핵심 성질 **discretization invariance**: 임의 해상도 입력/출력, 이산화 세밀화 시 연속 연산자로 수렴 (Riemann sum 관점). CNN/GNN/Transformer에는 없는 보장.
- 학습: 입력-출력 함수쌍 $\{(a^{(i)}, u^{(i)})\}$ 으로 ERM. PINN 대비 빠르고 일반화 강하나 데이터 요구량 큼.
- 변형: GNO / LNO / MGNO / **FNO** → 다음 강의에서 구체화.

---

## 관련 노트

**강의 노트**
- [[04_Physics-informed neural networks 3]]
- [[06_Neural Operator 2]]
- [[07_Neural Operator 3]]

**개념 노트 (50_Concepts)**
- [[Neural Operator]] — 함수공간→함수공간 사상 정의
- [[Operator_Math_Theory]] — kernel integral / 연산자 이론 기초

**연구 노트 (20_Research)**
- [[../../../../../20_Research/24_Idea_proposal/Neural Operator slam]] — Neural Operator를 SLAM에 적용하는 아이디어

**함수해석 관점 (50_Concepts)**
- [[Integral Operator and Kernel]] — kernel integral = 연속 버전 행렬곱
- [[Inner Product]] — discretization invariance와 리만 합
- [[함수해석학 로드맵]]
