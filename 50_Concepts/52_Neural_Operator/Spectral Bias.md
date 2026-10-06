---
tags:
  - concept
parent_concept:
  - "[[PINN]]"
  - "[[Fractional Operator]]"
---
## 정의
신경망(PINN, FNO 등)이 학습 시 **저주파 성분을 고주파보다 훨씬 빨리, 우선적으로** 학습하는 경향. NTK(Neural Tangent Kernel) 관점에서 고주파 모드의 eigenvalue가 작아 수렴이 느림.

## 증상
- PINN: 고주파/진동이 많은 해(turbulence, 충격파 등)에서 학습 실패 또는 과도하게 smooth한 해로 수렴
- FNO: $|k|^{-2}$로 eigenvalue decay가 고정되어 있어 고주파 모드의 정보가 억제됨

## 완화 시도들
- **Fourier feature embedding**: 입력에 $\sin(kx),\cos(kx)$를 추가해 고주파 학습 유도
- [[Fractional Operator]]의 learnable $\alpha$: $|k|^{-2\alpha}$로 decay rate 자체를 데이터에서 학습 → 단, 실험적으로는 "고주파 개선"보다 "주어진 모드 수에서 에너지 재분배 최적화"에 가까운 효과로 나타남
- **HANO (hierarchical attention)**, **F-FNO (factorization)**: 구조적으로 우회하는 접근, 근본 해결은 아님

## 의미
PINN/NO의 "왜 잘 안 되는가"를 설명하는 핵심 메커니즘 중 하나. multiscale PDE(난류, 균열 등)에서 모델 선택/설계 시 가장 먼저 점검해야 할 항목.

## 함수해석 관점
계수 감쇠 속도 = 매끄러움 → [[Orthonormal Basis Expansion]], [[FNO]]
