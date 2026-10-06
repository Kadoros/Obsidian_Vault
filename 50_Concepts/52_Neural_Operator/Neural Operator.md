---
tags:
  - concept
parent_concept:
  - "[[Operator_Math_Theory]]"
---
## 정의: 함수공간 → 함수공간 매핑
일반 신경망은 벡터→벡터 ($x\in\mathbb{R}^n \to y\in\mathbb{R}^m$)를 학습하지만, Neural Operator는 **함수 → 함수**를 학습:
$$\mathcal{G}_\theta : a(x) \mapsto u(x), \qquad a\in\mathcal{A},\ u\in\mathcal{U}$$
입력 함수 $a$(계수/초기조건/외력)를 출력 함수 $u$(PDE의 해)로 보내는 연산자 자체를 근사. 실제로는 격자/점 위의 샘플 $\{a(x_i)\}$로 이산화해서 입력.

## 대표 모델
- **FNO (Fourier Neural Operator)**: Lifting → Fourier 공간에서 global convolution (× L layers) → Projection
- **DeepONet**: Branch net이 입력 함수 $a$를 인코딩, Trunk net이 쿼리 좌표 $y$를 인코딩, $u(y)=\sum_k b_k(a)\,t_k(y)$

## 핵심 성질: discretization-invariance
$$\text{학습: } 64\times64 \text{ 격자} \;\longrightarrow\; \text{테스트: } 256\times256 \text{ 격자, 그대로 동작}$$
일반 CNN은 해상도가 고정되지만, NO는 함수 자체를 학습하므로 학습 때와 다른 해상도/샘플링에서도 평가 가능 (zero-shot super-resolution).

## [[PINN]]과의 핵심 차이
- PINN: **하나의 PDE 인스턴스**(고정된 $a$, 경계조건)에 대한 해 $u(x,t)$를 맞춤형으로 학습 — 조건이 바뀌면 재학습
- NO: $a \mapsto u$라는 **연산자(= 문제 클래스 전체의 해법)**를 학습 — 학습 후 새로운 $a$에 대해 즉시 추론 (forward pass만)

## 모델별 노트
- [[DeepONet]] · [[HyperDeepONet]] · [[FNO]] · [[Attention as Integral Operator]] · [[Koopman Operator]]
- 수학 배경: [[함수해석학 로드맵]], [[Integral Operator and Kernel]]
