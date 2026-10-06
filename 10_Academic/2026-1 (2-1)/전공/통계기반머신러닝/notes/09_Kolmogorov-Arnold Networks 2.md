---
tags:
  - note
  - SciML
  - KAN
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Kolmogorov-Arnold Networks 2 (11주차, 05/13) — 학습/표현력/spectral bias
paper: "On the expressiveness and spectral bias of KANs (ICLR 2025)"
---

# Kolmogorov-Arnold Networks (KAN) 2 — 학습, 표현력(Expressiveness), Spectral Bias

> **한 줄 요약:** KAN의 **구체적 학습 절차**(B-spline 계수 최적화, grid update/extension)와 두 가지 이론적 우위 — **(1) Expressiveness**(KAN ↔ MLP 상호 표현, 파라미터 효율) **(2) Spectral Bias**(KAN은 MLP보다 저주파 편향이 약해 **고주파를 잘 학습**). Hessian이 well-conditioned이기 때문.

논문: *On the expressiveness and spectral bias of KANs* (ICLR 2025). — 두 핵심 주제: ① expressiveness, ② spectral bias.

---

## 1. 복습 — Basic Idea
$$
f(x) = \sum_q \Phi_q\Big(\sum_p \phi_{q,p}(x_p)\Big)
$$
- 고차원 $y = f(x)$ ($x$=input, $y$=output)를 1D 함수의 합성으로 분해, 1D 함수는 학습 가능(spline).
- 장점: 해석가능성, 정확도(PDE), 더 나은 scaling law. → [[08_Kolmogorov-Arnold Networks 1]]

---

## 2. Training of KAN

### 2.1 Learnable Edge Functions
각 뉴런 연결에 학습 가능 함수:
$$
\phi(x) = w_b\,b(x) + w_s\,\text{spline}(x)
$$
- $b(x)$: 잔차 기저 활성화(residual base activation), 보통 **SiLU**
- $\text{spline}(x)$: B-spline 함수
- $w_b, w_s$: 학습 가능한 scaling 파라미터
- → 단일 스칼라 가중치 대신 **함수의 형태(shape)** 를 학습.
- (비유: MLP가 $f(x)=sx+b$ 의 $w=\{s,b\}$ 를 배운다면, KAN은 $f = \phi_1\circ\phi_2\cdots\phi_m$ 의 spline을 배움)

### 2.2 B-Spline Parameterization
$$
\text{spline}(x) = \sum_i^{n} c_i\,B_i(x)
$$
- $B_i(x)$: B-spline 기저함수, $c_i$: 학습 가능 계수.
- **KAN 학습 = 이 spline 계수 $c_i$ 를 최적화하는 것.**

### 2.3 Forward Propagation
$$
x_{l+1,j} = \sum_i \phi_{l,j,i}(x_{l,i})
$$
- 각 입력 신호가 대응 학습함수로 변환된 뒤 합산.

### 2.4 Backpropagation and Optimization
KAN은 **완전 미분가능(fully differentiable)** → 표준 gradient 기반 최적화.
1. spline 함수 통한 forward propagation
2. 손실 계산 (MSE, cross-entropy 등)
3. **spline 계수 $c_i$ 통한 backpropagation**
4. Adam/LBFGS 등으로 파라미터 갱신

### 2.5 Grid-Based Learning & Grid Update
- KAN은 spline 함수를 **grid** 로 이산화. 예: 초기 grid $[-1, -0.6, -0.2, 0.2, 0.6, 1]$ — 이 구간들 위에 spline 기저 정의.
- **Grid Update:** 학습 중 활성화 범위가 변하면, KAN이 활성화 통계에 따라 **spline grid를 동적으로 갱신**, 새 범위를 덮도록 자동 확장.

