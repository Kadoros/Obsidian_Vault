---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Completeness and Hilbert Space]]"
---
## 시공간 분리
시간 고정 시 $u(\cdot,t)\in L^2(\Omega)$ = 점 하나 → 해 전체 = 힐베르트 공간 속 **곡선**.
$$u(x,t) = \sum_k c_k(t)\,\varphi_k(x)$$
공간 정보 = 기저, 시간 정보 = 계수. $c(t)\in\ell^2$.

## PDE → 계수 ODE
$u_t = \mathcal{L}u$ 에 대입, $\varphi_j$ 와 내적:
$$\frac{dc}{dt} = Ac,\qquad A_{jk} = \langle\mathcal{L}\varphi_k,\varphi_j\rangle$$
- 고유함수 기저면 $A$ 대각 → $c_k(t) = c_k(0)e^{-\lambda_kt}$
- 비선형(Burgers): $+\sum T_{kij}c_ic_j$ → [[Triadic Interaction Tensor]]

## 비정규직교 기저 (랜덤 피처 등)
$$M\frac{dc}{dt} = Ac,\qquad M_{jk} = \langle\varphi_k,\varphi_j\rangle\ (\text{그람 행렬})$$
정규직교면 $M=I$. 기저가 겹치면 $M$ 조건수 악화 (수치해석).

## 정당성
- 공간 기저가 **완비**해야 수렴 ([[Completeness and Hilbert Space]])
- $N$개 절단 오차 = 꼬리합 $\sum_{k>N}|c_k|^2$
- 시공간 함수공간 = 시간 ⊗ 공간 (텐서곱) → $\psi_m(t)\varphi_k(x)$ 기저 → 분리형 모델(SPINN, separable DeepONet) 근거

## 사용처
[[Frozen-PINN]] (랜덤 피처 공간 기저 고정 + ODE solver), FEM, Operator Inference, [[Koopman Operator]] (계수 공간 선형 동역학), [[TCO 아이디어 정리]]
한계: 고정 기저 → 이동하는 해에 약함 ([[Kolmogorov n-width]])
