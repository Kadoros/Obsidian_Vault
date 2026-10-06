---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
---
비선형 동역학계를 **무한차원 선형 연산자**로 옮겨서 분석하는 도구.

시스템: $x_{t+1} = F(x_t)$ (비선형)

관측 함수(observable) $g(x)$에 작용하는 Koopman 연산자 $\mathcal{K}$:
$$\mathcal{K}g = g \circ F \quad\Leftrightarrow\quad (\mathcal{K}g)(x) = g(F(x))$$

- $\mathcal{K}$는 $F$가 비선형이어도 **항상 선형** (합성 연산은 선형 연산):
$$\mathcal{K}(\alpha g+\beta h) = \alpha \mathcal{K}g + \beta \mathcal{K}h$$

## Eigenfunction
$$\mathcal{K}\varphi = \lambda \varphi \quad\Leftrightarrow\quad \varphi(F(x)) = \lambda \varphi(x)$$
좋은 observable $\varphi$를 찾으면 미래 예측이 단순 곱셈:
$$\varphi(x_t) \to \lambda\varphi(x_{t-1}) \to \lambda^2 \varphi(x_{t-2}) \to \dots$$

## 한계
- 정확한 $\mathcal{K}$는 무한차원 → 실용적으로는 유한차원 근사 필요 (DMD: Dynamic Mode Decomposition)
- 핵심 난제: **어떤 observable $g$를 고를지** (직교성, 중요도 순서, 물리적 의미를 동시에 만족해야 eigenfunction에 가까워짐)

의미: "비선형 시스템을 선형 안경으로 보는 방법."

## 관련
- 비선형 PDE에서 모드가 섞이는 문제(대각화 실패)를 "대각화되는 공간으로 들어 올려" 해결 → [[Diagonalization of Convolution]], [[계수 구조에 물리 주입]]
- Koopman은 보통 비자기수반 → 자기수반 스펙트럼 이론 먼저 ([[함수해석학 로드맵]])
