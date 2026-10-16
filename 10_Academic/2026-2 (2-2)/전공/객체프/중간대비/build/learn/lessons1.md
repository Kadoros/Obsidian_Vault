@unit U1 | SW 공학과 OOP 입문 | L02 Intro to OOP.pdf + Handout 1
@intro 소프트웨어 위기 → SW 공학 → 좋은 SW의 요소 → 프로그래밍 패러다임 → OOP 개념. 기출 1번 빈칸(software crisis, complexity, maintenance, global/dependent)이 거의 매년 여기서 나와. 영어 단어를 정확히 외우는 게 점수야.

@lesson L1-1 | 소프트웨어 위기 · 생명주기 · SW 공학 | L02 p.3–6

## 소프트웨어 위기 (Software Crisis) {#crisis}

- 컴퓨터 성능(power)과 문제(SW)의 **복잡도(complexity)** 가 빠르게 늘어나는데 SW 기술이 그 복잡도를 따라가지 못함
- 올바르고, 이해하기 쉽고, 검증 가능한 프로그램을 쓰기가 어려워짐
- 증상: 관리 불가(unmanageable), 유지보수 어려움, **예산 초과(over-budget)**, **일정 초과(over-time)**, 품질 낮음, 요구사항 불충족
- **원인: 복잡도 (complexity)**

> 시험 포인트: 2025·2023·2022 빈칸. "(software crisis) arose because as computer hardware power grew rapidly, (complexity) of the software systems increased even faster".

## 소프트웨어 생명주기 (Software Life Cycle) {#lifecycle}

1. **Requirement Analysis** (요구 분석): 문제 명세
2. **Design** (설계): 프로그램 구조, 모듈 명세
3. **Implementation** (구현)
4. **Test** (테스트): unit test, integration test
5. **Maintenance** (유지보수)

**Fred Brooks**: 전형적인 시스템 **비용(costs)의 90% 이상이 유지보수(maintenance) 단계**에서 생기며, 성공한 SW는 반드시 유지보수된다(will inevitably be maintained).

> 시험 포인트: 2024·2017 빈칸 "over 90% of (the costs) of a typical system arise in (the maintenance) phase, and any successful piece of software will inevitably be (maintained)".

## SW 공학의 정의와 목표 {#se-def}

**정의**
- [IEEE] SW의 개발·운영·유지보수에 **체계적이고(systematic), 규율 있고(disciplined), 정량화 가능한(quantifiable)** 접근을 적용하는 것 = SW에 공학을 적용
- [Fritz Bauer] 신뢰할 수 있고 효율적으로 작동하는 SW를 **경제적으로(economically)** 얻기 위해 건전한 공학 원칙을 세우고 사용하는 것

**목표 (Goals)**
- **올바르고(correct), 효율적이고(efficient), 신뢰할 수 있는(reliable)** SW를 만든다
- SW 개발과 유지보수의 **비용(cost)을 최소화**한다

**SE의 목표 4가지 (Goals of SE 슬라이드)**
| 목표 | 뜻 |
|---|---|
| **Maintainability** | 변경·개선을 쉽게 할 수 있는 능력 |
| **Dependability** | 필요할 때 SW가 제대로 작동한다고 **믿을 수 있는** 능력 |
| **Efficiency** | 컴퓨팅 자원(주로 공간·시간)을 효과적으로 쓰는 능력 |
| **Usability** | 최종 사용자가 쉽고 효과적으로 쓰는 능력 |

> 시험 포인트: 2022·2019 빈칸 "(software engineering) … to (economically) obtain software that is reliable and works efficiently", 2025 "minimize (the cost)", 2017 "(Dependability) means the ability to rely on the software to function properly when needed".

@lesson L1-2 | 좋은 SW의 요소 · SW 성질 | L02 p.2, 7 + Handout 1

## 좋은 소프트웨어의 요소 (Handout 1) {#quality}

| 요소 | 뜻 |
|---|---|
| **correct** (correctness) | 사용자 요구·명세를 오류 없이 만족 |
| **efficient** (efficiency) | 자원(공간·시간, HW)을 최적으로 써서 빠르게 응답 |
| **easy to maintain** (maintainability) | 읽기 쉽고(readability), 고치기 쉽고(modifiability), 확장하기 쉽고(extensibility, scalability), 재사용하기 쉽고(reusability), 디버그·테스트 쉽고(testability), 모듈화(modularity), 이식 쉬움(portability) |
| **stable, reliable, robust** | 안정성, 신뢰성, 견고성 |
| **easy to use** (usability) | 쓰기 쉬움 |
| **secure** (security), integrity | 무단 접근·손상·악의적 공격으로부터 데이터 보호 |
| interoperability | 표준 프로토콜·인터페이스로 다른 시스템과 데이터 교환 |
| concise, complete, consistent, well-documented, well structured | 간결, 기능 완비, 일관성(명명 규칙 등), 문서화, 구조화 |

