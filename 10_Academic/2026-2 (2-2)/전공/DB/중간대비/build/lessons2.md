@unit U2 | ER 모델 (개념적 설계) | 2_intro-ER.pdf p.11–47 + 2-2_ER_model-practices.pdf
@intro 요구사항 → 개체·속성 → 관계와 제약조건 → 다듬기. 시험에서 요구사항 문장을 주고 ER 다이어그램이나 (min, max)를 쓰게 할 가능성이 크니, "요구사항 문장 → 어떤 표기"로 바꾸는 연습을 해.

@lesson L2-1 | 설계 과정 · 개체와 속성 | 2_intro-ER p.12–21

## DB 설계 과정 {#design-process}

1. **요구사항 수집·분석 (Requirements Collection and Analysis)**: 예상 사용자의 데이터 요구를 파악. 결과물 = 사용자의 상세 요구사항
2. **개념적 설계 (Conceptual Design)**: 데이터 모델을 고르고, 요구사항을 **개념 스키마**로 번역 (ER 모델)
3. **구현 (Implementation)**: 개념 스키마로 DB를 구현
   - **논리적 설계**: DB 스키마 (예: 관계 스키마, 3주차 ER→관계 매핑)
   - **물리적 설계**: DB의 물리적 배치

COMPANY 요구사항: 회사는 **부서**(고유한 이름·번호, 여러 위치, 관리자와 관리 시작일)로 조직되고, 부서는 여러 **프로젝트**(고유한 이름·번호, 위치 하나)를 통제한다. **사원**은 이름·SSN·주소·급여·성별·생일·일하는 프로젝트가 있고, 보험 때문에 사원의 **부양가족**(이름, 성별, 생일, 관계)도 관리한다.

## 개체와 속성 {#entity-attr}

**ER (Entity-Relationship) 모델**: 데이터를 **개체(entity)와 관계(relationship)의 모음**으로 기술. ER 다이어그램으로 그린다.
- **개체 (entity)**: 현실 세계에서 **독립적으로 존재**하고 다른 것과 구별되는 "것". 물리적 존재(사원)일 수도, 개념적 존재(회사)일 수도 있다
- **속성 (attribute)**: 개체를 기술하는 특정 성질. 예) 사원: 이름, 주소, 나이, 집 전화
- **관계 (relationship)**: 여러 개체 사이의 연관

## 속성의 분류 {#attr-types}

| 분류 | 짝 | 예 |
|---|---|---|
| ① 복합 vs 단순 | **복합 (composite)**: 더 작은 부분으로 나뉨 / **단순(원자, simple/atomic)**: 안 나뉨 | Address = (Street_address, City, State, Zip) / City, Zip |
| ② 단일값 vs 다중값 | **단일값 (single-valued)**: 개체마다 값 하나 / **다중값 (multivalued)**: 값의 집합 | Age, SSN / Phone numbers, College degrees, 부서의 Locations |
| ③ 저장 vs 유도 | **저장 (stored)**: DB에 실제 저장 / **유도 (derived)**: 다른 속성에서 계산 | Birth_date / Age (생일에서 유도) |

> 함정: "다중값"과 "복합"을 섞지 마. 복합 = 한 값이 여러 부분으로 쪼개짐, 다중값 = 값이 여러 개. 둘 다일 수도 있다 (예: {Address_phone(Phone, Address)}).

## 키 속성 {#key-attr}

**키 속성 (key attribute)**: 개체마다 값이 **서로 다른** 속성 → 각 개체를 유일하게 식별.
- 예) STUDENT의 학번, PERSON의 SSN
- 여러 속성이 모여서 하나의 키가 될 수 있다 (예: CAR의 Registration = (Number, State) 복합 키)
- 한 개체 타입이 키를 **둘 이상** 가질 수 있다 (예: CAR의 키 = Registration, Vehicle_id)
- 다이어그램에서 **밑줄**로 표시

## ER 다이어그램 표기법 {#er-notation}

