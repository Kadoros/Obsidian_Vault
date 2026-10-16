@unit U3 | 객체지향 설계 (IIKH) | L03 Object-Oriented Design.pdf (Budd Ch.3)
@intro 책임 주도 설계와 개발 9단계, IIKH 예제, 구성요소의 특징(결합도·응집도, 인터페이스·구현), 통합과 stub, 유지보수. 결합도/응집도 빈칸은 2024·2023·2022·2019·2016에 다 나왔고, stub·slowly integrated 서술도 단골이야.

@lesson L3-1 | 책임 주도 설계 · 개발 과정 · 시나리오 | L03 p.2–9

## 책임 주도 설계 (Responsibility Driven Design) {#rdd}

- OOP = 상호작용하는 객체들의 집합
- 각 객체는 공동체(community) 안에서 **책임(responsibility)** 을 가진 구성요소
- 시스템이 수행할 활동들을 나누고, 그 활동(책임)을 시스템의 객체들에 **분배**
- 책임 목록을 다 만든 뒤, 객체 집합을 정하고 어떤 책임을 어떤 객체에 줄지 결정
- **한 객체 안의 책임들은 서로 밀접하게 관련**되어야 함
- 설계 과정: 부정확하고 모호하고 불분명한 **명세(specification)** → 구체적 논리의 **SW 시스템 설계**

## 개발 과정 9단계 {#dev-process}

1. **Initial Description** (Specification) — 초기 명세
2. **Refine Specification** — 명세 다듬기 (시나리오)
3. **Identification of Components** — 구성요소 식별
4. **Identification of Components Responsibilities** — 구성요소의 책임 식별 (CRC 카드)
5. **Formalize the Interface** — 인터페이스 정형화
6. **Designing the Subsystem** — 설계
7. **Implementing Components** — 구성요소 구현 (+ unit test)
8. **Integration of Components** — 통합 (stub)
9. **Maintenance & Evolution** — 유지보수와 진화

## IIKH와 시나리오 {#scenario}

- **IIKH (Intelligent Interactive Kitchen Helper)**: 부엌의 레시피 색인 카드 상자를 대체하는 PC 응용. 레시피 DB 관리 + 일주일 같은 기간의 식사 계획, 인원수에 맞게 레시피 자동 조절(scale), 주간·일·끼니별 메뉴 출력, 통합 장보기 목록 출력
- 초기 명세는 **모호하고 불분명** (사장이 냅킨 뒤에 그려 옴) → 모호함을 없애야 함
- **명세 다듬기 = 시나리오 따라가기 (walking through scenarios)**: 이미 동작하는 응용이 있다고 **가정하고** 다양한 사용 방법을 따라가 본다
  - look and feel 정하기, 의도한 용도를 빠짐없이 찾기, 설명 문서와 상위 설계 만들기
  - 다른 저자들은 **use-cases**라고 부름 (시스템 사용 시나리오의 집합)
- IIKH 기능: 레시피 DB 탐색, 새 레시피 추가, 레시피 편집·주석, 여러 코스의 식사 계획, 인원수에 맞게 조절, 기간(일주일) 계획, 장보기 목록 생성

@lesson L3-2 | 구성요소 식별 · CRC 카드 · IIKH의 6개 구성요소 | L03 p.10–18

## 구성요소 (Component) {#component}

- **추상적 설계 단위**로, 서로 다른 작업에 대한 책임을 연결할 수 있는 것
- **작고 잘 정의된 책임 집합**을 가져야 함
- 다른 구성요소와의 상호작용은 **가능한 최소**로

## CRC 카드 {#crc}

- 구성요소는 **CRC 카드**로 가장 쉽게 기술한다: **C**omponent(이름), **R**esponsibility(맡은 책임 설명), **C**ollaborators(협력하는 다른 구성요소 목록)
- 예) **Greeter**: 책임 = 환영 메시지 표시, 사용자에게 선택지 제공, Recipe Database Manager나 Plan Manager로 제어 넘기기 / 협력자 = Database Manager, Plan Manager

## IIKH의 6개 구성요소 {#iikh-components}

