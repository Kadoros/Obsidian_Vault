---
tags:
  - note
  - SciML
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: PDE using Deep Learning (Neural PDE, 2주차)
paper: "Solving High-Dimensional Partial Differential Equations Using Deep Learning (PNAS, 2018)"
---

# PDE using Deep Learning — Deep BSDE Method

> **한 줄 요약:** 고차원 PDE를 직접 격자(grid)로 푸는 대신, **Feynman–Kac 정리**로 PDE를 **후방 확률미분방정식(BSDE)**으로 바꾸고, 해의 **gradient** $\nabla u$ 를 시간 단계마다 신경망으로 근사하여 **차원의 저주(curse of dimensionality)**를 회피한다.
>
> 핵심 파이프라인: **PDE → BSDE → Neural Network training**

논문: *Solving High-Dimensional Partial Differential Equations Using Deep Learning* (Proceedings of the National Academy of Sciences, 2018). — Han, Jentzen, E.

---

## 1. Problem Statement — Semilinear Parabolic PDE

대상은 **semilinear parabolic PDE** (준선형 포물형 편미분방정식):

$$
\frac{\partial u}{\partial t}(t,x) + \frac{1}{2}\,\mathrm{Tr}\!\big(\sigma\sigma^{T}\,\mathrm{Hess}_x u\big) + \nabla u(t,x)\cdot\mu(t,x) + f\big(t,x,u(t,x),\sigma^{T}\nabla u(t,x)\big) = 0
$$

**Notations**
- $u(t,x)$ : 미지의 해(unknown solution)
- $x \in \mathbb{R}^d$, 차원 $d$ 가 매우 클 수 있음 (예: **100차원**)
- $\nabla u$ : gradient, $\mathrm{Hess}_x u$ : Hessian
- $\mathrm{Tr}(\mathrm{Hessian}) = \Delta u$ (**Laplacian**) — Hessian의 대각합이 라플라시안
- **종단 조건(terminal condition):** $u(T,x) = g(x)$, $\;0 \le t \le T$

> 일반적인 PDE의 초기조건과 달리, 이 부류는 **미래의 종단 시점 $T$ 에서 해가 주어지고**($g(x)$) 과거로 풀어야 한다 → BSDE(후방)가 자연스러움.

### Applications (실제 등장하는 방정식)
| PDE | 응용 분야 |
|-----|----------|
| **Black–Scholes** | Financial derivative (금융 파생상품 가격) |
| **Hamilton–Jacobi–Bellman (HJB)** | Optimal control (최적 제어) |
| **Allen–Cahn** | Phase transition (상전이) |

### 왜 어려운가
- 이 PDE 모델들은 우아하지만 **실용적 사용은 매우 제한적** → **차원의 저주(curse of dimensionality)** 때문.
- 격자 기반 전통 수치해법은 **계산 비용이 차원에 대해 지수적으로(exponentially) 증가**. $d=100$ 이면 사실상 불가능.

---

## 2. Basic Idea: PDE → BSDE → NN

1. **PDE**를 직접 풀지 않고,
2. **비선형 Feynman–Kac 표현(nonlinear Feynman–Kac representation)**을 이용해 PDE 해가 만족하는 **Backward SDE(BSDE)**로 변환,
3. 미지의 해의 **gradient $\nabla u$ (그리고 $\Delta u$)** 를 **신경망(NN)으로 근사**.

---

## 3. BSDE 정식화

### 3.1 BSDE (적분형)
Feynman–Kac에 의해 해는 다음 후방 SDE를 만족:

$$
u(t,X_t) = u(0,X_0) - \int_0^t f\big(s,X_s,u,\sigma^{T}\nabla u\big)\,ds + \int_0^t (\nabla u)^{T}\sigma\,dW_s
$$

> BSDE 재정식화는 PDE를 **재귀적 시간 전진(time-stepping) 방정식**으로 바꾼다. 그래서 $u$ 를 **시뮬레이션된 확률 경로 $X_t$ 를 따라 전방(forward)으로 갱신**할 수 있다.

### 3.2 Simulated Stochastic Paths $X_t$
시간 분할 $0 = t_0 < t_1 < \dots < t_N = T$ 에 대해 상태 경로를 시뮬레이션:

