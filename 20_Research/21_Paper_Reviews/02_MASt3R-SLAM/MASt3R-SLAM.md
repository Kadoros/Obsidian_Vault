---
tags:
  - Paper
  - SLAM
parent_concept: "[[../../../50_Concepts/SLAM|SLAM]]"
status: 2nd Reading
date: 2026-01-27
paper_link: https://arxiv.org/abs/2412.12392
pdf: "[[PDF/MASt3R-SLAM_pdf.pdf]]"
code_link:
---

# 요약 
- 핵심 
	- [[MASt3R]] 이라는 인공 신경망을 통해서 두 이미지 인풋을 통해 3d point map 과 특징점 백터 그리고 신뢰도 를 각각 만들고 이를 통해서 설계된 실시간  [[../../../50_Concepts/Monocular SLAM|Monocular SLAM]], [[Dense SLAM]]을 구현
- 특징 
	- 많은 카메라 모델에 대하여 [[MASt3R]] 가 학습 되었기에 카메라 모델에 대한 정보가 없어도 가능함, 즉 K 행열 없이 구현됨 (play-and-play)시스탬
	-  [[MASt3R]] 의 강력한 사전 지식 덕분에 일관된 포즈와 밀집된 3D 형상을 구현 할 수 있음
- 성능
	- 4090환경에서 15fps : 실시간 성능

# 되는 것
- 아무 카메라나 사용해도됨 
	- 즉 K 행열 연산 안해도됨
- 3d 형상이 고품질
- 실시간 처리
- 카메라 캘리브레이션이 있으면 sota 성능

# 안되는 것
- 카메라가 왜곡이 심하면 작동 안됨
- 무거움 
- 실시간 3d 맵 전역 최적화; 포즈는 전역 최적화함
- 어려운 환경 예 저조도 격한 움직임

# Sections

## Abstract
- This paper present a real-time monocular [[../../../50_Concepts/Dense SLAM|Dense SLAM]] system designed bottom-up from [[../../../50_Concepts/MASt3R|MASt3R]], a two-view 3D reconstruction and matching prior.
- MASt3R의 강력한 능력 지능
- 와일드한 현장에서 강함
- 카메라 정보 필요 없음 (plug-and-play)
	- 만약 있으면 정확도 확 상승
- Efficient Pointmap Matching, 
	- MASt3R는 무거움 이걸 해결함
- Camera Tracking and Local Fusion
- Graph Construction and Loop Closure
	- 카메라 경로 그래프 형태로 , Loop Closure로 오차 잡음
- Second-order Global Optimisation
- 실시간으로 구동  15fps

## 3. Method
### 3.2. Pointmap Matching
- 
$$\mathbf{p}^* = \arg \min_{\mathbf{p}} \left\| \psi \left( [\mathbf{X}_i^i]_{\mathbf{p}} \right) - \psi (\mathbf{x}) \right\|^2 . \space \space \space \space \space where \space  x∈ X_{i}^j$$
- ⭐️ ***p는 pixel coordinates이며 이를 최적화 한다
	- 매칭 문제를 검색이 아닌 최적화로 본것이 흥미롭다
- 주의 여기서 p는 실수이다!!
- 즉 모든 좌표계는 i 에서 찍은 걸로 간주할 때, j위치에 찍은 어떤 포인트와 카메라 중심 선과 대하여 i위치에서 찍은 포인트맵중 p에서의 포인트와 카메라 중심 선를 가져온 후 각각의 선을 단위 벡터로 만든 뒤 
####  3.2.1   $\psi (\mathbf{X}_i^i)  , \psi (\mathbf{x})$ 
@`/mast3r_slam/matching.py`
@`match_iterative_proj`
```python
def match_iterative_proj(X11, X21, D11, D21, idx_1_to_2_init=None):
	#config
	rays_with_grad_img, pts3d_norm, p_init = prep_for_iter_proj (
											X11, X21, idx_1_to_2_init)
```

- **X11, X21**: 두 이미지의 3D Pointmap (MASt3R 예측값). -> $\mathbf{X}_i^i$ and $\mathbf{X}_i^j$ 
- **D11, D21**: 두 이미지의 Feature Descriptor (매칭 정제용). -> 이거 어디니?
- **idx_1_to_2_init**: 이미지 1의 각 픽셀이 이미지 2의 어떤 위치와 매칭될 것인지에 대한 초기 추정값을 담고 있는 정수형 인덱스 텐서
@`/mast3r_slam/matching.py`
@`prep_for_iter_proj`
```python
def prep_for_iter_proj(X11, X21, idx_1_to_2_init):
	#환경 설정 등 
	
	# Ray image
	rays_img = F.normalize(X11, dim=-1)
	# 기울기 정보?
	rays_img = rays_img.permute(0, 3, 1, 2) # (b,c,h,w)
	gx_img, gy_img = img_utils.img_gradient(rays_img)
	rays_with_grad_img = torch.cat((rays_img, gx_img, gy_img), dim=1)
	rays_with_grad_img = rays_with_grad_img.permute(
	0, 2, 3, 1
	).contiguous() # (b,h,w,c)
	
	# 3D points to project
	X21_vec = X21.view(b, -1, 3)
	pts3d_norm = F.normalize(X21_vec, dim=-1)
	
	# Initial guesses of projections 아직 여기 식에 안나옴
```

