I'll run M0 first.

M0 matches V2 exactly across all 10 values (0.000% difference). Now I'll run the 18 jobs for M1-M5 in parallel, which should use about 40GB of the 118GB available memory, with the two KS cubic runs allocated 6 threads each.

The 19 runs for M1~M5 are running in the background. I'll be notified when each one finishes or if memory runs low.

M4_fisher_mask_cubic is done (278s, 1.8GB).

M4_fisher_mask is done (291s).

M4 is fully done (fisher_lstsq took 400s).

M1_burgers_lstsq is done (423s).

M1 is fully done.

M2_kdv_mask is done (525s).

M2_kdv_mask_cubic_energy is done (541s).

M2_kdv_mask_cubic is done (543s).

M5_varvisc_ood_gap_lstsq is done (584s).

M5_varvisc_mask_cubic is done (590s).

M5_varvisc_ood_gap is done (618s).

M5_varvisc_mask_cubic_energy is done (628s).

M3_ks_mask is done (642s).

M2 is fully done (kdv_lstsq took 713s).

M3_ks_mask_cubic is done (822s, 12.2GB).

M5_varvisc_lstsq is done (838s).

M5 is fully done. M3_ks_lstsq and M3_ks_mask_cubic_energy are still running.

M3_ks_mask_cubic_energy is done (896s, 15.2GB). Only M3_ks_lstsq is left.

The final exit code 1 comes from my shell's last test statement; no stderr warnings were found. Next I'll read the truncated middle section (M2~M5_lstsq).

Every run finished without errors. Contrary to expectation, varvisc lstsq full did **not** diverge or emit overflow warnings at the default data size. Next I'll generate the comparison figures.

The M5 figures look fine, but two pairs of runs share duplicate legend labels (`lstsq+cubic+mask` and `lstsq`). I'll write the core table to a file using run directory names so the runs can be distinguished.

M0 reproduced V2 exactly, so I continued: M1~M5 (19 runs) and all five comparison figures finished with no errors and no divergence, and no code was changed. Contrary to your note, varvisc lstsq full did **not** diverge or raise overflow warnings at the default data size, so there was nothing to record as "발산". Closed-regime `nu_t_err` is excluded from the tables, as you said.

## 1. M0 reproduction check
| param | mask 기대 (V2e) | M0 mask | mask+cubic 기대 (V2g) | M0 mask+cubic |
|---|---|---|---|---|
| 0.5 | 1.48e-3 | 1.4842e-3 | 1.48e-3 | 1.4836e-3 |
| 0.2 | 6.91e-3 | 6.9080e-3 | 3.65e-3 | 3.6510e-3 |
| 0.1 | 3.11e-2 | 3.1125e-2 | 8.85e-3 | 8.8451e-3 |
| 0.05 | 8.08e-2 | 8.0841e-2 | 3.22e-2 | 3.2207e-2 |
| 0.02 | 1.40e-1 | 1.3979e-1 | 8.34e-2 | 8.3361e-2 |

All 10 values match the V2 `results.json` values exactly (0.000% difference). The largest difference from the 3-significant-figure expected values is 0.28% (p=0.5, a rounding effect). Rollout changed slightly because the calculation method changed (e.g. p=0.5: 2.21e-6 → 3.12e-6), which is allowed.

## 2. Figures
**Comparison figures**: `runs/M{1..5}_compare/compare.png` and `compare.md`. I checked the M3 and M5 figures and both render correctly.

**Representative closure figures** (lstsq and mask+cubic, smallest param):

| PDE | lstsq | mask+cubic |
|---|---|---|
| Burgers | [fig](runs/M1_burgers_lstsq/fig_closure_0.02.png) | [fig](runs/M0_burgers_mask_cubic/fig_closure_0.02.png) |
| KdV | [fig](runs/M2_kdv_lstsq/fig_closure_0.02.png) | [fig](runs/M2_kdv_mask_cubic/fig_closure_0.02.png) |
| KS | [fig](runs/M3_ks_lstsq/fig_closure_0.02.png) | [fig](runs/M3_ks_mask_cubic/fig_closure_0.02.png) |
| Fisher | [fig](runs/M4_fisher_lstsq/fig_closure_0.02.png) | [fig](runs/M4_fisher_mask_cubic/fig_closure_0.02.png) |
| varvisc | [fig](runs/M5_varvisc_lstsq/fig_closure_0.05.png) | [fig](runs/M5_varvisc_mask_cubic/fig_closure_0.05.png) |

## 3. Core table (full regime)
The full table, including closed rows and every column, is in [M_summary_table.md](runs/M_summary_table.md). Cells below are `T_rel_err` / `nu_t_rel_err`. For mask runs, `T_rel_err_on_rule` equals `T_rel_err`. For lstsq, the on-rule value is given in parentheses.