### 2.6 Grid Extension (coarse-to-fine)
- KAN 학습은 흔히 **coarse-to-fine refinement** 사용. 예: $G = 3 \to 5 \to 10 \to 20$.
- 거친 grid로 먼저 학습 후, 학습을 재시작하지 않고 더 세밀한 grid로 확장.
- 효과: **나쁜 local minima 회피, 최적화 안정성 향상**.

> 수업 메모: **KANO (Kolmogorov-Arnold Neural Operator, ICLR'26)** — KAN을 연산자(NO)로 확장, $f \to f$ 사상. physics implicit learning → physics discovery.

### 2.7 KAN Architecture 통합 수식
$$
\phi(x) = w_b\,\frac{x}{1+e^{-x}} + \sum_{i=0}^{G+k-1} c_i\,B_i(x)
$$
- $\frac{x}{1+e^{-x}}$ = SiLU 활성화, $c_i$: 학습 spline 계수, $w_b$: SiLU 항 계수, $G$: spline grid size, $k$: spline order.

---

## 3. Recent Variants

- KAN 관련 논문이 2024~2025 폭발적으로 증가 (월별 30+편).
- 예: **TKAN**(Temporal), **ReLU-KAN**, **U-KAN**(의료 영상), **Wav-KAN**(Wavelet), **FourierKAN-GCF**, **fKAN**(Fractional/Jacobi), **BSRBF-KAN**, **GraphKAN**, **rKAN**(Rational), **SigKAN**, **KANQAS**(양자), **DeepOKAN**(Deep Operator Network + KAN) 등.
- 참고: ramtinmoslemi.github.io/KAN-Papers, github.com/mintisan/awesome-kan

---

## 4. 주제 1 — Expressiveness (KAN vs. MLP 표현력)

### 4.1 두 가지 잠재적 우위
1. **Expressiveness:** grid size가 큰 KAN은 특정 함수 근사에서 MLP보다 효율적일 수 있다.
2. **Spectral Bias:** KAN은 MLP보다 **저주파 편향이 약함**.
   - 예: $f(x) = \underbrace{\sin(x)}_{\text{low freq}} + 0.1\underbrace{\sin(50x)}_{\text{high freq}}$ — MLP는 고주파 성분 학습이 느림.

### 4.2 Theorem 3.1 — Spline 근사 정확도
spline 기반 KAN이 grid가 세밀해질수록 목표 함수를 얼마나 정확히 근사하는가.
$$
\| (f - \Phi_{L-1}^G \circ \cdots \circ \Phi_0^G)x \|_{C^m} \le C\,G^{-k-1+m}, \quad 0 \le m \le k
$$
- 좌변: target $f$ 와 KAN $f$ 의 차이, 우변: **upper bound**.
- $G$: **Grid Size** (클수록 더 세밀한 spline 표현)
- $k$: **Spline Order** (클수록 더 매끄러운 spline)
- $C^m$-Norm: 함수 오차뿐 아니라 **$m$차 도함수 오차까지** 측정.

### 4.3 Theorem 3.2 — Any MLP can be represented by a KAN
활성화 $\sigma_k(x) = \max(0,x)^k$ 를 쓰는 임의의 MLP는, 다음 KAN으로 **정확히** 표현 가능:
- "comparable width", "at most twice the depth", "spline grid size $G=2$".
- 각 MLP 층은 **2개의 KAN 층**으로 재작성: 하나는 **linear part**, 하나는 **activation part**.

### 4.4 Theorem 3.3 — Any KAN can be represented by an MLP
width $W$, depth $L$, grid $G$, order $k$, ($w_b=0$ 가정)인 KAN은 $\sigma_k(x)=\max(0,x)^k$ MLP로 표현 가능:
- width: $(G+2k+1)W^2$, depth: 최대 $2L$.

**Parameter Complexity Comparison:**
- KAN 파라미터 수: $O(G W^2 L)$
- 등가 MLP 파라미터 수: $O(G^2 W^4 L)$

> **결론:** **KAN은 특정 함수를 MLP보다 훨씬 효율적으로 표현**할 수 있다. 특히 **grid size가 클 때**, 그리고 함수가 **국소적 고주파 구조(localized high-frequency structures)** 를 가질 때.

---

## 5. 주제 2 — Spectral Bias

### 5.1 Theorem 4.1 — 왜 shallow KAN은 강한 spectral bias를 안 겪나
단일층 KAN 분석 (SiLU 잔차 없음, least-squares regression):
$$
\text{KAN}(x,\theta)_i = \sum_{j=1}^{d}\sum_{l=1}^{G+k-1} c_{ijl}\,B_l(x_j)
$$
**Least-Squares Loss:**
$$
L(\theta) = \int_\Omega \|f(x) - \text{KAN}(x,\theta)\|^2 dx \;\Rightarrow\; L(\theta) = \frac{1}{2}\theta^T M\theta + b^T\theta
$$
- $M$: **Hessian matrix**.

### 5.2 Hessian 고유값 분석
$$
\frac{\lambda_N(M)}{\lambda_{d'(d-1)+1}(M)} \le C\,d
$$
- 좌변 = Hessian의 **effective condition number** (최대 고유값 / 첫 의미있는 고유값).
- $\lambda_i(M)$: Hessian 고유값, $d$: 입력 차원, $d'$: 출력 차원, $C$: spline order $k$ 에만 의존하는 상수.

> condition number는 최적화의 균형을 측정.
> → Hessian이 **well-conditioned**.
> → 대부분 방향이 비슷한 속도로 학습 → **최적화 안정**.
> → **고주파 성분도 효율적으로 학습** 가능.

### 5.3 Experiments — Spectral Bias
- **MLP** (위 행): 학습 반복이 진행돼도 **저주파(왼쪽)만 빨리 학습**, 고주파(오른쪽)는 늦게/약하게 → 강한 spectral bias.
- **KAN** (아래 행): 전 주파수 대역을 **고르게 빨리 학습** → 약한 spectral bias.
- (가로축: Frequency [Hz], 세로축: Training Iteration)

### 5.4 2D Poisson Equation with High-Frequency Components
$$
-u_{xx} - u_{yy} = f \quad \text{in } [0,1]^2, \quad u(x,0)=u(x,1)=u(0,y)=u(1,y)=0
$$
- scale_2, scale_4, scale_16 (주파수 스케일 증가)로 갈수록:
  - **KAN(파랑) loss가 MLP(주황)보다 훨씬 낮게 수렴** (특히 고주파 scale에서 격차 큼).
- 해 표면 비교: scale_4에서 MLP는 고주파 디테일을 뭉개지만 **KAN은 GT(truth)와 거의 일치**, scale_16에서도 KAN이 진동 구조를 잘 재현.

---

## 6. 요약

- **학습:** edge 함수 $\phi = w_b\,\text{SiLU} + w_s\sum c_i B_i$, **spline 계수 $c_i$ 최적화** (Adam/LBFGS). **grid update**(동적 범위) + **grid extension**(coarse→fine)로 안정화.
- **Expressiveness:** KAN ↔ MLP 상호 표현 가능(Thm 3.2/3.3). KAN $O(GW^2L)$ vs MLP $O(G^2W^4L)$ → **KAN이 더 효율적**(큰 grid, 국소 고주파).
- **Spectral Bias:** Hessian이 well-conditioned (condition number $\le Cd$) → KAN은 **고주파를 잘 학습**, MLP의 저주파 편향이 약함. 고주파 PDE(2D Poisson)에서 KAN 압승.

---

## 관련 노트

**강의 노트**
- [[08_Kolmogorov-Arnold Networks 1]]
- [[10_Kolmogorov-Arnold Networks 3]]
- [[11_Kolmogorov-Arnold Networks 4]]

**개념 노트 (50_Concepts)**
- [[KAN]]
- [[Spectral Bias]] — KAN이 MLP보다 고주파를 잘 학습하는 이유
