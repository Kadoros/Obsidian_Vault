---
tags:
  - note
  - SciML
  - PINN
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Physics-informed neural networks 3 — Self-adaptive PINN (5주차 연장)
paper: "Self-adaptive physics-informed neural networks (J. Comput. Phys., 2023)"
---

# Physics-Informed Neural Networks 3 — Self-Adaptive PINN (SA-PINN)

> **한 줄 요약:** Vanilla PINN은 모든 점을 거의 균일하게(uniform) 다뤄, 학습이 쉬운 영역만 빨리 맞추고 **어려운(hard) 영역은 방치**한다. SA-PINN은 **각 훈련점마다 학습 가능한(trainable) 손실 가중치 $\lambda$** 를 도입해, **min–max(saddle point) 최적화**로 어려운 점에 자동으로 더 집중(soft attention)한다.

논문: *Self-adaptive physics-informed neural networks* (Journal of Computational Physics, 2023). — McClenny & Braga-Neto.

---

## 1. 위치 — Vanilla PINN 문제 중 #3 (Loss/gradient imbalance)

| Vanilla PINN의 문제 | 대안 | 키워드 |
|---|---|---|
| Instance-wise retraining | Neural Operator | Operator learning |
| Noisy environments | Bayesian PINN | Uncertainty → [[03_Physics-informed neural networks 2]] |
| **Loss/gradient imbalance** | **Self-adaptive PINN (SA-PINN)** | **Self-adaptive weighting** (soft attention) |
| Unstable training | X-PINN | Domain decomposition |

- 손실 지형(loss landscape)이 한 골짜기처럼 단순하지 않고, 영역(domain)마다 쉬운/어려운 부분이 섞여 있다. SA-PINN은 attention처럼 어려운 점에 가중.

---

## 2. PINN vs. SA-PINN

### 2.1 구조 비교
- **PINN:** 데이터 $D$ → PINN → $\tilde u(x, w)$. 손실 = 각 항의 단순 합
$$
\mathcal{L}(w) = \mathcal{L}_s(w) + \mathcal{L}_r(w) + \mathcal{L}_b(w) + \mathcal{L}_0(w)
$$
  → 모든 점을 거의 **균일하게(uniformly)** 취급.
- **SA-PINN:** $\tilde u(x, w, \lambda)$. 각 항에 학습 가능한 가중치 $\lambda$:
$$
\mathcal{L}(w) = \lambda_s \mathcal{L}_s(w) + \lambda_r \mathcal{L}_r(w) + \lambda_b \mathcal{L}_b(w) + \lambda_0 \mathcal{L}_0(w)
$$
  → **어려운 점(difficult points)을 더 강조(emphasize)**.

### 2.2 특성 비교
| | Vanilla PINN | SA-PINN |
|---|---|---|
| Loss Weighting | Fixed 또는 수동 튜닝 | **Trainable, point-wise adaptive** |
| Stiff PDE 성능 | 종종 불안정 | **더 강건(robust)** |
| Training strategy | Minimize loss | **Min–maximize loss** (saddle point) |
| Interpretation | Uniform fitting | **Soft attention on difficult points** |

→ **SA-PINN:** 표준 PINN에 **점별(point-wise) 학습 가능 손실 가중치**를 도입해, 신경망이 해의 **어려운 영역에 자동으로 집중**하도록 확장.

---

## 3. Problem Statement

**SA-PINN : Difficulty-aware PDE solver**
- **Vanilla PINN의 단점:** 여러 손실 항을 동시에 최소화하는데, 일부(쉬운) 부분은 다른(어려운) 부분보다 훨씬 빨리 학습됨 → 불균형.
- **SA-PINN:** 개별 훈련점마다 **adaptive weight**를 도입해, 모델이 자동으로 **hard-to-fit 영역**에 집중.

**Core Idea**
- **손실이 클수록 그에 대응하는 가중치도 커지게** 만들어, 신경망이 **어려운 영역에 더 많은 주의(attention)** 를 기울이도록 강제.

---

## 4. Loss Function

