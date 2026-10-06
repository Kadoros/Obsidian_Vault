---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
---
## Gregory-Newton (Newton forward-difference) polynomial
등간격 센서 $a(x_0),\dots,a(x_{m-1})$, $x_i=ih$를 falling-factorial 기저로 표현:
$$a(x) = \sum_{k=0}^{m-1} \frac{\Delta^k a(x_0)}{k!}\, x^{(k)}, \qquad x^{(k)} = x(x-1)\cdots(x-k+1)$$
$d=m-1$차로 모든 점을 정확히 통과하는 **보간(interpolation)**, 잔차 0.

## Least-squares polynomial embedding (실제 구현)
$$f_{\text{poly}} = \arg\min_{\{c_k\}_{k=0}^d} \sum_{i=0}^{m-1}\Big(a(x_i)-\sum_k c_k x_i^k\Big)^2, \quad d<m-1$$
과결정(over-determined) 시스템 → **근사(approximation)**, 잔차 $\neq 0$이지만 노이즈에 강하고 Runge 현상 회피.
오차: $\|a-f_{\text{poly}}\|_{L^2}=O(h^{\min(s,d+1)})$ for $a\in H^s$.

**GN poly와의 관계**: $d=m-1$일 때 least-squares ≡ GN 보간(특수 케이스). $d<m-1$은 GN poly의 "model order reduction"(정규화가 아닌 차수 축소)에 해당.

## GN-Operator (GNR) 파이프라인
PDE solution operator를 적은 데이터(n=10~50)로 학습하기 위한 2단계 구조:

1. **Analytic prior (파라미터 0개)**: $f_{\text{poly}}$를 알려진 PDE $\mathcal{L}[u]=f$에 대입해 해석적으로 역연산:
$$u_{\text{GN}} = \mathcal{L}^{-1}[f_{\text{poly}}]$$
다항식 입력에 대해 $\mathcal{L}^{-1}$가 closed-form (Poisson: 두 번 적분, heat: Fourier mode propagation).

2. **Residual correction (소형 네트워크 <1k params)**:
$$u_{\text{exact}} - u_{\text{GN}} = O(h^{\min(s,d+1)})$$
$f$가 정확히 polynomial이면 잔차 0.

## 의미
- $\mathcal{L}^{-1}$이 polynomial → polynomial(또는 low-rank Fourier expansion)로 매핑되는 구조를 이용해, 데이터 없이(zero-shot, zero offline data) PDE-consistent baseline을 구성.
- 핵심 가치는 "exactness"가 아니라 **trainable parameter 0, offline data 0으로 prior를 만들 수 있다**는 점 — 불연속 계수(예: 반도체 열전도율 286배 차이) 같은 model mismatch도 residual이 흡수.

## 함수해석 관점
다항식 기저 전개 + least-squares = 기저 공간으로의 정사영 → [[Orthonormal Basis Expansion]], [[Least Squares vs Interpolation]]
