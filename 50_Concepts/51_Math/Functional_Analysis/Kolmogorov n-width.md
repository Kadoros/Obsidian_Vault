---
tags:
  - concept
  - functional-analysis
  - approximation-theory
parent_concept:
  - "[[함수해석학 로드맵]]"
---
## 아이디어
해 집합 $\mathcal{M}$을 **고정된 $n$차원 선형공간** $V_n$으로 얼마나 잘 덮을 수 있나의 최선값:
$$d_n(\mathcal{M}) = \inf_{\dim V_n = n}\ \sup_{u\in\mathcal{M}}\ \inf_{v\in V_n}\|u - v\|$$

## 왜 중요한가 (DeepONet의 벽)
[[DeepONet]] 출력 $\sum_{k=1}^p b_k(a)t_k(y)$는 고정된 $p$차원 공간 안 → 오차 $\ge d_p(\mathcal{M})$. **학습을 아무리 잘 해도 못 넘는 하한.**
- 선형 PDE: 해들이 중첩 원리를 따름 → 평평 → $d_n$이 빨리 감소
- 비선형 (이동하는 파동, 충격파): 해 집합이 휘어진 다양체 → $d_n$이 아주 느리게 감소
- 불연속이 생기면 계수가 $\sim1/k$로만 감쇠 (깁스) → 모드가 엄청 많이 필요

## 우회 방법
- 비선형 디코더: NOMAD (Seidman et al. 2022), [[HyperDeepONet]] — 기저 자체가 입력에 따라 휨
- 이동 기저 (shift를 따로 학습)
- 대각화되는 공간으로 들어 올리기: [[Koopman Operator]]
- 최적 선형 기저는 PCA/Karhunen–Loève와 연결 (Lanthaler et al.)

> 상태: 개념만 소개됨. 로드맵 6단계에서 제대로 공부 예정.

관련: [[ICA vs PCA]] (PCA/KL), [[07_Neural Operator 3]]
