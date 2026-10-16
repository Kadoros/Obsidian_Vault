---
tags:
  - concept
parent_concept:
  - "[[PINN]]"
  - "[[Galerkin Projection]]"
---
## 한 줄
"Fast training of accurate physics-informed neural networks without gradient descent" (Datar et al., ICLR 2026 oral, arXiv 2405.20836)

## 아이디어 (초록 수준 이해, 정독 전)
- **시공간 분리**: $u(x,t) = \sum_kc_k(t)\varphi_k(x)$
- 공간 기저 $\varphi_k$ = 랜덤 피처 신경망 은닉층, **학습 안 함(frozen)**
- 시간 계수 $c(t)$ = **고전 ODE solver로 적분** (경사하강법 없음) → 빠르고 정확
- 기저가 정규직교 아님 → 그람 행렬 $M$ 필요 ([[Galerkin Projection]])

## 함수해석 관점
PDE → 계수 ODE (Galerkin). 시간 방향을 신경망 대신 잘 풀리는 ODE 문제로 넘김.

## 한계
- PDE **인스턴스 하나** (operator learning 아님)
- 고정 기저 → 이동하는 해에 약함 ([[Kolmogorov n-width]])

## 관련
DeepONet 이식은 새로움 약함 (RandONet 등) → [[TCO 관련 연구 지도]]