| 기호 | 의미 |
|---|---|
| 직사각형 | 개체 타입 |
| **이중** 직사각형 | 약한 개체 타입 |
| 마름모 | 관계 타입 |
| **이중** 마름모 | 식별 관계 타입 |
| 타원 | 속성 |
| 밑줄 친 타원 | 키 속성 |
| **이중** 타원 | 다중값 속성 |
| 타원에 타원이 달림 | 복합 속성 |
| **점선** 타원 | 유도 속성 |
| E₁ — R **═** E₂ (이중선) | E₂가 R에 **전체 참여** |
| E₁ ─1─ R ─N─ E₂ | 카디널리티 비 1:N |
| R ─(min,max)─ E | E가 R에 참여하는 구조적 제약 |

## 초기 개념 설계: COMPANY {#initial-design}

- **DEPARTMENT**: Name, Number, {Locations}, Manager, Manager_start_date. Name과 Number가 각각 키 (둘 다 고유). Locations는 다중값
- **PROJECT**: Name, Number, Location, Controlling_department. Name, Number가 키
- **EMPLOYEE**: Name(Fname, Minit, Lname 복합), SSN(키), Address, Salary, Birth_date, Sex, Department, Supervisor, {Works_on(Project, Hours)}
- **DEPENDENT**: Employee, Dependent_name, Sex, Birth_date, Relationship

문제: Manager, Department, Supervisor, Works_on, Employee 같은 속성은 사실 **다른 개체를 참조**한다. 관계가 속성 형태로 **암묵적으로** 들어가 있음 → 이걸 명시적인 **관계 타입**으로 바꿔야 한다 (L2-4 다듬기).

@lesson L2-2 | 관계 타입 · 차수 · 역할 · 제약조건 | 2_intro-ER p.23–30, 36–37

## 관계 타입, 차수, 역할 이름 {#rel-type}

**관계 타입**: 이름 + 참여하는 개체 타입들로 기술. 참여 개체들 사이의 연관 집합을 정의한다.
- 예) WORKS_FOR: EMPLOYEE와 DEPARTMENT 사이. 각 사원을 그가 일하는 부서와 연관시킴
- **차수 (degree)**: 참여하는 개체 타입의 수. 2진(binary), 3진(ternary)… 대부분은 2진
  - 2진 예: rᵢ = (eⱼ, dₖ), 3진 예: SUPPLY의 rᵢ = (sⱼ, pₖ, jₗ) (SUPPLIER, PART, PROJECT)
- **역할 이름 (role name)**: 참여 개체가 관계 인스턴스에서 맡는 역할. 관계의 의미를 이해하게 해줌. 예) WORKS_FOR에서 EMPLOYEE = worker, DEPARTMENT = employer

## 순환 관계 (Recursive Relationship) {#recursive}

**같은 개체 타입이 한 관계 타입에 두 번 이상 참여**하는 관계. 참여 개체를 구별하려면 **역할 이름이 필수**.
- 예) SUPERVISION: EMPLOYEE가 supervisor 역할(선 '1')과 supervisee 역할(선 '2')로 참여
- r₂ = (e₁, e₂): Kim이 Lee의 상사 / r₁ = (e₅, e₁): Kim은 Kang의 부하

## 제약조건 ① 카디널리티 비 {#cardinality}

**한 개체가 참여할 수 있는 관계 인스턴스의 최대 개수**. 2진 관계에서 1:1, 1:N, M:N.

| 비 | 예 | 현실 제약 |
|---|---|---|
| **1:N** | WORKS_FOR (DEPARTMENT 1 : EMPLOYEE N) | 사원은 한 부서에서만 일하고, 부서는 사원을 몇 명이든 둘 수 있다 |
| **1:1** | MANAGES (EMPLOYEE 1 : DEPARTMENT 1) | 사원은 최대 한 부서를 관리, 부서는 관리자가 최대 한 명 |
| **M:N** | WORKS_ON (EMPLOYEE M : PROJECT N) | 사원은 프로젝트 여러 개, 프로젝트도 사원 여러 명 |

> 함정: 1:N에서 **N쪽** 개체 하나는 1쪽 개체 **최대 하나**와 연결된다. "사원 하나 → 부서 최대 하나"니까 사원이 N쪽.

## 제약조건 ② 참여 제약 {#participation}

**개체의 존재가 다른 개체와의 관계에 의존하는지** 지정. 최소 참여 수와 관련.
- **전체 참여 (total)**: **모든** 개체가 관계에 참여해야 함. 이중선. 예) 모든 사원은 어떤 부서에서 일해야 하므로 EMPLOYEE는 WORKS_FOR에 전체 참여 (= existence dependency)
- **부분 참여 (partial)**: 모든 개체가 참여할 필요는 없음. 단일선. 예) 모든 사원이 부서를 관리하진 않으므로 EMPLOYEE는 MANAGES에 부분 참여

