@unit U6 | 관계 대수 (Relational Algebra) | 6-1_relational-algebra.pdf + db-exercises Week 7
@intro σ π ρ, 집합 연산, ×, ⋈(세타·동등·자연), ÷, ℑ(집계), 외부 조인. 질의를 "중간 릴레이션 이름 ← 연산" 순서로 쪼개 쓰는 연습이 핵심. 답안에 기호 대신 SELECT, PROJECT, JOIN 같은 단어를 써도 채점돼.

@lesson L6-1 | 관계 대수 소개 · 질의 트리 | 6-1 p.3–6

## 관계 대수란 {#ra-intro}

- **관계 대수 (relational algebra)**: "데이터를 **어떻게** 가져오나"에 대한 이론적·수학적 모델 → **절차적 (procedural)**
- **SQL**은 고급 **선언적 (declarative)** 언어 → "**무슨** 데이터가 필요한가"만 말하고 어떻게 가져올지는 신경 안 씀
- 형식적 관계 모델의 **기본 연산 집합**. 집합에 대한 수학 개념에 엄격하게 기반

왜 중요한가:
- 관계 모델 연산(선택, 투영, 이름 바꾸기, 조인, 카티션 곱…)의 **형식적 기초**
- **질의 처리와 최적화의 기반**: 결과를 얻기 위한 연산의 **순서(sequence)** 를 명시

> 시험 포인트: "SQL = what (선언적), 관계 대수 = how (절차적)". 그리고 관계 대수는 **닫힌 체계**: 모든 연산의 결과가 다시 릴레이션.

## 질의 (실행) 트리 {#query-tree}

**질의 트리 (query tree)**: DBMS 내부에서 질의를 표현하는 트리 = 관계 대수 식.
- **잎 노드 = 입력 릴레이션**, **내부 노드 = 관계 대수 연산**
- **잎에서 시작해 루트에서 끝난다** (아래에서 위로 실행)
- 연산 순서를 명시적으로 보여줘서 질의를 이해하기 좋음

교안 예: 'Stafford'에 있는 프로젝트마다 프로젝트 번호, 통제 부서 번호, 부서 관리자의 성·주소·생일
```
SELECT P.Pnumber, P.Dnum, E.Lname, E.Address, E.Bdate
FROM   PROJECT P, DEPARTMENT D, EMPLOYEE E
WHERE  P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND P.Plocation = 'Stafford';
```
트리: (1) σ Plocation='Stafford' (P) → (2) ⋈ P.Dnum=D.Dnumber D → (3) ⋈ D.Mgr_ssn=E.Ssn E → 루트 π Pnumber, Dnum, Lname, Address, Bdate

**질의 처리**: 가능한 실행 전략(질의 트리) 중 적절한 걸 고르는 과정. **SQL 하나에 질의 트리(계획)가 여러 개** 있을 수 있다 → 어느 게 최선인지는 질의 최적화 (13주차).

@lesson L6-2 | 단항 연산: SELECT · PROJECT · RENAME | 6-1 p.8–15

## SELECT (σ) {#ra-select}

**σ<선택 조건>(R)**: 릴레이션에서 **선택 조건을 만족하는 투플의 부분집합**을 고름 → **수평 필터링**.
- 조건은 투플 **각각에** 개별 적용
- 결과는 R과 **같은 속성** → **결과 차수 = R의 차수**
- 조건 = `<속성> <비교연산> <상수>` 또는 `<속성> <비교연산> <속성>` 절들을 **AND, OR**로 연결
  - 비교 연산 {=, <, ≤, >, ≥, ≠}. 순서 있는 값(숫자, 날짜)은 전부, 순서 없는 값(색깔 등)은 {=, ≠}만
- 예) σ Dno=4 (EMPLOYEE) → Zelaya, Wallace, Jabbar
- 예) σ (Dno=4 AND Salary>25000) OR (Dno=5 AND Salary>30000) (EMPLOYEE) → Wong, Wallace, Narayan

**성질**
- **교환 법칙**: σ c1(σ c2(R)) = σ c2(σ c1(R))
- 여러 σ는 AND로 **하나로 합칠 수 있음**: σ c1(σ c2(…σ cn(R))) = σ c1 AND c2 AND … AND cn(R)

