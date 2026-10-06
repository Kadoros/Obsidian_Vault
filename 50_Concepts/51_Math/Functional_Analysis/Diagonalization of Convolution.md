---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Integral Operator and Kernel]]"
---
## 대각화 복습
대각행렬은 각 성분에 숫자 하나씩만 곱하고 **섞지 않음**:
$$\begin{pmatrix}2&0\\0&5\end{pmatrix}\begin{pmatrix}a\\b\end{pmatrix} = \begin{pmatrix}2a\\5b\end{pmatrix}$$
**대각화** $A = PDP^{-1}$: 고유벡터 기저로 바꾸면 복잡한 행렬도 대각처럼 동작.

## 합성곱 연산자의 고유함수 = $e^{ikx}$
$z = x-y$ 치환:
$$\int\kappa(x-y)\,e^{iky}dy = \underbrace{\left(\int\kappa(z)e^{-ikz}dz\right)}_{\hat\kappa(k):\ \text{숫자 하나}}e^{ikx}$$
$e^{ikx}$가 들어가서 $e^{ikx}$ 그대로 나오고 숫자만 곱해짐 → **고유함수**, 고윳값 $\hat\kappa(k)$.
→ 푸리에 기저에서 합성곱 = 각 계수에 숫자 하나 곱하기 = **대각행렬** (합성곱 정리).

## 선형 PDE의 해 연산자도 같은 그림
$\mathcal{L}\varphi_k = \lambda_k\varphi_k$ 이면 $\mathcal{L}^{-1}$은 고유기저에서 $c_k\mapsto c_k/\lambda_k$.
"무한차원 행렬이 대각행렬이 된다" ([[Orthonormal Basis Expansion]] 참고)

## FNO의 $R_k$
[[FNO]]는 커널 $\kappa$ 대신 이 "숫자 하나" $R_k$를 **학습 파라미터**로 둠 = $k$번째 주파수를 얼마나 키우고 줄일지 정하는 필터.
선형 PDE면 이상적으로 $R_k = 1/\lambda_k$.

## 비선형에선 깨짐
Burgers $u_t+uu_x=\nu u_{xx}$의 푸리에 계수:
$$\frac{dc_k}{dt} = -\nu k^2c_k - \frac{ik}{2}\sum_{p+q=k}c_pc_q$$
선형항은 대각, 비선형항은 **합성곱** (곱 ↔ 합성곱; $e^{ipx}e^{iqx}=e^{i(p+q)x}$) → 모드가 섞임, 에너지 캐스케이드.
→ 대각화되는 공간으로 들어 올리기: [[Koopman Operator]]

## 다른 기저에서 대각화하는 변형들
- [[Fractional Operator]] — $|k|^{-2\alpha}$ = 푸리에 기저의 대각 성분(symbol)을 학습
- [[Mellin Neural Operator]] — scale-convolution(Euler형 연산자)은 Mellin 기저에서 대각
- [[06_Neural Operator 2]] — FNO 수업 노트