## (min, max) 표기 {#minmax}

각 참여에 **(min, max)** 를 붙여서 카디널리티와 참여를 함께 표시. 0 ≤ min ≤ max, max ≥ 1.
- **min = 0 → 부분 참여, min ≥ 1 → 전체 참여**
- max = 그 개체가 참여할 수 있는 관계 인스턴스 수의 최대
- 예) MANAGES: EMPLOYEE (0,1), DEPARTMENT (1,1)

> 함정: (min,max)는 **그 개체 쪽에 붙고, 그 개체 하나가** 관계에 몇 번 참여하는지를 뜻한다. 1:N 표기의 "1", "N"은 **반대편**에 붙는다 (DEPARTMENT ─1─ WORKS_FOR ─N─ EMPLOYEE). 그래서 WORKS_FOR는 (min,max)로 EMPLOYEE (1,1), DEPARTMENT (4,N)처럼 위치가 뒤집혀 보인다.

교안 연습 1 (INSTRUCTOR–TEACHES–COURSE–USES–TEXT):
- 강의는 교재를 쓸 수도 안 쓸 수도, 다섯 권 초과는 안 됨 → COURSE의 USES 참여 **(0, 5)**
- 강의는 최소 1명, 최대 4명이 가르침 → COURSE의 TEACHES 참여 **(1, 4)**
- 교재는 어떤 강의들에서 쓰임 → TEXT의 USES 참여 **(1, N)**
- 강사는 2~4개 강의를 가르침 → INSTRUCTOR의 TEACHES 참여 **(2, 4)**

@lesson L2-3 | 관계 속성 · 약한 개체 | 2_intro-ER p.31–35

## 관계 타입의 속성 {#rel-attr}

관계 타입도 속성을 가질 수 있다. 예) MANAGES의 StartDate, WORKS_ON의 Hours, WORKS_FOR의 StartDate.

| 관계 | 속성을 옮길(migrate) 수 있는 곳 |
|---|---|
| **1:1** | **어느 쪽** 참여 개체로든 옮길 수 있음 (MANAGES.StartDate → DEPARTMENT 또는 EMPLOYEE) |
| **1:N** | **N쪽 개체로만** 옮길 수 있음 (WORKS_FOR.StartDate → EMPLOYEE) |
| **M:N** | **어느 개체로도 못 옮김**. 개체 조합에 의해서만 결정되기 때문 (WORKS_ON.Hours는 사원–프로젝트 조합으로 결정) |

> 시험 포인트: "1:N 관계의 속성은 왜 N쪽으로만?" → N쪽 개체 하나는 관계 인스턴스에 최대 1번 참여하니까 값이 하나로 정해진다. 1쪽 개체는 여러 인스턴스에 참여하므로 값이 여러 개가 됨.

## 약한 개체 타입 {#weak-entity}

**약한 개체 타입 (weak entity type)**: 자기 자신의 **키 속성이 없는** 개체 타입. **식별(소유) 개체 타입**에 의존한다.
- 약한 개체는 반드시 식별 개체와 연관되어야 함
- **식별 관계 (identifying relationship)**: 약한 개체 타입과 소유자(owner) 개체 타입을 잇는 관계. 이중 마름모
- 약한 개체 타입은 식별 관계에 **항상 전체 참여**
- **부분 키 (partial key)**: 같은 소유자에 딸린 약한 개체들끼리 구별하는 속성. 점선 밑줄
  - 예) DEPENDENT의 Dependent_name (같은 사원의 부양가족끼리는 이름이 안 겹친다고 가정)
  - 부분 키만으로는 식별 못 함 (다른 사원의 부양가족 Tom이 또 있을 수 있음) → **소유자 키 + 부분 키**로 식별

@lesson L2-4 | COMPANY 설계 다듬기 · 실습 (MOVIE, CONF_REVIEW) | 2_intro-ER p.38–47, 2-2 p.14–26

## COMPANY 설계 다듬기 {#refine}

관계를 표현하던 속성을 **관계 타입으로** 바꾼다.