> 함정: 관계 대수의 SELECT(σ)는 SQL의 **SELECT 절이 아니라 WHERE 절**에 대응. `σ Dno=4 AND Salary>25000 (EMPLOYEE)` = `SELECT * FROM EMPLOYEE WHERE Dno=4 AND Salary>25000;`

## PROJECT (π) {#ra-project}

**π<속성 리스트>(R)**: 원하는 **열만** 남기고 나머지 열은 버림 → **수직 필터링**.
- 결과 차수 = 속성 리스트의 속성 수
- **중복 제거**: 속성 리스트에 키가 없으면(비키 속성만) 중복 투플이 생길 수 있는데, **π는 중복을 제거** → 결과는 서로 다른 투플의 **집합**
  - 예) π Sex, Salary (EMPLOYEE) → 8행이 아니라 **7행** ((F, 25000)이 두 번 → 한 번)
- SQL 대응: π 속성 리스트 = **SELECT 절**. 그런데 SQL은 중복을 안 지우므로 정확한 대응은 `SELECT DISTINCT Sex, Salary FROM EMPLOYEE;`

## RENAME (ρ) {#ra-rename}

**ρ**: 릴레이션 이름이나 속성 이름, 또는 둘 다 바꿈.
- ρ S(B₁, …, Bₙ)(R): 둘 다 / ρ S(R): 릴레이션 이름만 / ρ (B₁, …, Bₙ)(R): 속성 이름만
- 대입 형태로도 씀: `R(First_name, Last_name, Salary) ← π Fname, Lname, Salary (TEMP)`
- SQL에서는 **AS (별칭)** 로 이름 바꾸기를 한다

## 연산의 순서 (중간 릴레이션) {#ra-sequence}

여러 연산을 쓸 때 두 방법:
- **방법 1**: 중간 릴레이션에 이름을 붙여 순서를 명시
```
DEP5_EMPS ← σ Dno=5 (EMPLOYEE)
RESULT    ← π Fname, Lname, Salary (DEP5_EMPS)
```
- **방법 2**: 연산을 **중첩**해서 하나의 식으로
```
π Fname, Lname, Salary ( σ Dno=5 (EMPLOYEE) )
```
→ Smith 30000, Wong 40000, Narayan 38000, English 25000

복잡한 질의는 하나의 식보다 **중간 결과 릴레이션으로 쪼개는 게 보통 더 쉽다**.

@lesson L6-3 | 집합 연산 · 카티션 곱 | 6-1 p.17–22

## 합 · 교 · 차 {#ra-setops}

**합집합 R ∪ S**, **교집합 R ∩ S**, **차집합 R − S** (MINUS, EXCEPT). 결과에서 **중복 제거**.
- **타입 호환 (type compatible, union compatible)** 인 릴레이션에만 적용: R(A₁…Aₙ)과 S(B₁…Bₙ)의 **속성 수가 같고**, 모든 i에 대해 **dom(Aᵢ) = dom(Bᵢ)**
- 교안 예: 5번 부서에서 일하거나, 5번 부서 사원을 직접 감독하는 사원의 SSN
```
DEP5_EMPS ← σ Dno=5 (EMPLOYEE)
RESULT1   ← π Ssn (DEP5_EMPS)
RESULT2(Ssn) ← π Super_ssn (DEP5_EMPS)
RESULT    ← RESULT1 ∪ RESULT2
```
→ RESULT1 = {123456789, 333445555, 666884444, 453453453}, RESULT2 = {333445555, 888665555}, RESULT = 5개 (333445555는 한 번만)

**성질**
- ∪와 ∩는 **교환** (R ∪ S = S ∪ R) **결합** (R ∪ (S ∪ T) = (R ∪ S) ∪ T)
- **−는 교환 법칙이 성립하지 않는다**: R − S ≠ S − R (STUDENT − INSTRUCTOR와 INSTRUCTOR − STUDENT는 다름)
- 결과 속성 이름은 관례상 **첫 번째 릴레이션**의 이름을 따름

## 카티션 곱 (×) {#ra-cartesian}

**R(A₁…Aₙ) × S(B₁…Bₘ) → Q(A₁…Aₙ, B₁…Bₘ)**: 두 릴레이션 투플의 **모든 가능한 조합**을 이어 붙임. CROSS PRODUCT, CROSS JOIN.
- **타입 호환 아니어도** 적용 가능한 이항 집합 연산
- 결과 속성 수 = **n + m**, 투플 수 = **|R| × |S|**
- 그 자체로는 대개 의미 없음 → **뒤에 SELECT가 와서** 관련 있는 투플만 고를 때 유용

