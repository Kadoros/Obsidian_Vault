---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[함수해석학 2강 - 완비성과 힐베르트 공간]]"
---
## 수렴은 노름에 따라 다르다
$f_n\to f \iff \|f_n-f\|\to0$. 예: $[0,1]$에서 $x^n$
- $L^2$: $\|x^n\|^2 = \frac1{2n+1}\to0$ → 수렴
- 최댓값 노름: $\max|x^n| = 1$ → 수렴 안 함 (오른쪽 끝 한 점)

## 코시 수열
극한을 모를 때: $\|f_n - f_m\|\to0$ ($n,m\to\infty$). 수렴 ⇒ 코시, 반대는 공간에 따라 다름.

## 완비 = 구멍 없음
- $\mathbb{Q}$: $1, 1.4, 1.41,\dots$ 코시인데 $\sqrt2\notin\mathbb{Q}$ → 구멍
- 연속함수 + $L^2$ 노름: 점점 가파른 경사로 $f_n$ 은 코시, 극한은 **계단함수**(불연속) → 구멍
- 메운 공간 = $L^2$ (엄밀히는 르베그 적분 필요). 충격파 같은 불연속 해도 들어감 → PDE 이론이 완비 공간($L^2$, 소볼레프)에서 시작하는 이유

## 정의
- **바나흐 공간**: 노름 + 완비
- **힐베르트 공간**: 내적 + 완비 = [[Inner Product]]의 기하 + 극한 자유

## 무한합 수렴 (1강 질문의 답)
$S_n = \sum_{k\le n}c_k\varphi_k$, 직교라서 피타고라스:
$$\|S_m - S_n\|^2 = \sum_{k=n+1}^m|c_k|^2$$
$\sum|c_k|^2<\infty$ ⇒ 코시 ⇒ 완비라서 수렴. $c_k = \langle f,\varphi_k\rangle$ 는 항상 만족 (**베셀** $\sum|c_k|^2\le\|f\|^2$).

## 기저 충분성 (두 번째 "완비")
수렴한 함수가 $f$ 와 같으려면 기저가 모자라지 않아야 함 = **완비 정규직교계(정규직교기저)** → **파세발** $\|f\|^2 = \sum|c_k|^2$.
- 공간이 완비: 구멍 없음
- 기저가 완비: 모자라지 않음

## 함수 = 계수 수열
$$f\longleftrightarrow(c_1,c_2,\dots)\in\ell^2,\qquad \|f\|_{L^2} = \|c\|_{\ell^2}$$
함수 공간에서 할 일을 계수 공간에서 해도 잃는 게 없음 → DeepONet branch·FNO 모드·[[TCO 아이디어 정리|TCO]]의 수학적 근거. 관련: [[Orthonormal Basis Expansion]], [[Galerkin Projection]]
