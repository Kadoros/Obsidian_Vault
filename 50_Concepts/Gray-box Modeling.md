---
tags:
  - concept
parent_concept:
  - "[[GN-Operator]]"
---
## 정의
$$y = f_{\text{known}}(x) + \text{NN}(x)$$
알려진 물리/수식($f_{\text{known}}$, white-box)을 모델 구조에 고정해 넣고, 신경망은 **모르는 부분(잔차)만** 학습 (black-box 부분).

## Prior 주입 방식 3가지
- **Hard (구조적)**: 수식을 모델 안에 고정 — 아는 게 확실할 때 (예: [[GN-Operator]], Hamiltonian/Lagrangian NN, Equivariant NN)
- **Soft (손실함수)**: 위반 시 페널티 — $\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda \cdot |\text{물리법칙 위반량}|$, 아는 수식이 근사치일 때 (예: [[PINN]])
- **대칭성 Prior**: "이 변수를 바꿔도 결과가 같아야 한다" 같은 제약을 구조에 반영

## 왜 유리한가
순수 신경망은 아는 부분도 처음부터 다시 배워야 해서 데이터가 많이 필요하고 불안정. Prior로 고정하면 신경망은 "틀린 부분"만 좁혀서 학습 → 데이터 적어도 됨, 결과 해석 쉬움 ([[GN-Operator]]가 잔차를 0~1k 파라미터로 학습하는 이유).

## 주의
잔차가 거의 0이면(prior가 exact) 신경망이 학습할 시그널이 없어 noise를 학습 (overfitting). 이 경우 threshold 이하면 residual network를 bypass하고 prior만 반환하는 설계가 필요.
