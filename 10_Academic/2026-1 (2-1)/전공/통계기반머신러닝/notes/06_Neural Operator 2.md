---
tags:
  - note
  - SciML
  - NeuralOperator
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Neural Operator 2 (7주차, 04/15) — Kernel 구현 변형 (GNO/LNO/MGNO/FNO)
paper: "Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs (JMLR, 2021)"
---

# Neural Operator 2 — Kernel 구현 변형 (GNO / LNO / MGNO / FNO)

> **한 줄 요약:** Neural Operator의 핵심 연산인 **kernel integral $u(x) = \int_D \kappa(x,y)\,v(y)\,d\nu(y)$** 를 어떻게 효율적으로 계산(parameterize)하느냐에 따라 4가지 변형이 나뉜다. **GNO**(그래프 메시지 패싱), **LNO**(저랭크 분해), **MGNO**(계층 multipole), **FNO**(Fourier 공간). 각각 비용·표현력·적합 도메인이 다르다.

논문: *Neural Operator: Learning Maps Between Function Spaces With Applications to PDEs* (JMLR, 2021).

---

## 1. 복습 — Neural Operator 구조

- $G: a(x) \to u(x)$ — **함수(연속) → 함수(연속) 사상** (PDE는 implicit, NO PDE in loss).
- **Key Advantages:** 임의 해상도/메시, 이산화 무관 동일 파라미터, 함수 공간에서 일관, PDE에 적합.
- **3단계 아키텍처:**
  1. **Lifting (enc)** $a(x) \to v_0(x)$ — 점별 변환, 고차원 feature space로 (Data → Feature)
  2. **Iterative Kernel Integration** $v_t \to v_{t+1}$ — physics를 반영
  $$
  v_{t+1}(x) = \sigma\Big(W v_t(x) + \int \kappa(x,y)\,v_t(y)\,dy + b(x)\Big)
  $$
  3. **Projection (dec)** $v_T(x) \to u(x)$ — feature → 출력 함수 (Feature → Data)

→ 자세한 이론: [[05_Neural Operator 1]]

이 강의는 **kernel 층의 4가지 구현 변형(Implementation Variants)** 을 다룬다: **GNO, LNO, MGNO, FNO.**

---

## 2. Graph Neural Operator (GNO)

**Core Idea:** Integral operator → **Graph message passing**

- GNO는 연속 적분 연산자를 **그래프 신경망(GNN) 프레임워크**로 근사.
- 원래 연산자:
$$
u(x) = \int_D \kappa(x,y)\,v(y)\,d\nu(y)
$$
- GNO의 근사 방법:
  1. 영역을 **점(node)** 으로 이산화
  2. 그것들을 **graph**(node + edge)로 취급 (fully-connected graph 가능)
  3. 적분을 **message passing**으로 대체

### 2.1 GNO as a GNN
- **Nodes:** 공간 점 $x_i$
- **Edges:** 연결 (local 또는 global)
- **Message passing:** $\kappa(x_i, x_j)\,v(x_j)$

> kernel 함수 $\kappa(x,y)$ 는 **edge function 으로 학습**된다.
> - 적분 → 이웃에 대한 aggregation
> - kernel 학습 → edge weight 학습

### 2.2 Key Advantages
- **Discretization-invariant:** 서로 다른 grid에서 작동
- **새 query point 처리:** 재학습 없이 node 추가 가능
- **non-local dependency 포착**
- kernel $\kappa(x,y)$ 는 "$y$ 의 소스가 $x$ 의 해에 어떻게 영향을 주는가" = **물리적 상호작용 메커니즘**을 인코딩.

> GNO는 kernel을 최적화로 **shaping**하여, 예측 오차를 최소화하는 데 필요한 올바른 공간 상호작용 패턴(확산·파동·유체)을 재현하도록 학습한다.

---

## 3. Low-rank Neural Operator (LNO)

**Core Idea:** Integral operator → **Low-rank decomposition**

- LNO는 kernel을 **저랭크 분해(low-rank decomposition)** 로 근사 → 표현력 유지하며 계산 비용 대폭 감소.
- 원래 연산자는 $u(x) = \int_D \kappa(x,y)v(y)d\nu(y)$ — kernel $\kappa(x,y)$ 학습은 **$O(N^2)$ 상호작용** 으로 비쌈.

