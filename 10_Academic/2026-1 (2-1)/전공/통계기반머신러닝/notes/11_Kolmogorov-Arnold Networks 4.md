---
tags:
  - note
  - SciML
  - KAN
  - Application
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Kolmogorov-Arnold Networks 4 (13주차, 05/27 — Applications) — KAN-AD & LESA
paper: "KAN-AD: Time Series Anomaly Detection with KAN (ICML 2025); LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration (CVPR 2026)"
---

# Kolmogorov-Arnold Networks 4 — 응용: KAN-AD & LESA

> **한 줄 요약:** KAN을 실제 응용에 적용한 두 사례. **(1) KAN-AD**: KAN의 B-spline을 **Fourier series**로 바꿔, 시계열 이상탐지(TSAD)에서 국소 잡음에 강건하고 가볍게. **(2) LESA**: diffusion model 가속을 위해, diffusion feature 진화가 단계별로 다르다는 점을 이용해 **stage-aware predictor**를 두고 timestep modulation에 **KAN**을 사용.

논문: ① *KAN-AD: Time Series Anomaly Detection with Kolmogorov–Arnold Network* (ICML 2025). ② *LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration* (CVPR 2026).

---

# Part 1. KAN-AD — Time Series Anomaly Detection

## 1. Motivation
- 기존 forecasting 기반 TSAD(시계열 이상탐지)는 **작은 국소 peak/drop 등 모든 디테일을 맞추려다** 잡음에 과적합.
- KAN도 1변수 함수(B-spline)를 쓰는데, **시계열 전용이 아니라 국소 특징에 과적합**할 수 있음.
- 비교 그림: clean train에선 TimesNet/KAN/KAN-AD 모두 OK지만, **noisy train**에선 TimesNet·KAN이 오탐(✗), **KAN-AD만 정상 탐지(✓)**.

## 2. Basic Idea — KAN-AD
- 잡음 섞인 국소 변동(noisy local fluctuations)에 **강건하면서 가벼운(lightweight)** TSAD 모델.
- KAN backbone 위에 정교하게 구축 → **탐지 정밀도 + 추론 효율** 모두 향상.
- **핵심: B-spline 함수를 Fourier series로 대체.** (B-spline은 highly localized·flexible·작은 국소 구조까지 fit → 잡음 과적합 / Fourier는 전역·매끄러움)

## 3. Problem Statement — Univariate TSAD
- 관측 시계열: $x_{0:t} = \{x_0, x_1, \dots, x_t\}$
- 이상 라벨: $C = \{c_0,\dots,c_t\}$, $c_i \in \{0,1\}$
- 목표: 시각 $i$ 이전의 모든 과거 관측으로 현재 점이 이상인지 예측: $[x_0,\dots,x_i] \to c_i$.

## 4. KAN-AD Core Idea
원시 시계열을 직접 예측하는 대신, 신호를 **매끄러운 기저함수**로 분해:
$$
f(x_{0:i}) = A_0 + \sum_{n=1}^{N}\big(A_n\cos(n x_{0:i}) + B_n\sin(n x_{0:i})\big) + \epsilon
$$
- $A_0$: 평균 성분, $A_n, B_n$: 학습 계수, sin/cos: 매끄러운 주기 기저, $\epsilon$: 국소 잡음/교란.

### Design Objective — 정상 신호의 매끄러운 근사 재구성
$$
x'_{0:i} = A_0 + \Theta(x_{0:i})\times H
$$
- $H$: sin/cos 기저함수 행렬, $\Theta(x_{0:i})$: 학습 계수.

## 5. Three Stages
### 5.1 Mapping Phase
원시 시계열을 여러 새 값 집합으로 변환: $x_{0:i}\in\mathbb{R}^T \to x_{0:i}\in\mathbb{R}^{T\times(N+N)}$
$$
X = x_{0:i}, \quad S_n = \{\sin(n x_{0:i}), \cos(n x_{0:i})\}, \quad P_n = \Big\{\sin\big(\tfrac{2\pi n i}{T}\big), \cos\big(\tfrac{2\pi n i}{T}\big)\Big\}
$$
- sine/cosine/periodic-wave 성분 → raw 신호의 **저주파 트렌드, 주기 패턴, 진동 구조** 추출.

### 5.2 Reducing Phase
mapping 후 많은 function channel을 어떻게 결합할지 학습.
- Univariate Function Matrix: $H^{(0)} = \text{Stack}(X, S_1, P_1, \dots, S_n, P_n)$
- CNN 기반 계수 학습: $H^{(l)} = \text{CNN}(\text{CNN}(H^{(l-1)}))$
- $\text{CNN}(H) = \text{GELU}(\text{BN}(\text{Conv}(H)))$ (BatchNorm + GELU)
- → many Fourier features → 계수 추정 → 매끄러운 정상 신호 재구성.

### 5.3 Projection Phase + Anomaly Detection
- 재구성된 정상 패턴으로 다음 값 예측 (single-layer MLP): $x_{i+1} = W\cdot x'_{0:i} + b$
- **이상탐지:** 추론 시 예측 정상값과 실제 관측값을 비교 → **차이가 크면 이상(anomaly)**.

