---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
---
## Fractional power of an operator (Gamma function 정의)
$$L^{-\alpha} = \frac{1}{\Gamma(\alpha)} \int_0^\infty t^{\alpha-1} e^{-tL}\, dt$$
$e^{-tL}$은 heat semigroup → FNO의 convolution 구조와 자연스럽게 연결됨.

## Fourier space에서의 구현
$$\hat u(k) \mapsto |k|^{-2\alpha}\,\hat u(k)$$
- $\alpha=1$: 일반 Poisson ($L^{-1}$)
- $\alpha<1$: 덜 smooth → sharp feature 포착
- $\alpha>1$: 더 smooth → regularization 강화

$\alpha$를 learnable로 두면 "PDE의 regularity 자체를 학습"하는 것으로 해석 가능 (task-adaptive regularity).

## Gradient 안정성 이슈
$$\frac{\partial}{\partial\alpha}|k|^{-2\alpha} = -2\ln|k|\cdot|k|^{-2\alpha}$$
고주파($|k|$ 큼)에서 gradient 불안정 가능. $\Gamma(\alpha)$는 $\alpha\to0^+$에서 폭발.

## Mellin symbol과의 관계
$$R(s) = \frac{\Gamma(s+\alpha)}{\Gamma(s)}$$
fractional diffusion $\partial_t u = (-\partial_{xx})^\alpha u$의 exact Mellin symbol. → [[Mellin Neural Operator]]

## 의미
Spectral bias(저주파 편향) 완화: 기존 FNO는 $|k|^{-2}$로 eigenvalue decay rate가 고정되어 multiscale/anomalous diffusion을 못 표현 → $|k|^{-2\alpha}$로 decay rate를 데이터에서 학습.

## 함수해석 관점
$|k|^{-2\alpha}$는 푸리에 기저에서의 대각 성분 → [[Diagonalization of Convolution]], [[FNO]]의 $R_k$를 구조화한 것
