---
tags:
  - note
  - SciML
  - KAN
  - ActNet
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Kolmogorov-Arnold Networks 3 (12주차, 05/20) — ActNet
paper: "Deep Learning Alternatives of the Kolmogorov Superposition Theorem (ICLR 2025)"
---

# Kolmogorov-Arnold Networks 3 — ActNet (KST의 더 실용적인 대안)

> **한 줄 요약:** KAN은 spline 기반이라 비효율적(엣지마다 많은 파라미터, grid 표현). KST(Kolmogorov Superposition Theorem)는 사실 **여러 버전**이 있고, 더 현대적인 **Laczkovich(2021)** 정식화를 쓰면 **multi-head MLP** 형태의 효율적 구조 **ActNet**이 나온다. ActNet = 공유 basis-function 활성화 + 다중 헤드. PDE에서 KAN/MLP/Siren보다 우수.

논문: *Deep Learning Alternatives of the Kolmogorov Superposition Theorem* (ICLR 2025).

---

## 1. 복습 — KAN Basic Idea
$$
f(x) = \sum_q \Phi_q\Big(\sum_p \phi_{q,p}(x_p)\Big), \qquad \phi(x) = w_b\frac{x}{1+e^{-x}} + \sum_{i=0}^{G+k-1} c_i B_i(x)
$$
- 고차원 함수를 1D 함수(spline)의 합성으로. 장점: 해석가능성·정확도·scaling. → [[08_Kolmogorov-Arnold Networks 1]], [[09_Kolmogorov-Arnold Networks 2]]

---

## 2. Limitation of KAN

### 2.1 Computational Inefficiency
- KAN은 spline 함수($k$ order), **엣지마다 많은 학습 파라미터**, grid 기반 표현($g$) 사용 → 비효율.

### 2.2 Original KST is Not Practical
- 원래 정리(Kolmogorov Superposition Theorem)는 **많은 중간 함수**를 요구, 구성이 복잡, 현대 딥러닝에 직접 부적합.

> **KST는 신경망의 강력한 이론적 기반이지만, 기존 KST 기반 모델(KAN)은 비효율적이다. 따라서 더 실용적인 KST-inspired 구조가 필요 → ActNet.**

---

## 3. Basic Idea of ActNet

- **새 KST-inspired 구조:** ActNet과 ActLayer 도입.
- **이론적 보장:** universal approximation property 증명.
- **더 나은 PDE 성능:** Poisson, Helmholtz, Allen–Cahn에서 강한 성능.
- **효율 향상:** KAN 대비 파라미터 적음, 계산 비용 낮음, 확장성 좋음.

---

## 4. KST is Not Just One Theorem

일반형 (outer/inner functions):
$$
f(x_1,\dots,x_d) = \sum_{q=0}^{2d}\underbrace{\Phi_q}_{\text{outer}}\Big(\sum_{p=1}^{d}\underbrace{\phi_{q,p}(x_p)}_{\text{inner}}\Big)
$$

| 버전 | 공식 | Inner | Outer | 기타 |
|------|------|-------|-------|------|
| **Kolmogorov (1957)** | $\sum_{q=0}^{2d}\Phi_q(\sum_p \phi_{q,p}(x_p))$ | $2d^2$ | $2d$ | N/A |
| **Lorentz (1962)** | $\sum_{q=0}^{2d} g(\sum_p \lambda_p\phi_q(x_p))$ | $2d$ | 1 | $\lambda\in\mathbb{R}^d$ (inner 단순화) |
| **Sprecher (1965)** | $\sum_{q=0}^{2d} g_q(\sum_p \lambda_p\phi(x_p+qa))$ | 1 | $2d$ | shifted 함수 사용 |
| **Laczkovich (2021)** | $\sum_{q=1}^{m} g(\sum_p \lambda_{pq}\phi_q(x_p))$ | $m=O(d)$ | 1 | $\lambda\in\mathbb{R}^{d\times m}$ (더 확장적/현대적) |

> **서로 다른 KST 정식화는 서로 다른 신경망 구조를 함의한다.** ActNet은 Laczkovich를 채택.

---

## 5. Simple Intuition — Laczkovich(2021) 기반

$$
f(x) = \sum_{i=1}^{m} g\Big(\sum_{j=1}^{d}\lambda_{ij}\phi_i(x_j)\Big) \;\Rightarrow\; f(x) = \sum_{i=1}^{m} g(\lambda_i\cdot\phi_i(x))
$$
- $f(x)$: 다변수 목표 함수, $g$: outer function, $\phi_i$: inner functions, $\lambda_{ij}$: 계수, $m$: 표현 폭(width).

> **$d$차원 입력이 $m$개의 서로 다른 functional head를 통해 multi-head 방식으로 처리된다.**

---

## 6. Matrix Interpretation
$$
f(x) = \sum_{i=1}^{m} g(\lambda_i\cdot\phi_i(x)) \;\Rightarrow\; f(x) = S\big(g[S(\Lambda\odot\Phi(x))]\big)
$$
- $\Phi(x)$: 활성화 행렬(activation matrix), $\Lambda$: 학습 가능 가중치 행렬, $\odot$: 원소별 곱(element-wise), $S$: 행 합산(row summation).

---

## 7. ActNet Architecture

### 7.1 ActLayer (Computational Block)
$$
f(x) = S\big(g[\underbrace{S(\Lambda\odot\Phi(x))}_{\text{ActLayer}}]\big)
$$
활성화 행렬을 basis로 전개:
$$
\Phi(x) = (\phi_1(x),\dots,\phi_m(x)) = \beta B(x), \qquad \phi_k(t) = \sum_{j=1}^{N}\beta_{kj}b_j(t)
$$
$$
\boxed{\text{ActLayer}_{\beta,\Lambda}(x) = S(\Lambda\odot\beta B(x))}
$$
> **ActLayer는 각 head가 서로 다른, 조정 가능한(tunable) 활성화 함수 $\phi_i$ 를 갖는 Multi-Head MLP Layer로 볼 수 있다.**