### 3.1 Low-rank decomposition
kernel을 다음처럼 근사:
$$
\kappa(x,y) \approx \sum_{k=1}^{r} \phi_k(x)\,\psi_k(y)
$$
- $r$: rank (작음), $\phi_k(x)$: **출력 기저(output basis)**, $\psi_k(y)$: **입력 기저(input basis)**

**Key Interpretation:**
1. 입력 $v(y)$ 를 기저 $\psi_k(y)$ 에 **사영(project)**
2. 출력 기저 $\phi_k(x)$ 와 결합
$$
u(x) = \sum_{j=1}^{r} \langle \psi^{(j)}, v\rangle\,\varphi^{(j)}(x)
$$

### 3.2 비용과 한계
- **Computational Benefit:** kernel이 full $N\times N$ 복잡도 불필요. 소수의 **global interaction pattern** 만 학습.
  - Original: $O(N^2)$ → Low-rank: **$O(Nr)$**
- **Limitation:** **고도로 비국소적(highly nonlocal) 상호작용**이나 **매우 복잡한 kernel** 은 rank $r$ 이 제한되어 표현력 부족.

---

## 4. Multipole Neural Operator (MGNO/MNO)

**Core Idea:** Integral operator → **Hierarchical, multipole-style approximation**

- MNO는 **계층적(hierarchical) multipole 분해**로 long-range 상호작용을 효율적으로 모델링.
- **Key Insight:** 모든 쌍 $(x,y)$ 의 상호작용을 직접 계산하는 대신, 점들을 **계층적으로 그룹화**하고 **그룹 간 상호작용을 근사**.

### 4.1 Hierarchical Structure
**tree structure (quadtree/octree 같은)** 를 만듦:
- **Fine level → 상세한 국소(local) 상호작용** (high/local)
- **Coarse level → 요약된 전역(global) 상호작용** (low/global)

**계층적 행렬 분해 (Hierarchical matrix decomposition):**
$$
K = K_1 + K_2 + K_3 \quad(\text{fine} \to \text{coarse})
$$
- $K_1$: 대각 부근(국소), $K_2$: 중간 스케일, $K_3$: 전역(coarse 블록).

### 4.2 비용·강점·한계
- **Computational Benefit:** Standard $O(N^2)$ → MNO **$O(N\log N)$** 또는 $O(N)$ (구현에 따라).
- **Strengths:** 대규모(large-scale) 문제에 효율적, **local + global 상호작용 모두 포착**, 물리 시뮬레이션에 적합.
- **Limitations:** 더 복잡한 아키텍처, 계층 설계에 신중함 필요, 단순 연산자보다 학습이 어려울 수 있음.

---

## 5. Fourier Neural Operator (FNO)

**Core Idea:** Integral operator → **Fourier space**

- FNO는 **Fourier(주파수) 공간에서 global convolution** 을 수행해 함수 사이 사상을 학습.
- 합성곱 정리: 공간에서의 convolution = **Fourier 공간에서의 곱(multiplication)**.
$$
\hat u(k) = R_\theta(k)\,\hat v(k)
$$
- $\hat v(k)$: 입력의 Fourier 변환, $R_\theta(k)$: 주파수 공간에서 학습되는 변환.

### 5.1 Key Procedure (4단계)
1. **Fourier Transform:** $v(x) \to \hat v(k)$
2. **Spectral Transformation:** $\hat v(k) \to R_\theta(k)\,\hat v(k)$
   - **저주파(low-frequency) 모드만 유지, 고주파는 절단(truncation)** (low-frequency truncation)
3. **Inverse Fourier Transform:** $\hat u(k) \to u(x)$
4. **Local Linear Layer 추가:**
$$
u(x) = \mathcal{F}^{-1}(R_\theta \hat v) + W v(x)
$$
   - $\mathcal{F}^{-1}(R_\theta\hat v)$: **global interaction (Fourier)**, $W v(x)$: **local correction (linear layer)**

### 5.2 Strengths
- **계산 효율적:** Fourier 변환(FFT)이 convolution을 곱셈으로 변환.
- **물리적 해석:** 서로 다른 주파수 모드들이 어떻게 상호작용하는지 학습.
- **적합 분야:** CFD, 날씨 예측, 확산 시스템 (smooth/주기적 PDE).

