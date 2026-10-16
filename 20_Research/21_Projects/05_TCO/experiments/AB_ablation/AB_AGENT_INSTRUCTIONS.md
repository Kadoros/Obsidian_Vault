# 통제 실험(AB): DeepONet에서 branch만 3차 텐서로 바꾸기 (서버 에이전트용)

## 무엇을 비교하나
세 모델 모두 같은 일을 배운다. 입력은 순간의 해 u(x), 출력은 그 순간의 변화율 u_t(x)다(진화 연산자).
trunk(기저), 데이터, 손실(필드 공간 MSE), 옵티마이저(Adam + cosine), step 수, seed가 모두 같다. **branch만 다르다.**

| 모델 | branch |
|---|---|
| `deeponet` | b = MLP(센서값 u) — 표준 DeepONet |
| `coeffmlp` | b = MLP(c), c = ⟨u, Φ⟩ — 텐서와 같은 입력 좌표를 쓰는 MLP |
| `tensor` | b = A c + T(c, c) — TCO, 3차 텐서 |

평가는 모든 모델에 똑같이 한다. 정확도는 test u_t 오차(`dz`), 짧은 롤아웃 오차, 스펙트럼 오차로 본다. 물리는 각 모델의 생성자를 실수 푸리에 좌표로 옮겨 0에서 Taylor 계수(선형 A, 이차 T)를 뽑고, 이것을 Galerkin 참값과 비교한다. MLP에 대해서는 "블랙박스가 암묵적으로 갖고 있는 텐서"가 된다.

## 파일
기존 폴더에 `tco_ablation.py`를 추가한다. `tco_pde.py`, `tco_pod.py`, `tco_trunk.py`가 같은 폴더에 있어야 한다. torch가 필요하며 GPU가 있으면 자동으로 쓴다.

## 스모크 테스트
```bash
python3 tco_ablation.py --pde burgers --quick --tensor_solver lstsq --out runs/AB_smoke
```
통과 기준: closed `tensor` 줄의 `Trel`이 1e-8 이하이고, 세 모델 모두 에러 없이 끝난다. MLP 숫자는 quick에서 의미가 없다.

주의: **`--quick` + `--tensor_solver adam`은 실패하는 것이 정상이다.** 40개 궤적으로는 Adam이 잘 들뜨지 않은 모드의 텐서 성분을 고정하지 못한다. 확인 결과 closed dz는 1.7이었다. 본 실험의 데이터 크기(200개 궤적)에서는 정확하다.

## 실험
### AB-1 본 실험 (가장 중요)
4개 PDE × lr 3개 × 모델 3개 × seed 3개 × regime 2개다. lr 스윕은 모든 모델에 똑같이 적용해 공정성을 확보하려는 것이다.
```bash
for lr in 1e-3 3e-3 1e-2; do
  python3 tco_ablation.py --pde burgers        --lr $lr --out runs/AB_burgers_lr$lr
  python3 tco_ablation.py --pde kdv            --lr $lr --out runs/AB_kdv_lr$lr
  python3 tco_ablation.py --pde ks --K 12      --lr $lr --out runs/AB_ks_lr$lr
  python3 tco_ablation.py --pde fisher         --lr $lr --out runs/AB_fisher_lr$lr
done
```
기본값: `--steps 20000 --seeds 0 1 2 --trunk pod --tensor_solver adam --n_traj 200`.

### AB-2 기준선: 텐서를 최소제곱으로 풀었을 때 (같은 손실의 정확한 최소점)
```bash
for p in burgers kdv fisher; do
  python3 tco_ablation.py --pde $p --models tensor --tensor_solver lstsq --seeds 0 --out runs/AB_${p}_lstsq
done
python3 tco_ablation.py --pde ks --K 12 --models tensor --tensor_solver lstsq --seeds 0 --out runs/AB_ks_lstsq
```

### AB-3 데이터 양 (Burgers)
각 모델에는 AB-1 Burgers에서 closed `dz` 평균이 가장 낮았던 lr을 쓴다. 그 lr을 보고서에 적는다.
```bash
for n in 25 50 100 400; do
  python3 tco_ablation.py --pde burgers --n_traj $n --lr <모델별 최적 lr> --models <모델> --out runs/AB_burgers_n${n}_<모델>
done
```

### AB-4 (선택, 시간이 남으면) trunk도 함께 학습
```bash
python3 tco_ablation.py --pde burgers --trunk joint --lr 1e-3 --out runs/AB_burgers_joint
```
joint는 최적화가 어려운 설정이라 결과를 그대로 보고만 하면 된다.

## 내가 미리 확인한 것 (참고)
Burgers ν=0.2, closed, 200개 궤적, 6000 step, seed 0 기준이다.

| 모델 | dz | T 오차 | 선택 규칙 질량 | 파라미터 |
|---|---|---|---|---|
| deeponet (lr 1e-3) | 0.186 | 2.54 | 0.18 | 43,537 |
| coeffmlp (lr 1e-3) | 0.268 | 4.47 | 0.15 | 37,521 |
| tensor, adam lr 1e-3 | 1.8e-4 | 1.8e-3 | 0.997 | 2,890 |
| tensor, adam lr 1e-2 | 3e-15 | 5e-13 | 1.000 | 2,890 |

MLP를 lr 1e-2로 돌린 결과는 아직 없다. 그래서 AB-1에서 lr을 스윕한다.

## 보고할 것
1. 스모크 결과
2. **AB-1 표**: PDE × regime × 모델별로 최적 lr의 seed 평균±표준편차를 적는다. 열은 `dz`, `rollout_short`, `spectrum`, `T_rel_err`, `T_rel_err_on_rule`, `T_selection_mass`, `A_rel_err`, `eig_purity_mean`, `n_params`, `train_time_s`이다. lr별 전체 표도 첨부한다(`summary.md` 12개).
3. AB-2 lstsq 기준선과 AB-1 adam 텐서의 비교
4. AB-3: 모델별로 n_traj에 따른 `dz`와 `T_rel_err` 표
5. 그림: 각 PDE의 `fig_implied_tensor_closed.png`, `fig_implied_tensor_full.png`(최적 lr run)
6. 이상한 점: 발산(inf), seed 간 큰 편차, 학습 곡선이 수렴하지 않은 경우, GPU 사용 여부, 총 실행 시간

코드는 수정하지 말고, 에러가 나면 고치기 전에 보고한다.