교안 예: 여성 사원의 부양가족 이름
```
FEMALE_EMPS       ← σ Sex='F' (EMPLOYEE)
EMPNAMES          ← π Fname, Lname, Ssn (FEMALE_EMPS)
EMP_DEPENDENTS    ← EMPNAMES × DEPENDENT              -- 3 × 7 = 21행 (의미 없음)
ACTUAL_DEPENDENTS ← σ Ssn=Essn (EMP_DEPENDENTS)
RESULT            ← π Fname, Lname, Dependent_name (ACTUAL_DEPENDENTS)
```
→ Jennifer Wallace – Abner 한 행. **× 다음 σ = JOIN** (다음 레슨).

@lesson L6-4 | JOIN · DIVISION · 완전 집합 | 6-1 p.24–34

## JOIN (⋈) {#ra-join}

**R ⋈<조인 조건> S**: 두 릴레이션의 **관련 있는 투플을 하나의 긴 투플로** 결합. 결과 Q(A₁…Aₙ, B₁…Bₘ)에는 **조인 조건을 만족하는 조합만**.
- 예) 각 부서 관리자의 이름
```
DEPT_MGR ← DEPARTMENT ⋈ Mgr_ssn=Ssn EMPLOYEE
RESULT   ← π Dname, Lname, Fname (DEPT_MGR)
```
→ Research–Wong, Administration–Wallace, Headquarters–Borg
- **JOIN = 카티션 곱 + SELECT**: `EMP_DEPENDENTS ← EMPNAMES × DEPENDENT; ACTUAL ← σ Ssn=Essn (EMP_DEPENDENTS)` 두 줄을 `ACTUAL ← EMPNAMES ⋈ Ssn=Essn DEPENDENT` 한 줄로

## 세타 · 동등 · 자연 조인 {#join-variants}

- **세타 조인 (THETA JOIN)**: 일반 조인 조건. `<조건> AND <조건> AND …`, 각 조건은 **Aᵢ θ Bⱼ** (θ ∈ {=, <, ≤, >, ≥, ≠}). 조건을 모두 만족하는 투플만
- **동등 조인 (EQUIJOIN)**: 비교 연산자가 **= 만** 쓰인 조인. 결과에 값이 똑같은 속성 쌍이 생김 (예: Mgr_ssn과 Ssn) → 하나는 불필요
- **자연 조인 (NATURAL JOIN, * 로 표기)**: 동등 조인에서 **중복 속성 하나를 없앤 것**
  - 조인 속성은 두 릴레이션에서 **이름이 같아야** 함. 다르면 **먼저 이름을 바꿈**
  - `DEPT_LOCS ← DEPARTMENT * DEPT_LOCATIONS` (Dnumber가 같은 이름) → Dnumber 한 번만
  - `DEPT ← ρ (Dname, Dnum, Mgr_ssn, Mgr_start_date) (DEPARTMENT); PROJ_DEPT ← PROJECT * DEPT` (Dnum으로 맞춤)

> 함정: 자연 조인은 이름이 같은 속성 **전부**를 조인 조건으로 쓴다. 의도치 않게 이름이 같은 속성(예: 둘 다 Name)이 있으면 엉뚱한 조건이 붙는다.

## 조인 결과의 크기 {#join-size}

- **0 ≤ |R ⋈ S| ≤ |R| × |S|**
- 최소: 조인 조건을 만족하는 조합이 하나도 없으면 → **빈 릴레이션**
- 최대: 모든 조합이 조건을 만족하거나 조건이 없으면 → **카티션 곱**과 같음
- **조인 선택도 (join selectivity)** = 예상 조인 결과 크기 / (|R| × |S|). 질의 최적화에서 질의 계획의 비용 추정에 씀

## DIVISION (÷) {#ra-division}

"**모든** ~를 하는" 질의를 위한 연산. 기본 연산으로 표현할 수 있지만 따로 둠.
- 형식: **R(Z) ÷ S(X) = T(Y)**, X ⊆ Z (S의 속성은 R 속성의 부분집합), **Y = Z − X**
- T에는 R에서 **S의 모든 값과 짝지어 나타나는** Y 값만 들어감 (분모 S가 분자 R을 제한)
- 예) R(A, B) = {(a1,b1), (a2,b1), (a3,b1), (a4,b1), (a1,b2), (a3,b2), (a2,b3), (a3,b3), (a4,b3), (a1,b4), (a2,b4), (a3,b4)}, S(A) = {a1, a2, a3} → T(B) = {b1, b4}

