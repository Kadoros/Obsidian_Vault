---
tags:
  - note
  - SciML
  - KAN
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Kolmogorov-Arnold Networks 1 (10주차, 05/06) — KA representation theorem
paper: "KAN: Kolmogorov-Arnold Networks (ICLR 2025)"
---

# Kolmogorov-Arnold Networks (KAN) 1 — 표현정리와 구조

> **한 줄 요약:** MLP가 "노드에 고정 활성화 + 엣지에 스칼라 가중치"라면, KAN은 **엣지에 학습 가능한 1D 함수(B-spline) + 노드는 단순 합**. 근거는 **Kolmogorov–Arnold representation theorem**(임의의 다변수 함수 = 1D 함수들의 합·합성). 결과적으로 해석가능(함수를 직접 들여다봄)하고, 과학 함수(PDE)에 정확하며, **차원 독립적 근사율**로 차원의 저주를 피한다.

논문: *KAN: Kolmogorov–Arnold Networks* (ICLR 2025). — Liu et al.

> 강의 맥락 메모: **PDE를 함수들의 합성(compositions of functions, $\Phi_1, \Phi_2, \dots, \Phi_n$)으로 보고**, 각 1D 함수를 sin/cos/exp 같은 **specific function** 으로 표현/학습한다.

---

## 1. Basic Idea of KAN

- **고차원 함수 $y = f(x)$ 를 1D 함수들의 합·합성으로 분해(decompose)** 할 수 있다:
$$
f(x) = \sum_q \Phi_q\Big(\sum_p \phi_{q,p}(x_p)\Big)
$$
  - **n-dim = sum of 1-dim** (n차원 문제를 1차원 함수들의 합으로).
- 이 1D 함수들은 **학습 가능(learnable)** — 예: **spline**.

### Advantages
- **Interpretability:** 각 함수를 개별적으로 들여다볼 수 있음(inspect).
- **Accuracy:** 구조화된(PDE) 함수의 근사가 더 좋음.
- **Better scaling laws:** 모델 크기에 따라 더 빠르게 개선.

---

## 2. MLP vs. KAN

### 2.1 핵심 구조 전환 (Core Architectural Shift)
각 "가중치(weight)"가 **학습 가능한 1D 함수(spline)** 로 대체된다.

| | MLP | KAN |
|---|---|---|
| Diff 1 | 활성화가 **노드(node)** 에 있음 (**fixed**) | 활성화가 **엣지(edge)** 에 있음 (**learned**) |
| Diff 2 | 가중치가 **스칼라(scalar)** | 가중치가 **함수(function)** |
| Diff 3 | 노드가 **비선형(nonlinearity) 적용** | 노드는 **입력을 합산(sum)만** |

- 연산 흐름: **MLP** $x \to Wx \to \sigma(\cdot)$ vs. **KAN** $x \to \phi(x) \to \text{sum}$.

### 2.2 "MLPs on the outside, Splines on the inside"
KAN은 두 강점을 결합:
| | Splines | MLPs |
|---|---|---|
| Pros | 저차원에서 매우 정확 (**local**) | 고차원 합성을 잘 처리 (**global**) |
| Cons | 차원의 저주에 취약 | 국소적으로 덜 정밀 |

### 2.3 이론·수식 비교
| | MLP | KAN |
|---|---|---|
| 정리 | **Universal Approximation Theorem** | **Kolmogorov–Arnold Representation Theorem** |
| Shallow 수식 | $f(x) \approx \sum_{i=1}^{N(\epsilon)} a_i\,\sigma(w_i\cdot x + b_i)$ | $f(x) = \sum_{q=1}^{2n+1}\Phi_q\big(\sum_{p=1}^{n}\phi_{q,p}(x_p)\big)$ |
| 활성화 | **노드에 고정(fixed)** 활성화, 엣지에 학습 가능 가중치 | **엣지에 학습 가능(learnable)** 활성화, 노드는 합 연산 |
| Deep 수식 | $\text{MLP}(x) = (W_3\circ\sigma_2\circ W_2\circ\sigma_1\circ W_1)(x)$ | $\text{KAN}(x) = (\Phi_3\circ\Phi_2\circ\Phi_1)(x)$ |
| Deep 구조 | $\sigma$: nonlinear & **fixed**, $W$: linear & **learnable** | $\Phi$: nonlinear & **learnable** |

