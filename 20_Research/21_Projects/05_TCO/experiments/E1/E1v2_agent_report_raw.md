The files are already in the right folder.

Smoke test passed: sanity residual 0.00e+00, closed relT at 9.09e-09 and 1.66e-08. Now running V2a~V2h in parallel (cubic runs with 6 BLAS threads, others with 2), tracking peak memory.

The 8 V2 runs are now running in the background, and a monitor will report each completion and any errors. For reference, E1f nu=0.02 closed has `rel_err_A_diag` = **1.07e-02** (0.010677).

That was the old E1 monitor expiring; it's no longer needed. The V2 monitor is still running.

V2e finished normally (320s, ~0.3GB). Waiting on the rest.

V2b is done (321s).

V2f is done (325s).

V2c is done (333s). V2a and the three cubic runs (V2d/g/h) are left.

V2d is done (344s, ~1.8GB).

V2g is done (356s, ~1.8GB).

V2h is done (360s, ~2.1GB). Only V2a (closed+full) is left.

Both figures rendered correctly. Next I'll build the key table from results.json, check the exact constraint-residual values, and confirm that `n_samples` is larger than the feature count.

That traceback came from my own table script, not the experiment code: the directory listing picked up the output file itself. I'll filter to directories and rerun.

스모크 테스트, V2a~V2h 8개 run, 비교 그림 두 장까지 모두 에러·발산 없이 끝났습니다. 코드는 수정하지 않았습니다. 다만 지시문 기준에 걸리는 결과가 있습니다. V2c(에너지 제약 + STLSQ)의 제약 위반 크기가 nu=0.05와 0.02에서 1.20e-10, 1.00e-10으로 기준선 1e-10을 근소하게 넘었습니다.

스모크 테스트는 통과했습니다. sanity 줄은 `energy-constraint residual of TRUE tensor = 0.00e+00`, closed `relT`는 9.09e-09(nu=0.2)와 1.66e-08(nu=0.05)이었습니다.

## 1. 결과 파일
위치는 `runs/` 아래입니다.
- **run 폴더** `V2_smoke`, `V2a_stlsq` ~ `V2h_mask_cubic_energy`: 각각 `results.json`, `log.txt`, `tensors_nu{nu}_{regime}.npz`, 텐서 그림 `fig_tensor_k3_nu0.02_full.png`가 있습니다. 코드가 마지막 (nu, regime)에 대해서만 그림을 저장해서 run당 한 장입니다.
- **비교 그림** [V2_compare_discovery/compare_full.png](runs/V2_compare_discovery/compare_full.png), [V2_compare_prior/compare_full.png](runs/V2_compare_prior/compare_full.png): 각각 옆에 `compare_full.md`가 있습니다. 두 그림 모두 정상적으로 그려진 것을 확인했습니다.
- **전체 핵심 표** [V2_summary_table.md](runs/V2_summary_table.md): `cons_res`(에너지 제약 위반 크기)까지 넣었습니다.
- **콘솔 출력, 시간, 메모리**: `runs/_stdout_v2/`

## 2. 핵심 표 (full regime)
`rel_err_T` / `rel_err_T_on_rule`:

| run | nu=0.5 | 0.2 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|---|---|
| E1a lstsq | 3.17e-2 / 3.31e-3 | 8.63e-2 / 9.87e-3 | 2.07e-1 / 3.77e-2 | 3.45e-1 / 8.64e-2 | 4.32e-1 / 1.42e-1 |
| V2a stlsq | 1.48e-3 / 1.48e-3 | 4.19e-2 / 7.36e-3 | 1.93e-1 / 3.43e-2 | 3.25e-1 / 8.26e-2 | 4.12e-1 / 1.41e-1 |
| V2b energy | 2.17e-2 / 3.57e-3 | 6.96e-2 / 1.09e-2 | 1.69e-1 / 4.56e-2 | 2.99e-1 / 1.03e-1 | 3.60e-1 / 1.45e-1 |
| V2c energy+stlsq | 1.89e-3 / 1.89e-3 | 2.10e-2 / 8.67e-3 | 1.38e-1 / 4.25e-2 | 2.74e-1 / 1.01e-1 | 3.37e-1 / 1.44e-1 |
| V2d cubic | 3.03e-1 / 2.43e-2 | 4.30e-1 / 5.42e-2 | 5.39e-1 / 1.10e-1 | 7.65e-1 / 1.85e-1 | 9.37e-1 / 2.53e-1 |
| V2e mask | 1.48e-3 (같음) | 6.91e-3 | 3.11e-2 | 8.08e-2 | 1.40e-1 |
| V2f mask+energy | 1.89e-3 | 8.79e-3 | 4.07e-2 | 1.02e-1 | 1.47e-1 |
| V2g mask+cubic | 1.48e-3 | 3.65e-3 | 8.85e-3 | 3.22e-2 | 8.34e-2 |
| V2h mask+cubic+energy | 2.13e-3 | 5.17e-3 | 1.08e-2 | 3.44e-2 | 9.12e-2 |

mask가 들어간 run(V2e~V2h)은 `selection_mass`가 1.000이라 두 값이 같아서 하나만 적었습니다.

나머지 지표:

