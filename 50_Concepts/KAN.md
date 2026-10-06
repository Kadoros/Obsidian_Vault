---
tags:
  - concept
parent_concept:
---
## Kolmogorov-Arnold 표현 정리
임의의 연속 다변수 함수는 단변수 함수들의 합성과 덧셈으로 표현 가능:
$$f(x_1,\dots,x_n) = \sum_q \Phi_q\left(\sum_p \phi_{q,p}(x_p)\right)$$
이미 2-layer 구조: $\sum_p \phi_{q,p}(x_p)$ = Layer 1, $\sum_q \Phi_q(\cdot)$ = Layer 2.

## KAN (Kolmogorov-Arnold Networks)
MLP의 (고정 activation + learnable weight)를 뒤집어, **learnable activation function**(보통 B-spline) + 고정 합을 사용:
$$x_{l+1,j} = \sum_i \phi_{l,j,i}(x_{l,i})$$
근사 오차율: $O(N^{-3})$ (B-spline) vs MLP $O(N^{-1})$ — 같은 파라미터 수에서 더 빠른 수렴.

## 구조적 한계: 좌표축 의존성
$f(\mathbf{x}) = \sum_n \varphi_n(x_n)$ 형태는 **입력 좌표축 = 의미 있는 축**이라는 가정.
좌표가 회전되면 ($z \to Rx$) 단일 레이어로 표현 불가.

### 반례: 회전된 진자 퍼텐셜
$$f_0(z_1,z_2) = 1-\cos(z_1), \qquad f_R(x_1,x_2) = 1-\cos(cx_1+sx_2)$$
($c=\cos\theta, s=\sin\theta$). $f_R = \varphi_1(x_1)+\varphi_2(x_2)$ 가정 후 교차편미분:
$$\partial^2_{x_1x_2}[\varphi_1+\varphi_2] = 0 \quad\text{vs}\quad \partial^2_{x_1x_2}[1-\cos(cx_1+sx_2)] = cs\cdot\cos(cx_1+sx_2)$$
$(0,0)$에서 $0 = cs$ 모순 ($cs\neq0$). → KAN은 좌표 혼합(rotation)을 표현 못 함.
실험적으로 $\theta=19.6°$ 회전 시 MSE $1174\times$ 증가.

## 의미
KAT는 분해의 **존재성**만 보장, **유일성은 보장 안 함** → 좌표계 선택이 곧 inductive bias. KAN은 "좌표 = 의미축"이 맞는 도메인(잘 설계된 피처)에 적합, 측정좌표 ≠ 의미좌표인 센서 데이터에는 부적합.