$$
X_{t_{n+1}} = X_{t_n} + \underbrace{\mu(t_n,X_{t_n})\,\Delta t_n}_{\text{Drift term (deterministic)}} + \underbrace{\sigma(t_n,X_{t_n})\,\Delta W_n}_{\text{Diffusion term (stochastic)}}
$$

- **Drift term** (결정론적): $\mu \,\Delta t$
- **Diffusion term** (확률적): $\sigma \,\Delta W_n$, 여기서 $\Delta W_n$ 은 **Brownian motion** 증분
- 하나의 경로: $X_0 \to X_1 \to \dots \to X_T$ (여러 path를 샘플링)

### 3.3 Discretized BSDE (이산화)
$$
u(t_{n+1},X_{t_{n+1}}) \approx u(t_n,X_{t_n}) - f(\cdot)\,\Delta t + (\nabla u)^{T}\sigma\,\Delta W_n
$$

→ 이것이 $u$ 를 계산하는 **forward iterative scheme** (전방 반복 계산). `Next u ← Current u`.

---

## 4. Neural Network Approximation

- **미지량(unknown quantity)** 은 $\sigma^{T}\nabla u(t,x)$ (해의 gradient).
- 이를 신경망으로 근사:
$$
\sigma^{T}\nabla u(t_n,X_{t_n}) \approx (\sigma^{T}\nabla u)(t_n,X_{t_n}\,|\,\theta_n)
$$
  - **입력(input):** $(t_n, X_{t_n})$ → NN($\theta_n$) → **출력(output):** $\sigma^{T}\nabla u$
- **각 시간 단계 $t_n$ 마다 독립적인 sub-network** 를 둔다. (시간별 서브넷)

### Deep BSDE Sub-networks 동작 순서
1. 경로 시뮬레이션 $X_{t_0},\dots,X_{t_N}$ (drift + diffusion)
2. 신경망으로 gradient 추정: $(t,X_{t_n}) \to \text{NN} \to \sigma^T\nabla u$
3. Discretized BSDE로 해를 **전방 전파(propagate forward)**: $u(t_n,X_{t_n}) \to u(t_{n+1},X_{t_{n+1}})$
4. 최종적으로 $u(T,X_T)$ 추정치 생성 ($u(0,X_0)\to\dots\to u(T,X_T)$)
5. PDE의 종단 조건 $u(T,x)=g(x)$ 으로 **손실 정의**

### Loss Function
$$
l(\theta) = \mathbb{E}\big[\,|\,g(X_T) - \hat{u}(X_T)\,|^2\,\big]
$$
- $g(X_T)$: 종단 조건(ground truth) / $\hat u(X_T)$: 신경망이 전파해 만든 추정치
- 즉 "PDE가 지정한 종단값"과 "전방 전파 추정값"의 $L_2$ 차이를 최소화.

---

## 5. Pipeline (전체 학습 구조)

```
Input: Brownian Path X_t
   → NN_θ(t1) → Update u(t1)
   → NN_θ(t2) → Update u(t2)
        ⋮  (sub-network 마다)
   → NN_θ(T)  → Update u(T)
   → Compute loss  l(θ) = E[ |g(X_T) − û(X_T)|² ]
   → Back-propagation: Update θ  (loss를 위로 역전파)
```

- 입력은 Brownian 경로, 각 시간 단계의 서브네트워크가 순차적으로 $u$ 를 갱신, 종단에서 손실 계산 후 전체 $\theta$ 를 역전파로 학습.

---

## 6. 실험 결과 (응용별)

### 6.1 Black–Scholes Equation (with default risk)
고차원 비선형 PDE를 금융에 적용:
$$
\frac{\partial u}{\partial t} + \bar\mu\,x\cdot\nabla u + \frac{\bar\sigma^2}{2}\sum_{i=1}^{d} x_i^2 \frac{\partial^2 u}{\partial x_i^2} - (1-\delta)\,Q(u)\,u - R u = 0
$$
- $x_i$: $i$-번째 기초자산 가격(자산가격), $R$: 무위험 이자율(이자율), $\sigma$: 변동성, $\delta$: 회수율(recovery rate), $Q(u)$: 부도율(default intensity, 감소함수)
- $(1-\delta)Q(u)u$ 항이 **nonlinear**
- 설정: 자산수 $d=100$, $\sigma=0.2$, drift $\bar\mu=0.02$, 이자율 $R=0.02$
- 종단조건(payoff, 만기 시 받는 금액): $g(x) = \min(x_1,\dots,x_{100})$
- **결과: 상대오차 0.46%, 런타임 1607초** (반복에 따라 $u(0,\cdot)$ 가 ~57로 수렴)