**Burgers** (param 0.5 → 0.02)
| 방법 | 0.5 | 0.2 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|---|---|
| lstsq | 3.2e-2 (3.3e-3) / 0.41 | 8.6e-2 (9.9e-3) / 0.27 | 2.1e-1 (3.8e-2) / 4.3e-2 | 3.5e-1 (8.6e-2) / 2.8e-2 | 4.3e-1 (1.4e-1) / 3.0e-2 |
| mask | 1.5e-3 / 0.15 | 6.9e-3 / 0.16 | 3.1e-2 / 0.14 | 8.1e-2 / 7.7e-2 | 1.4e-1 / 3.9e-2 |
| mask+cubic | 1.5e-3 / 0.10 | 3.7e-3 / 4.9e-2 | 8.8e-3 / 2.0e-2 | 3.2e-2 / 6.2e-3 | 8.3e-2 / 2.2e-2 |
| mask+cubic+energy | 2.1e-3 / 0.10 | 5.2e-3 / 4.9e-2 | 1.1e-2 / 2.0e-2 | 3.4e-2 / 6.3e-3 | 9.1e-2 / 2.2e-2 |
| closure_rel_size | 2.0e-3 | 1.2e-2 | 4.6e-2 | 1.5e-1 | 3.0e-1 |
| rollout (mask+cubic) | 2.1e-6 | 3.0e-5 | 3.7e-4 | 3.0e-3 | 1.4e-2 |

**KdV** (0.1 → 0.02)
| 방법 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|
| lstsq | 1.7e-2 (9.4e-3) / 1.4 | 4.3e-2 (2.5e-2) / 0.16 | 1.1e-1 (6.6e-2) / 0.24 |
| mask | 9.4e-3 / 1.0 | 2.6e-2 / 0.13 | 6.9e-2 / 0.23 |
| mask+cubic | 3.2e-3 / 0.51 | 1.1e-2 / 0.11 | 3.7e-2 / 8.8e-2 |
| mask+cubic+energy | 4.0e-3 / 0.51 | 1.4e-2 / 0.12 | 4.3e-2 / 0.10 |
| closure_rel_size | 7.3e-3 | 2.8e-2 | 1.4e-1 |
| rollout (lstsq → mask+cubic) | 1.1e-2 → 2.0e-3 | 2.3e-2 → 1.0e-2 | 9.0e-2 → 4.0e-2 |

**KS, K=12** (0.1 → 0.02)
| 방법 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|
| lstsq | 8.9e-2 (1.8e-2) / 0.11 | 3.4e-1 (9.5e-2) / 9.7e-3 | 1.3e-1 (1.3e-1) / 1.1e-2 |
| mask | 1.2e-2 / 2.8e-2 | 9.6e-2 / 1.6e-2 | 1.3e-1 / 1.0e-2 |
| mask+cubic | **1.3e-4** / 1.1e-3 | **2.1e-3** / 2.2e-5 | 5.4e-2 / 9.2e-4 |
| mask+cubic+energy | 1.6e-4 / 1.1e-3 | 2.7e-3 / 2.2e-5 | 5.3e-2 / 2.7e-4 |
| closure_rel_size | 3.0e-4 (<1e-3) | 1.8e-2 | 2.6e-1 |
| rollout (모든 방법 거의 동일) | 2.5e-4 | 0.20~0.23 | 1.25~1.47 |

**Fisher** (0.1 → 0.02)
| 방법 | 0.1 | 0.05 | 0.02 |
|---|---|---|---|
| lstsq | 9.5e-3 (8.2e-4) / 0.44 | 2.4e-2 (2.3e-3) / 0.48 | 9.4e-2 (1.1e-2) / 0.37 |
| mask | 5.2e-4 / 0.15 | 1.8e-3 / 0.14 | 1.3e-2 / 0.10 |
| mask+cubic | 1.3e-3 / 9.3e-2 | 1.9e-3 / 0.14 | 7.9e-3 / 0.14 |
| closure_rel_size | 8.4e-5 (<1e-3) | 2.8e-4 (<1e-3) | 1.5e-3 |
| rollout | 1e-6 수준 | 1e-5 수준 | 5e-5~3e-4 |

