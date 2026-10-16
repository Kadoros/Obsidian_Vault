---
tags:
  - idea
parent_concept:
  - "[[20_Research/21_Projects/05_TCO/DOCS_MAP|05_TCO]]"
date: 2026-10-10
---
# TCO 논문 프레이밍

## 핵심 주장
> **"Neural operator의 계수를 대각이 아니라 텐서로 쓰면, 모델 안의 물리가 보인다."**

*Writing the coefficients of a neural operator as a tensor, rather than a diagonal pairing, makes the learned physics visible: which modes interact, how energy moves between scales, and what the unresolved scales do.*

## "보인다"의 다섯 조건
| 의미 | 증거 | 상태 |
|---|---|---|
| ① **맞다** — 보이는 게 진짜 물리 | 배운 텐서 = 교과서 텐서 (5개 PDE, 정확 복원) | ✅ 1단계 |
| ② **읽힌다** — 사람이 해석 가능 | 선택 규칙 p+q=k가 데이터에서 나타남, 에너지 흐름, eddy viscosity 블록 분해 | ✅ 1단계 |
| ③ **버틴다** — 쉬운 조건 한정이 아님 | 잘린 데이터(closure), 기저 미제공(M6), 2D, 함수 입력 | 🔄 M6·2단계 |
| ④ **대가 없다** — 성능 손실 없음 | DeepONet·FNO와 정확도 비슷 + 물리 보장 | ⏳ (a) |
| ⑤ **기존 모델에선 안 보인다** — "텐서로 **써야** 보인다" | FNO·DeepONet 속 암묵 텐서 검사 | ⏳ (b) |

→ **우선순위: ⑤와 ④가 가장 시급** (①② 있음, ③ 서버 진행 중)

## 논문 구조 (안)
1. **서론** — NO는 정확하지만 무슨 물리를 배웠는지 안 보임. DeepONet은 계수-기저 1:1(대각)이라 모드 간 상호작용을 표현할 자리가 없음
2. **방법** — 계수를 3차 텐서로. 이차 PDE에선 **정확한** 형태(Galerkin). 대칭→선택 규칙, closure 채널, 에너지 보장
3. **보인다 ①②** — 5개 PDE 정답 복원, 선택 규칙, eddy viscosity
4. **보인다 ③** — 오염 두 종류와 처방, 기저 미제공 시 A 고유기저가 푸리에 복원, 2D NS
5. **보인다 ⑤** — 기존 NO 속 텐서 검사, "정확도 ≠ 물리를 배움"
6. **대가 없음 ④** — 벤치마크 비교, OOD, 학습 시간
7. **한계** — 비다항식 PDE, 고윳값 겹침, 고전 방법이 이미 최적에 가까운 경우(Darcy)

## 핵심 그림 후보
1. DeepONet 대각 결합 vs 텐서 결합 (개념도)
2. 데이터로 배운 텐서 히트맵 위에 선택 규칙 선이 나타남 (`E1_smoke_fig_tensor_k3.png` 계열)
3. eddy viscosity 블록 분해: 구조 모델은 closure를 제자리에, 블랙박스는 텐서 안에 숨김 (`smoke_closure_burgers_*`)
4. POD 모드 계단 정렬 + 고유기저 순도 (`smoke_pod_modes_burgers_0.2_full.png`)
5. FNO·DeepONet 속 텐서 vs 정답 (실험 b, 예정)

## 과장 금지
- ✗ "정확도가 더 좋다" → ✓ "비슷한 정확도에서 물리가 보인다"
- ✗ "모든 PDE" → ✓ "다항식 비선형 PDE" (대부분의 유체 PDE 포함)