- MLP: $a_i\sigma(\cdot)$ 에서 $\sigma$ 가 비선형(고정), $w_i$ 가 선형(학습). KAN: $\phi_{q,p}$ 자체가 비선형이며 학습 가능.

---

## 3. Kolmogorov–Arnold Representation Theorem

### Theorem
- **고차원 함수는 1D 함수 + 덧셈으로 분해 가능.**
- 임의의 다변수(multivariate) 함수는 다음으로 쓸 수 있다:
  - **합(sums of)** + **1변수(univariate, 1D) 함수의 합성(compositions)**.

### Limitation of Theorem
- 이 1D 함수들이 **비매끄럽(non-smooth)** 거나 **fractal** 일 수 있다.
- 따라서 **실제로 학습하기 어렵다(hard to learn in practice)**.
  → KAN은 이 한계를 **B-spline** 으로 극복.

---

## 4. KAN Architecture

### 4.1 Layer & Edge
- **Layer:** 함수들의 행렬(matrix of functions):
$$
\Phi = \{\phi_{q,p}\}, \quad p=1,\dots,n_{\text{in}},\ q=1,\dots,n_{\text{out}}
$$
  - 입력 차원 $n_{\text{in}}$, 출력 차원 $n_{\text{out}}$. ($\Phi$ 는 $\phi_{1,1}\dots\phi_{q,p}$ 의 행렬)
- **Edge:** 각 연결마다 함수(**B-spline로 parameterize**):
$$
\phi_{q,p} : \mathbb{R} \to \mathbb{R}
$$
  - 스칼라 입력 → 변환된 스칼라 출력 (1D).

### 4.2 Forward Pass
각 뉴런 계산:
$$
x_{l+1,j} = \sum_{i=1}^{n} \phi_{l,j,i}(x_{l,i})
$$
1. 각 입력값이 함수(edge)를 통과
2. 모든 출력이 노드에서 합산
- **Nodes = aggregation only (합산만), Edges = nonlinearity.**
- 행렬 형태: $x_{l+1} = \Phi_l(x_l)$ ($\Phi_l$ = 함수의 행렬, $x_l$ = $l$-번째 층 데이터)
- **Full Network:** $\text{KAN}(x) = (\Phi_{L-1}\circ\cdots\circ\Phi_0)(x)$

### 4.3 왜 B-spline인가
정리의 한계(1D 함수가 non-smooth/fractal → 학습 곤란)를 B-spline으로 해결:
- 1D 함수를 잘 근사(approximate)
- **smooth (매끄럽고 미분가능, differentiable)**
- **local support** (국소 지지)

> **요약:** KAN은 스칼라 가중치를 **학습 가능한 1D 함수**로 대체해, 층을 **함수 행렬**로 구성. 노드는 입력을 **합산만** 하고, 모델은 다변수 함수를 1변수 함수들의 합성으로 분해하는 **Kolmogorov–Arnold 정리**에서 영감.

---

## 5. Approximation Theory — 차원의 저주 회피

### Core Statement
KAN은 **입력 차원에 의존하지 않는 수렴율(convergence rate)** 로 다변수 함수를 근사한다.

### Intuition
$$
\text{MLP: Error} \sim O(N^{-k/d}) \qquad \text{KAN: Error} \sim O(N^{-k})
$$
- $N$: 파라미터 수, $d$: 입력 차원, $k$: 매끄러움(spline order 관련).
- MLP는 오차가 **데이터 차원 $d$ 에 의존(나누기 $d$)** → 차원 커지면 수렴 느림.
- KAN은 **차원 무관** ($O(N^{-k})$).

