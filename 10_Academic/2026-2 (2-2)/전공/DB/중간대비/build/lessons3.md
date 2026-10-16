@unit U3 | 관계 데이터 모델 · ER→관계 매핑 | 3-1_RDB.pdf
@intro 용어(릴레이션·투플·속성·도메인·차수), 키 계열(슈퍼키 ⊃ 키 = 후보 키 ∋ 기본 키), 무결성 제약 3가지, 삽입·삭제·갱신이 어떤 제약을 깨는지, 그리고 ER→관계 매핑. 매핑은 "FK를 어디에 넣나"만 정확하면 된다.

@lesson L3-1 | 관계 모델 기본 개념 | 3-1 p.4–12

## 관계 데이터 모델 {#rel-model}

- 1970년 IBM의 **Ted Codd**가 제안
- 데이터를 **릴레이션(relation, 테이블)** 으로 표현. 각 릴레이션은 **투플(tuple, 행)** 과 **속성(attribute, 열 헤더)** 으로 구성
- 각 행 = 특정 개체에 대한 사실(관련된 데이터 값들의 모음), 속성 = 각 행의 값을 어떻게 해석할지 지정

**장점 4가지**: **단순성** (평평한 테이블 구조), **데이터 무결성** (유효·일관·정확한 데이터 보장), **쉬운 데이터 조작** (SQL 같은 강력한 고급 언어로 복잡한 조건도 유연하게), **보안** (인증, 권한, 암호화)

## 도메인 · 릴레이션 스키마 · 인스턴스 {#domain-schema}

- **도메인 D**: 각 속성에 허용되는 **원자 값(atomic value)들의 집합**. 도메인 = 데이터 타입 + 제약조건
  - 예) Usa_phone_numbers: (ddd)ddd-dddd 형식, Employee_ages: 15~80 사이 정수
- **릴레이션 스키마 R(A₁, …, Aₙ)**: 릴레이션 이름 + 속성 리스트. 예) STUDENT(Name, Ssn, …, Gpa)
- **차수 (degree)**: 릴레이션 스키마의 **속성 개수 n**. 예) STUDENT(Name, Ssn, Home_phone, Address, Office_phone, Age, Gpa)는 차수 7
- **릴레이션 인스턴스(상태) r(R)**: n-투플들의 **집합** {t₁, …, tₘ}
- **투플 t**: n개 값의 **순서 있는** 리스트 <v₁, …, vₙ>. 각 vᵢ는 dom(Aᵢ)의 원소이거나 특수값 **NULL**

> 함정: 차수(degree) = 속성(열) 수. 투플(행) 수는 카디널리티(cardinality)라고 부른다. 섞지 마.

## 릴레이션의 특성 {#rel-chars}

- **투플의 값은 원자 값**이어야 함 (더 쪼개지지 않음)
  - **복합 속성·다중값 속성은 허용 안 됨**
  - 다중값 속성 → **별도 릴레이션**으로 표현
  - 복합 속성 → **단순 구성 속성들**로만 표현
- **NULL**: 값을 모르거나(unknown), 얻을 수 없거나(unavailable), 해당 투플에 적용되지 않는(undefined/not applicable) 경우
- 릴레이션은 투플의 **집합**이므로 정의상 **투플끼리는 모두 달라야** 한다

## 관계 DB 스키마와 상태 {#db-schema-state}

- **관계 DB 스키마 S** = 릴레이션 스키마들의 집합 {R₁, …, Rₘ} + **무결성 제약조건 집합 IC**
  - 예) COMPANY = {EMPLOYEE, DEPARTMENT, DEPT_LOCATIONS, PROJECT, WORKS_ON, DEPENDENT}
  - 스키마 그림에서 **밑줄 = 기본 키**, **화살표 = 참조 무결성** (FK → 참조되는 PK)
- **관계 DB 상태 DB** = 릴레이션 상태들의 집합 {r₁, …, rₘ}, rᵢ는 Rᵢ의 상태
  - 모든 무결성 제약을 만족하면 **유효(valid) 상태**, 하나라도 어기면 **무효(invalid) 상태**

@lesson L3-2 | 키 · 무결성 제약조건 | 3-1 p.13–21

## 슈퍼키와 키 {#superkey-key}

DBMS는 제약조건을 정의하고 강제하는 기능을 제공해야 한다. 핵심 제약 3가지 = **키 제약, 개체 무결성, 참조 무결성**.