| 구성요소 | 책임 |
|---|---|
| **Greeter** | 시작 시 환영 창. 레시피 DB 탐색, 새 레시피 추가, 레시피 편집·주석, 식사 계획 검토·생성 선택 |
| **Recipe Database** | 레시피 DB 유지, 탐색 허용, 기존 레시피 편집·주석, 새 레시피 추가 |
| **Recipe** | 재료 목록과 변환 알고리즘 유지, 자기 데이터 편집, 화면에 자기 표시, 자기 인쇄 |
| **Planner** (Plan Manager) | 계획할 날짜 범위 선택, 기존 계획 편집, Date 객체와 연관 |
| **Date** | 특정 끼니 편집, 날짜에 주석("Bob's Birthday"), 전체 끼니의 장보기 목록 출력 |
| **Meal** | 한 끼 정보, 레시피 DB와 상호작용해 레시피 선택, 인원수 설정 → 레시피 자동 조절, 끼니 장보기 목록 |

- 6개 구성요소만으로 다 됨 → 이 시점에 구성요소를 **다른 프로그래머들에게 나눠** 개발시킬 수 있다

> 시험 포인트: 2025 서술 "In project 1 (IIKH), main difference between Recipe class and RecipeDB class?" → Recipe = 레시피 **하나**의 데이터를 유지하고 자기를 편집·표시·인쇄, RecipeDB = 레시피 **모음**을 관리(탐색, 검색, 추가, 편집).

@lesson L3-3 | 구성요소의 특징: 행동·상태, 결합도·응집도, 인터페이스·구현 | L03 p.19–25

## 행동과 상태 · 인스턴스와 클래스 {#behavior-state}

- **Behavior**: 구성요소가 수행할 수 있는 행동들의 집합
- **State**: 구성요소 안에 있는 모든 정보(데이터 값). 행동이 상태를 바꾸는 게 일반적
- **Instances and Classes**: Recipe 인스턴스는 많지만 모두 같은 방식으로 행동 → 그 행동은 **Recipe 클래스에 공통**

## 결합도와 응집도 (Coupling and Cohesion) {#coupling-cohesion}

| | 정의 | 목표 |
|---|---|---|
| **Cohesion** (응집도) | 한 구성요소에 배정된 작업들이 **의미 있는 하나의 단위**를 이루는 정도 (책임들이 얼마나 강하게 관련되어 있나) | **최대화 (maximize)** |
| **Coupling** (결합도) | 어떤 책임을 수행하는 능력이 **다른 구성요소의 행동에 의존하는** 정도 (모듈 간 상호 의존도) | **최소화 (minimize)** |

- 좋은 설계 = **high cohesion, low (loose) coupling**
- 결합도가 높으면: 한 모듈의 변경이 다른 모듈에 영향 → 유지보수·재사용이 어려움

> 시험 포인트: 2024 "(Coupling) and (Cohesion) are two key concepts used to measure design quality… good design = (high) cohesion, (low) coupling", 2023 "Coupling is the degree to which each module (relies/depends) on … (Cohesion) … (minimize) … (maximize)", 2016 "(depends upon) … desirable to (minimize)". 영어 정의 문장을 그대로 외워.

## 인터페이스와 구현 · 정보 은닉 {#interface-impl}

- 구성요소를 **무엇을 할 수 있는지(what)** 로 특징지음
- 구성요소의 사용자는 **무엇을 하는지만 알면 되고 어떻게 하는지(how)는 몰라도 됨**
- **Two views of a software system**: 인터페이스(edit a recipe, create new recipe, display on terminal) vs 구현(text buffer, window pointer, ingredient list)
- **information hiding**: 구현 세부를 **의도적으로(purposeful) 숨기는 것**. 덮개(cover)가 있어서 내부를 볼 수 없고, 덕분에 **보호(protection)** 도 됨

## Public view와 Private view {#public-private}

- **Public view**: 다른 구성요소가 보고 쓸 수 있는 특징(데이터 또는 행동) → 인터페이스
- **Private view**: 구성요소 **안에서만** 쓰는 특징 → 구현
- public/private을 구분하는 것이 객체지향 프로그래밍의 핵심 특징 (교수님 강조)

@lesson L3-4 | 인터페이스 정형화 · 이름 · 구현 · 통합(stub) · 유지보수 | L03 p.26–33

## 인터페이스 정형화와 이름 짓기 {#naming}

