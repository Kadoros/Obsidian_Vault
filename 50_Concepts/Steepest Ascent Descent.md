---
tags:
  - concept
parent_concept:
  - "[[50_Concepts/Jacobian|Jacobian]]"
---
다변수 함수의 최적화에서, 현재 점의 그래디언트 방향으로 이동하며 매 스텝마다 **이동 거리(step size) $\alpha$를 line search로 직접 최적화**하는 방법.

1. 현재 점 $(x_0, y_0)$에서 그래디언트 계산:
$$\nabla f(x_0, y_0) = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}\right)$$

2. 그 방향으로의 직선 위 점 $(x_0,y_0) + \alpha \nabla f$를 $f$에 대입하면 $\alpha$에 대한 1변수 함수가 되고, 이를 미분해 $\frac{d}{d\alpha}=0$인 $\alpha$를 구해 다음 점으로 이동한다.

최댓값을 찾을 때는 Steepest Ascent(그래디언트 방향), 최솟값을 찾을 때는 Steepest Descent(그래디언트 반대 방향)이라 부른다.
