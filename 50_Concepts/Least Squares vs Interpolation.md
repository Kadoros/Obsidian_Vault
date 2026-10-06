---
tags:
  - concept
parent_concept:
  - "[[50_Concepts/Interpolation|Interpolation]]"
---
$m$개의 데이터 점에 차수 $d$의 다항식을 최소제곱(least squares)으로 피팅할 때, $d$의 선택에 따라 의미가 달라진다.

- **$d = m-1$ (정확히 결정됨)**: Vandermonde 행렬이 정칙(non-singular)이 되어, 최소제곱 해가 곧 모든 점을 정확히 지나는 **보간(interpolation)**, 즉 Newton 전진차분/Gregory-Newton 다항식과 동일해진다. 잔차 = 0.
- **$d < m-1$ (과결정, over-determined)**: 모든 점을 정확히 지나지 않는 근사(approximation)가 되어 잔차 ≠ 0.

$d$를 일부러 줄이는 것은 (Ridge/Tikhonov 같은) 정식 정규화가 아니라 **모델 차수 축소(model order reduction / truncation)**이며, 고차 다항식 보간에서 발생하는 Runge's phenomenon을 피하고 노이즈에 덜 민감하게 만드는 효과가 있다.

관련: least-squares = 정사영 → [[Orthonormal Basis Expansion]], [[GN-Operator]]