### 4.1 표준 PINN 손실 (가중치 없음)
$$
L(w) = \mathcal{L}_s(w) + \mathcal{L}_r(w) + \mathcal{L}_b(w) + \mathcal{L}_0(w)
$$
($w$ = NN 파라미터)
$$
\mathcal{L}_s(w) = \frac{1}{2}\sum_{i=1}^{N_s} |u(x_s^i, t_s^i; w) - y_s^i|^2 \quad(\text{sensor/data loss})
$$
$$
\mathcal{L}_r(w) = \frac{1}{2}\sum_{i=1}^{N_r} |\mathcal{N}_{x,t}[u(x_r^i,t_r^i;w)] - f(x_r^i,t_r^i)|^2 \quad(\text{PDE residual / physics})
$$
$$
\mathcal{L}_b(w) = \frac{1}{2}\sum_{i=1}^{N_b} |\mathcal{B}_{x,t}[u(x_b^i,t_b^i;w)] - g(x_b^i,t_b^i)|^2 \quad(\text{boundary})
$$
$$
\mathcal{L}_0(w) = \frac{1}{2}\sum_{i=1}^{N_0} |u(x_0^i,0;w) - h(x_0^i)|^2 \quad(\text{initial})
$$

### 4.2 SA-PINN 손실 (점별 학습 가중치 도입)
$$
\mathcal{L}(w, \lambda_r, \lambda_b, \lambda_0) = \mathcal{L}_s(w) + \mathcal{L}_r(w, \lambda_r) + \mathcal{L}_b(w, \lambda_b) + \mathcal{L}_0(w, \lambda_0)
$$
$$
\mathcal{L}_r(w, \lambda_r) = \frac{1}{2}\sum_{i=1}^{N_r} m(\lambda_r^i)\,\underbrace{|\mathcal{N}_{x,t}[u(\cdot;w)] - f(\cdot)|^2}_{\text{error}}
$$
$$
\mathcal{L}_b(w, \lambda_b) = \frac{1}{2}\sum_{i=1}^{N_b} m(\lambda_b^i)\,|\mathcal{B}_{x,t}[u(\cdot;w)] - g(\cdot)|^2
$$
$$
\mathcal{L}_0(w, \lambda_0) = \frac{1}{2}\sum_{i=1}^{N_0} m(\lambda_0^i)\,|u(\cdot;w) - h(\cdot)|^2
$$
- **자기적응 마스크 함수(self-adaptation mask function) $m(\lambda)$**: 비음수(nonnegative), 미분가능(differentiable), $\lambda$ 에 대해 **순증가(strictly increasing)** 인 함수.

---

## 5. Minimax Weighting Scheme (Saddle Point Optimization)

손실을 $w$ 에 대해서는 **최소화**, 자기적응 가중치 $\lambda$ 에 대해서는 **최대화** → saddle point.

$$
w^{k+1} = w^k - \eta_k\,\nabla_w \mathcal{L}(w^k, \lambda_r^k, \lambda_b^k, \lambda_0^k) \qquad(\text{Minimized over } w)
$$
$$
\lambda_r^{k+1} = \lambda_r^k + \rho_r^k\,\nabla_{\lambda_r}\mathcal{L}(\cdot) \qquad(\text{Maximized})
$$
$$
\lambda_b^{k+1} = \lambda_b^k + \rho_b^k\,\nabla_{\lambda_b}\mathcal{L}(\cdot)
$$
$$
\lambda_0^{k+1} = \lambda_0^k + \rho_0^k\,\nabla_{\lambda_0}\mathcal{L}(\cdot)
$$

> 신경망은 손실을 **최소화**하는 동시에, 적응 가중치는 **어려운 점에 대한 페널티를 증가**시킨다. ($w$ 는 gradient descent, $\lambda$ 는 gradient ascent.)

### Self-adaptation Mask Function $m(\lambda)$ 후보
$m(\lambda)$ 는 적합이 안 된 residual/boundary/initial 점에 **점진적으로(progressively)** 더 큰 페널티를 준다. 후보:
- **Exponential** (지수형, 빠르게 증가)
- **Polynomial**
- **Sigmoid** (포화형, 상한 존재)
- **Step형(sharp sigmoid)**

---

## 6. 왜 발산하지 않는가 — Saddle Point Optimization 분석

가중치 $m(\lambda)$ 가 단조증가하지만 학습이 **발산하지 않는다**. 이유: $\lambda$ 의 성장은 각 점의 error와 결합되어 있고, 그 error는 동시에 $w$ 에 의해 줄어들기 때문.

점별 손실:
$$
L_i(w, \lambda_i) = \frac{1}{2}\,m(\lambda_i)\,e_i(w)^2
$$
- $e_i(w)$: 그 점의 (마스크 안 씌운) error, $m(\lambda_i)$: 적응 마스크, $m'(\lambda_i) > 0$ (순증가).

