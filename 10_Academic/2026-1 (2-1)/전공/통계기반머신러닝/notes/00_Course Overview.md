---
tags:
  - note
  - SciML
course: 통계기반머신러닝 (Statistical Machine Learning, 56262)
lecture: Course Overview (1주차, 03/04)
---

# Course Overview — Statistical Machine Learning (56262)

> 강의 전체를 관통하는 주제: **Scientific Machine Learning (SciML)** — 물리 법칙(physical laws)과 데이터 기반 학습(data-driven learning)을 어떻게 결합할 것인가.

---

## 1. 강의 정보 (Course Information)

- **담당 교수:** Dr. Junseok Kwon (권준석)
- **강의 시간:** 매주 목요일 15:00–17:50
- **강의실:** Room 209, 101동 (310-735)

---

## 2. 왜 SciML인가 — 두 가지 큰 흐름

| 키워드 | 핵심 주장 |
|--------|-----------|
| **AI4Science** | AI/ML이 과학 계산(scientific computation)과 발견(discovery)의 근본을 혁신할 잠재력. **물리(physics), 화학(chemistry), 생물(biology), 공학(engineering)** 전반의 발견을 가속. |
| **World Model** | Yann LeCun: 진정한 기계 지능은 토큰 예측(token prediction)을 넘어서야 한다. LLM 대신 **JEPA & World Models**로 전환 — **Physical World Understanding**(시각·감각 입력의 연속적 데이터 스트림을 표현·예측)을 체화해야 함. |

→ 두 흐름 모두 **연속적인 물리 세계(continuous physical world)를 표현하고 예측**하는 능력을 요구한다. 이 강의는 그 도구들을 다룬다.

---

## 3. 강의의 두 핵심 질문 (Scientific Machine Learning)

1. **물리 법칙을 어떻게 데이터 기반 학습에 통합(integrate)할 것인가?**
2. **고차원 연산자(high-dimensional operators)를 학습하는 신경망 구조(neural architecture)를 어떻게 설계할 것인가?**

이 두 질문을 4개의 주제 축으로 풀어간다:

| # | 주제 | 한 줄 정의 (역할) |
|---|------|-------------------|
| 1 | **PDE → NN** | PDE 자체를 학습 대상으로 (PDE를 신경망으로 푸는 문제 설정) |
| 2 | **Physics-Informed Neural Networks (PINN)** | **하나의 PDE 해(one PDE solution)**를 신경망으로 표현. 변형: MS-PINN, XPINN, Bayesian PINN, PINO |
| 3 | **Neural Operator** | **함수 → 함수 (Function → Function)** 사상을 학습. continuous → continuous. 대표: DeepONet, GNO, LNO, MGNO, FNO |
| 4 | **Kolmogorov–Arnold Networks (KAN)** | **명시적 함수 구조(Explicit Functional Structure)** 학습. 기반: Kolmogorov–Arnold Theorem, Physics-Informed KANs |

> **핵심 대비:** PINN은 *하나의* PDE 해(특정 초기/경계조건)를 푸는 반면, Neural Operator는 함수 공간 사이의 사상(예: 초기조건 함수 → 해 함수)을 학습해 **여러 PDE 인스턴스에 일반화**한다.

---

## 4. 성적 (Grade)

- **Project 90%**
  - 자신의 연구(own research)에 **물리 법칙(Physics Law)을 적용**.
  - 기본 아이디어를 담은 **논문(paper) 작성** (가능하면 실험 결과 포함).
- **Participation 10%**
  - Project Presentation (원하는 경우).

### Reference
- AI for Science Seminar (252-5256-00L)
- AI in the Sciences and Engineering (2024)

---

## 5. 잠정 강의 일정 (Tentative Schedule)

| 주차 | 날짜 | 주제 | 세부 내용 |
|------|------|------|-----------|
| 1주차 | 03/04 | Course overview | 강의 개요 |
| 2주차 | 03/11 | Neural PDE 1 | PDEs as learning targets |
| 3주차 | 03/18 | Neural PDE 2 | Limitations of black-box neural networks |
| 4주차 | 03/25 | PINNs 1 | Physics-informed loss formulation, Forward & inverse PDE problems |
| 5주차 | 04/01 | PINNs 2 | Advanced PINNs |
| 6주차 | 04/08 | Neural Operators 1 | Operator learning theory |
| 7주차 | 04/15 | Neural Operators 2 | DeepONet architecture |
| 9주차 | 04/29 | Neural Operators 3 | Advanced NOs |
| 10주차 | 05/06 | KAN 1 | Kolmogorov–Arnold representation theorem |
| 11주차 | 05/13 | KAN 2 | KAN architecture and spline-based edges |
| 12주차 | 05/20 | KAN 3 | Advanced KANs |
| 13주차 | 05/27 | Applications | — |
| 14주차 | 06/03 | Project presentation 1 | — |
| 15주차 | 06/10 | Project presentation 2 | — |

---

## 6. Application 예시

- **Genie 3** (Google DeepMind) — "A new frontier for world models". 월드 모델의 응용 예시로 소개됨.
  - https://www.youtube.com/watch?v=hUONc4FRS1Q

---

## 관련 노트

**강의 노트**
- [[01_PDE using Deep Learning]]
- [[02_Physics-informed neural networks 1]]
- [[05_Neural Operator 1]]
- [[08_Kolmogorov-Arnold Networks 1]]

**개념 노트 (50_Concepts)**
- [[Operator_Math_Theory]] — 연산자 수학 기초 (강의 전반의 토대)
- [[PINN]]
- [[Neural Operator]]
- [[KAN]]
