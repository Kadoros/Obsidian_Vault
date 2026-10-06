---
tags:
  - concept
parent_concept:
---
$$\mathbf{h} = \sigma\left(
\underbrace{\begin{bmatrix}
w_{11} & w_{12} & \cdots & w_{1n} \\
w_{21} & w_{22} & \cdots & w_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
w_{n1} & w_{n2} & \cdots & w_{nn}
\end{bmatrix}}_{W:\ n\times n}
\underbrace{\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}}_{x:\ n\times 1}
+
\underbrace{\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{bmatrix}}_{b:\ n\times 1}
\right)$$
$$f(x) = 
\underbrace{\begin{bmatrix}
u_{11} & u_{12} & \cdots & u_{1r} \\
u_{21} & u_{22} & \cdots & u_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
u_{K1} & u_{K2} & \cdots & u_{Kr}
\end{bmatrix}}_{U:\ K\times r}
\underbrace{\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_r
\end{bmatrix}}_{\mathrm{diag}(\lambda):\ r\times r}
\ \phi\!\left(
\underbrace{\begin{bmatrix}
v_{11} & v_{12} & \cdots & v_{1d} \\
v_{21} & v_{22} & \cdots & v_{2d} \\
\vdots & \vdots & \ddots & \vdots \\
v_{r1} & v_{r2} & \cdots & v_{rd}
\end{bmatrix}}_{V^\top:\ r\times d}
\underbrace{\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_d \end{bmatrix}}_{x:\ d\times 1}
\right)
+
\underbrace{\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_K \end{bmatrix}}_{b:\ K\times 1}$$
$$U \xrightarrow{\text{학습 후}}
\underbrace{\begin{bmatrix}
0 & 0 & +1 & \cdots & 0 \\
-1 & 0 & 0 & \cdots & 0 \\
0 & +1 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & s_r
\end{bmatrix}}_{U:\ K\times r,\ \text{각 열에 } \pm1 \text{ 하나뿐}}$$

$$V^{(0)} \xleftarrow{\text{LDA}}
\underbrace{\begin{bmatrix}
v_{11} & v_{12} & \cdots & v_{1r} \\
v_{21} & v_{22} & \cdots & v_{2r} \\
\vdots & \vdots & \ddots & \vdots \\
v_{d1} & v_{d2} & \cdots & v_{dr}
\end{bmatrix}}_{V:\ d\times r,\ V^\top V = I_r,\ \text{LDA 방향}}$$

$$U^{(0)} \xleftarrow{\text{init}}
\underbrace{\begin{bmatrix}
1 & 0 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & 1
\end{bmatrix}}_{U^{(0)} = I_K:\ K\times r,\ \text{항등 (대각선 모두 }+1\text{)}}$$
$$U \xrightarrow{\text{학습 후}}
\underbrace{\begin{bmatrix}
0 & 0 & +1 & \cdots & 0 \\
-1 & 0 & 0 & \cdots & 0 \\
0 & +1 & 0 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
0 & 0 & 0 & \cdots & s_r
\end{bmatrix}}_{U:\ K\times r,\ \text{각 열에 } \pm1 \text{ 하나뿐}}$$

$$f(x) = 
\underbrace{\begin{bmatrix}
0 & -1  & \cdots & 0 \\
+1 & 0  & \cdots & 0 \\
\vdots  & \vdots & \ddots & \vdots \\
0 & 0  & \cdots & s_r
\end{bmatrix}}_{U:\ K\times r}
\underbrace{\begin{bmatrix}
\lambda_1 & 0 & \cdots & 0 \\
0 & \lambda_2 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & \lambda_r
\end{bmatrix}}_{\mathrm{diag}(\lambda):\ r\times r}
\ \phi\!\left(
\underbrace{\begin{bmatrix}
v_{11} & v_{12} & \cdots & v_{1d} \\
v_{21} & v_{22} & \cdots & v_{2d} \\
\vdots & \vdots & \ddots & \vdots \\
v_{r1} & v_{r2} & \cdots & v_{rd}
\end{bmatrix}}_{V^\top:\ r\times d}
\underbrace{\begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_d \end{bmatrix}}_{x:\ d\times 1}
\right)
+
\underbrace{\begin{bmatrix} b_1 \\ b_2 \\ \vdots \\ b_K \end{bmatrix}}_{b:\ K\times 1}$$
