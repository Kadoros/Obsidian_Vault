---
tags:
  - concept
parent_concept:
---
고차원 데이터에서 "진짜 의미 있는 축(기저)"이 회전되어 섞여 있을 때, PCA와 ICA는 서로 다른 기준으로 축을 찾는다.

| | PCA | ICA |
|---|---|---|
| 찾는 축 | 분산이 큰 방향 (직교) | 통계적으로 **독립**인 방향 |
| 분포 가정 | 가우시안이어도 OK | 소스가 **비가우시안**이어야 함 |
| 회전된 잠재 기저 복원 | 취약 (분산 기준이라 진짜 축과 다를 수 있음) | 가능 (독립성 기준이 회전 모호성을 깸) |

대표 예시: EEG에서 눈 깜빡임 아티팩트를 다른 신경 신호와 분리할 때 ICA가 표준적으로 쓰인다.

관련: PCA = Karhunen–Loève 기저 → [[Orthonormal Basis Expansion]], [[Kolmogorov n-width]], [[DeepONet]] (최적 trunk)