교안 예: 'John Smith'가 일하는 **모든** 프로젝트에서 일하는 사원의 이름
```
SMITH      ← σ Fname='John' AND Lname='Smith' (EMPLOYEE)
SMITH_PNOS ← π Pno (WORKS_ON ⋈ Essn=Ssn SMITH)            -- {1, 2}
SSN_PNOS   ← π Essn, Pno (WORKS_ON)
SSNS(Ssn)  ← SSN_PNOS ÷ SMITH_PNOS                         -- {123456789, 453453453}
RESULT     ← π Fname, Lname (SSNS * EMPLOYEE)
```
→ John Smith, Joyce English

> 시험 포인트: 분자 R의 속성 순서·이름을 맞춰야 한다. SSN_PNOS(Essn, Pno) ÷ SMITH_PNOS(Pno) → 남는 속성 Essn. 결과를 EMPLOYEE와 자연 조인하려고 SSNS(Ssn)으로 이름을 바꿨다.

## 관계 대수 연산의 완전 집합 {#ra-complete}

**{σ, π, ∪, ρ, −, ×}** 6개가 완전 집합. 다른 모든 (원래의) 관계 대수 연산은 이 6개의 조합으로 표현 가능.
- **교집합**: R ∩ S ≡ (R ∪ S) − ((R − S) ∪ (S − R))
- **조인**: R ⋈<조건> S ≡ σ<조건>(R × S)
- **자연 조인**: 카티션 곱 앞에 RENAME, 뒤에 SELECT와 PROJECT
- 엄밀히는 ∩와 ⋈가 필요 없지만 **자주 쓰여서** 별도 연산으로 둔다

@lesson L6-5 | 추가 연산: 집계 · 그룹 · 외부 조인 | 6-1 p.36–43

## 집계 함수와 그룹화 (ℑ) {#ra-aggregate}

기본 연산만으로는 **집계(SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT)**, **그룹별 집계**, **외부 조인**을 표현 못 함 → 추가 연산으로 **표현력 확장**.

**<그룹화 속성> ℑ <함수 리스트> (R)** (ℑ = script F)
- 그룹화 속성: R의 속성 중 그룹을 나눌 기준 (없어도 됨)
- 함수 리스트: (<함수> <속성>) 쌍들. 함수 = SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT
- **결과**: 그룹화 속성 + 함수 리스트 원소마다 속성 하나

예
```
ρ R(Dno, No_of_employees, Average_sal) ( Dno ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE) )
```
→ (5, 4, 33250), (4, 3, 31000), (1, 1, 55000)
- **이름을 안 바꾸면**: 속성 이름 = `<함수>_<속성>` → Dno, Count_ssn, Average_salary
- **그룹화 속성이 없으면**: 함수를 **모든 투플에** 적용 → 결과는 **투플 하나** `ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE)` → (8, 35125)

## 집계의 성질 {#ra-agg-props}

- 집계 함수를 적용할 때 **중복은 제거하지 않는다** (급여 합·평균을 제대로 구해야 하니까)
- **NULL은 집계에서 고려하지 않는다**
- 관계 대수는 **닫힌 수학 체계**: 집계 결과도 스칼라 숫자가 아니라 **릴레이션** (값 하나, 투플 하나여도)

## 외부 조인 {#ra-outer}

EQUIJOIN·NATURAL JOIN(내부 조인)은 **조건을 만족하는 투플만** 결과에 넣고, 짝이 없는 투플은 버린다. 짝이 없어도 **한쪽(또는 양쪽) 릴레이션의 모든 투플을 남기고 싶을 때** 외부 조인을 쓴다.
- 예) 모든 사원 이름과, 그 사원이 부서를 관리하면 그 부서 이름 (관리 안 하면 NULL)
```
TEMP   ← EMPLOYEE ⟕ Ssn=Mgr_ssn DEPARTMENT
RESULT ← π Fname, Minit, Lname, Dname (TEMP)
```
→ 8행. Wong–Research, Wallace–Administration, Borg–Headquarters, 나머지 5명은 Dname = NULL
- 종류: **LEFT OUTER JOIN ⟕** (왼쪽 모든 투플), **RIGHT OUTER JOIN ⟖** (오른쪽 모든 투플), **FULL OUTER JOIN ⟗** (양쪽 모두). 짝 없는 쪽 속성은 **NULL로 채움**