### 6.1 $\lambda_i$ 에 대한 미분 (가중치 갱신)
$$
\frac{\partial L_i}{\partial \lambda_i} = \frac{1}{2}\,m'(\lambda_i)\,e_i(w)^2
$$
$$
\lambda_i^{k+1} = \lambda_i^k + \rho\,\frac{1}{2}\,m'(\lambda_i^k)\,e_i(w^k)^2
$$
→ **error가 크면 가중치가 더 빨리 성장.**

### 6.2 $w$ 에 대한 미분 (네트워크 갱신)
$$
\nabla_w L_i = m(\lambda_i)\,e_i(w)\,\nabla_w e_i(w)
$$
→ **$m(\lambda_i)$ 가 커지면 그 점의 error $e_i$ 를 줄이도록 더 강하게 밀어붙임.**

### 6.3 자기 안정화 피드백 루프
$$
e_i \uparrow \;\Rightarrow\; \lambda_i \uparrow \;\Rightarrow\; m(\lambda_i) \uparrow \;\Rightarrow\; \text{stronger correction on } w \;\Rightarrow\; e_i \downarrow
$$
어려운 점의 error가 커지면 가중치가 커지고, 그 결과 네트워크가 그 점을 더 강하게 보정해 error가 다시 줄어든다 → 균형(수렴).

---

## 7. Numerical Examples

### 7.1 Viscous Burgers Equation (유체 동역학)
$$
u_t + u u_x - (0.01/\pi)u_{xx} = 0, \quad x\in[-1,1],\ t\in[0,1]
$$
- 초기조건: $u(0,x) = -\sin(\pi x)$, 경계조건: $u(t,-1)=u(t,1)=0$
- 결과: 예측 $u$ 가 GT와 일치. **Trained Weights $\lambda$** 시각화: 충격파(shock, $x\approx0$의 가파른 영역)를 따라 가중치가 집중됨.

### 7.2 Helmholtz Equation (파동·확산 과정)
$$
u_{xx} + u_{yy} + k^2 u - q(x,y) = 0
$$
- 경계조건: $u(-1,y)=u(1,y)=u(x,-1)=u(x,1)=0$
- 결과: 예측이 GT 진동 패턴을 정확히 재현. 가중치 $\lambda$ 가 진동 줄무늬 구조에 분포.

### 7.3 Allen–Cahn Equation (상장(phase-field) 모델)
$$
u_t - 0.0001 u_{xx} + 5u^3 - 5u = 0, \quad x\in[-1,1],\ t\in[0,1]
$$
- 초기조건: $u(x,0) = x^2\cos(\pi x)$, 경계조건: $u(t,-1)=u(t,1)$
- **핵심 관찰:** **초기조건 가중치(Initial Weight)가 residue 가중치보다 훨씬 빨리 성장**한다. 일반 PINN이 초기조건을 **방치하는 경향**이 있기 때문에, SA-PINN이 자동으로 이를 보정 — error 큰 영역(decision boundary 부근의 hard 영역)에 가중치 집중.

> 직관: easy(○) / hard(×, decision boundary 근처) 점이 섞여 있을 때, SA-PINN은 hard 점들에 가중치를 키워 균형 있게 학습.

---

## 8. 요약

- SA-PINN = **점별 학습 가중치 $\lambda$ + min–max(saddle) 최적화** → 어려운 영역에 **soft attention**.
- 마스크 $m(\lambda)$ 는 비음수·미분가능·순증가. $w$ 는 minimize, $\lambda$ 는 maximize.
- 피드백 루프 $e_i\uparrow \Rightarrow \lambda_i\uparrow \Rightarrow$ 더 강한 보정 $\Rightarrow e_i\downarrow$ 가 발산을 막고 stiff PDE에 강건.
- Burgers/Helmholtz/Allen–Cahn에서 충격파·경계·초기조건 등 어려운 부분을 자동으로 포착.

---

## 관련 노트

**강의 노트**
- [[02_Physics-informed neural networks 1]]
- [[03_Physics-informed neural networks 2]]
- [[05_Neural Operator 1]]

**개념 노트 (50_Concepts)**
- [[PINN]]
- [[Spectral Bias]] — 어려운(고주파) 영역 학습 지연과 가중 전략의 배경
