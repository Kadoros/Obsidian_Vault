---
tags:
  - note
parent_concept:
  - "[[20_Research/21_Projects/05_TCO/DOCS_MAP|05_TCO]]"
date: 2026-10-09
---
# TCO 관련 연구 지도

> 2026-10-09 웹 서치 기준. **각 논문은 아직 본문 정독 전** — 요약은 초록/페이지 수준. 포지셔닝 굳히기 전에 정독 필요.

## A. 시공간 분리 / 고정 기저 / 경사하강법 없는 학습
| 논문 | 한 일 | TCO와의 관계 |
|---|---|---|
| Frozen-PINN — Datar et al., ICLR 2026 oral ([arXiv](https://arxiv.org/abs/2405.20836)) | 공간: 랜덤 피처 고정, 시간: ODE solver로 계수 적분, GD 없음 | **PDE 하나**만 풂. 시공간 분리의 출처 → [[Frozen-PINN]] |
| RandONet ([arXiv 2406.05470](https://arxiv.org/pdf/2406.05470)) | DeepONet branch/trunk 내부 가중치 랜덤 고정, 출력만 least-squares | "Frozen + DeepONet"이 이미 있음 |
| DeepONet + Randomized NN ([arXiv 2503.00317](https://arxiv.org/html/2503.00317v1)) | 비슷한 계열 | |
| Randomized sampling 학습 ([arXiv 2409.13280](https://arxiv.org/pdf/2409.13280)) | DeepONet 효율 학습 | |
| Deep Neural ODE Operator Networks ([arXiv 2510.15651](https://arxiv.org/html/2510.15651v1)) | $u=\sum_j\alpha_j(x)\psi_j(t)$, 계수를 Neural ODE로, 비선형은 이차 결합 | **"공간 기저 + 계수 ODE" operator learning이 이미 있음**. 텐서 해석·대칭 보장은? → 정독 필요 |

→ 결론: "Frozen-PINN을 DeepONet으로"는 **새로움 약함**.

## B. 구조 보존 / 안정성 보장 (가장 가까운 경쟁)
| 논문 | 한 일 | TCO와의 관계 |
|---|---|---|
| **NIGO** — ICML 2026 ([page](https://icml.cc/virtual/2026/72656)) | 잠재 동역학 = 반대칭 이동 + 음의 반정치 소산, 행렬 지수로 적분, 생성 행렬 계수를 입력에서 예측. Burgers/NS/KS | **$A(a)=S(a)-D(a)$ 를 이미 함.** TCO는 선형 이상(3차 텐서, 비선형 대칭, 모드 결합 해석)이어야 함 |
| ECO ([arXiv 2512.01984](https://arxiv.org/html/2512.01984v1)) | 학습 가능한 이차 에너지 타원체 + 투영층으로 카오스 궤적 유계성 보장 (KS, Kolmogorov NS) | 장시간 카오스 쪽 경쟁 |
| Learning Dissipative Dynamics in Chaotic Systems ([ar5iv 2106.06898](https://ar5iv.labs.arxiv.org/html/2106.06898)) | 소산 구조로 카오스 학습 | |

## C. 이차 텐서 학습 (Operator Inference, 축소모델)
| 논문 | 한 일 | TCO와의 관계 |
|---|---|---|
| Energy-Preserving Reduced OpInf ([arXiv 2401.02889](https://arxiv.org/pdf/2401.02889)) | $\dot c=Ac+H(c\otimes c)$ 의 $H$ 를 데이터에서, 에너지 보존 제약 | **텐서 + 에너지 보존 조합 자체는 있음**. 단 **PDE 하나** 축소모델 |
| Energy-preserving quadratic operators의 표현 ([arXiv 2503.10824](https://arxiv.org/html/2503.10824v1)) | 에너지 보존 이차 연산자 파라미터화 이론 | 텐서 대칭 조건 정리에 바로 쓸 것 |
| Tensor parametric Hamiltonian OpInf ([arXiv 2502.10888](https://arxiv.org/pdf/2502.10888)) | 파라미터 의존 해밀토니안 텐서 | **"입력 의존 텐서"에 가장 가까움 → 최우선 정독** |

## D. 불연속 / n-width
| 논문 | 한 일 |
|---|---|
| Lanthaler et al., ICLR 2023 ([arXiv 2210.01074](https://arxiv.org/pdf/2210.01074)) | 선형 디코더(DeepONet, PCA-Net) 오차 하한 $\gtrsim 1/p$ (이동 불연속). shift-DeepONet·FNO는 비선형 재구성으로 극복. Burgers 충격 후 지수 수렴 |
→ "DeepONet이 충격파를 못 잡는다"는 **이미 증명됨**. 대박 자리 아님.

## E. 엔트로피 안정 (열린 문제 2번 관련)
- Entropy stable conservative flux form NN — JSC 2026 ([page](https://math.dartmouth.edu/~ylee/published/2026/02/18/EntropyCFN.html))
- [arXiv 2507.01795](https://arxiv.org/abs/2507.01795v1)
→ 단일 PDE 수치기법 쪽. **입력 족 operator learning + 비이차 엔트로피 보장**은 상대적으로 비어 보임 (확인 필요)


## ★ 정독 결과 (2026-10-09)

### Tensor parametric Hamiltonian OpInf — Vijaywargiya, McQuarrie, Gruber (arXiv 2502.10888, 2025)
- 모델: $\dot{\hat q} = (\bar{\mathbf T}\boldsymbol\mu')\hat q$, 즉 $A(\mu) = \sum_x\theta_x(\mu)A_x$ = **3차 텐서와 파라미터 벡터의 축약**
- 열방정식 텐서: $T_{ijk} = (\nabla\phi_i,\nabla\phi_j)_{\Omega_k}$ → **우리 §3 "입력이 모드를 섞는 텐서"와 같은 형태** ⚠️
- 단, 파라미터 = **조각별 상수 계수 3~4개** ($p=3,4$). 임의의 계수장(함수 입력) ✗
- **선형만**. 이차 항은 future work (Remark 2.2). 해밀토니안 ROM도 비선형항 $f\equiv0$
- 대칭($\bar T^\top=\bar T$, 해밀토니안 → 에너지 보존)은 등식 제약 least-squares로 강제
- 텐서 성분의 물리적 해석(모드 상호작용) ✗
- 고차원 파라미터, 함수 입력 논의 ✗
- 결과: 1D 열 p=3, r=6에서 최대 상대오차 ~6%, OpInf 오차 ~0.1%에서 정체

### NODE-ONet — Li, Liu, Song, Yue, Zuazua (arXiv 2510.15651)
- 모델: $u = \sum_j\alpha_j(x)\psi_j(t)$, $\dot\psi = \mathcal N(\psi, v, t)$. 입력 = **함수** (초기조건, 계수장, 소스)를 센서로
- 이차형 결합: NS에서 $[C_i\odot\psi]\odot[D_i\odot\psi]$ — **원소별(Hadamard) 곱**, 활성화 안에. 일반 이중선형 텐서 $\sum T_{kij}c_ic_j$ ✗ → 교차 모드 삼체 결합이 명시되지 않음
- 입력 영향: 확산-반응에선 $D,R$ 이 곱으로 들어가 결합을 바꿈. NS에선 이차항이 입력과 무관
- 결합 해석(모드 상호작용, 에너지 전달, 선택 규칙) ✗
- 구조 보장(에너지 보존/소산, 반대칭, 안정성) ✗. 적분기는 explicit Euler
- 한계로 **분포 밖 입력 외삽**을 직접 언급 (미해결)
- 베이스라인: DeepONet, MIONet

### NIGO — ICML 2026 (초록만, 본문 미확인)
- 잠재 동역학 = $S - D$ 생성 행렬, 행렬 지수로 적분, 입력에서 생성 계수 예측
- 초록상 **선형 생성 행렬만**, 이차 모드 결합 언급 ✗ (비선형은 인코더·입력 의존 생성자가 흡수하는 듯)

## 4가지 성질 비교 (포지셔닝 근거)
| | ① 명시적 교차모드 3차 텐서 | ② 입력 = 함수, 텐서가 입력 의존 | ③ 이차항 대칭 보장 | ④ 텐서 해석/복원 검증 |
|---|---|---|---|---|
| Energy-preserving OpInf | ✓ | ✗ (PDE 하나) | ✓ | ✗ |
| Tensor parametric H-OpInf | △ (입력-모드 텐서, 선형만) | △ (스칼라 3~4개) | △ (선형부만) | ✗ |
| NODE-ONet | ✗ (원소별 곱) | ✓ | ✗ | ✗ |
| NIGO | ✗ (선형 생성자) | ✓ | △ (선형부 $S-D$) | ✗ |
| **TCO 목표** | **✓** | **✓** | **✓** | **✓** |

→ 각 성질 쌍은 선행이 있지만 **넷을 동시에** 가진 건 아직 못 찾음. 새로움 = "통합 + 해석 검증". 단일 성질로는 새로움 약함.


## F. 방정식 발견 (SINDy / PDE-FIND) ⚠️ 2026-10-09 추가, 정독 전
- SINDy (Brunton, Proctor, Kutz 2016), PDE-FIND (Rudy et al. 2017): 후보 항 라이브러리 + 희소 회귀로 데이터에서 PDE를 찾음. **Burgers의 $uu_x$ 를 데이터에서 찾는 건 이미 유명한 결과**
- 예상 공격: "TCO E1 = 푸리에 공간의 SINDy 아니냐"
- 차별점 후보: ① 입력이 **함수**이고 텐서 인덱스로 축약 (SINDy는 보통 PDE 하나) ② 잘린 데이터에서의 오염 분석 + 대칭으로 해결 ③ 구조 보장 ④ DeepONet/FNO와 같은 operator learning 과제에서 비교
- → E1만으로는 못 막음. **E4(함수 입력)와 벤치마크 비교가 필수**

## 빈자리 가설
1. **입력 의존 3차 텐서 + 대칭 보장 + 모드 결합 해석** (OpInf는 PDE 하나, NIGO는 선형만)
2. ~~입력이 모드를 섞는 텐서~~ → **Tensor parametric H-OpInf가 이미 함** (조각별 상수 3~4개, 선형). 남는 자리: 함수 입력 + 이차항
3. 비이차 엔트로피 구조

## TODO (서치)
- [x] Tensor parametric Hamiltonian OpInf 정독 (2026-10-09)
- [ ] NIGO 본문: 비선형항을 어떻게 다루는지 (초록상 선형 생성자만, OpenReview 1yRpUPopFM)
- [x] Deep NODE Operator Nets 정독 (2026-10-09)
- [ ] "Galerkin neural operator", "triadic interaction learning", "parametric operator inference" 서치
- [ ] Darcy + Galerkin 텐서 구조 학습 선례 서치
- [ ] parametric OpInf가 입력을 어디까지 다루는지 (스칼라 파라미터 vs 함수)
- [ ] KAN + neural operator (KANO 등) — 결합 방향 검토용
- [ ] 다항식/텐서 네트워크 계열 (Volterra network, Π-net, tensor regression) — 계보 정리
- [ ] SINDy / PDE-FIND / 푸리에 공간 방정식 발견, parametric SINDy 서치·정독 (차별점 확정)
- [ ] DeepONet·FNO와 정확도 비교 실험 설계
