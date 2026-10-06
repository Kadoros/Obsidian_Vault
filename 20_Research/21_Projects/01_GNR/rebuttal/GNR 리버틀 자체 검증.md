---
tags:
  - project
parent_concept:
---
# GN-Operator (NeurIPS 2026 #19877) — 리버틀 준비 중 자체 검증 결과

**작성일**: 2026-07-25 **리버틀 마감**: Phase 1 초안 7/27, 토론 8/3까지

---

## 0. 한 줄 요약

리버틀 준비를 위해 리뷰어 지적사항을 검증하는 과정에서, **논문의 핵심 주장("neural operator가 baseline을 이긴다")을 증거가 지지하지 않는다**는 것을 확인했습니다. 실제 기여는 **analytic prior 자체**이며, 그 위의 neural residual은 성능에 거의 기여하지 않습니다.

---

## 1. 리뷰 현황

|리뷰어|Rating|Confidence|핵심 지적|
|---|---|---|---|
|AC (yf3F)|—|—|리젝 방향 권고. "misleading claims", "completely rewritten"|
|RfHu|3|4|Quality 2 / Significance 2. 주장 범위 > 실험 범위|
|qJ9G|5|4|Quality/Clarity/Significance 전부 4|
|mDio|3|3|**"대부분의 벤치마크에서 zero-shot prior가 full GNR보다 정확하다"**|

mDio의 지적이 이번 검증의 출발점이 되었습니다.

---

## 2. 확정된 사실 (실험 8종, 7 seeds)

### 2-1. 반도체 벤치마크 격자 미수렴

논문 파이프라인:

- ground truth: `fdm_k(..., ng=100)`
- GN prior: `gn_semiconductor(..., ng=80)`

불연속 계수에서는 이 격자가 수렴하지 않습니다.

||수렴해(ng=6400) 대비 오차|
|---|---|
|논문의 "정답" ng=100|12.2%|
|논문의 GN prior ng=80|14.5% (보고값 3.3%)|

**비슷하게 틀린 두 이산화를 서로 비교**하고 있었습니다. 3.3%는 PDE 해에 대한 정확도가 아니라 두 근사해 사이의 일치도입니다.

**수정 가능하며, 수정하면 수치가 개선됩니다.** prior 격자를 800으로 올리면 (비용 0.051ms → 0.086ms, 논문 보고 추론시간 0.170ms 내):

|n|DON|GNR@80 (논문)|GNR@800 (수정)|배율|
|---|---|---|---|---|
|5|1.185|0.178|0.045|26.5×|
|10|0.834|0.142|0.023|36.8×|
|20|0.684|0.131|0.019|35.7×|
|50|0.657|0.119|0.015|42.7×|

**범위**: 불연속 계수인 반도체 벤치마크만 해당. VC(매끈한 계수)는 ng=100에서 이미 0.09% 수렴, Poisson/Heat/2D/nonlinear는 해석적 정답이라 무관.

### 2-2. 이론(Eq.1)과 구현(Eq.2)의 불일치

논문 Section 3.1은 두 식이 equivalent하다고 서술하나, 실제로는 다른 함수입니다.

||값|
|---|---|
|Eq.1 vs Eq.2(d=8) 상대차, clean|5.6e-2|
|Eq.1 vs Eq.2(d=8) 상대차, noisy|8.0e-2|
|센서점에서 \|Eq.1 − sensor\||1.3e-13 (정확히 보간)|
|센서점에서 \|Eq.2 − sensor\||1.1e-2 (보간 안 함)|

5.6e-2는 논문이 1D Poisson에서 보고한 GN prior floor 9.1e-4보다 **60배 큰 값**입니다.

**영향**:

- Proposition 1의 exactness는 degree ≤ m−1이 아니라 degree ≤ d(=8)에서만 성립
- Proposition 2의 m-의존 rate는 Eq.1의 d=m−1 전제에서 나온 것이며, 고정 차수 구현에는 적용되지 않음 (mDio Q2가 정확히 이 지점을 지적)
- "Gregory-Newton"이라는 명명이 정당화하려던 보장이 구현에서 성립하지 않음 (AC 지적과 연결)

### 2-3. AC의 단항식 기저 지적은 사실이 아님

||값|
|---|---|
|square Vandermonde 조건수|1.16e8|
|Eq.1 vs monomial 상대차 (30개 함수 중앙값)|6.5e-12|

노이즈 조건에서도 동일:

|σ|Eq.1 forward-diff|monomial d=10|
|---|---|---|
|0|1.275e-2|1.275e-2|
|1e-3|1.416e-2|1.416e-2|
|1e-2|5.865e-2|5.865e-2|