> 시험 포인트: maintainability에 들어가는 "easy to read, modify, extend, reuse, debug/test, port"를 영어로 쓸 수 있어야 해 (2019·2016 서술 "A program with high maintainability is easy to (read), easy to (modify), easy to (extend)…").

## 안정성 · 신뢰성 · 견고성 {#robust}

- **stability**: 조건이 바뀌어도 시간이 지나도 올바른 기능을 유지 (어떨 땐 되고 어떨 땐 안 되면 unstable)
- **reliability**: 정해진 조건에서 정해진 기간 동안 요구 기능을 **실패 없이 일관되게** 수행하는 능력
- **robustness**: 예외 상황(잘못된 입력, 재해)에서도 기능을 유지
- 세 단어는 뜻이 거의 같고 강조점만 조금 다르다

> 함정: 2025 빈칸 "(reliability) means the ability of the software to consistently perform its required functions without failure under specified conditions for a specified period" vs 2017 "(Dependability) means the ability to rely on the software to function properly when needed". 정의 문장으로 구별해.

## SW 성질 (Software Properties) {#sw-props}

- **Modularity** – divide and conquer (분할 정복)
- **Encapsulation** – hide the implementation (구현 숨기기)
- **Localization** – collect similar things together (비슷한 것 모으기)
- **Abstraction** – simplifying complex reality (복잡한 현실 단순화)
- **Uniformity** – make everything look similar
- **Completeness** – do everything required
- **Confirmability** – be able to prove that the software works properly

@lesson L1-3 | 프로그래밍 패러다임 | L02 p.8–15

## 비구조적 프로그래밍 (Unstructured Programming) {#unstructured}

- **main 프로그램 하나**로만 구성, 명령어들의 나열
- **전역 데이터만** 사용
- **goto 문**을 사용
- 단점: 같은 문장 시퀀스가 반복되면 다 다시 써야 함
- **스파게티 코드**: goto가 여기저기 점프해서 구조가 복잡하게 얽힘 → 이해·흐름 추적·수정이 거의 불가능

> 시험 포인트: 2024 빈칸 "(Unstructured programming) makes extensive use of GOTO statements… a program contains only a single code block".

## 절차적 · 모듈 프로그래밍 {#procedural}

**절차적 프로그래밍 (Procedural)** — 스파게티 코드의 남용 때문에 구조적 언어가 등장
- 프로그램 = **프로시저 호출의 나열**, 프로시저 = 같은 문장 시퀀스를 묶은 것
- 반복이 줄고 오류가 줄어듦
- **구조적 프로그래밍 (Structured Programming)** ≒ **top-down approach** ≒ **divide and conquer** ≒ **functional decomposition**

**모듈 프로그래밍 (Modular)**
- SW가 분리된 부분(**module**)들로 구성. 공통 기능의 프로시저들을 모듈로 묶음
- 프로그램은 **인터페이스**로 모듈을 사용: **interface는 보이고(visible), implementation은 숨겨짐(hidden)**
- 유지보수성 향상

> 시험 포인트: 2022 빈칸 "structured programming ≒ (top-down approach) ≒ (divide and conquer) ≒ functional decomposition".

## 전역 변수를 쓰지 마라 {#global-vars}

- **전역 변수 사용은 위험(unsafe)**
  - 데이터(전역 변수) 공유는 모듈 프로그래밍 원칙 위반
  - 모든 모듈이 아무 제약 없이 모든 전역 변수에 접근 → 어떤 모듈도 독립적으로 개발·이해할 수 없음
  - **모든 모듈이 서로 의존(dependent on one another)** 하게 만든다
- 해결: **Modularized Data** — 데이터를 모듈 안에 **지역화(localize)** → 모듈끼리 더 독립적 → 안전

> 시험 포인트: 2024·2022·2019·2017·2016 거의 매년! "Using (global) variables is often unsafe because this makes all modules (dependent) on one another."

## 절차적/모듈 방식의 문제와 OOP {#oop-why}

**절차적·모듈 방식의 문제**
- 데이터와 연산이 **분리(decoupled)** 되어 있음
- 큰 시스템에서 잘 안 됨: 디버그·확장·유지보수 어려움, 코드 재사용 제한
- 명시적인 생성·소멸

