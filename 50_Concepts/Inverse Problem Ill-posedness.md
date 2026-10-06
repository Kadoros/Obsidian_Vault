---
tags:
  - concept
parent_concept:
  - "[[PINN]]"
---
## Forward vs Inverse problem
- **Forward**: PDE 파라미터 $k(x)$, 경계/초기조건이 주어졌을 때 해 $u$를 구함 (전통 수치해석의 영역)
- **Inverse**: 관측된 $u$(변위, 영상 등)로부터 PDE 파라미터 $k(x)$(물성치, 점성계수 등)를 역추정

## Ill-posedness (Hadamard 조건 위반)
Inverse problem은 일반적으로 다음 중 하나 이상을 위반:
1. **해의 존재성**: 노이즈가 있으면 정확히 일치하는 $k(x)$가 없을 수 있음
2. **해의 유일성**: 서로 다른 $k(x)$가 거의 같은 $u$를 만들 수 있음 (non-identifiability)
3. **해의 안정성**: $u$의 작은 노이즈가 $k(x)$ 추정에서 큰 오차로 증폭

## PINN/PINO에서의 증상
탄성도 같은 물성치를 변위로부터 역추정할 때, 손실이 줄어도 추정값이 0이나 임의값으로 수렴 — "모델이 안 배운다"가 아니라 **문제 자체가 여러 해를 허용**하는 구조적 현상. 균일한 영역(노이즈 데이터에 다양한 패턴이 없음)에서 특히 심함.

## 완화 방법
- Regularization (Tikhonov 등)으로 해 공간을 제한
- 물리적으로 타당한 범위로 파라미터 clamp/prior 부여
- 다양한 변형 시나리오(데이터 다양성)를 확보해 비식별성(non-identifiability) 줄이기
