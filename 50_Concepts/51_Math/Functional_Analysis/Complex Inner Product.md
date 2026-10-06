---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Inner Product]]"
---
## 정의: 한쪽에만 켤레
$$\langle f,g\rangle = \int f(x)\,\overline{g(x)}\,dx$$

## 왜 켤레가 필요한가
$\int_0^{2\pi}e^{ix}\cdot e^{ix}dx = \int_0^{2\pi} e^{2ix}dx = 0$ — $|e^{ix}|=1$인 함수의 "길이 제곱"이 0?! 양정치성 붕괴.
더 간단히: $i\cdot i = -1$ → 길이 제곱이 음수.

$z = a+bi$의 길이 제곱은 $a^2+b^2$이어야 함:
| 계산 | 결과 |
|---|---|
| $z\cdot z$ | $a^2-b^2+2abi$ ✗ |
| $\bar z\cdot\bar z$ | $a^2-b^2-2abi$ ✗ |
| $z\cdot\bar z$ | $a^2+b^2$ ✓ |

**둘 다 켤레 = 안 붙인 것과 똑같이 망가짐.** 정확히 한쪽만.
벡터 $(1,i)$: 그냥 → $1-1=0$, 한쪽 켤레 → $1+1=2$ ✓
함수: $e^{ix}\overline{e^{ix}} = 1$ → $\langle e^{ix},e^{ix}\rangle = 2\pi$ ✓

## 막 붙여도 되나?
- 내적은 성질로 정의된 것 → 원하는 성질(양정치)이 나오게 정하면 됨
- **실수에선 $\bar a = a$** → 기존 실수 내적과 완전히 동일. 바꾼 게 아니라 확장

## 순서 바꾸면?
$$\langle f,g\rangle = \overline{\langle g,f\rangle}$$
예: $\langle i,1\rangle = i$, $\langle 1,i\rangle = -i$
그래도 OK: $\langle f,f\rangle$은 항상 $\ge0$ 실수, 직교($=0$)도 켤레 무관.

관습: 수학자는 뒤($\int f\bar g$), 물리학자는 앞($\langle\psi|\phi\rangle = \int\bar\psi\phi$).

## 푸리에 계수의 마이너스
$$c_k = \frac1{2\pi}\int f(x)\,e^{-ikx}dx, \qquad \overline{e^{ikx}} = e^{-ikx}$$
$f$ 쪽에 켤레를 주면 안 되는 이유:
1. $f$가 실수면 $\bar f = f$ → 아무 효과 없음
2. $\int f e^{-ikx}dx = \sum_j c_j\int e^{i(j-k)x}dx$ → $j=k$만 생존 → $c_k$
   $e^{+ikx}$를 곱하면 $e^{i(j+k)x}$ → $j=-k$ 생존 → **$c_{-k}$가 나옴**

## 왜 $e^{ikx}$ 기저를 쓰나
$\frac{d}{dx}e^{ikx} = ik\,e^{ikx}$ → 미분 연산자의 **고유함수**. 미분이 곱셈이 됨.
- $u_x \to ik\,c_k$, $u_{xx}\to -k^2c_k$ (확산항에선 $i$가 사라짐)
- 실수 $u$면 $c_{-k} = \overline{c_k}$ → 허수부 상쇄
- $\frac{d^2}{dx^2}$ 자기수반 → 실수 고윳값 (감쇠), $\frac{d}{dx}$ 반자기수반 → 순허수 고윳값 (진동/이동). 근거: 부분적분 $\langle u',v\rangle = -\langle u,v'\rangle$
- 연결: [[Operator_Math_Theory]], 양자역학 $\langle\psi|\phi\rangle$
