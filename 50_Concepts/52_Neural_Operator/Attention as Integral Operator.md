---
tags:
  - concept
parent_concept:
  - "[[Neural Operator]]"
  - "[[Integral Operator and Kernel]]"
---
## Attention = 입력 의존 커널의 적분 연산자
$$\mathrm{out}_i = \sum_j\mathrm{softmax}_j(\langle q_i,k_j\rangle)\,v_j \;\xrightarrow{\text{토큰 연속화}}\; \mathrm{out}(x) = \int\kappa(x,y)\,v(y)\,dy,\quad \kappa(x,y) = \mathrm{softmax}(\langle q(x),k(y)\rangle)$$
- $\langle q,k\rangle$: 내적 = "얼마나 같은 방향" = 유사도 ([[Inner Product]])
- softmax의 합=1 정규화 ≈ 리만 합의 $\Delta x$ 역할 (토큰 수가 바뀌어도 출력 크기 안 터짐)

## FNO와 비교
| | [[FNO]] | Attention |
|---|---|---|
| 커널 | $\kappa(x-y)$ | $\mathrm{softmax}(\langle q(x),k(y)\rangle)$ |
| 입력 의존 | ✗ (학습 후 고정) | **✓** |
| 한 층의 선형성 | 선형 | 이미 비선형 |
| 계산 | FFT $O(N\log N)$ | $O(N^2)$ |
뼈대(적분 연산자 + 점별 비선형)는 같고 커널이 다름. DeepONet vs [[HyperDeepONet]] 구도와 비슷 ("입력이 기저/커널까지 바꾸냐").

## 참고
- Neural Operator 논문(Kovachki et al.)에서 attention을 적분 연산자 특수 경우로 다룸
- Galerkin Transformer: attention을 Galerkin 투영으로 해석
