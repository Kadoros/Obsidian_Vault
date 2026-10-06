---
tags:
  - concept
parent_concept:
  - "[[Neural Operator]]"
---
## 함수해석 관점의 Fourier layer
1. 입력 $v$의 푸리에 계수: $c_k = \langle v,e^{ikx}\rangle = \int v\,e^{-ikx}dx$ (마이너스 = 켤레, [[Complex Inner Product]]) — FFT는 이 적분의 격자 근사
2. 각 계수에 학습 가중치: $c_k\mapsto R_k\,c_k$
3. 고주파 절단 후 재조립: $\sum_{|k|\le K}R_kc_k\,e^{ikx}$ (절단 = "계수 감쇠 = 매끄러움" 가정)

## 한 줄 아이디어
배우려는 건 적분 연산자 $\int\kappa(x,y)v(y)dy$ ([[Integral Operator and Kernel]]). 커널을 $\kappa(x-y)$로 가정하면 **푸리에 기저에서 대각화** → 대각 성분 $R_k$만 학습 ([[Diagonalization of Convolution]]).
선형 PDE면 이상적으로 $R_k = 1/\lambda_k$.

## 한계 → 변형들
- 비주기/복잡 영역 → 푸리에가 고유기저 아님 → 라플라시안 고유함수, 웨이블릿
- 시간 방향 → Laplace Neural Operator
- 비선형 → [[Koopman Operator]] 기반 NO
- 한 층은 선형 (커널이 입력과 무관) ↔ [[Attention as Integral Operator]]
- [[Spectral Bias]], discretization invariance → [[Neural Operator]]

새 아키텍처 레시피: **"어떤 기저에서 이 연산자가 단순해지나?"**

## 관련 노트
- 수업: [[06_Neural Operator 2]]
- 대각 성분(symbol) 자체를 구조화: [[Fractional Operator]] ($|k|^{-2\alpha}$), [[Mellin Neural Operator]] (Mellin 기저)
