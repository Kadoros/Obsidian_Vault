---
tags:
  - concept
parent_concept:
---

    프로젝트 회고

1. 서론: 가설의 수립

  - 배경: 연속 수학(미적분)과 이산 수학(차분/수열합)의 평형 이론인 Heinn-X(H(x) 보정항)를 Neural Operator의 적분
    커널에 이식하면, 물리적 무결성을 가진 강력한 AI가 될 것이라 가설을 세움.
  - 목표: 고정된 대수적 적분 행렬(S-Matrix)을 통해 이산화 오차(Discretization error)가 없는 완벽한 물리
    시뮬레이터 구축.

2. 실험 과정과 도메인의 확장

  - Phase 1 (다항식): 노이즈 없는 수열의 합 학습. (결과: 오차 0에 가까운 완벽한 성공)
  - Phase 2 (동적 PDE): 1D Advection, Burgers' 방정식 적용. (결과: 파동 속도가 빨라지거나 충격파 발생 시
    FNO/ChebNO 대비 성능 하락)
  - Phase 3 (역문제 및 노이즈): Poisson 방정식 역산 및 20~30% 노이즈 환경 테스트. (결과: 노이즈가 적분기를 타고
    증폭되는 부작용 발견)

3. 핵심 발견 (Critical Findings): 왜 터졌는가?

  - 수치적 폭주(Numerical Blow-up): 자기회귀(Autoregressive) 예측 시 H(x) 보정항이 신경망의 미세 오차를
    다항 차수로 증폭시켜 경계값에서 무한대로 발산하는 현상 규명.
  - 경직성(Rigidity)의 함정: 하드코딩된 S행렬은 다항식 세계에선 완벽하지만, 비다항식(삼각함수/지수함수) 기반의 실제 물리
    데이터에서는 학습을 방해하는 '족쇄'로 작용함을 데이터로 확인.
  - 노이즈 증폭기: 적분 연산의 본질(Smoothing)을 기대했으나, 엄격한 대수 규칙이 랜덤 노이즈마저 '적분해야 할 신호'로 인식하여
    고차원적으로 왜곡함.

4. 데이터가 말해주는 최종 결론

  - Heinn-X의 적합 도메인: 노이즈가 없는(Zero-noise) 순수 이산 수학 및 기호 추론(Symbolic AI) 영역.
  - Neural Operator 설계 지침: 딥러닝에서 사전 지식(Prior)을 주입할 때는 데이터의 불완전성을 수용할 수 있도록
    'Hard-constraint'가 아닌 'Soft-regularization' 혹은 'Learnable structure' 방식이
    필수적임.

5. 프로젝트 소회 및 향후 과제

  - "수학적으로 완벽한 이론이 신경망이라는 유연한 시스템 내에서 어떻게 독이 될 수 있는지 직접 겪어본 값진 경험이었다."
  - "비록 일반적인 PDE Solver로서는 실패했으나, 이 과정에서 획득한 스펙트럴 신경망(FNO, ChebNO) 구현 기술과 물리 데이터
    핸들링 능력은 향후 더 유연한 Physics-Informed AI 설계의 밑거름이 될 것이다."


https://github.com/Kadoros/X-NO