**키 제약**: "서로 다른 두 투플은 SK 속성들에 대해 같은 값을 가질 수 없다" → 모든 상태 r에서 t₁[SK] ≠ t₂[SK].
- **슈퍼키 (SK)**: 각 투플을 **유일하게 식별하는 속성 부분집합**. 모든 릴레이션은 최소 하나의 기본 슈퍼키(속성 전체)를 가진다
- **키 (K)**: 슈퍼키이면서, 어떤 속성 A를 빼도 더 이상 슈퍼키가 아닌 것 = **최소(minimal) 슈퍼키**
  - 최소성은 키에는 필수, 슈퍼키에는 선택
  - 예) {Ssn, Home_phone}은 슈퍼키. Home_phone을 빼도 {Ssn}이 유일 → {Ssn, Home_phone}은 키가 아님, {Ssn}이 키

> 함정: 키 ⊂ 슈퍼키. "모든 키는 슈퍼키지만, 모든 슈퍼키가 키는 아니다".

## 후보 키와 기본 키 {#candidate-pk}

- 릴레이션 스키마에 키가 여러 개면, 각각을 **후보 키 (candidate key)** 라고 부른다
- 후보 키 중 하나를 **기본 키 (primary key)** 로 지정해 투플을 식별하는 데 쓴다. 스키마에서 **밑줄**
- 예) CAR의 후보 키 = License_number, Engine_serial_number → License_number를 PK로 지정
- 보통은 **속성 하나 또는 적은 수**로 된 키를 PK로 고르는 게 좋다

## 개체 무결성 제약 {#entity-integrity}

**"기본 키 값은 NULL일 수 없다"** → 모든 투플 t에 대해 t[PK] ≠ NULL.
- 이유: PK가 NULL인 투플이 둘 이상이면, 다른 릴레이션에서 참조할 때 **서로 구별할 수 없다**
- 예) Office_phone처럼 NULL이 있는 속성은 키가 될 수 없음
- 복합 PK면 **PK의 어느 부분도** NULL이면 안 됨

## 참조 무결성 제약 {#ref-integrity}

**"투플 t₁의 FK 값은 어떤 투플 t₂의 PK 값과 같거나, NULL이어야 한다"**
- **외래 키 (FK)**: 릴레이션 R₁의 속성 집합으로, R₂를 **참조**한다. t₁[FK] = t₂[PK]이면 t₁이 t₂를 참조
- R₁의 FK는 R₂의 PK와 **같은 도메인**을 가진다
- R₁ = **참조하는(referencing) 릴레이션**, R₂ = **참조되는(referenced) 릴레이션**
- 예) EMPLOYEE.Dno → DEPARTMENT.Dnumber. 'John Smith'의 Dno=5 → 'Research' 부서 투플을 참조 = Smith는 Research에서 일함
- 필요한 이유: 두 릴레이션 투플 사이의 **일관성** 유지. Dno=3인데 3번 부서가 없으면 그 값의 의미를 해석할 수 없다
- FK는 **자기 자신의 릴레이션을 참조**할 수도 있다 (EMPLOYEE.Super_ssn → EMPLOYEE.Ssn)