기저 선택(monomial/Chebyshev/forward-difference)은 이 문제 규모에서 결과에 영향을 주지 않습니다. **AC 지적 중 유일한 기술적 항목이며, 반박 가능합니다.**

### 2-4. Clean 벤치마크에서 residual은 음(-)의 기여

Table 1 캡션에 GN prior 값이 명시되어 있습니다 (Poisson 0.001, Heat 1.6e-4).

|벤치마크|prior|GNR (n=50)|비율|
|---|---|---|---|
|1D Poisson|0.0009|0.082|prior가 91배 나음|
|Heat|0.00016|0.023|prior가 144배 나음|

CV 게이트(훈련 데이터 k-fold만 사용, 테스트 라벨 미사용)를 구현한 결과:

|벤치마크|prior|GNR (ungated)|GNR-gated|게이트 동작|
|---|---|---|---|---|
|1D Poisson (전 n)|0.0009|0.09~0.52|0.0009|**항상 prior (0% full)**|
|Heat (전 n)|0.0002|0.016~0.14|0.0002|**항상 prior (0% full)**|
|반도체 n=5→50|0.034|0.060→0.029|0.034→0.029|full 비율 0→86%|
|Mismatch n=5→100|0.171|0.35→0.073|0.24→0.073|full 비율 43→100%|

Ungated GNR은 정확한 prior를 **최대 896배까지 악화**시킵니다. 게이트가 이를 1.40배로 억제합니다.

mDio는 "n=5에서만"이 아니라 "대부분의 벤치마크에서"라고 지적했고, 검증 결과 **매끈한 벤치마크 전 구간**에서 사실이었습니다.

### 2-5. 불연속 반도체에서도 residual 기여는 ~0

수렴 격자 + full peer 비교 (7 seeds):

```
GN prior floor: 0.0154

n     DON    POD    FNO    GP   |  GNR     GP-res
5    1.19   0.72   0.80   0.67  | 0.0175   0.0150
50   0.66   0.52   0.63   0.66  | 0.0136   0.0144
```

두 가지가 드러납니다.

1. **블랙박스는 불연속에서 원리적으로 실패** (0.5~1.2 vs 0.015). "prior가 필요하다"는 명제는 참이고 robust합니다.
2. **prior floor 0.0154, GNR 0.0136, GP-res 0.0144 — 셋이 사실상 동일.** residual이 무엇이든 prior 위에 더하는 것은 10% 안팎입니다.

또한 논문 Appendix F.4의 "반도체에서 GP-res가 GNR보다 1.3~1.5배 나쁘다"가 **재현되지 않았습니다** (실측 1.17배 → 0.95배, 사실상 타이).

### 2-6. Neural residual의 territory 탐색 — 결과: 없음

뉴럴 residual이 GP-on-residual보다 나은 영역을 찾기 위해 원리적 후보를 전부 검증했습니다.

|영역|최강 방법|뉴럴 GNR|
|---|---|---|
|prior 정확 (clean/불연속)|prior 단독|무의미 (기여 ~0 또는 음수)|
|1D 매끈 incomplete, **n≤10**|**GNR**|**유일한 승리 구간**|
|1D 매끈 incomplete, n≥20|GP-res|짐|
|prior 많이 틀림 (강비선형)|블랙박스|짐|
|non-stationary defect|GP-res / FNO|꼴찌권|
|**고차원 3D (64센서)**|GP-res|**7.8~9.6배 짐**|

3D 상세 (prior floor 0.060):

|n|DON|GP|GNR|GP-res|GNR/GP-res|
|---|---|---|---|---|---|
|10|0.70|0.25|0.52|0.054|9.6×|
|20|0.58|0.19|0.38|0.044|8.5×|
|50|—|—|0.277|0.036|7.8×|

고차원에서 뉴럴이 유리할 것이라는 가설과 정반대 결과입니다. 작은 DeepONet은 64차원 residual을 소수 샘플로 학습하지 못하고, GP-res는 prior가 덜어낸 매끈한 residual을 효과적으로 학습합니다.

---

## 3. 부수적으로 확보한 결과

리버틀 대응용으로 준비했으나, 위 결론 때문에 활용도가 제한적입니다.

**3D 벤치마크 (RfHu Q1 대응)**

|벤치마크|계수|정답|GN floor|n=5|n=20|n=50|
|---|---|---|---|---|---|---|
|P1 3D Poisson|상수|해석적 Fourier|5.9%|1.2×|1.5×|1.7×|
|P2 3D 변수계수|매끈한 k|FDM (수렴)|6.0%|1.2×|1.6×|1.8×|
|P3 3D-IC 층상|불연속 k 30× + 단열 BC|FDM ng=61 (수렴 검증)|6.5%|1.3×|1.7×|2.0×|

