---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Galerkin Projection]]"
  - "[[Operator_Math_Theory]]"
---
## 에너지 변화는 $A$ 의 대칭 부분이 결정
$\dot c = Ac$, $E = c^\top c$ (정규직교, 파세발):
$$\frac{dE}{dt} = c^\top(A+A^\top)c$$

## 보존: $A^\top = -A$ (반대칭)
$\dot E = 0$, 고윳값 순허수. 이류·파동·슈뢰딩거. ($\frac{d}{dx}$ 반자기수반, 고윳값 $ik$ — [[Complex Inner Product]])

## 감쇠: $A + A^\top\preceq0$ — 고윳값 음수만으론 부족!
반례 (non-normal):
$$A = \begin{pmatrix}-1&10\\0&-1\end{pmatrix},\quad e^{tA} = e^{-t}\begin{pmatrix}1&10t\\0&1\end{pmatrix}$$
고윳값 $-1$ 인데 $t\approx1$ 에서 $\|e^{tA}\|\approx3.7$ → 에너지 일시적 10배+ (과도 성장). 롤아웃 폭발의 씨앗.

## 구조로 박기
$$A = \underbrace{(W - W^\top)}_{S}\;-\;\underbrace{(LL^\top + \varepsilon I)}_{D}\ \Rightarrow\ A + A^\top = -2D\preceq0\ (\text{항상})$$
- 입력 의존: $A(a) = S(a) - D(a)$ → **모든 입력**(분포 밖 포함)에서 보장. 이미 NIGO (ICML 2026)가 함 → [[TCO 관련 연구 지도]]
- 해석: $S$ = 에너지를 옮김(이류), $D$ = 없앰(확산)
- 비선형: $N(c) = B(c)c$, $B(c)$ 반대칭 → $c^\top N(c) = 0$ ([[Triadic Interaction Tensor]])
- closure: $-D_{\text{cl}}(c)c$ (잘린 고주파로 갈 에너지를 빼감)
- 비정규직교: $MA + A^\top M\preceq0$, $A = M^{-1}(S-D)$
- 적분기: implicit midpoint는 이차 불변량 보존, explicit Euler는 반대칭계에서 에너지 증가
- 외력: port-Hamiltonian 구조

## 무한차원 버전 (3강 이후)
- 소산 연산자 $\langle\mathcal{A}u,u\rangle\le0$ ↔ 축소 반군 $\|e^{t\mathcal{A}}\|\le1$: **Lumer–Phillips 정리**
- 반자기수반 ↔ 유니터리 군: **Stone 정리**
- 비이차 엔트로피로의 확장 → [[TCO 열린 문제 후보]] 2번