### 6.2 Hamilton–Jacobi–Bellman (HJB) Equation
**최적 제어(optimal control)** 에서 등장 — 시간에 걸쳐 비용을 최소화하는 최적 전략 결정.
- 상태 과정: $dX_t = 2\sqrt{\lambda}\,m_t\,dt + \sqrt{2}\,dW_t$
  - $X_t$: 상태(state), $m_t$: 제어(control), $W_t$: Brownian motion, $\lambda$: 제어 강도 파라미터
- 비용 함수(cost functional) 최소화:
$$
J(\{m_t\}) = \mathbb{E}\Big[\int_0^T \|m_t\|^2\,dt + g(X_T)\Big]
$$
  - **running cost** $\|m_t\|^2$ (제어 적용 비용) + **terminal cost** $g(X_T)$ (최종 상태 비용)
- **가치 함수(value function):** 상태가 $x$, 시각 $t$ 일 때 최소 기대 미래 비용
$$
u(t,x) = \min_{m_t}\ \mathbb{E}\Big[\int_0^T \|m_t\|^2\,dt + g(X_T)\Big]
$$
- **Itô 공식(stochastic Taylor expansion)** 으로 가치함수는 HJB PDE를 만족:
$$
\frac{\partial u}{\partial t}(t,x) + \Delta u(t,x) - \lambda\,\|\nabla u(t,x)\|^2 = 0, \qquad u(T,x)=g(x)
$$
  - $\lambda\|\nabla u\|^2$ 항이 **nonlinear**
- **결과: 상대오차 0.17%, 런타임 330초** (Deep BSDE Solver가 Monte Carlo와 거의 일치)

### 6.3 Allen–Cahn Equation
**반응–확산(reaction–diffusion) PDE** — 물질의 상분리(phase separation) 및 질서–무질서 전이 모델링:
$$
\frac{\partial u}{\partial t}(t,x) = \underbrace{\Delta u(t,x)}_{\text{Diffusion (공간 확산/평활)}} + \underbrace{u(t,x) - [u(t,x)]^3}_{\text{Nonlinear reaction term}}
$$
- $\Delta u$: 확산을 나타내는 Laplacian, $u-u^3$: 비선형 반응항
- 종단조건: $u(T,x)=g(x)$, $\;g(x) = \dfrac{1}{2 + 0.4\|x\|^2}$
- **결과: 상대오차 0.30%, 런타임 647초**

---

## 7. Final Intuition (핵심 직관)

- 이 방법론은 **PDE 풀이를 머신러닝 문제로 변환**한다.
- 격자 위에서 해를 계산하는 대신:
  1. **확률 경로(stochastic paths)를 시뮬레이션**하고,
  2. **신경망으로 gradient를 근사**하며,
  3. **종단 조건을 손실 함수로 강제(enforce)** 한다.
- 결과적으로 **차원의 저주를 회피** → **매우 고차원(예: 100차원 이상)** PDE도 효율적으로 풀 수 있다.

> **다음 강의와의 연결 (수업 중 메모):** 이후 PINN은 PDE residual $u_t + a\nabla u + b\nabla u = 0$ 자체를 손실로 넣어 계수 $(a,b)$ 까지 추정하는 방향(inverse problem)으로 확장된다. → [[02_Physics-informed neural networks 1]]

---

## 관련 노트

**강의 노트**
- [[00_Course Overview]]
- [[02_Physics-informed neural networks 1]]

**개념 노트 (50_Concepts)**
- [[Operator_Math_Theory]] — 미분 연산자 / PDE의 연산자 관점
- [[AutoDiff]] — 신경망 gradient 계산의 기반