> - KAN은 고차원 근사 문제를 **여러 개의 저차원(1D, spline) 문제로 축소** — 1D에서는 강한 근사 성질.
> - 그래서 **차원 독립적 근사율로 차원의 저주(curse of dimensionality)를 회피**.

---

## 6. Interpretability in KAN — Symbolification

### Symbolification
학습된 함수를 **사람이 읽을 수 있는 수학식(human-readable mathematical expressions)** 으로 변환.
KAN은 함수를 spline으로 학습한다. 학습 후:
1. 각 spline 함수를 후보 함수 집합으로 근사: **linear, polynomial, sinusoidal, exponential** 등
2. 가장 잘 맞는(best-fitting) 심볼 형태 선택.

→ **KAN은 모델을 명시적 수학 공식(explicit mathematical formula)으로 바꿀 수 있다.**

### 예시 (계산 그래프로 표현)
- **(a) multiplication $xy$:** 입력 $x, y$ → 제곱/덧셈 패턴으로 곱셈 합성.
- **(b) division $x/y$:** 분수 구조.
- **(c) deeper compositions:** $\exp(\sin(x_1^2 + x_2^2) + \sin(x_3^2 + x_4^2))$ 같은 식을 $\exp(a+b)$, $\sin(a+b)$, $x^2 = f(x)$ 의 트리로 분해.

---

## 7. 실험

### 7.1 Function Fitting — Special Functions
수학·물리의 **15개 special function** (Jacobian elliptic, Bessel, Legendre, spherical harmonics 등)을 fit.
- Minimal/Best KAN shape와 RMSE를 MLP와 비교 → **대부분 KAN test RMSE가 MLP보다 작음** (예: sph_harm $10^{-7}$ 수준).
- **KAN matches the underlying structure of the function** — RMSE vs. 파라미터 수에서 KAN(파랑)이 MLP(주황)보다 가파르게 감소.
- **KAN은 1D 분해 덕분에 파라미터를 더 효율적으로 사용.**

### 7.2 Fitting Images
난류(turbulence) 이미지 fit: **KAN의 PSNR(62.45, 82.6)** 이 SIREN, MLP, MLP_RFF보다 높음 → 세밀한 구조 재현 우수.

### 7.3 Partial Differential Equations
- **Scientific functions are naturally compositional → KAN matches inductive bias** (과학 함수는 본래 합성적이라 KAN의 귀납 편향과 일치).
- **Poisson equation with zero Dirichlet boundary data**, 손실 = **KAN Loss + PDE Loss**.
- L2/H1 error: KAN이 MLP보다 빠르게 수렴하고, 파라미터 수 대비 error가 이론선 $N^{-4}$ 에 근접.

---

## 8. 요약

- **KAN = 엣지에 학습 가능한 1D 함수(B-spline) + 노드는 합산.** MLP의 "고정 활성화 + 스칼라 가중치"와 정반대.
- 근거: **Kolmogorov–Arnold representation theorem** (다변수 = 1D 함수의 합·합성). 한계(non-smooth)는 **B-spline**(smooth, local support)으로 보완.
- **차원 독립 근사율** $O(N^{-k})$ → 차원의 저주 회피. 과학/PDE 함수에 특히 적합 (compositional inductive bias).
- **Symbolification** 으로 학습 모델을 명시적 수식으로 변환 → 높은 해석가능성.

---

## 관련 노트

**강의 노트**
- [[07_Neural Operator 3]]
- [[09_Kolmogorov-Arnold Networks 2]]
- [[10_Kolmogorov-Arnold Networks 3]]
- [[11_Kolmogorov-Arnold Networks 4]]

**개념 노트 (50_Concepts)**
- [[KAN]] — Kolmogorov-Arnold 표현정리 / B-spline 엣지 함수
