---
tags:
  - note
  - index
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
---

# 통계기반 머신러닝 (Statistical Machine Learning, 56262) — 강의 노트 인덱스

> 주제: **Scientific Machine Learning (SciML)** — 물리 법칙을 데이터 기반 학습에 통합하고, 고차원 연산자를 학습하는 신경망 설계.

## 강의 노트
0. [[00_Course Overview]] — 강의 개요, 4대 주제(PDE→NN / PINN / Neural Operator / KAN)
1. [[01_PDE using Deep Learning]] — Deep BSDE: 고차원 PDE를 BSDE로 변환해 신경망으로
2. [[02_Physics-informed neural networks 1]] — PINN 기초: PDE residual을 손실로 (forward/inverse)
3. [[03_Physics-informed neural networks 2]] — Bayesian PINN: 불확실성 정량화, HMC
4. [[04_Physics-informed neural networks 3]] — Self-Adaptive PINN: 점별 가중치 min-max
5. [[05_Neural Operator 1]] — Operator learning 이론, discretization invariance
6. [[06_Neural Operator 2]] — kernel 변형: GNO / LNO / MGNO / FNO
7. [[07_Neural Operator 3]] — DeepONet (Branch/Trunk), Physics-Informed DeepONet
8. [[08_Kolmogorov-Arnold Networks 1]] — KAN 표현정리, 구조, B-spline
9. [[09_Kolmogorov-Arnold Networks 2]] — KAN 학습, expressiveness, spectral bias
10. [[10_Kolmogorov-Arnold Networks 3]] — ActNet (KST의 실용적 대안)
11. [[11_Kolmogorov-Arnold Networks 4]] — 응용: KAN-AD(이상탐지), LESA(diffusion 가속)

## 큰 흐름 (한눈에)
| 패러다임 | 무엇을 학습 | 핵심 |
|----------|-------------|------|
| PDE→NN (Deep BSDE) | 해의 gradient | 차원의 저주 회피 (확률 경로 + NN) |
| PINN | 특정 PDE 해 1개 | PDE residual을 explicit 손실로 |
| Neural Operator | 함수→함수 사상 | 여러 PDE 인스턴스에 일반화, kernel integral |
| KAN | 명시적 함수 구조 | 엣지에 학습 가능 1D 함수, 해석가능 |

## 관련 Vault 노트

**개념 노트 (50_Concepts)**
- [[Operator_Math_Theory]] — 연산자 수학 (강의 전반의 토대)
- [[PINN]] · [[Inverse Problem Ill-posedness]] · [[AutoDiff]] — PINN 계열
- [[Neural Operator]] · [[Fractional Operator]] · [[Mellin Neural Operator]] · [[GN-Operator]] — Neural Operator 계열
- [[KAN]] · [[Spectral Bias]] — KAN 계열

**연구 노트 (20_Research)**
- [[../../../../../20_Research/24_Idea_proposal/Neural Operator slam]] · [[../../../../../20_Research/24_Idea_proposal/pino slam]] · [[../../../../../20_Research/25_Research_log/PINO_3DGS_Notes]] — Neural Operator/PINO의 SLAM·3DGS 응용
- [[../../../../../20_Research/21_Projects/01_GNR/origin/XNO expriment]] — 적분 연산자 행렬 실험

---

원본 강의 PDF: [ppts 폴더](../ppts/)
