---
tags:
  - concept
parent_concept:
---
$$\alpha_i = 1 - \exp(-\sigma_i \delta_i)$$
- $\sigma_i$: 그 지점의 밀도 (안개가 얼마나 진한가?)
    
- $\delta_i$: 그 구간의 길이 (안개를 얼마나 길게 지나가는가?)
    
- **의미:** "밀도가 높거나 구간이 길수록, 빛을 더 많이 막는다(알파 값이 커진다)."
$$T_i = \exp\left( -\sum_{j=1}^{i-1} \sigma_j \delta_j \right)$$
$e^{a+b} = e^a \cdot e^b$

$$T_i = \prod_{j=1}^{i-1} \exp(-\sigma_j \delta_j)$$
$$T_i = (1 - \alpha_1) \times (1 - \alpha_2) \times \dots \times (1 - \alpha_{i-1})$$
1번 레이어에서 통과한 양($1-\alpha_1$)" 곱하기 "2번 레이어에서 통과한 양($1-\alpha_2$)"... 즉, 내 순서가 올 때까지 앞에서 안 막히고 살아남은 비율


$$\hat{C}(r) = \underbrace{T_1 \alpha_1 c_1}_{\text{1번 레이어}} + \underbrace{T_2 \alpha_2 c_2}_{\text{2번 레이어}} + \dots$$

$$\hat{C}(r) = { \alpha_1 c_1} + {(1 - \alpha_1) \cdot \alpha_2 c_2 } + {(1 - \alpha_1) \cdot (1 - \alpha_2) \cdot \alpha_2 c_2 } + \dots  $$