교안 연습 (FK 찾기):
- SALESPERSON(Ssn, Name, Start_year, Dept_no), TRIP(Ssn, From_city, To_city, Departure_date, Return_date, Trip_id), EXPENSE(Trip_id, Account#, Amount)
  → TRIP.Ssn → SALESPERSON, EXPENSE.Trip_id → TRIP
- STUDENT(Ssn, …), COURSE(Course#, …), ENROLL(Ssn, Course#, Quarter, Grade), BOOK_ADOPTION(Course#, Quarter, Book_isbn), TEXT(Book_isbn, …)
  → ENROLL.Ssn → STUDENT, ENROLL.Course# → COURSE, BOOK_ADOPTION.Course# → COURSE, BOOK_ADOPTION.Book_isbn → TEXT

@lesson L3-3 | 갱신 연산과 제약 위반 | 3-1 p.23–30

## 삽입 (Insert) {#op-insert}

연산 종류: **검색(retrieval)** 과 **갱신(update)**. 기본 갱신 연산 = Insert, Delete, Update(Modify). 적용할 때마다 제약이 깨질 수 있다.

**Insert**: 릴레이션에 투플 하나 추가. 릴레이션 이름 + 값 리스트(속성 순서대로).

**Insert는 세 가지 제약을 다 어길 수 있다.**

| 위반 | 원인 | 교안 예 (COMPANY 상태) |
|---|---|---|
| **키 제약** | 새 투플의 키 값이 이미 다른 투플에 있음 | <'Alicia', …, **'999887777'**, …, 4> → Ssn 999887777은 이미 Zelaya |
| **개체 무결성** | 새 투플의 PK(의 일부)가 NULL | <'Cecilia', …, **NULL**, …, 4> |
| **참조 무결성** | FK가 참조하는 투플이 없음 | <'Cecilia', …, '677678989', …, **7**> → Dnumber=7인 부서 없음 |

<'Cecilia', 'F', 'Kolonsky', '677678989', …, NULL, 4> 는 **모든 제약을 만족** (Super_ssn이 NULL인 건 FK니까 허용).

## 삭제 (Delete) {#op-delete}

**Delete**: 릴레이션 이름 + 지울 투플의 PK 값 지정.

**Delete는 참조 무결성만 어길 수 있다** (지운 투플을 다른 투플이 참조하고 있을 때).
- EMPLOYEE에서 Ssn='999887777' 삭제 → WORKS_ON 투플 2개가 참조 → **위반**
- EMPLOYEE에서 Ssn='333445555' 삭제 → WORKS_ON 4개 + EMPLOYEE 2개(Super_ssn)가 참조 → **위반** (실제로는 DEPARTMENT.Mgr_ssn, DEPENDENT.Essn도 참조함)
- WORKS_ON에서 Essn='999887777' AND Pno=10 삭제 → 아무도 참조 안 함 → 만족

## 수정 (Update) {#op-update}

**Update**: 바꿀 속성과 새 값 지정.

**Update는 키 제약과 참조 무결성을 어길 수 있다. PK나 FK 속성을 바꿀 때만 문제가 된다.**
- Ssn='999887777'인 사원의 Dno를 **7**로 → 7번 부서 없음 → **참조 무결성** 위반
- Ssn='999887777'을 **'987654321'** 로 → 이미 Wallace의 Ssn(키 제약) + WORKS_ON 등에서 999887777을 참조하던 투플이 고아가 됨(참조 무결성) → **둘 다** 위반
- PK를 NULL로 바꾸면 개체 무결성도 깨진다 (교안 요약엔 키·참조만 나옴)

> 시험 포인트: 요약표 그대로 — Insert = 키·개체·참조 **전부 가능**, Delete = **참조만**, Update = **키·참조** (PK/FK를 바꿀 때만).

@lesson L3-4 | ER→관계 매핑 ① 개체 · 다중값 · 약한 개체 | 3-1 p.32–36

## 정규 개체 타입 매핑 {#map-entity}

매핑 순서: 개체 타입(정규·약한) → 다중값 속성 → 관계 타입(1:1, 1:N, M:N, n진).

**정규(regular) 개체 타입 E**
1. E의 **단순 속성을 모두** 포함하는 릴레이션 R 생성. 복합 속성은 **단순 구성 속성만** 넣음 (Name → Fname, Minit, Lname)
2. E의 키 속성 중 하나를 R의 **PK**로 지정 (나머지 키는 UNIQUE 후보 키)
3. 다중값 속성은 여기서 넣지 않음 → 다음 단계

예) DEPARTMENT(Dname, **Dnumber**) — Locations는 아직 빠짐.

## 다중값 속성 매핑 {#map-multival}

**다중값 속성 A** (릴레이션에서는 허용 안 됨)
1. A마다 **별도 릴레이션 R** 생성
2. R에 A와, 원래 릴레이션의 PK K를 넣는다. K는 R에서 **FK** (원래 릴레이션 참조). 키 값이 반복됨
3. **(A, K) 조합을 PK**로

예) DEPT_LOCATIONS(**Dnumber**, **Dlocation**), Dnumber → DEPARTMENT. (5, Seoul), (5, Incheon), (5, Suwon), (3, Seoul), (3, Daejeon)

## 약한 개체 타입 매핑 {#map-weak}

**약한 개체 타입 W**
1. W의 단순 속성을 모두 포함하는 릴레이션 R 생성 (복합은 구성 속성만)
2. **소유 개체 타입의 PK를 FK로** 포함 → 이게 **식별 관계 타입을 매핑**한 것
3. **소유자 PK + 부분 키 조합을 PK**로

예) DEPENDENT(**Essn**, **Dependent_name**, Sex, Bdate, Relationship), Essn → EMPLOYEE.Ssn

> 함정: 식별 관계(DEPENDENTS_OF)는 별도 릴레이션을 만들지 않는다. 소유자 PK를 FK로 넣는 것 자체가 식별 관계의 매핑.

@lesson L3-5 | ER→관계 매핑 ② 관계 타입 | 3-1 p.37–49

## 1:1 관계 매핑 {#map-11}

방법 3가지: **외래 키 방식** (가장 많이 쓰고 유용), **합병 릴레이션 방식** (두 개체를 한 릴레이션으로), **교차 참조(관계 릴레이션) 방식**.

**외래 키 방식**
1. 참여 개체 타입 S, T 확인
2. 한쪽(S)을 골라 **상대(T)의 PK를 FK로** 넣는다. **전체 참여 쪽을 S로** 고르는 게 낫다
3. 관계의 단순 속성도 S에 넣는다