| run | `selection_mass` (0.5→0.02) | `rel_err_A_diag` (0.5→0.02) | `rollout` (0.5→0.02) | `cubic/quad` (0.5→0.02) |
|---|---|---|---|---|
| E1a | 0.935 → 0.506 | 9.5e-4 → 1.02 | 3.3e-6 → 5.2e-2 | – |
| V2a | 1.000 → 0.570 | 1.1e-3 → 1.02 | 2.2e-6 → 5.0e-2 | – |
| V2b | 0.939 → 0.496 | 9.1e-4 → 1.06 | 3.6e-5 → 5.0e-2 | – |
| V2c | 1.000 → 0.578 | 1.1e-3 → 1.05 | 2.5e-6 → 4.8e-2 | – |
| V2d | 0.597 → 0.332 | 9.0e-3 → **1.53** | 7.6e-5 → **2.1e-1** | 7.5e-2 → 3.9e-1 |
| V2e | 1.000 | 1.1e-3 → 0.98 | 2.2e-6 → 4.1e-2 | – |
| V2f | 1.000 | 1.1e-3 → 1.02 | 3.1e-6 → 4.3e-2 | – |
| V2g | 1.000 | 3.6e-3 → 1.17 | 2.1e-6 → 1.4e-2 | 5.4e-3 → 1.6e-1 |
| V2h | 1.000 | 3.6e-3 → 1.16 | 3.6e-6 → 1.5e-2 | 5.4e-3 → 1.6e-1 |

- **`energy_violation`**: 에너지 제약을 건 run(V2b·c·f·h)은 4e-17~1e-11이고, 나머지는 E1a와 같은 수준(1e-6~3e-2)입니다.
- **V2a closed**: 모든 nu에서 `rel_err_T`가 8e-15~1e-14였습니다.

## 3. E1f nu=0.02 closed의 `rel_err_A_diag`
**1.07e-02** (0.010677)입니다. V2a에서 같은 조건은 1.46e-14였고, `rel_err_T`도 2.49e-2에서 8.15e-15로 바뀌었습니다. E1f의 nu=0.02 closed 이상이 블록별 STLSQ에서는 재현되지 않았습니다.

## 4. 스모크 관찰과 다른 결과
1. **에너지 제약**: 
   - 스모크는 nu=0.2 오차가 1.50에서 0.84로 줄었다고 했는데, 기본 설정에서는 8.63e-2에서 6.96e-2로 소폭 줄었습니다.
   - 대신 **`on_rule` 오차는 모든 nu에서 E1a보다 커졌습니다**(예: nu=0.1에서 3.77e-2 → 4.56e-2).
   - rollout도 nu=0.5·0.2·0.1에서 나빠졌습니다(nu=0.5: 3.3e-6 → 3.6e-5).
2. **제약 위반 크기**: 스모크는 1e-15 수준이었는데, 기본 설정에서는 nu가 작을수록 커져서 4e-15~1.2e-10입니다. V2c의 nu=0.05(1.199e-10)와 nu=0.02(1.003e-10)는 지시문 기준(1e-10 이하)을 근소하게 넘습니다. V2b·V2f·V2h는 모두 기준 이내입니다.
3. **대칭 + closure 대 대칭만**: 스모크에서는 거의 같았지만, 기본 설정에서는 nu ≤ 0.2에서 V2g가 V2e보다 확실히 좋습니다(nu=0.1에서 8.85e-3 대 3.11e-2, nu=0.02에서 8.34e-2 대 1.40e-1).
4. **closure 단독(V2d)**: 
   - 데이터가 2만 개 이상이라 발산하지 않았습니다.
   - 그러나 `rel_err_T`, `on_rule`, `selection_mass`가 **모든 nu에서 E1a 기준선보다 나쁩니다**.
   - 3차 항의 성분은 거의 전부 0이 아닙니다(`n_nonzero_C` 약 15,500/16,473).
5. **블록별 STLSQ(V2a) full**: 
   - nu=0.2에서 `on_rule` 개선 폭이 스모크(0.135 → 0.039)보다 훨씬 작습니다(9.87e-3 → 7.36e-3).
   - nu=0.5, 0.1, 0.05 full 수치는 E1f와 정확히 같습니다.
   - nu=0.5 full 결과는 V2e(mask)와 모든 지표가 똑같습니다. 이때 `n_nonzero_T`가 104로 정답 지지집합 크기와 같습니다.
6. **대칭 사전지식 단독(V2e)**: 규칙 밖 성분이 0이 되어 전체 오차는 크게 줄었습니다. 하지만 규칙 위 오차는 E1a의 on_rule과 비슷합니다(nu=0.02에서 1.40e-1 대 1.42e-1, nu=0.05에서 8.08e-2 대 8.64e-2).

nu=0.02 full에서는 모든 방법의 `rel_err_A_diag`가 약 1 이상(0.98~1.53)이고, 3차 항이 들어간 run(V2d, V2g, V2h)에서 가장 큽니다.

## 5. 에러, 발산, 메모리, 실행 시간
- **에러**: 실험 코드에서는 traceback이나 경고가 없었습니다. 제 표 생성 스크립트에서 한 번 에러가 났는데, 결과 파일 자체를 폴더로 읽으려 한 제 쪽 문제였고 고쳐서 다시 만들었습니다.
- **발산**: `solver blew up`이나 rollout `inf`는 없었습니다. rollout 최대값은 V2d nu=0.02의 2.13e-1입니다.
- **메모리**: 3차 항 run이 최대 약 2.1GB(V2h)였고, 나머지는 약 0.3GB입니다. 서버 메모리가 125GB라 문제없었습니다.
- **실행 시간**: 8개를 동시에 돌렸습니다. 3차 항 run은 BLAS 스레드 6개, 나머지는 2개를 썼습니다.

| run | 실행 시간 | fit 시간 (nu당) |
|---|---|---|
| V2b, V2c, V2e, V2f | 각 320~333초 | 0.3~2초 |
| V2d, V2g, V2h | 각 344~360초 | 5~7초 |
| V2a (closed+full) | 476초 | – |

전체 시간의 대부분은 데이터 생성(nu당 약 60초)이었습니다.