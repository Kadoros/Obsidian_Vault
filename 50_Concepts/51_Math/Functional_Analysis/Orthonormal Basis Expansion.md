---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[함수해석학 1강 - 함수를 벡터로]]"
---
## 핵심: 계수 = 내적
정규직교기저 $\{\varphi_k\}$에 대해
$$f = \sum_{k=1}^\infty c_k\varphi_k, \qquad c_k = \langle f,\varphi_k\rangle = \int f(x)\varphi_k(x)\,dx$$
$c_k$ = "$f$ 안에 $k$번째 파동이 얼마나 들어 있나" = $f$를 $\varphi_k$ 방향으로 **정사영**한 길이.

## 용어
- **정규직교**: 서로 직교 + 길이 1. $\langle\varphi_k,\varphi_j\rangle = \delta_{kj}$
- **기저**: 이걸로 모든 벡터를 조합할 수 있는 뼈대
- **정사영**: 어떤 방향에 수직으로 비춘 그림자

## $\mathbb{R}^2$ 예: 45° 돌린 기저
$v=(3,4)$, $e_1 = (\tfrac1{\sqrt2},\tfrac1{\sqrt2})$, $e_2 = (-\tfrac1{\sqrt2},\tfrac1{\sqrt2})$
연립방정식 없이 내적만: $c_1 = \tfrac7{\sqrt2}$, $c_2 = \tfrac1{\sqrt2}$ → $(3.5,3.5)+(-0.5,0.5) = (3,4)$ ✓

## 왜 성립하나 — 두 개의 주장
### 1. (쉬움) 쓸 수 *있다면* 계수는 반드시 내적
$f = \sum_k c_k\varphi_k$ 양변에 $\varphi_j$ 내적:
$$\langle f,\varphi_j\rangle = \sum_k c_k\langle\varphi_k,\varphi_j\rangle = c_j$$
직교라서 다른 항이 죽고, 정규라서 $c_j$만 깔끔히 남음. **정규직교기저를 쓰는 이유 전부.**
확인: $f = 2\varphi_1 + 5\varphi_3$ → $\langle f,\varphi_3\rangle = 5$

### 2. (깊음) 애초에 그렇게 쓸 수 *있나*? → 완비성
- 기저가 모자라면 표현 불가 ($\mathbb{R}^3$에서 $e_1,e_2$로 $e_3$ 못 만듦)
- $[0,\pi]$에서 $\{\sin kx\}$는 충분함 (푸리에 해석의 핵심 정리) — 증명엔 해석학 필요
- 여기서 "$=$"은 **$L^2$ 의미**: $\|f - \sum_{k\le N}c_k\varphi_k\|\to0$. 점별로는 틀릴 수 있음
- → 2강: 완비성, 힐베르트 공간

## 예: $f(x)=x$ on $[0,\pi]$
$c_1 = \sqrt{\tfrac2\pi}\int_0^\pi x\sin x\,dx = \sqrt{\tfrac2\pi}\cdot\pi = \sqrt{2\pi}$ → $c_1\varphi_1 = 2\sin x$
$$x = 2\left(\sin x - \frac{\sin 2x}{2} + \frac{\sin 3x}{3} - \cdots\right)$$
계수가 $1/k$로 **천천히** 감쇠 — $x=\pi$에서 $f=\pi$인데 사인은 모두 0 (끝점 불일치 → 깁스).

## 계수가 말해주는 것 (선형 자기수반 PDE)
$\mathcal{L}\varphi_k = \lambda_k\varphi_k$, $\mathcal{L}u=f$이면
$$c_k = \frac{\langle f,\varphi_k\rangle}{\lambda_k}$$
- 고유기저에서 해 연산자는 **대각** (성분마다 $\lambda_k$로 나누기) → [[Diagonalization of Convolution]]
- **감쇠 속도 = 매끄러움**: $\|u\|_{H^s}^2 \sim \sum\lambda_k^s|c_k|^2$
- **파세발**: $\|u-u_N\|^2 = \sum|c_k-\hat c_k|^2$ → 오차 = 계수 오차
- 열방정식: $c_k(t) = c_k(0)e^{-\lambda_kt}$ (고주파일수록 빨리 사라짐)
- 잔차의 쌍대 노름: $\|r\|_{H^{-1}}^2\sim\sum|r_k|^2/\lambda_k$ → "올바른 노름의 loss" = "계수별 가중치"

## 연구 연결
- [[DeepONet]] branch 출력이 이상적으로 배워야 하는 숫자
- [[FNO]] 1단계 = 푸리에 계수 구하기
- [[계수 구조에 물리 주입]]

## 같은 아이디어가 나오는 곳
- [[GN-Operator]] — 다항식 기저 전개, least-squares = 기저 공간으로의 정사영
- [[Least Squares vs Interpolation]] — 차수 축소 = 모드 절단
- [[XNO expriment]] — 기저 변환(change of basis)
- [[Spectral Bias]] — 계수 감쇠와 주파수
- [[ICA vs PCA]] — PCA = 데이터에 최적인 정규직교기저 (Karhunen–Loève)

다음: [[Completeness and Hilbert Space]] (완비성, 파세발)