P3는 초기에 box-core 구조로 설계했으나 정답이 수렴하지 않았습니다 (추정오차 15~20%, 육면체의 12모서리·8꼭짓점 특이점). 대비 완화와 조화평균 FDM 모두 실패했고, z축 층상 구조로 변경하여 해결했습니다 (추정오차 0.67%). 층상 구조가 실제 3D-IC 물리(die/접착층/금속층/산화막의 z방향 적층)에 더 부합합니다.

**HBM 8단 적층 벤치마크 (D.17 형식 통제 비교)**

|n|None|FDM@sensor|FDM@fine|GN|
|---|---|---|---|---|
|10|0.278|0.256|0.032|0.031|
|20|0.248|0.230|0.030|0.028|
|50|0.219|0.204|0.025|0.023|

기여 분해: 격자 해상도(FDM@sensor → FDM@fine) 약 8배, GN 임베딩(FDM@fine → GN) 1.05~1.10배 (p=0.0002~0.0034). **RfHu의 "임베딩 기여가 작다"는 지적이 정량적으로 확인됩니다.**

---

## 4. 무엇이 죽고 무엇이 살아있는가

### 죽은 것

1. **"neural operator가 baseline을 19-23배 이긴다"는 프레이밍.** 개선은 prior에서 나오며 학습 기여는 사실상 0입니다.
2. **Table 1의 Poisson/Heat GNR 열.** prior 단독이 91~144배 나으며, 게이트가 전 구간 prior를 선택합니다.
3. **"뉴럴 residual이 핵심 기여"라는 논문 정체성.** GP-on-residual이 거의 모든 regime에서 같거나 앞서며, 고차원에서는 8~10배 앞섭니다.
4. **Appendix F.4의 GP-res 비교 수치.** 재현되지 않습니다.

### 살아있는 것

1. **블랙박스 operator/GP는 불연속 계수에서 원리적으로 실패합니다** (0.5~1.2 vs 0.015). robust하게 재현됩니다.
2. **data-free analytic prior가 결정적입니다.** zero-parameter, 학습 불필요, 오프라인 사전계산 불필요.
3. **prior를 붙이면 어떤 residual learner든 개선됩니다** (GP-res > GP, GNR > DON).
4. **이산화 규율, 수렴 검증, peer 비교 셋업, 3D 솔버, 벤치마크 생성기** — 다음 작업에 그대로 재사용 가능합니다.

### 정직한 명제

> 알려진 물리로 구성한 zero-parameter data-free analytic prior가 결정적 요소이다. 이를 적용하면 계수가 불연속이거나 데이터가 극히 부족한 — 블랙박스가 실패하는 — 영역에서 우위를 갖는다. 그 위에 얹는 residual learner는 부차적이며(뉴럴과 GP의 차이가 크지 않거나 GP가 우세), prior 자체가 성능의 대부분을 설명한다.

이는 **hybrid-physics 기여**이지 **neural operator 기여가 아닙니다.**

---

## 5. 상의드리고 싶은 것

**(1) 이번 제출 처리**

- 정직한 리버틀 후 리젝 감수: 정정 사항을 공개 기록에 남김. 재제출 시 신뢰도 확보.
- Withdraw: 리뷰 비공개 유지.

개인 의견으로는 전자가 낫다고 봅니다. mDio가 이미 표에서 prior 값을 확인한 상태이고, Table 1 캡션에 수치가 공개되어 있어 숨길 수 있는 성질이 아닙니다.

**(2) 논문 방향**

- prior 중심으로 재구성 (neural operator → hybrid physics). 벤뉴 변경 필요 가능성 (JCP, CMAME 등).
- 방향 전환.

**(3) 다른 논문과의 우선순위**


---

## 부록: 실행한 검증 스크립트

|파일|목적|
|---|---|
|`gn_equivalence.py`|Eq.1 vs Eq.2 등가성, 기저 비교, 조건수|
|`bench_semi_converged.py`|반도체 수렴 격자 재실행|
|`bench_hbm_priorform.py`|HBM D.17 형식 통제 비교|
|`bench_3d.py`, `bench_3d_convergence.py`|3D 벤치마크 + 수렴 검증|
|`bench_gating.py`|CV 게이팅|
|`bench_incomplete.py`|incomplete-physics peer 비교 (GP-res 포함)|
|`chebyshev_ablation.py`|직교 기저 비교|