**5. Formalize the Interface**: 구성요소 간 통신 채널을 정형화
- 각 구성요소의 일반 구조 식별. 행동이 **하나뿐인 구성요소는 함수**로, **여러 개면 클래스**로
- 책임마다 이름을 붙임 → 나중에 프로시저 이름이 됨. 함수 매개변수 식별, 정보를 구성요소에 배정, 시나리오를 다시 돌려 필요한 데이터가 다 있는지 확인

**이름 선택 지침**
- **evocative** (문제 맥락에서 의미를 떠올리게 하는) — 예: 의미 없는 이름보다 무엇을 세는지 드러나는 이름
- **short** (짧게)
- **pronounceable** (발음할 수 있게, 소리 내어 읽어 보기)
- **consistent** (프로젝트 안에서 일관되게, 예: 변수는 소문자로 시작·함수는 대문자로 시작 규칙을 정했으면 끝까지)
- **avoid digits** (이름에 숫자 피하기: count1, count2는 차이를 알 수 없음)

> 시험 포인트: 2016 서술 "What does 'evocative' mean?" → The name should call to mind (suggest) the meaning/role of the thing in the problem domain.

## 설계 · 구현 · 단위 테스트 {#implement}

- **6. Design**: 설명을 SW 배치로 바꿈, 각 구성요소의 자료구조 설계, 행동 설명을 알고리즘으로
- **7. Implementing Components**: 각 구성요소의 활동 구현. 팀원에게 구성요소를 나눠 맡김
  - **Unit testing**: 서브시스템을 **개별적으로 검증(validate)**. 올바르게 동작하기 위한 조건을 찾고, 합법적인 입력 값으로 테스트

## 통합과 stub {#stub}

**8. Integration of Components**: 구성요소들을 **천천히(slowly) 통합**해 완성 시스템으로, 아직 구현 안 된 부분은 **stub**으로
- **stub**: 행동이 없거나 아주 제한된 행동만 하는 **간단한 더미 루틴 (simple dummy routine)**. 아직 개발 안 된 구성요소의 임시 대체물
- **slowly integrated**: 한꺼번에(all at once) 통합하지 않고 **하나(또는 몇 개)씩 추가하며 테스트** → 문제가 생기면 방금 추가한 부분이 원인이라 찾고 고치기 쉬움. 한꺼번에 하면 어디서 생긴 문제인지 알 수 없음
- 통합 중 발견된 오류는 서브시스템 수준의 검증 기법을 다시 조사하게 만든다

> 시험 포인트: 2025·2016 서술 "Meaning of 'slowly integrated'? Meaning of 'stubs'?", 2022 빈칸 "(Stub) is a simple dummy routine with no behavior or with very limited behavior".

## 유지보수와 진화 · 흔한 설계 결함 {#maintenance}

**9. Maintenance and Evolution**
- **Software maintenance**: 초기 동작 버전을 **전달한 뒤에(subsequent to the delivery)** 하는 활동들
- SW는 첫 버전 후에도 고정되지 않는다: 버그 발견·수정, 요구사항 변경(정부 규제, 표준화), 하드웨어 변경, 사용자 기대 변화(경쟁 제품 때문에 기능 추가), 더 나은 문서 요구
- **좋은 설계는 변화가 불가피함을 인정하고 처음부터 대비한다**
- **Prepare for Change**: 가장 가능성 높은 변화 원인을 예측해 영향을 격리(인터페이스, 파일 형식, 통신 프로토콜), 바뀔 하드웨어 인터페이스 격리, **구성요소 간 의존 줄이기**, 주요 결정의 이유를 설계 문서에 기록

**흔한 설계 결함 (Common Design Flaws)**
- **Direct modification**: 다른 구성요소의 데이터를 직접 수정 → **캡슐화 위반**
- **Too much responsibility**: 이해하고 쓰기 어려움
- **No responsibility**: 쓸모없음
- **Unused responsibility**: 어떻게 쓰일지 생각하지 않고 설계한 결과
- **Misleading names**: 이름은 짧고 책임을 모호하지 않게 드러내야 함

> 시험 포인트: 2023 빈칸 "(Software maintenance) is the process of changing, modifying, and updating software to keep up with customer needs. (It) is done after the product has launched".
