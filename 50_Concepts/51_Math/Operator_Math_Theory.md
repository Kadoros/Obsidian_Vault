---
tags:
  - concept
parent_concept:
---
## 연산자(Operator)
함수공간 위의 변환 $T: f \mapsto Tf$. 선형 연산자:
$$T(f+g) = T(f) + T(g), \quad T(cf) = cT(f)$$

## 미분 연산자
$$D^n f = \frac{d^n f}{dx^n}, \qquad L = a_n D^n + a_{n-1}D^{n-1} + \cdots + a_0$$
다항식처럼 다룰 수 있어 ODE/PDE의 algebraic structure 분석에 사용.

## 적분 연산자
$$T[f](x) = \int_a^b K(x,y)\, f(y)\, dy$$
$K(x,y)$: 커널(kernel). Green's function이 대표적인 예 (PDE의 inverse operator).

## 고유값/스펙트럼
$$Tv = \lambda v$$
스펙트럼(spectrum) = 고유값의 집합, 연산자의 핵심 성질을 담음.

### 스펙트럼 정리 (자기수반 연산자)
$$T = \int \lambda \, dE(\lambda)$$
무한차원에서의 대각화.

| 종류 | 조건 | 특징 |
|---|---|---|
| 자기수반 | $T = T^*$ | 고유값이 실수 |
| 유니터리 | $TT^* = I$ | 길이 보존 |
| 정규 | $TT^* = T^*T$ | 스펙트럼 분해 가능 |
| 컴팩트 | 유계집합 → 상대적 컴팩트 | 무한차원의 "행렬" |

## 양자역학에서의 연산자
- 위치: $\hat{x}\psi(x) = x\psi(x)$
- 운동량: $\hat{p} = -i\hbar \partial_x$
- 교환자(commutator): $[\hat{x},\hat{p}] = i\hbar$

## Neural Operator (학습 대상)
$$\mathcal{G}_\theta : a(x) \mapsto u(x), \quad u = \mathcal{L}^{-1}[a]$$
입력 함수 $a$를 PDE solution $u$로 보내는 연산자 자체를 신경망으로 근사. (FNO, DeepONet, [[Mellin Neural Operator]], [[GN-Operator]] 등) → 자세한 정의는 [[Neural Operator]]

## 함수해석학 공부
→ [[함수해석학 로드맵]] (강의 노트, 개념 노트, 연습문제)