## 6. Illustration & Performance
- KAN(엣지에 학습 가능 1D 함수)과 달리, **KAN-AD는 노드에 고정 활성화 + 엣지에 고정 1D 함수(cos/sin) + 학습 가능 가중치**. Mapping(sliding window → sin/cos 행렬) → Reducing(1D CNN으로 $A_n,B_n$) → Projection(출력).
- **성능:** KPI/TODS/WSD/UCR 벤치마크에서 **KAN-AD가 평균 F1e 최고(0.7798)**. 동시에 **파라미터 274개**(KAN 1360, FITS 624), **CPU 36s / GPU 42s** 로 매우 가볍고 빠름.

---

# Part 2. LESA — Diffusion Model Acceleration

## 7. Motivation
- Diffusion model은 **많은 denoising step** → 계산 비용 큼.
- 기존 가속법은 이전 feature 재사용 또는 단순 수학적 외삽(extrapolation)에 의존.
- **핵심 관찰: diffusion feature 진화는 전역적으로 매끄럽지 않다(NOT globally smooth).**
  - **early timestep: 급격한 변화(drastic change)**
  - **middle timestep: 매끄러운 진화(smooth)**
  - **late timestep: 디테일 정제(detail refinement)**

## 8. Basic Idea — LESA
- Diffusion dynamics는 **강하게 단계 의존적(stage-dependent)**.
- LESA는 단계별로 diffusion 과정의 **시간적 동역학(temporal dynamics)** 을 학습.

### Stage-Aware Design — 궤적을 3단계로
| Stage | Characteristic |
|-------|----------------|
| High-noise | rapid feature change |
| Mid-noise | smooth evolution |
| Low-noise | detail refinement |
- 각 단계마다 **전용 predictor**와 **다른 temporal window size** 사용.

## 9. Methodology — Predictor
입력: 이전 $K$ timestep feature, 출력: 예측된 미래 feature.

### Step 1: Linear Projection (이전 feature를 latent로 융합)
$$
z = W[h_{t+K-1}, h_{t+K-2}, \dots, h_t] + b
$$

### Step 2: Timestep Modulation with KAN
$$
\alpha = f_{\text{KAN}}(\Delta t_{L-1}, \dots, \Delta t_0)
$$
- **왜 KAN인가:** diffusion dynamics는 비선형·불규칙·단계 의존적 → 고정 비선형(fixed nonlinearity)으론 부족. **KAN은 활성화 함수 자체를 학습**:
$$
\alpha = f_{\text{KAN}}(\Delta t) = \sum_{m=1}^{M} w_m\,\phi_m(a_m^\top \Delta t)
$$

### Step 3: Feature Prediction (residual update)
$$
\hat h_{t-1} = h_t + \alpha z
$$
- 현재 feature에서 시작 → 학습된 시간적 보정(temporal correction) 적용.

## 10. Training and Inference
- **Training:** DiT(Diffusion Transformer)를 모든 step 계산해 GT 생성, predictor는 다음 step feature를 예측하고 그 차이를 loss로.
- **Inference:** 일부 step은 DiT로 계산(Compute), 나머지는 predictor로 건너뜀(Skip) → 가속.
- **Window 크기:** high-noise 단계는 **짧은 window ($K=4$)** (급격·약상관 전이), 이후 안정 단계는 **긴 window ($K=8$)** (복잡·history 의존 진화 포착).

## 11. Experiments
### 11.1 Text-to-Image (FLUX)
- LESA가 동일 속도 대비 **품질(Image Reward, CLIP) + 지각 지표(PSNR/SSIM/LPIPS)** 우수. 예: LESA($N=7$) 5.00× 가속에 CLIP 32.88, LESA($N=10$) 6.25× 가속.
- Ablation: **KAN module + Segmented(stage-aware)** 조합이 MLP/비분할보다 일관되게 우수.
- 정성: LESA(5.00×)는 공간 관계 정확, TaylorSeer/ToCa/DuCa/TeaCache/FORA는 색·중복 객체 오류.

### 11.2 Text-to-Video (HunyuanVideo)
- **LESA($N=8$) 5.66× 가속, PSNR 21.05~21.43** 로 ToCa/DuCa/TeaCache/FORA/TaylorSeer/SpeCa/ClusCa보다 지각 품질 높음.
- 정성: 객체 구조·동적 과정·색 정확도·공간 관계에서 원본에 가장 충실.

---

## 12. 요약 (강의 전체 마무리)

- **KAN-AD:** KAN의 B-spline → **Fourier series**. Mapping(sin/cos 분해) → Reducing(1D CNN 계수) → Projection. 잡음에 강건, 초경량(274 파라미터), TSAD SOTA.
- **LESA:** diffusion feature 진화의 **단계 의존성**을 활용한 stage-aware predictor. timestep modulation에 **KAN**(학습 가능 활성화)으로 비선형·불규칙 동역학 포착. T2I/T2V 가속에서 품질 유지하며 5~6× 가속.
- **공통 메시지:** KAN의 "학습 가능한 1D 함수" 아이디어는 PDE를 넘어 시계열·생성모델 가속 등 다양한 응용으로 확장된다.

---

## 관련 노트

**강의 노트**
- [[08_Kolmogorov-Arnold Networks 1]]
- [[09_Kolmogorov-Arnold Networks 2]]
- [[10_Kolmogorov-Arnold Networks 3]]
- [[00_Course Overview]]

**개념 노트 (50_Concepts)**
- [[KAN]] — KAN-AD / LESA 응용의 기반
