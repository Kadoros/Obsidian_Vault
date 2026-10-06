---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
---
## Physics-Informed Neural Network (PINN)
PDE의 해 $u_\theta(x,t)$를 신경망으로 직접 근사하고, 손실함수에 PDE residual을 넣어 물리 법칙을 강제:
$$\mathcal{L} = \mathcal{L}_{\text{data}} + \lambda_{\text{pde}}\mathcal{L}_{\text{pde}} + \lambda_{\text{bc}}\mathcal{L}_{\text{bc}}$$

- $\mathcal{L}_{\text{data}} = \frac{1}{N}\sum_i |u_\theta(x_i,t_i) - u_i|^2$ — 관측값과의 오차 (없어도 됨)
- $\mathcal{L}_{\text{pde}} = \frac{1}{M}\sum_j |\mathcal{N}[u_\theta](x_j,t_j) - f(x_j,t_j)|^2$ — PDE residual, $\mathcal{N}$은 미분 연산자 (AutoDiff로 계산)
- $\mathcal{L}_{\text{bc}}$ — 경계/초기조건 residual

## 의미
mesh 없이 임의의 collocation point에서 PDE residual을 계산 → 데이터가 적어도 물리 법칙이 regularizer 역할. Inverse problem(관측값으로 PDE 파라미터 역추정)에 특히 강함.

## 알려진 한계
- **Spectral bias**: 저주파 성분 위주로 학습되어 고주파/stiff 해에서 학습 실패
- **Gradient pathology**: $\mathcal{L}_{\text{data}}$, $\mathcal{L}_{\text{pde}}$, $\mathcal{L}_{\text{bc}}$ 사이 gradient 크기 불균형 → 학습 불안정
- 새 초기조건/PDE 파라미터마다 **재학습** 필요 (한 PDE의 한 해만 학습) → [[Neural Operator]]와의 핵심 차이

## 함수해석 관점
PDE residual은 쌍대공간($H^{-1}$)에 사는데 $L^2$로 재는 불일치 → [[계수 구조에 물리 주입]], [[함수해석학 로드맵]]