예) MANAGES: DEPARTMENT(전체 참여)를 S로 → DEPARTMENT(Dname, **Dnumber**, Mgr_ssn, Mgr_start_date), Mgr_ssn → EMPLOYEE.

**왜 전체 참여 쪽?** 반대로 EMPLOYEE(부분 참여)를 S로 하면 EMPLOYEE에 D_managed, Mgr_start_date가 들어가는데, 부서를 관리하지 않는 대부분의 사원은 이 값이 **NULL**이 된다. 전체 참여 쪽에 넣으면 NULL이 생기지 않는다.

## 1:N 관계 매핑 {#map-1n}

방법 2가지: **외래 키 방식** (릴레이션 수가 줄어서 선호), 교차 참조 방식.

**외래 키 방식**
1. **N쪽** 개체 타입을 나타내는 릴레이션 S 확인
2. S에 상대(1쪽) 릴레이션 T의 **PK를 FK로** 넣는다
3. 관계의 단순 속성도 S에 넣는다

이유: N쪽 개체 인스턴스 하나는 1쪽 개체 **최대 하나**와 연결 → FK 값 하나로 표현 가능.
- WORKS_FOR → EMPLOYEE에 **Dno** (→ DEPARTMENT)
- SUPERVISION → EMPLOYEE에 **Super_ssn** (→ EMPLOYEE, 자기 참조)
- CONTROLS → PROJECT에 **Dnum** (→ DEPARTMENT)

> 함정: 1쪽에 FK를 넣으면 다중값이 돼서 원자성을 어긴다. FK는 **항상 N쪽**.

## M:N 관계 매핑 {#map-mn}

방법 **하나뿐**: **교차 참조 (관계 릴레이션) 방식**. M:N은 FK 하나로 표현할 수 없다.
1. 관계 타입 R을 나타내는 **별도 릴레이션 S** 생성
2. 참여 개체 릴레이션들의 **PK를 FK로** S에 넣는다
3. **FK들의 조합을 PK**로
4. M:N 관계의 단순 속성도 S에 넣는다

예) WORKS_ON(**Essn**, **Pno**, Hours), Essn → EMPLOYEE, Pno → PROJECT. 관계 릴레이션 = lookup table.

## n진 관계 매핑 {#map-nary}

**교차 참조 방식** (M:N과 같은 절차)
1. 별도 릴레이션 S 생성
2. 참여하는 n개 개체 릴레이션의 PK를 FK로 넣음
3. FK 전부의 조합을 PK로 (보통. 어느 참여에 max가 1이면 그 FK는 PK에서 빠질 수 있다)
4. 관계의 단순 속성 포함

예) SUPPLY(**Sname**, **Proj_name**, **Part_no**, Quantity) — SUPPLIER, PROJECT, PART 참조.

## ER ↔ 관계 모델 대응 {#map-summary}

| ER 모델 | 관계 모델 |
|---|---|
| 개체 타입 | 개체 릴레이션 |
| 1:1 또는 1:N 관계 타입 | 외래 키 (또는 관계 릴레이션) |
| M:N 관계 타입 | 관계 릴레이션 + FK **2개** |
| n진 관계 타입 | 관계 릴레이션 + FK **n개** |
| 단순 속성 | 속성 |
| 복합 속성 | 단순 구성 속성들의 집합 |
| 다중값 속성 | 릴레이션 + 외래 키 |
| 값 집합 (value set) | 도메인 |
| 키 속성 | 기본 키 (또는 보조 키) |

교안 연습 3 (UNIVERSITY: COLLEGE, INSTRUCTOR, DEPT, STUDENT, COURSE, SECTION) 풀이 순서:
1. 정규 개체 → COLLEGE(CName, COffice, CPhone), INSTRUCTOR(Id, Rank, IName, IOffice, IPhone), DEPT(DName, DCode, DOffice, DPhone), COURSE(CCode, Credits, CoName, Level, CDesc), SECTION(SecId, SecNo, Sem, Year, Bldg, RoomNo, DaysTime), STUDENT(Sid, DOB, FName, MName, LName, Addr, Phone, Major)
2. 1:1 → DEAN: COLLEGE에 DeanId (COLLEGE가 (1,1) 전체 참여), CHAIR: DEPT에 ChairId, CStartDate
3. 1:N → INSTRUCTOR.Employed(EMPLOYS), DEPT.Admined(ADMINS), COURSE.Offered(OFFERS), SECTION.Taught(TEACHES), SECTION.Belongs(SECS), STUDENT.Dept(HAS)
4. M:N → TAKES(**Sid**, **SecId**, Grade)