- X21_vec = X21.view(b, -1, 3) : 이미지 $j$의 포인트맵 데이터인 `X21`을 한 점($x, y, z$)씩 나열된 벡터 형태(`X21_vec`)로 재구성하는 것 ->  $x∈ X_{i}^j$
- pts3d_norm = F.normalize(X21_vec, dim=-1): 단위 백터로 변환 ->  $\psi (\mathbf{x})$ 
- rays_img = F.normalize(X11, dim=-1) : x11의 생 ray를 구하고 단위 백터로 면환 하는 과정 과정 -> $\psi (\mathbf{X}_i^i)$ 




#### 3.2.2.  $[\mathbf{X}_i^i]_{\mathbf{p}}$
이 것은 Pointmap $\mathbf{X}_i^i$의 실수 좌표 p 위치에서 ray 값을 가져오라 이다.
$[⋅]p$ :  **Sampling**, [[../../../50_Concepts/Interpolation|Interpolation]]

그런데 p는 실수 좌표 라는 것을 기억 해야 한다. 
우리는 식수 좌표에 대한  ray 값이 없다. 
 그 실수 p값을 사용해서 ray 값을 계산 해야 한다. 여기서는 따라서 우리는 [[../../../50_Concepts/Interpolation|Interpolation]] 중에서도 [[../../../50_Concepts/Bilinear Interpolation|Bilinear Interpolation]]을 사용해서 한다 

이것은 gpu의 병열 계산을 위해  [[../../../50_Concepts/CUDA|CUDA]] 언어를 이용하여 [[../../../50_Concepts/GPU Kernel|GPU Kernel]] 을 사용한다

@`/mast3r_slam/backend/src/matching_kernels.cu` 
@`iter_proj_kernel()`
```cpp
// Bilinear interpolation
int u11 = static_cast<int>(floor(u));
int v11 = static_cast<int>(floor(v));
float du = u - static_cast<float>(u11);
float dv = v - static_cast<float>(v11); 

// Clamping always ensures full bilinear is fine to calculate
float w11 = du * dv; // top left
float w12 = (1.0-du) * dv; // top right
float w21 = du * (1.0-dv); // bottom left
float w22 = (1.0-du) * (1.0-dv); // bottom right 

// NOTE: Pixels are opposite the area calc!
float const* r11 = &rays_img[b][v11+1][u11+1][0]; // bottom right
float const* r12 = &rays_img[b][v11+1][u11][0]; // bottom left
float const* r21 = &rays_img[b][v11][u11+1][0]; // top right
float const* r22 = &rays_img[b][v11][u11][0]; // top left

#pragma unroll
for (int j=0; j<3; j++) {
	r[j] = w11*r11[j] + w12*r12[j] + w21*r21[j] + w22*r22[j];
}
```
1. 좌표의 각 정수 실수 정보를 가져옴
2. 각 가중치를 계산: 
	1. 현재 좌표의 소수점 위치(`du`, `dv`)를 기준으로 4개 영역의 넓이를 계산합니다. (이 넓이는 기하학적으로 **대각선 반대편 픽셀**이 가져가야 할 가중치가 됩니다.)
3. 각 픽셀의 ray 정보를 가져온다 
4. 각 ray와 가중치를 각각 반대 쪽에 있는 것들 끼리 곱한후 더한다 
5. 실수 좌표의 ray값이 반환된다 
	1. 즉 이것이 $[\mathbf{X}_i^i]_{\mathbf{p}}$ 이다. 계산되었다.




#### 3.2.3 $\psi \left( [\mathbf{X}i^i]_{\mathbf{p}} \right)$
@`/mast3r_slam/backend/src/matching_kernels.cu` 
@`iter_proj_kernel()`
```cpp
// Normalize ray
float r_norm = sqrtf(r[0]*r[0] + r[1]*r[1] + r[2]*r[2]);
float r_norm_inv = 1.0/r_norm;

#pragma unroll
for (int j=0; j<3; j++) {
	r[j] *= r_norm_inv;
}
```
이건 각 길이가 1인 4개의 ray에 가중치를 곱해서 나온 p에 대한 ray가 길이가 1이 아니기 때문에 그에 대한 normalization 해준 것이다 
#### 3.2.4  기하학적 해석
![[../../../90_Resources/92_Images/MASt3R-SLAM_geometric_interpretation.png]]
1. **카메라 원점 (Camera Center):** 좌표계의 원점 O=(0,0,0) 에 위치함.
2. **광선 (Ray):** 원점 O에서 뻗어나가는 화살표.
3. **단위 구 (Unit Sphere):** 원점을 감싸고 있는 반지름 1짜리 구.
4. **투영 :** 3D 공간상의 점 X를 원점과 이었을 때, 선이 **구의 표면과 만나는 점**이 바로ψ(x) 


