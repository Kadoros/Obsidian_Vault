Both files are already in the same folder.

Smoke test passed: closed `relT` = 8.98e-09 and 1.65e-08, both ≤ 1e-7. Next I'll run all 16 jobs for E1a–E1f in parallel, with BLAS limited to 2 threads per job and wall time recorded for each.

The 15 jobs are running in the background, and I'll report once they finish.

Two E1c jobs finished normally (about 38s each). I'm waiting for the rest.

All four E1c jobs are done. Waiting on the rest.

E1e_K6 is done (68s).

E1e_K12 is done (69s).

E1d_ridge1e-10 is done (70s).

E1e_K8 is done (70s).

E1d_ridge1e-6 is done (72s).

E1d is fully done. E1a, E1b, and E1f are still running.

E1b_kic4 is done (100s).

E1b_kic8 is done (102s).

E1b is fully done. Only E1a and E1f are left.

E1a is done (468s). Only E1f is left.

스모크 테스트와 E1a~E1f 15개 run이 모두 에러 없이 끝났습니다(종료 코드 0). 코드는 수정하지 않았습니다. 다만 스모크 노트와 크게 다른 결과가 두 군데 있습니다. E1d에서는 K=12, nu=1.0의 `rel_err_T`가 약 1e5가 아니라 5.24e-2였고, E1f에서는 nu=0.02 closed만 잘 맞지 않았습니다(아래 3번).

스모크 테스트 closed 줄의 `relT`는 8.98e-09(nu=0.2), 1.65e-08(nu=0.05)로, 기준인 1e-7보다 작아 통과했습니다.

## 1. 결과 파일
위치는 `runs/` 아래입니다.
- **`results.json`, `log.txt`, `fig_nu_sweep.png`**: 15개 폴더 전부와 `e1_smoke`에 있습니다.
- **`fig_tensor_k3.png`**: E1a, E1b(kic2/4/8), E1f, smoke에만 있습니다. 코드가 closed와 full을 둘 다 돌린 경우에만 이 그림을 저장하기 때문에, E1c(closed만)와 E1d·E1e(full만)에는 없습니다.
- **콘솔 출력과 실행 시간**: `runs/_stdout/*.out`, `runs/_stdout/_timing.txt`
- **요약 표 파일**: [E1_summary_table.md](E1_summary_table.md) (results.json에서 바로 뽑았습니다)