### 5.3 구조
$$
a(x) \to P \to \text{Fourier layer 1} \to \cdots \to \text{Fourier layer T} \to Q \to u(x)
$$
각 Fourier layer: $v(x) \to [\mathcal{F} \to R \to \mathcal{F}^{-1}]$ (위 경로) + $W$ (아래 경로) → 합 → $\sigma$.

---

## 6. Summary — 변형별 핵심 수식

| 변형 | 키워드 | 핵심 계산 |
|------|--------|-----------|
| **GNO** | Graph | $u(x) = \int_{B(x,r)} \kappa(x,y)v(y)\,dy$ ($J$-점 중 $J'$ 서브샘플, 절단 적분) |
| **LNO** | Low-rank | $u(x) = \sum_{j=1}^{r} \langle\psi^{(j)},v\rangle\,\varphi^{(j)}(x)$ (텐서곱 분해) |
| **MGNO** | Multi-scale | $K = K_{1,1} + K_{1,2}K_{2,2}K_{2,1} + \cdots$, $u(x) = (Kv)(x)$ (멀티스케일 분해) |
| **FNO** | Fourier | $u(x) = \mathcal{F}^{-1}(R_\phi\cdot\mathcal{F}(v))(x)$ (FFT로 Fourier 도메인 parameterize) |

---

## 7. Comparisons (종합 비교표)

| Aspect | GNO | LNO | MNO | FNO |
|--------|-----|-----|-----|-----|
| **Core idea** | Full kernel learning (graph 기반) | Low-rank factorization | Hierarchical multipole | Fourier transform |
| **Interaction** | All-to-all (explicit) | Global (compressed) | Local + global (hierarchical) | Global (frequency) |
| **Structure** | Graph / message passing | Basis decomposition | Tree / multi-scale | Spectral |
| **Complexity** | $O(N^2)$ | $O(Nr)$ | $O(N\log N)$ | $O(N\log N)$ |
| **Strength** | 가장 일반적, 유연, 불규칙 메시 가능 | low-rank 시스템에 효율적 | long-range 상호작용에 효율적 | smooth PDE에 강함 |
| **Weakness** | 확장성 나쁨(비쌈) | 복잡한 물리에 표현력 제한 | 복잡한 설계 | 비주기/불규칙 도메인에 약함 |

---

## 8. 요약

- 모든 변형은 같은 **kernel integral**을 다르게 근사하는 방식.
- **GNO**: 그래프 메시지 패싱(유연하나 $O(N^2)$). **LNO**: 저랭크($O(Nr)$, 표현력 제한). **MGNO**: 계층 멀티폴($O(N\log N)$, local+global). **FNO**: Fourier 공간($O(N\log N)$, smooth PDE 강점, 비주기 약점).
- 선택 기준: 도메인 규칙성, 상호작용 범위(local/global), 계산 예산.

---

## 관련 노트

**강의 노트**
- [[05_Neural Operator 1]]
- [[07_Neural Operator 3]]
- [[02_Physics-informed neural networks 1]]

**개념 노트 (50_Concepts)**
- [[Neural Operator]]
- [[Fractional Operator]] — heat semigroup ↔ FNO convolution 구조
- [[Mellin Neural Operator]] — FNO의 Mellin 변환 기반 변형
- [[GN-Operator]] — Gregory-Newton 기반 적분 연산자
- [[Spectral Bias]] — FNO의 Fourier 공간 학습 특성

**연구 노트 (20_Research)**
- [[../../../../../20_Research/21_Projects/01_GNR/origin/XNO expriment]] — 적분 연산자 행렬 $S$ (체비쇼프 기반) 실험

**함수해석 관점 (50_Concepts)**
- [[Integral Operator and Kernel]] — GNO/LNO/MGNO/FNO = 같은 적분 연산자의 다른 parameterize
- [[Diagonalization of Convolution]] — FNO가 Fourier 공간에서 곱셈인 이유
- [[Orthonormal Basis Expansion]] — LNO의 저랭크 분해 $\sum\phi_k(x)\psi_k(y)$ = 기저 전개
- [[FNO]] · [[Attention as Integral Operator]]
