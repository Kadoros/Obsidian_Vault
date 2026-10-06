---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
  - "[[Fractional Operator]]"
---
## Mellin transform = log-warp 후 Laplace/Fourier
변수치환 $x = e^{-t}$ ($t=-\log x$):
$$M[f](s) = \int_0^1 f(x)\,x^{s-1}dx = \int_0^\infty \underbrace{f(e^{-t})}_{g(t)} e^{-st}\,dt = \mathcal{L}[g](s)$$
$s = i\xi$로 제한하면 그냥 Fourier:
$$M[f](i\xi) = \hat{g}(\xi)$$
→ $[0,1]$ 위의 Mellin transform = log-domain의 FFT로 계산 가능.

## MNO 아키텍처
```
u(x) → Log Warp (x_k = e^{-kh}) → FFT → kernel R_θ(ξ) 곱 → IFFT → Inverse Warp → v(x)
```
FNO의 kernel $\hat K(k)$는 **translation-equivariant**, MNO의 kernel $R(i\xi)$는 **scale-equivariant**.

## Euler-type 연산자의 Mellin symbol
$\mathcal{L} = x^2\partial_{xx} + \alpha x \partial_x$ 같은 scale-invariant PDE는 Mellin space에서 대수식이 됨:
$$\mathcal{M}[\mathcal{L}u](s) = s(s-1+\alpha)\cdot \hat U(s)$$
→ 학습할 kernel이 closed-form이라 학습 부담이 줄어듦.

## Gamma function과의 연결 (fractional diffusion)
$$R(s) = \frac{\Gamma(s+\alpha)}{\Gamma(s)}$$
fractional diffusion의 exact Mellin symbol. → [[Fractional Operator]]

## 의미
입력 도메인이 $[0,1]$ (bounded, scale 구조 있음)일 때, FNO의 translation-equivariance 대신 **scale-equivariance**를 활용해 power-law/Euler-Cauchy형 PDE를 더 압축적으로 표현.

## 함수해석 관점
FNO가 translation-convolution을 푸리에에서 대각화하듯, scale-convolution을 Mellin 기저에서 대각화 → [[Diagonalization of Convolution]], [[FNO]]