## 2. 요약 표
| 실험 | nu | regime | rel_err_T | on_rule | sel_mass | E_viol | test_dzdt | rollout |
|---|---|---|---|---|---|---|---|---|
| E1a | 0.5 | closed | 3.70e-13 | 3.39e-14 | 1.000 | 1.9e-15 | 1.9e-14 | 1.5e-11 |
| E1a | 0.5 | full | 3.17e-02 | 3.31e-03 | 0.935 | 1.1e-05 | 2.2e-03 | 3.3e-06 |
| E1a | 0.2 | closed | 1.57e-13 | 1.96e-14 | 1.000 | 2.0e-15 | 1.7e-14 | 2.4e-12 |
| E1a | 0.2 | full | 8.63e-02 | 9.87e-03 | 0.835 | 7.0e-05 | 1.2e-02 | 9.9e-05 |
| E1a | 0.1 | closed | 9.10e-14 | 1.73e-14 | 1.000 | 2.0e-15 | 1.5e-14 | 2.3e-12 |
| E1a | 0.1 | full | 2.07e-01 | 3.77e-02 | 0.704 | 6.9e-04 | 3.9e-02 | 8.6e-04 |
| E1a | 0.05 | closed | 4.10e-14 | 1.37e-14 | 1.000 | 1.6e-15 | 1.3e-14 | 6.9e-12 |
| E1a | 0.05 | full | 3.45e-01 | 8.64e-02 | 0.580 | 7.5e-03 | 9.3e-02 | 9.2e-03 |
| E1a | 0.02 | closed | 1.64e-14 | 9.83e-15 | 1.000 | 8.9e-16 | 9.5e-15 | 2.3e-11 |
| E1a | 0.02 | full | 4.32e-01 | 1.42e-01 | 0.506 | 2.7e-02 | 1.8e-01 | 5.2e-02 |
| E1b kic2 | 0.1 | closed | 7.45e-12 | 2.94e-12 | 1.000 | 2.0e-14 | 3.7e-14 | 5.4e-13 |
| E1b kic2 | 0.1 | full | 2.90e+00 | 1.93e-01 | 0.217 | 8.3e-04 | 1.3e-02 | 5.6e-04 |
| E1b kic4 | 0.1 | closed | 6.51e-13 | 1.35e-13 | 1.000 | 5.7e-15 | 1.8e-14 | 5.0e-13 |
| E1b kic4 | 0.1 | full | 1.56e+00 | 7.39e-02 | 0.338 | 7.3e-04 | 2.4e-02 | 4.6e-04 |
| E1b kic8 | 0.1 | closed/full | = E1a nu=0.1과 동일 | | | | | |
| E1c noise0 | 0.1 | closed | 9.10e-14 | 1.73e-14 | 1.000 | 2.0e-15 | 1.5e-14 | 2.3e-12 |
| E1c 1e-4 | 0.1 | closed | 8.07e-04 | 5.65e-05 | 0.998 | 2.5e-06 | 7.8e-05 | 7.7e-06 |
| E1c 1e-3 | 0.1 | closed | 8.14e-03 | 5.96e-04 | 0.978 | 2.5e-05 | 7.9e-04 | 7.8e-05 |
| E1c 1e-2 | 0.1 | closed | 1.41e-01 | 1.98e-02 | 0.750 | 4.0e-04 | 1.8e-02 | 1.1e-03 |
| E1d ridge1e-10 | 1.0 | full | 5.24e-02 | 3.89e-03 | 0.888 | 3.3e-06 | 5.9e-04 | 1.3e-07 |
| E1d ridge1e-6 | 1.0 | full | 5.24e-02 | 3.89e-03 | 0.888 | 3.3e-06 | 5.9e-04 | 1.3e-07 |
| E1d ridge1e-3 | 1.0 | full | 5.24e-02 | 3.90e-03 | 0.888 | 3.3e-06 | 5.9e-04 | 1.7e-07 |
| E1e K6 | 0.1 | full | 2.14e-01 | 4.57e-02 | 0.740 | 2.3e-03 | 5.4e-02 | 3.1e-03 |
| E1e K8 | 0.1 | full | = E1a nu=0.1 full과 동일 | | | | | |
| E1e K12 | 0.1 | full | 4.04e-01 | 3.12e-02 | 0.518 | 1.1e-04 | 2.6e-02 | 2.2e-04 |
| E1f stlsq | 0.5 | closed | 1.04e-14 | 1.04e-14 | 1.000 | 8.3e-16 | 5.3e-15 | 1.5e-11 |
| E1f stlsq | 0.5 | full | 1.48e-03 | 1.48e-03 | 1.000 | 2.1e-06 | 1.8e-03 | 2.2e-06 |
| E1f stlsq | 0.2 | closed | 8.48e-15 | 8.48e-15 | 1.000 | 8.5e-16 | 6.0e-15 | 2.4e-12 |
| E1f stlsq | 0.2 | full | 3.45e-02 | 7.21e-03 | 0.985 | 2.3e-05 | 1.0e-02 | 5.8e-05 |
| E1f stlsq | 0.1 | closed | 9.18e-15 | 9.18e-15 | 1.000 | 9.2e-16 | 7.0e-15 | 2.3e-12 |
| E1f stlsq | 0.1 | full | 1.93e-01 | 3.43e-02 | 0.796 | 5.9e-04 | 3.5e-02 | 6.1e-04 |
| E1f stlsq | 0.05 | closed | 9.71e-15 | 9.71e-15 | 1.000 | 9.7e-16 | 7.7e-15 | 6.9e-12 |
| E1f stlsq | 0.05 | full | 3.25e-01 | 8.26e-02 | 0.646 | 7.1e-03 | 8.4e-02 | 8.3e-03 |
| E1f stlsq | 0.02 | **closed** | **2.49e-02** | 2.49e-02 | 1.000 | 7.3e-03 | 1.3e-02 | 1.4e-02 |
| E1f stlsq | 0.02 | full | 4.15e-01 | 1.52e-01 | 0.574 | 3.5e-02 | 1.7e-01 | 5.8e-02 |

