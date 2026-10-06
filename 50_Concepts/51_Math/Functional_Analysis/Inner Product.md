---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[함수해석학 1강 - 함수를 벡터로]]"
---
## 정의: 같은 자리끼리 곱해서 다 더하기
$$\langle u,v\rangle = \sum_{i=1}^n u_i v_i \qquad\longrightarrow\qquad \langle f,g\rangle = \int_a^b f(x)\,g(x)\,dx$$
예: $u=(1,2,3),\ v=(4,0,-1)$ → $4+0-3 = 1$

## 내적 하나로 기하학이 다 나온다
- **길이**: $\|u\| = \sqrt{\langle u,u\rangle}$ (피타고라스). 함수에선 $L^2$ 노름 $\|f\| = \left(\int|f|^2dx\right)^{1/2}$ → 실험의 relative $L^2$ error
- **각도**: $\langle u,v\rangle = \|u\|\|v\|\cos\theta$ → 내적 0이면 직교 ([[Orthogonality]])
- **같은 방향 정도**: 크면 비슷, 0이면 무관, 음수면 반대 → 계수 = 내적의 직관 ([[Orthonormal Basis Expansion]])

## 왜 $\langle\cdot,\cdot\rangle$ 기호를 쓰나
$u\cdot v$는 특정 계산법. 기하학에 필요한 건 **성질**뿐:
1. 대칭: $\langle u,v\rangle = \langle v,u\rangle$ (복소수면 켤레 대칭 → [[Complex Inner Product]])
2. 선형: $\langle au+bw, v\rangle = a\langle u,v\rangle + b\langle w,v\rangle$
3. 양정치: $\langle u,u\rangle \ge 0$, $=0 \iff u=0$

이걸 만족하면 다 내적 → $\mathbb{R}^n$의 정리가 함수에도 그대로 통함.

## 왜 합이 적분이 되나 (센서 실험)
$[0,1]$에서 $f=g=1$(상수함수)를 센서 $n$개로 샘플링하면 $\sum f(x_i)g(x_i) = n$ → **센서 개수에 따라 답이 바뀜**.
각 점이 대표하는 폭 $\Delta x = 1/n$을 곱해 보정:
$$\sum_{i=1}^n f(x_i)g(x_i)\,\Delta x \;\xrightarrow{n\to\infty}\; \int_0^1 f(x)g(x)\,dx \quad(\text{리만 합})$$
적분 내적 = **센서를 무한히 촘촘하게 놓은 벡터 내적**.

### 직접 계산: $\int_0^1 x^2dx$ (오른쪽 끝점 리만 합)
| $n$ | 리만 합 $\frac{(n+1)(2n+1)}{6n^2}$ |
|---|---|
| 4 | 0.469 |
| 10 | 0.385 |
| 100 | 0.338 |
| 1000 | 0.3338 |
→ $\frac13$로 수렴. $x^2$이 증가함수라 오른쪽 끝점은 과대평가.

## 연구 연결
- 센서 수/해상도가 바뀌면 $L^2$ 오차 계산값 자체가 흔들림 → [[Neural Operator]]의 discretization invariance가 중요한 이유
- Attention의 $\langle q,k\rangle$도 내적 = 유사도 → [[Attention as Integral Operator]]
