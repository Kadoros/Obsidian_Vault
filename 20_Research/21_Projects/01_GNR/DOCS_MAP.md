# 문서 지도 — 어디에 뭐가 있나

> 이번 세션(2026-07-29~30)에 만든 것과 이전 것이 섞여 있어 구분해 둔다.
> **⚠️ 표 파일명이 겹친다**: `table1_unified.tex`(구 NeurIPS판) vs `table1_plugin.tex`(신 ICLR판).
> 신규 세트는 전부 `make_iclr_tables.py` 가 생성하며 접미사가 의미어(plugin/whyanalytic/…)다.

## 1. 읽는 순서 (새로 오는 사람용)

| # | 파일 | 무엇 |
|---|---|---|
| 1 | `ICLR_OUTLINE.md` | **여기서 시작.** 포지셔닝(DeltaPhi 형태), 9절 구성, 지적↔해결 대응표 |
| 2 | `PAPER_REFRAME_NOTES.md` | 통일 원리(prior 자기오차), 두 regime, 3-Tier, 한계 11개 |
| 3 | `DRAFT_sec1_sec2.md` | §1 Intro / §2 Related work **본문 초안** |
| 4 | `DRAFT_sec3_sec4.md` | §3 Method / §4 Plug-and-play **본문 초안** |
| 5 | `DRAFT_sec5_sec8.md` | §5 Why analytic / §8 Limitations **본문 초안** |
| 6 | `DRAFT_sec6_sec9_appendix.md` | §6 Generality / §7 Correction space / §9 / Appendix A |
| 5 | `EXPERIMENT_CACHE_MAP.md` | (구) NeurIPS PDF ↔ 캐시 ↔ 생성기 매핑 |
| 6 | `README.md` | (구) 초기 프로젝트 개요 — **오래됨**, 참고만 |

## 2. 표 — 신규 세트 (ICLR용)

`python make_iclr_tables.py` 한 번이면 **재학습 0** 으로 전부 재생성된다.

| 표 | 파일 | 내용 | 소스 캐시 |
|---|---|---|---|
| **T1** | `table1_plugin.tex` | 9벤치 × 5아키텍처 (구 설정: 게이트/MSE 혼용) | `bench_plugin_gated`, `_vc`, `_2d`, `bench_3d_plugin`, `bench_optical_plugin` |
| **T1-final** | `bench_t1_final.json` | **본문용 최종**: MSE + zero-init scale, +82/+73/+74/+79/+70%, dagger 2/25 | `bench_t1_final.py` |
| T2 | `table2_whyanalytic.tex` | 학습prior 1.3~2.5x / coarse FDM 4.5~27.6x | `bench_headline`, `bench_analytic_vs_fdm`, `bench_3d_layered` |
| T3 | `table3_generality.tex` | 기하 3종 + 3D (전부 exact) | `bench_cylindrical`, `bench_spherical`, `bench_3d_layered` |
| T4 | `table4_gate.tex` | do-no-harm 129.1x → 1.00x | `bench_plugin_gated` |
| T5 | `table5_correction_space.tex` | 출력 vs 파라미터 공간 | `bench_paramres_general`, `_limits`, `bench_optical_paramres` |
| T6 | `table6_twostage.tex` | 2단계(보정 prior + base model) 3.65x | `bench_optical_twostage` |
| T7 | `table7_subspace.tex` | 부분공간 포함 여부가 성패 | `bench_paramres_subspace`, `bench_ns_subspace` |
| T8 | `table8_cost.tex` | **새 문제에 몇 줄** (1줄~수십 줄) | 코드에서 직접 셈 |

**구 세트**(NeurIPS판, 건드리지 말 것): `table1_unified` `table2_heat` `table3_vc` `table4_2d`
`table5_nonlinear` `table6_semiconductor` `table7_noise` `table8_ablation` + `table_*.tex`

## 3. 그림

| 파일 | 내용 |
|---|---|
| `fig_missing_physics.{png,pdf}` | **신규**. 정성 필드 5열, two-regime + 게이트 ON/OFF |
| `fig1~4_*.{png,pdf}` | (구) NeurIPS판 메인 그림 |

## 4. 실험 스크립트 — 이번 세션 신규

| 그룹 | 파일 |
|---|---|
| 메인/차별화 | `bench_headline`, `bench_analytic_vs_fdm` |
| plug-and-play | `bench_3d_plugin`, `bench_optical_plugin` |
| 일반성 | `bench_cylindrical`, `bench_spherical`, `bench_3d_layered` |
| OOD | `bench_ood` |
| 실데이터 | `bench_optical` (+ `data/refractiveindex/`, CC0) |
| 보정 공간 | `bench_optical_paramres`, `bench_paramres_general`, `_limits`, `_subspace`, `bench_optical_twostage`, `bench_neural_correction` |
| 예측 진단(실패) | `bench_placement_predictor`, `_sweep`, `_dials` |
| NS | `bench_navier_stokes`, `bench_ns_eddy`, `bench_ns_subspace`, `bench_ns_time` |
| residual 살리기 | `bench_fno_residual` |

## 4-b. 핵심 메커니즘 (이번 세션 후반 확립)

| 발견 | 파일 | 요지 |
|---|---|---|
| 왜 GP 만 안전한가 | `bench_why_gp` | GP 사후평균은 훈련잔차의 선형 평활 -> 크기가 묶임. 신경망은 **107x 폭주** |
| **zero-init 스케일** | `bench_bounded_residual`, `bench_scaled_plugin` | 파라미터 1개로 해로운 칸 9/20 -> 2/20. 손실항·하이퍼파라미터 없음 |
| 최종 T1 | `bench_t1_final` | 위를 반영. **손실은 MSE**(baseline 에 유리한 쪽; rel-L2 는 baseline 을 ~2x 불리하게 만듦) |

⚠️ **손실 규칙**: T1 은 MSE. `bench_ood` / `bench_ns_time` 만 relative-L2 (동적범위 130x 라
MSE 로는 baseline 이 학습 실패). 이 예외는 논문에 명시할 것.

## 5. 실행 메모

- 파이썬: `~/miniconda3/envs/cv/bin/python` (torch 2.7.1, sklearn 포함)
- **스레드 캡 필수**: `OMP_NUM_THREADS=1` 등. 안 하면 작은 행렬에서 스레드 경합으로 수십 배 느려짐
- numpy<2 이므로 `np.trapezoid` shim 필요한 파일이 있음
- 장시간 작업 주의: `bench_ns_time` cfg B 는 **truth 비용이 T 에 비례**해 총 ~13시간