## 3. 스모크 테스트 관찰과 다른 결과
1. **E1d (조건수 붕괴가 재현되지 않음)**: 지시문 노트는 K=12, nu=1.0, 기본 ridge에서 `rel_err_T`가 약 1e5라고 했지만, 실제로는 5.24e-2였습니다. ridge를 1e-10, 1e-6, 1e-3으로 바꿔도 지표가 거의 같았고, rollout만 1.25e-7에서 1.74e-7로 조금 달라졌습니다.
2. **full regime 오차 크기**: 스모크(quick 설정)에서는 `rel_err_T`가 1.5~3.0, `on_rule`이 0.13~0.31이었습니다. 기본 설정인 E1a에서는 각각 0.032~0.43, 0.0033~0.14로 한 자릿수 정도 작습니다. 두 설정은 n_traj, t_final, kmax_full이 달라서 그대로 비교하기는 어렵습니다. nu가 작을수록 나빠지는 경향은 같습니다.
3. **E1b (식별 불가능성)**: 
   - closed에서는 kic=2에서도 `rel_err_T`가 7.45e-12로 정답 텐서를 복원했습니다.
   - 노트에 적힌 "미분 예측은 잘 맞는데 텐서가 엉뚱함"은 full에서만 나왔습니다. kic=2 full에서 `relT`는 2.90인데 `test_dzdt`는 1.3e-2로, kic=8의 3.9e-2보다 오히려 작습니다.
4. **E1f (STLSQ)**: 
   - nu=0.02 closed에서 STLSQ는 `rel_err_T`가 2.49e-2였습니다. 같은 조건의 lstsq는 1.64e-14입니다.
   - 규칙 밖 성분은 0이므로 이 오차는 전부 규칙 위 성분에서 나옵니다.
   - 나머지 closed 조건은 모두 1e-14 수준이었습니다. nu=0.5 full에서는 `sel_mass`가 1.000, `relT`가 1.5e-3으로 lstsq보다 훨씬 좋았습니다.
5. **closed 정밀도**: 기본 설정에서는 1e-13~1e-14로, 스모크의 1e-8보다 훨씬 정확했습니다. 이건 문제라기보다 참고 사항입니다.
6. **설정이 같아 결과도 같은 run**: E1b_kic8, E1e_K8, E1c_noise0, E1a의 nu=0.1은 설정이 같아서 숫자가 정확히 일치합니다.

## 4. 에러, 발산, 실행 시간
- **에러**: 없었습니다. traceback, 경고, `solver blew up` 모두 0건입니다.
- **발산**: rollout이 `inf`가 된 경우는 없었습니다. 가장 큰 rollout 오차는 E1f nu=0.02 full의 5.8e-2입니다.
- **실행 시간**: 15개를 동시에 돌렸고, 각 작업은 BLAS 스레드를 2개로 제한했습니다(환경 변수만 설정했고 코드는 건드리지 않았습니다).

| 실험 | 실행 시간 |
|---|---|
| E1c | 각 38~39초 |
| E1d, E1e | 각 68~74초 |
| E1b | 각 100~103초 |
| E1a, E1f | 각 468초 (약 7.8분) |
| 스모크 테스트 | 약 10초 |