@lesson L6-6 | 관계 대수 작성 연습 | db-exercises Week 7 (p.55–59)

## 연습 1–2: 조인 경로 {#ra-practice-join}

**연습 1**: 'Research' 부서에서 일하는 모든 사원의 이름과 주소
```
RESEARCH_DEPT ← σ Dname='Research' (DEPARTMENT)
RESEARCH_EMPS ← RESEARCH_DEPT ⋈ Dnumber=Dno EMPLOYEE
RESULT        ← π Fname, Lname, Address (RESEARCH_EMPS)
```
**연습 2**: 'Stafford'에 있는 프로젝트마다 프로젝트 번호, 통제 부서 번호, 관리자의 성·주소·생일
```
STAFFORD_PROJS ← σ Plocation='Stafford' (PROJECT)
CONTR_DEPTS    ← STAFFORD_PROJS ⋈ Dnum=Dnumber DEPARTMENT
PROJ_DEPT_MGRS ← CONTR_DEPTS ⋈ Mgr_ssn=Ssn EMPLOYEE
RESULT         ← π Pnumber, Dnum, Lname, Address, Bdate (PROJ_DEPT_MGRS)
```
→ (10, 4, Wallace, 291 Berry, Bellaire, TX, 1941-06-20), (30, 4, Wallace, …)

요령: 조건이 있는 릴레이션에서 **σ를 먼저** → FK–PK를 따라 **⋈** → 마지막에 **π**.

## 연습 3: 합집합 {#ra-practice-union}

성이 'Smith'인 사원이 일꾼으로든, 프로젝트를 통제하는 부서의 관리자로든 관련된 프로젝트 번호
```
SMITHS(Essn)        ← π Ssn (σ Lname='Smith' (EMPLOYEE))
SMITH_WORKER_PROJS  ← π Pno (WORKS_ON * SMITHS)
MGRS                ← π Lname, Dnumber (EMPLOYEE ⋈ Ssn=Mgr_ssn DEPARTMENT)
SMITH_MANAGED_DEPTS(Dnum) ← π Dnumber (σ Lname='Smith' (MGRS))
SMITH_MGR_PROJS(Pno)      ← π Pnumber (SMITH_MANAGED_DEPTS * PROJECT)
RESULT              ← SMITH_WORKER_PROJS ∪ SMITH_MGR_PROJS
```
- ∪를 하려고 두 결과의 속성 이름을 **Pno로 맞춤** (타입 호환)
- SMITHS(Essn)으로 이름을 바꿔서 WORKS_ON과 **자연 조인**이 Essn으로 걸리게 함

## 연습 4–5: 차집합과 교집합 {#ra-practice-diff}

**연습 4**: 부양가족이 **없는** 사원의 이름
```
ALL_EMPS             ← π Ssn (EMPLOYEE)
EMPS_WITH_DEPS(Ssn)  ← π Essn (DEPENDENT)
EMPS_WITHOUT_DEPS    ← ALL_EMPS − EMPS_WITH_DEPS
RESULT               ← π Lname, Fname (EMPS_WITHOUT_DEPS * EMPLOYEE)
```
**연습 5**: 부양가족이 **하나 이상 있는 관리자**의 이름
```
MGRS(Ssn)            ← π Mgr_ssn (DEPARTMENT)
EMPS_WITH_DEPS(Ssn)  ← π Essn (DEPENDENT)
MGRS_WITH_DEPS       ← MGRS ∩ EMPS_WITH_DEPS
RESULT               ← π Lname, Fname (MGRS_WITH_DEPS * EMPLOYEE)
```
→ Wong, Wallace

> 시험 포인트: "~가 없는" = **차집합 (−)**, "A이면서 B" = **교집합 (∩)**, "A이거나 B" = **합집합 (∪)**, "모든 ~" = **나눗셈 (÷)**. SQL의 NOT EXISTS / EXISTS AND EXISTS / UNION / NOT EXISTS(EXCEPT)와 1:1로 대응시켜 외워.
