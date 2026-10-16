---
tags:
  - concept
parent_concept:
  - "[[Neural Operator]]"
---
## 구조 = 기저 전개
$$u(y)\approx\sum_{k=1}^p b_k(a)\,t_k(y)$$
- trunk net $t_k(y)$ = **기저 함수**
- branch net $b_k(a)$ = **계수** → 이상적으로는 $\langle u,\varphi_k\rangle$ ([[Orthonormal Basis Expansion]])
- 근원: Chen & Chen (1995) 연산자 보편근사 정리

다르게 보면: trunk net의 **마지막 선형층 가중치**를 branch가 입력에 따라 정해주는 것.

## 선형 PDE에서 잘 되는 이유
고유기저에서 해 연산자가 대각: $c_k = f_k/\lambda_k$ → 고정 기저 + 계수만 바꾸기와 구조가 딱 맞음 (중첩 원리).

## 비선형 PDE에서 안 되는 이유 (내 실험: 선형 ✓, 비선형 ✗)
1. **모드 결합**: 비선형항이 계수끼리의 합성곱 → 계수가 독립적인 "그냥 숫자"가 아님 ([[Diagonalization of Convolution]])
2. **$p$차원 선형공간에 갇힘**: 해 집합이 휘어진 다양체면 [[Kolmogorov n-width]] 하한을 못 넘음
3. **정칙성 붕괴**: 충격파 → 계수 $\sim1/k$ 감쇠 → 모드 폭증

## 열린 질문
- 학습된 branch 출력이 실제 스펙트럼 계수와 얼마나 닮았나? 감쇠 속도는?
- trunk 기저 vs 고유기저 vs POD 기저, 언제 뭐가 유리? (최적 trunk ↔ PCA/KL, Lanthaler et al. 2022)
- 계수별 가중치 loss(소볼레프/쌍대 노름)로 안정화? → [[계수 구조에 물리 주입]]

관련: [[HyperDeepONet]], [[FNO]], [[함수해석학 로드맵]]

수업 노트: [[07_Neural Operator 3]] · 최적 trunk ↔ [[ICA vs PCA]]

## 대각 결합의 일반화
$b^\top I t$ → 행렬은 흡수돼서 의미 없음, **3차 텐서**부터 모드 결합 → [[Triadic Interaction Tensor]], [[TCO 아이디어 정리]]