#### 3.2.5 $\arg \min_{\mathbf{p}} \left\| \psi \left( [\mathbf{X}_i^i]_{\mathbf{p}} \right) - \psi (\mathbf{x}) \right\|^2$
Squared Euclidean Distance를 cost 로 하여  [[Levenberg-Marquardt|Levenberg-Marquardt|]] 알고리즘으로 푼다
즉 Squared Euclidean Distance가 cost fuction인 것이다. 

$$E(\mathbf{p})=\underbrace { \left\| \psi \left( [\mathbf{X}_i^i]_{\mathbf{p}} \right) - \psi (\mathbf{x}) \right\|^2}_{Squared Euclidean Distance}$$

이 식을 사용하여 최적화 하기 위해서 Residual Vector, r 의 형태로 표현한다. 
$$
r(\mathbf{p}) = \psi \left( [\mathbf{X}_i^i]_{\mathbf{p}} \right) - \psi (\mathbf{x}) 
$$@`/mast3r_slam/backend/src/matching_kernels.cu` 
@`iter_proj_kernel()`
```cpp
for (int j=0; j<3; j++) {
	err[j] = r[j] - pts_3d_norm[b][n][j];
}
```
$$E(\mathbf{p})= \left\| r(\mathbf{p}) \right\|^2 =r^Tr$$@`/mast3r_slam/backend/src/matching_kernels.cu` 
@`iter_proj_kernel()`
```cpp
float cost = err[0]*err[0] + err[1]*err[1] + err[2]*err[2];
```


최적의 이동량 $\Delta p$를 구하기 위해, **Gauss-Newton** 방법에 Damping Factor $\lambda$를 추가한  [[Levenberg-Marquardt|Levenberg-Marquardt]] 공식을 사용한다 
$$(J^T J + \lambda I) \delta = J^T e$$
논문에서는 [[Analytical Jacobians|Analytical Jacobians]]를 사용한다고 언급되어 있으나, 이는 수식적으로 Pointmap의 공간적 변화율(Spatial Gradient)을 의미한다. @8.2. Rays and Distance 에서 확인 할 수 있다.(사실 뭔말인지 모르겠다)

최적화 대상은 픽셀 좌표 $\mathbf{p}=(u, v)$이며, 이를 $\mathbf{p}$에 대해 편미분한 [[Jacobian|Jacobian]]$\mathbf{J}$는, Pointmap 이미지 상에서의 기울기(Gradient)와 같다.



#### 3.2.3        $\|\psi_1 - \psi_2\|^2 = 2(1 - \cos \theta), \space \cos \theta=\psi_1^T \psi_2$ 의 수학 증명
$$\psi_1^T \psi_2=각\space 행열(여기서는 벡터)의 \space 내적$$ 이거는 공부 쫌 더 해야할듯 
$$\|\psi_1 - \psi_2\|^2 = (\psi_1 - \psi_2)^T (\psi_1 - \psi_2)$$
$$= \psi_1^T\psi_1 - \psi_1^T\psi_2 - \psi_2^T\psi_1 + \psi_2^T\psi_2$$
$$= 2 - 2(\psi_1^T\psi_2)$$
$$\psi_1^T\psi_2 = \|\psi_1\|\|\psi_2\|\cos\theta = 1 \cdot 1 \cdot \cos\theta$$
$$= 2 - 2\cos\theta$$
$$= 2(1 - \cos\theta)$$

#### 3.2.3   코사인을 이용한 직관 밑 논문 부연 설명

$$\mathbf{p}^* = \arg \min_{\mathbf{p}} \left\| \psi \left( [\mathbf{X}_i^i]_{\mathbf{p}} \right) - \psi (\mathbf{x}) \right\|^2 . \space \space \space \space \space where \space  x∈ X_{i}^j$$
Squared Euclidean Distance를 cost 로 하여  [[Levenberg-Marquardt|Levenberg-Marquardt|]] 알고리즘으로 푼다

그런데 왜 $$\|\psi_1 - \psi_2\|^2 = 2(1 - \cos \theta), \space \cos \theta=\psi_1^T \psi_2$$라고 하면서 설명을 할까? 코드에서는 쓰이지도 않는데 말이다. 
![[../../../90_Resources/92_Images/MASt3R-SLAM_3.2Matching_Additional_explanation.png]]
이는 gpu가 연산하기 편한  [[Squared Euclidean Distance|Squared Euclidean Distance]] 로 풀지만  두 단위 백터의 각도를 점점 작게 만들어 결국에는 가장 각도 차이가 작은 것을 찾아 낸다 는 알고리즘이 사람의 직관으로는 더 편하기 떄문이며 이 편한 알고리즘이 gpu가 연산하기 좋은 알고리즘과 동치임을 알려주는 것이다. 


