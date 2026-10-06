---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Operator_Math_Theory]]"
  - "[[함수해석학 1강 - 함수를 벡터로]]"
---
## 연산자 = 함수를 넣으면 함수가 나오는 것
| | 입력 → 출력 |
|---|---|
| 함수 | 숫자 → 숫자 |
| 행렬 | 벡터 → 벡터 |
| **연산자** | 함수 → 함수 |
예: $\frac{d}{dx}$ ($\sin x\mapsto\cos x$), [[DeepONet]]이 배우는 해 연산자 $\mathcal{G}: a\mapsto u$ → 그래서 "operator learning".

## 적분 연산자 = 행렬곱의 연속 버전
$$(Av)_i = \sum_j A_{ij}v_j \qquad\longrightarrow\qquad (\mathcal{K}v)(x) = \int\kappa(x,y)\,v(y)\,dy$$
"번호 → $x$, 합 → 적분" ([[Inner Product]]와 같은 규칙).

**커널 $\kappa(x,y)$ = 연속 버전 행렬의 성분** = "입력의 $y$ 위치 값이 출력의 $x$ 위치에 얼마나 영향을 주나".
(선대의 커널=영공간과는 다른 뜻. 여기선 적분 커널. Green's function이 대표 예)

## 합성곱 커널 $\kappa(x-y)$
두 점의 **거리만** 보고 위치는 무시 → 어디서든 같은 규칙 (CNN 필터와 같음).
행렬로는 $A_{ij}$가 $i-j$에만 의존 → 대각선마다 같은 값 (Toeplitz/circulant).
→ 푸리에 기저에서 대각화: [[Diagonalization of Convolution]]

## 세 모델 비교
| | 내적이 쓰이는 곳 | 커널 |
|---|---|---|
| [[FNO]] | 푸리에 계수 $\langle v,e^{ikx}\rangle$ | $\kappa(x-y)$, 고정, 푸리에에서 대각 |
| [[Attention as Integral Operator\|Attention]] | 유사도 $\langle q,k\rangle$ | $\mathrm{softmax}(\langle q(x),k(y)\rangle)$, **입력 의존** |
| [[DeepONet]] | 이상적 branch 출력 = 계수 | 고정 기저 $t_k$ 위 선형결합 |
세 모델 모두 "함수공간 위 적분 연산자를 어떻게 근사하냐"의 서로 다른 답.

## 수업 노트
- [[05_Neural Operator 1]] — kernel integral 정의
- [[06_Neural Operator 2]] — GNO/LNO/MGNO/FNO kernel 변형
- [[XNO expriment]] — 체비쇼프 기저에서 적분 연산자를 행렬로 쓴 실험
