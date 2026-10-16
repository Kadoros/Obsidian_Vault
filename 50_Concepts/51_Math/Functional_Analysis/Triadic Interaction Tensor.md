---
tags:
  - concept
  - functional-analysis
parent_concept:
  - "[[Galerkin Projection]]"
---
## 정의
이차 비선형 PDE를 기저로 전개하면
$$\frac{dc_k}{dt} = \sum_jA_{kj}c_j + \sum_{i,j}T_{kij}\,c_ic_j$$
$T_{kij}$ = "$i$번·$j$번 모드가 만나 $k$번 모드에 주는 영향" = **삼체(triadic) 상호작용**. 난류 이론의 언어.
Burgers: $T_{kij} = -\langle\varphi_i\,\partial_x\varphi_j,\varphi_k\rangle$

## 왜 행렬이 아니라 3차인가
DeepONet $b^\top I t$ → $b^\top Wt$ 는 $W$ 를 $b$ 에 흡수 가능, 표현력 동일. **3차부터** 모드 간 곱 결합이 생김.

## 성질
- **선택 규칙**: 푸리에 기저면 $i+j=k$ 일 때만 ≠ 0 ($e^{ipx}e^{iqx} = e^{i(p+q)x}$; 곱 ↔ 합성곱) → 희소
- **에너지 흐름 지도**: 저주파 → 고주파 캐스케이드 경로
- **에너지 보존 ⇔ 대칭**: $\sum T_{kij}c_kc_ic_j = 0$ ⇐ $T_{kij} = -T_{jik}$. Burgers: $\langle uu_x,u\rangle = \int(u^3/3)_x = 0$
- 파라미터 $p^3$ → CP 저랭크 분해, 선택 규칙 희소성

## 두 번째 용도: 입력이 모드를 섞는 텐서
가변계수 $-\nabla\cdot(a\nabla u)=f$, $a=\sum a_i\psi_i$:
$A(a)_{kj} = \sum_ia_iT_{kji}$, $T_{kji} = \langle\psi_i\nabla\varphi_j,\nabla\varphi_k\rangle$ → 해 연산자의 비선형성 = 텐서(선형) + 역행렬

## 관련
- Operator Inference: $\dot c = Ac + H(c\otimes c)$ 의 $H$ 를 데이터에서 학습 (PDE 하나)
- [[Dissipative Operator]], [[Diagonalization of Convolution]] (비선형에서 대각화가 깨지는 지점)
- 프로젝트: [[TCO 아이디어 정리]], [[TCO 실험 계획]] E1
- 대칭 → 선택 규칙 일반화, 적용 PDE 목록: [[TCO PDE 후보]]
