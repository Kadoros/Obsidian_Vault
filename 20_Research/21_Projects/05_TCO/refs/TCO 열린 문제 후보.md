---
tags:
  - note
parent_concept:
  - "[[20_Research/21_Projects/05_TCO/DOCS_MAP|05_TCO]]"
date: 2026-10-09
---
# TCO 열린 문제 후보 — DeepONet·HyperDeepONet이 못 잡는 것

## 이미 풀린 것 (대박 자리 아님)
- **이동하는 불연속**: 선형 디코더 하한 증명 + 비선형 재구성(shift-DeepONet, FNO, HyperDeepONet 계열)으로 극복 → Lanthaler et al. 2023, [[Kolmogorov n-width]]

## 1. 불연속 / 다중해 해 연산자 ⭐ (가장 근본적)
- 보편근사 정리(Chen & Chen)는 **연산자가 연속**이라고 가정
- **분기(bifurcation)**: 좌굴, 유동 천이, 패턴 형성 → $a\mapsto u$ 가 문턱에서 점프
- **다중해**: Bratu 방정식, 다중 안정, 상분리 → MSE 학습은 **해들의 평균**(비물리적)을 출력
- DeepONet·HyperDeepONet·FNO 모두 구조적으로 걸림
- 함수해석: well-posedness 붕괴 = 음함수 정리 실패 = Fréchet 도함수가 가역 아님
- 접근: 생성형 연산자(여러 해), 분기 구조를 아는 operator learning (비어 있는 편)
- 첫 실패 재현: 1D Bratu에서 DeepONet이 평균 해 출력

## 2. 엔트로피 해 고르기 (보존법칙) ⭐ (TCO와 직결)
- 비점성 Burgers / Euler: 약해 무수히 많음, 물리적인 건 **엔트로피 조건** 만족하는 하나
- 학습된 연산자: 분포 밖에서 팽창 충격파 같은 엔트로피 위반 해 가능
- NIGO는 **이차 에너지**만 → 엔트로피는 **비이차 볼록 함수** → 엔트로피 변수로 구조 재설계 필요
- 첫 실패 재현: 비점성 Burgers, 분포 밖 입력에서 엔트로피 위반 확인

## 3. 장시간 카오스 (붐빔)
- 궤적 예측 불가 → 목표가 "통계·끌개 맞추기"
- 경쟁: NIGO, ECO, dissipative chaos learning

## 4. 기타 (붐빔)
- 입력 의존 다중스케일 (고주파 Helmholtz, 균질화) — [[Spectral Bias]]
- 영역·위상 변화 (자유경계, 파괴)

## 판단
- TCO 본류: **2번**과 결합하기 좋음 (텐서 대칭 → 엔트로피)
- 장기 큰 그림: **1번** (수학 많이 필요, 2–6강 이후)