### 7.2 ActNet 전체
$$
\text{Input} \to \text{Linear Projection} \to \text{ActLayer}\times L \to \text{Linear Projection} \to \text{Output}
$$
- **ActLayer 내부:** 입력 $x$ → tunable activation $\phi_1(x),\dots,\phi_m(x)$ → activation-specific dense layer → $\lambda_1\cdot\phi_1(x),\dots,\lambda_m\cdot\phi_m(x)$.
- **ActNet:** Linear Projection → (ActLayer × N) → Linear Projection → 출력.

---

## 8. KAN vs. ActNet

| | KAN | ActNet |
|---|---|---|
| Core Function | Spline 기반 활성화 | **공유 basis-function 활성화** |
| Activation | Edge-wise spline learning | **Multi-head 학습 활성화** |
| Complexity | $O(L d^2(G+K))$ | $O(L m(m+N))$ |

---

## 9. Universal Approximation Property

> 충분히 넓은(wide) **2개의 ActLayer를 가진 ActNet**은 compact domain의 **임의의 연속 함수를 근사**할 수 있다.
$$
\sup_{x\in\Omega} |f(x) - f_\theta(x)| < \epsilon
$$
- 이유: 학습 가능한 basis-확장 활성화가 임의의 1D 함수를 근사할 수 있고, 이를 superposition 구조로 결합하기 때문.

---

## 10. Basis Functions — Sinusoidal

**Sinusoidal basis** 가 SciML/PDE 문제에 특히 효과적:
$$
\phi_k(t) = \sum_{j=1}^{N}\beta_{kj}b_j(t), \qquad b_i(t) = \sin(\omega_i t + p_i)
$$
- $b_j(t)$: 기저함수, $\beta_{kj}$: 학습 계수, $\omega_i$: 주파수, $p_i$: 위상(phase shift).
- **Fourier Representation Ability:** sine은 주기 패턴, 진동 해, 고주파 신호 표현.
- **Smooth Higher-Order Derivatives:** sine은 무한 미분가능, 어디서나 매끄러움 (PDE 미분에 유리).
- **Reduced Spectral Bias:** sinusoidal basis가 고주파 정보를 더 일찍·정확히 표현. (← [[09_Kolmogorov-Arnold Networks 2]]의 spectral bias 주제와 연결)

---

## 11. Experiments

### 11.1 PINN benchmark (Relative L2 Error / Residual Loss, 낮을수록 좋음)
| Benchmark | ActNet | KAN | Siren | MLP |
|-----------|--------|-----|-------|-----|
| Poisson (w=16) | **6.3e-4** | 1.8e-1 | 9.6e-2 | 6.6e-2 |
| Poisson (w=32) | **6.3e-2** | 1.1e0 | 1.8e-1 | 1.0e0 |
| Helmholtz (w=16) | **1.3e-3** | 2.8e-1 | 1.2e-1 | 4.6e-2 |
| Helmholtz (w=32) | **1.1e-1** | 1.1e0 | 1.3e-1 | 1.0e0 |
| Allen-Cahn | 5.6e-5 | 5.3e-4 | **2.1e-5** | 1.1e-4 |
→ 대부분 **ActNet이 최저 오차** (고주파 w=32에서 격차 큼).

### 11.2 SOTA PINN과 비교 (Relative L2)
| Benchmark | ActNet | JaxPi (2023) | PirateNet (2024) |
|-----------|--------|--------------|------------------|
| Advection (c=80) | **9.50e-5** | 6.88e-4 | 5.48e-4 |
| Kuramoto–Sivashinsky (first window) | 1.34e-5 | 1.42e-4 | **1.23e-5** |
| Kuramoto–Sivashinsky (full) | **8.53e-2** | 1.61e-1 | 2.11e-1 |

### 11.3 정성적 결과
- **Helmholtz (w=16):** ActNet absolute error가 거의 0 (균일하게 파랑), Siren/KAN은 큰 오차 영역. (rel. L2: ActNet 1.04e-3, Siren 8.82e-2, KAN 2.64e-1)
- **Advection (c=80):** ActNet 예측이 exact와 일치, abs. error ~1e-4.
- **chaotic Kuramoto–Sivashinsky:** ActNet이 카오스 패턴까지 재현 (rel. L2 8.53e-2, 문헌 최고 1.61e-1보다 우수).

---

## 12. 요약

- KAN은 spline 기반이라 비효율 → KST의 더 실용적 정식화(**Laczkovich 2021**)로 **ActNet** 도출.
- **ActLayer = 각 head가 tunable 활성화를 갖는 multi-head MLP 층**, $\phi_k = \sum_j\beta_{kj}b_j$ (공유 basis 전개), 행렬형 $\text{ActLayer} = S(\Lambda\odot\beta B(x))$.
- **Sinusoidal basis** ($\sin(\omega t+p)$)로 고주파/주기 해를 잘 표현, spectral bias 완화.
- Universal approximation 보장, KAN 대비 효율적, PDE(Poisson/Helmholtz/Allen-Cahn/Advection/KS)에서 KAN·MLP·Siren·SOTA PINN을 능가.

---

## 관련 노트

**강의 노트**
- [[08_Kolmogorov-Arnold Networks 1]]
- [[09_Kolmogorov-Arnold Networks 2]]
- [[11_Kolmogorov-Arnold Networks 4]]

**개념 노트 (50_Concepts)**
- [[KAN]] — KST / spline 구조 (ActNet의 출발점)