**varvisc** (0.2 → 0.05). Cells are `T_rel_err` / `L_rel_err` / OOD_dzdt / OOD_rollout.
| run | 0.2 | 0.1 | 0.05 |
|---|---|---|---|
| lstsq | 2.2e-1 / 8.5e-2 / 0.11 / 7.3e-3 | 3.3e-1 / 2.3e-1 / 0.13 / 2.1e-2 | 4.0e-1 / 5.5e-1 / 0.18 / 3.7e-2 |
| mask | 1.3e-2 / 2.4e-2 / 0.10 / 7.4e-3 | 4.7e-2 / 1.0e-1 / 0.11 / 2.0e-2 | 1.0e-1 / 2.4e-1 / 0.14 / 2.3e-2 |
| mask+cubic | 1.3e-2 / 2.3e-2 / 0.10 / 7.3e-3 | 2.4e-2 / 7.5e-2 / 0.10 / 1.6e-2 | 5.0e-2 / 1.8e-1 / 0.10 / 2.5e-2 |
| mask+cubic+energy | 1.6e-2 / 2.3e-2 / 0.10 / 7.3e-3 | 2.8e-2 / 7.5e-2 / 0.10 / 1.6e-2 | 5.8e-2 / 1.8e-1 / 0.10 / 2.5e-2 |
| ood_gap (eps 0.3, mask+cubic) | 7.7e-3 / 1.7e-2 / 0.11 / 7.5e-3 | 1.8e-2 / 6.4e-2 / 0.10 / 1.6e-2 | 4.5e-2 / 1.7e-1 / 0.11 / 2.7e-2 |
| ood_gap_lstsq | 1.6e-1 / 1.0e-1 / 0.11 / 7.6e-3 | 2.9e-1 / 3.1e-1 / 0.14 / 2.1e-2 | 3.8e-1 / 7.9e-1 / 0.20 / 3.8e-2 |

`nu_t_err` for varvisc was 1.0~1.4 at p=0.2 for every method, and 1.3e-2~5.7e-2 at p=0.05. Closed regime: every PDE recovered the tensor to `T_rel_err` 1e-10~1e-14, including Fisher and varvisc.

## 4. Differences from the smoke notes, and other oddities
1. **varvisc lstsq full didn't diverge.** At the default data size there was no rollout `inf` and no overflow warning; the overflow seen in the smoke test did not recur.
2. **KS rollout is much larger than the note expected.** The note said about 2% in closed at nu=0.02, but closed rollout was **1.39** at nu=0.02 and **0.19** at nu=0.05. Full is similar: every method gives 1.25~1.47 at 0.02 and 0.20~0.23 at 0.05. At those two params, rollout is almost unaffected by the method.
3. **Fisher closed recovered far better than the note expected.** The note expected 1e-4~1e-2, but closed gave 4e-11~6e-11.
4. **KS lstsq full error is not monotonic in nu.** `T_rel_err` goes 8.9e-2 → 3.4e-1 → 1.3e-1. The selection-rule mass is lower at 0.05 (0.714) than at 0.02 (0.888).
5. **Adding the energy constraint raises `T_rel_err` slightly almost everywhere.** In Burgers, KdV, KS (0.1, 0.05) and varvisc, mask+cubic+energy is slightly worse than mask+cubic. KS 0.02 is the one exception (5.3e-2 vs 5.4e-2).
6. **Fisher p=0.1: mask+cubic is worse than mask alone** (1.3e-3 vs 5.2e-4).
7. **Several cases have `closure_rel_size` < 1e-3**, so their `nu_t_err` means little: KS 0.1 (3.0e-4), Fisher 0.1 (8.4e-5), Fisher 0.05 (2.8e-4). The large `nu_t_err` values (0.4~1.4) mostly occur where closure is small.
8. **varvisc OOD:**
   - For every mask run, OOD_dzdt is pinned near 0.10 regardless of param or method, while in-distribution dz at p=0.2 is 0.021.
   - Training with a narrower input range (ood_gap, eps 0.3) gives about the same OOD_dzdt as eps 0.5 (0.10~0.11).
   - Its `T_rel_err` and `L_rel_err` are actually slightly *better* than eps 0.5.
9. **One energy-constraint residual is just over 1e-10.** KS mask+cubic+energy at nu=0.02 is **1.1e-10** (1e-10 is the threshold the V2 instructions used). All other constrained runs are 2.7e-15~1.2e-11.
10. **Duplicate legend labels in M5_compare.** M5_varvisc_mask_cubic and ood_gap are both labelled `lstsq+cubic+mask`, and the two lstsq runs are both `lstsq`, so they can't be told apart in the figure or in compare.md. In the figure, the second of each pair is ood_gap (pink: mask+cubic, dark green: lstsq).
11. **Overlapping axis labels in M3_compare.** The x-axis tick labels (2e-2, 3e-2, 4e-2) overlap slightly, but the figure is still readable.

## 5. Errors, divergence, memory, runtime
- **Errors and divergence:** All 21 runs (M0 2 + M1~M5 19) finished with rc=0. stderr had no warnings or tracebacks, there were no solver blowups, and no rollout was `inf`.
- **Peak memory:**
  - KS mask+cubic+energy: **15.2GB**
  - KS mask+cubic: 12.2GB
  - K=8 cubic runs: 1.8~2.3GB
  - The rest: 0.3~0.5GB

  Total concurrent use stayed within the free memory (118GB).
- **Runtime:**
  - M0: 278s / 307s (the two ran in parallel)
  - M1~M5: all 19 in parallel, finished in about **15 minutes** (longest was M3_ks_lstsq at 915s)
  - Comparison figures: a few seconds

  Most of the time was data generation (KS/KdV full).

That's just the M1–M5 monitor timing out. All runs had already finished, so nothing needs re-arming and the report above is final.