**OOP**
- 프로그램 = **상호작용하는 객체들의 집합**, 각 객체가 자기 상태를 유지
- **데이터와 연산을 객체 하나로 결합**
- 구조적 = "data + function = program", OOP = "data + function = object, **object + object = program**"
- 문제 영역을 처리의 흐름이 아니라, 서로 **메시지를 주고받는 객체들**로 본다
- 객체는 SW의 **부품(component)** 이고, 객체의 **인터페이스는 잘 정의**되어야 함

**Why OO?** 큰 SW 개발에 좋음, 유지보수성, **재사용(reuse, not rewrite)** → 생산성·품질·이해도·확장성·수명 향상. 이미 잘 테스트된 재사용 모듈을 쓰므로 **신뢰성도 증가**.

> 시험 포인트: 2024 빈칸 "(Object-oriented programming) is a programming paradigm based on the concept of (objects), which can contain data and code".

@lesson L1-4 | OOP 개념: ADT · 객체 · 캡슐화 · 상속 · 다형성 | L02 p.24–33

## 추상 자료형 (ADT) {#adt}

- **ADT**: 데이터 변수들과 관련 연산들의 집합으로, **특정 구현과 독립적으로 정밀하게 명세된** 것
- **ADT = data + operations (no implementation)**
- OOP에서는 프로시저를 정의하려고 데이터를 정의하는 게 아니라, **데이터를 정의하는 데 필요한 프로시저를 정의**한다
- ADT는 데이터와 프로시저를 결합한 타입. C++에서는 **class**로 ADT를 정의
- 사용자는 ADT가 **무엇을 하는지(what)** 만 알면 되고 **어떻게 하는지(how)** 는 몰라도 됨 (예: stack의 push/pop)

> 시험 포인트: 2025 서술 "ADT is called abstract because … (its data and operations are specified independently of any particular implementation)".

## 클래스와 객체 {#class-object}

- **class**: 객체의 속성(attributes = **member variables**)과 행동(behaviors = **member functions**)을 정의
- **object**: **클래스의 인스턴스(instance of a class)**. 내부 데이터, 내부 연산, **인터페이스 연산**으로 구성
  - identity, attribute, behavior(method), 다른 객체와의 관계를 가짐
  - **클래스의 메서드만** 객체의 내부 데이터에 접근 가능
  - **메시지 전달 (message passing)**: 메서드를 호출해서 다른 객체에 작업을 요청
- **Class vs Object**
  - 같은 클래스로 만든 객체들은 서로 **다른 객체** (각자 다른 메모리 공간·주소)
  - 같은 클래스의 객체들은 클래스의 **메서드를 공유**
  - 객체는 실행 시간에 동적으로 생성·소멸될 수 있다

> 시험 포인트: 2016 빈칸 "(An object) is an instance of a class".

## 정보 은닉 · 캡슐화 (개요) {#encap-intro}

- **캡슐화**는 메시지를 보내는 객체들로부터 클래스의 기능적 세부를 **감춘다 (conceals the functional details)**
- 객체의 **내부 데이터는 인터페이스를 통해서만 수정**될 수 있다
- 객체 그림: 바깥에 interface operations(specification), 안에 data와 internal operations(implementation)

> 시험 포인트: 2025 빈칸 "In the concept of information hiding, (internal data) of an object can be modified only through (an interface)". 자세한 건 U4.

## 상속과 다형성 {#inherit-poly}

- **상속 (Inheritance)**: 자식 클래스(sub class)가 부모 클래스(super class)의 속성·행동을 물려받고 자기 것을 추가. 자식의 속성은 부모와 대부분 비슷해야 함. **목표: 객체(클래스) 재사용** → 대형 SW 개발 비용 절감
- **다형성 (Polymorphism)**: 같은 메서드(메시지)가 다른 의미를 가질 수 있음. 서로 다른 타입의 객체가 같은 이름의 메서드 호출에 각자 타입에 맞게 반응
  - C++에서: **virtual function, operator overloading, function overloading, template**
- 동적 바인딩 (dynamic binding)
- **객체 모델의 이점**: 시간이 지나며 진화하는 시스템(확장 가능, 안정적), 객체·클래스로 생각하는 게 사람에게 쉬움, 클라이언트와 구현자를 분리해 캡슐화로 실수로 인한 손상 방지, 재사용

> 함정: 상속·virtual은 중간 이후 진도(교안 일정 6–7주차지만 올해는 아직). 대시보드의 '범위 밖' 표시와 같음.
