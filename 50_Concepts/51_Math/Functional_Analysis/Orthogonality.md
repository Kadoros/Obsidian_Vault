---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[함수해석학 1강 - 함수를 벡터로]]"
---
## 정의: 내적 = 0
$$f\perp g \iff \langle f,g\rangle = 0$$

## 왜 "내적 0"이 직교인가
$\mathbb{R}^2$에서 $u=(3,4),\ v=(-4,3)$: 그리면 직각, 내적 $-12+12=0$.
$$\|u+v\|^2 = \|u\|^2 + \|v\|^2 + 2\langle u,v\rangle$$
$\langle u,v\rangle=0$일 때만 피타고라스 성립 = 직각.

함수 사이 각도는 눈으로 못 봄 → $\mathbb{R}^n$에서 직교와 동치였던 "내적 = 0"을 **정의로 채택**. 그러면 피타고라스가 따라옴:
$$\|\sin x + \sin 2x\|^2 = \|\sin x\|^2 + \|\sin 2x\|^2$$
물리적 의미: **두 파동을 합쳐도 간섭 없이 에너지가 그냥 더해진다.**

## 예: $\sin x \perp \sin 2x$ on $[0,\pi]$
$$\int_0^\pi \sin x\sin 2x\,dx = \int_0^\pi \tfrac12(\cos x - \cos 3x)\,dx = 0$$
($\sin A\sin B = \tfrac12[\cos(A-B) - \cos(A+B)]$)
직관: $\sin x\sin 2x$는 앞 절반 양수, 뒤 절반 음수, 면적이 같아 상쇄.
일반적으로 $m\ne n$이면 $\sin mx\perp\sin nx$.

## 정규화
$\|\sin kx\|^2 = \int_0^\pi\sin^2kx\,dx = \int_0^\pi\frac{1-\cos2kx}{2}dx = \frac\pi2$ ($k$와 무관)
$$\varphi_k(x) = \sqrt{\tfrac{2}{\pi}}\,\sin kx \quad (\|\varphi_k\|=1)$$
직관 체크: $\sin^2$ 평균 $\frac12$ × 구간 길이 $\pi$ = $\frac\pi2$.

직교 + 길이 1 = **정규직교** → [[Orthonormal Basis Expansion]]