| 관계 | 참여 | 카디널리티 | 참여 제약 | 속성 |
|---|---|---|---|---|
| **MANAGES** | EMPLOYEE, DEPARTMENT | 1:1 | EMPLOYEE 부분, DEPARTMENT 전체 | Start_date (Manager_start_date) |
| **WORKS_FOR** | EMPLOYEE, DEPARTMENT | 1:N (DEPARTMENT 1, EMPLOYEE N) | 둘 다 전체 | 없음 |
| **CONTROLS** | DEPARTMENT, PROJECT | 1:N (DEPARTMENT 1, PROJECT N) | PROJECT 전체, DEPARTMENT 부분 | 없음 |
| **SUPERVISION** | EMPLOYEE (supervisor, supervisee) | 1:N (supervisor 1, supervisee N) | 둘 다 부분 | 없음 |
| **WORKS_ON** | EMPLOYEE, PROJECT | M:N | 둘 다 전체 | Hours |
| **DEPENDENTS_OF** | EMPLOYEE(식별), DEPENDENT(약한) | 1:N (EMPLOYEE 1) | EMPLOYEE 부분, DEPENDENT 전체 | 없음 (식별 관계) |

옮겨진 것: DEPARTMENT의 Manager·Manager_start_date → MANAGES, PROJECT의 Controlling_department → CONTROLS, EMPLOYEE의 Department·Supervisor·Works_on → WORKS_FOR·SUPERVISION·WORKS_ON, DEPENDENT의 Employee → DEPENDENTS_OF.

> 주의: 교안 p.42 SUPERVISION 설명은 1쪽/N쪽 역할이 뒤바뀌어 적혀 있어. 상사(supervisor) 한 명이 여러 부하(supervisee)를 두므로 **supervisor가 1쪽**이 맞고, 결과 다이어그램(p.45)의 (min,max)도 supervisor (0,N), supervisee (0,1)이야.

**ER 스키마 설계 3단계 요약**: (1) 요구사항에서 개체 타입과 속성 기술 → (2) 관계 타입과 제약조건 지정 → (3) 관계를 표현하던 속성을 관계 타입으로 바꿈. 인스턴스가 아니라 **스키마**에 집중.

## 실습: MOVIE / CONF_REVIEW {#er-practice}

**MOVIE DB** (2-2 p.14–23)
- MOVIE: 키 MKey(Title, Year) 복합, Length, Plot_outline, {Genre} 다중값
- ACTOR, DIRECTOR: 키 (Name, Date_of_birth). PRODUCTION: 키 Name, Address
- **PRODUCES** (PRODUCTION 1 : MOVIE N): 영화는 제작사 하나가 만든다. MOVIE 전체 참여
- **ACTS** (ACTOR M : MOVIE N): 관계 속성 Role, {Quotes}(다중값). 양쪽 전체 참여
- **DIRECTS** (DIRECTOR M : MOVIE N): MOVIE 전체 참여 (감독이 최소 1명)
- **DIR_ACTS**: 감독도 영화에 출연할 수 있음 (Role, {Quotes})

**CONF_REVIEW DB** (2-2 p.24–26, 풀이는 db-exercises)
- AUTHOR(A_email 키, First_name, Last_name), PAPER(P_id 키, Title, Abstract, File_name), REVIEWER(R_email 키, 이름, Phone_no, Affiliation, {Interest_topic})
- **SUBMITS** AUTHOR (1,N) – PAPER (1,M): 저자는 논문을 내야 기록되고, 논문은 여러 저자 가능 (M:N)
- **IS_CONTACT** AUTHOR (0,N) – PAPER (1,1): 논문마다 연락 저자가 정확히 한 명. SUBMITS만으로는 이 요구를 못 나타내서 따로 둠
- **REVIEWS** REVIEWER (1,N) – PAPER (2,4): 논문당 리뷰어 2~4명. 관계 속성 Recommendation, Comments(For_committee, Feedback) 복합, Rating(C1 Technical_merit, C2 Readability, C3 Originality, C4 Relevance) 복합

> 시험 포인트: "~마다 정확히 하나" = (1,1), "할 수도 안 할 수도" = min 0, "최소 a 최대 b" = (a,b), "여러 개" = max N. 요구사항 문장에서 이 단어들을 찾아 표기로 옮기는 게 핵심.
