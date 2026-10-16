@unit U5 | Advanced SQL (중첩 · 조인 · 집계 · 뷰) | 5-1_Advanced-SQL.pdf
@intro 중첩 질의(IN, ALL/ANY, EXISTS), 조인 테이블(NATURAL, OUTER), 집계와 GROUP BY/HAVING, Assertion·Trigger, 뷰. SQL 작성 문제의 본체라서 문제를 많이 풀어봐. 특히 "모든 ~를 하는" 질의(나눗셈)와 GROUP BY + HAVING은 꼭.

@lesson L5-1 | 중첩 질의 · IN · ALL/ANY | 5-1 p.3–6

## 중첩 질의와 IN {#nested-in}

**중첩 질의 (nested query)**: 다른 질의의 **WHERE 절 안에** 들어간 완전한 SELECT-FROM-WHERE 블록.
- DB에 있는 값을 가져와서 WHERE 조건의 비교에 쓸 때 유용
- 결과는 투플의 (다중)집합 → 바깥 질의 = outer query, 안쪽 = inner query

**IN**: 값 v를 값의 (다중)집합 V와 비교. **v가 V의 원소 중 하나면 TRUE**.
```
SELECT DISTINCT Pnumber
FROM   PROJECT
WHERE  Pnumber IN ( SELECT Pnumber
                    FROM   PROJECT, DEPARTMENT, EMPLOYEE
                    WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )
   OR  Pnumber IN ( SELECT Pno
                    FROM   WORKS_ON, EMPLOYEE
                    WHERE  Essn = Ssn AND Lname = 'Smith' );
```
→ 질의 4(UNION 버전)와 같은 결과 {1, 2}. 안쪽 질의 V1, V2가 각각 프로젝트 번호의 집합.

## ALL / ANY (SOME) {#all-any}

**= ANY (= SOME)**: v가 V의 **어떤** 값과 같으면 TRUE → **IN과 동치**. **= ALL**: **모든** 값과 같으면 TRUE.
- = 말고 >, >=, <, <=, <> 와도 결합 가능

```
SELECT Lname, Fname
FROM   EMPLOYEE
WHERE  Salary > ALL ( SELECT Salary FROM EMPLOYEE WHERE Dno = 5 );
```
→ 5번 부서 **모든** 사원보다 급여가 많은 사원. 5번 부서 급여 = {30000, 40000, 38000, 25000} → 40000 초과 → Wallace(43000), Borg(55000)

> 함정: `> ANY`는 "어느 하나보다라도 크면" = 최솟값보다 크면. `> ALL`은 최댓값보다 커야 함. 그리고 실습 환경 **SQLite는 ALL/ANY를 지원 안 하니** `> (SELECT MAX(Salary) ...)` 로 바꿔 써.

## 중첩 질의의 모호성과 상관 질의 {#correlated}

여러 단계 중첩에서 바깥 FROM과 안쪽 FROM에 **같은 이름의 속성**이 있으면 모호해진다 → **별칭**으로 해결.

**질의 16**: 부양가족 중에 **이름(first name)과 성별이 사원 자신과 같은** 사람이 있는 사원
```
SELECT E.Fname, E.Lname
FROM   EMPLOYEE AS E
WHERE  E.Ssn IN ( SELECT D.Essn
                  FROM   DEPENDENT AS D
                  WHERE  E.Fname = D.Dependent_name AND E.Sex = D.Sex );
```
- 안쪽 질의가 바깥의 E를 참조 → **상관 중첩 질의 (correlated nested query)**: 바깥 투플마다 안쪽 질의를 다시 평가하는 것처럼 동작
- 안쪽에서 별칭 없이 Sex라고 쓰면 가장 가까운(안쪽) 테이블의 속성으로 해석된다
- COMPANY 상태에서는 결과 0행 (그런 부양가족이 없음)

> 시험 포인트: "질의에서 참조하는 **모든 테이블에 별칭을** 붙이는 게 일반적으로 권장된다" (교안 문장 그대로).

@lesson L5-2 | EXISTS / NOT EXISTS · 나눗셈 질의 | 5-1 p.7–9

## EXISTS와 NOT EXISTS {#exists}

**중첩 질의 결과가 비었는지** 검사하는 불리언 함수. 보통 WHERE에서 씀.
- **EXISTS (Q)**: Q의 결과에 투플이 **하나라도 있으면** TRUE
- **NOT EXISTS (Q)**: Q의 결과가 **비어 있으면** TRUE

**질의 6**: 부양가족이 **없는** 사원
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  NOT EXISTS ( SELECT * FROM DEPENDENT WHERE Ssn = Essn );
```
→ Zelaya, Narayan, English, Jabbar, Borg (5명)

**부양가족이 하나 이상 있는 관리자**: 두 조건을 AND
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  EXISTS ( SELECT * FROM DEPENDENT  WHERE Ssn = Essn )
  AND  EXISTS ( SELECT * FROM DEPARTMENT WHERE Ssn = Mgr_ssn );
```
→ Franklin Wong, Jennifer Wallace

## "모든 ~에 대해" (나눗셈) 질의 {#division-sql}

**연습 1**: 5번 부서가 통제하는 **모든** 프로젝트에서 일하는 사원의 이름
```
SELECT Fname, Lname
FROM   EMPLOYEE
WHERE  NOT EXISTS ( ( SELECT Pnumber FROM PROJECT WHERE Dnum = 5 )
                    EXCEPT
                    ( SELECT Pno FROM WORKS_ON WHERE Ssn = Essn ) );
```
읽는 법: (5번 부서 프로젝트 전체) − (이 사원이 일하는 프로젝트) = **빠진 프로젝트**. 빠진 게 **없으면**(NOT EXISTS) 전부 하는 것.
- 예: 5번 부서 프로젝트 = {1, 2, 3}. A는 {1, 2, 4} → 차집합 {3} ≠ ∅ → 탈락. B는 {1, 2, 3, 4} → 차집합 ∅ → 선택
- COMPANY 상태에서 5번 부서 프로젝트 = {1, 2, 3}인데 세 개 다 하는 사원이 없어서 결과는 **0행**

EXCEPT 없이 NOT EXISTS 두 번으로도 쓸 수 있다 ("이 사원이 안 하는 5번 부서 프로젝트가 존재하지 않는다"):
```
SELECT E.Fname, E.Lname
FROM   EMPLOYEE AS E
WHERE  NOT EXISTS ( SELECT * FROM PROJECT AS P
                    WHERE  P.Dnum = 5
                      AND  NOT EXISTS ( SELECT * FROM WORKS_ON AS W
                                        WHERE W.Essn = E.Ssn AND W.Pno = P.Pnumber ) );
```

> 함정: "어떤" 프로젝트에서 일하는 사원(EXISTS, IN)과 "모든" 프로젝트에서 일하는 사원(NOT EXISTS + EXCEPT)을 구별해. 문장에 **all**이 나오면 나눗셈 패턴.

@lesson L5-3 | 조인 테이블 · NATURAL · INNER/OUTER | 5-1 p.10–14

## 조인 테이블 {#joined-table}

**조인 테이블 (joined table)**: **FROM 절에서** 조인 연산으로 만들어지는 테이블. WHERE에 선택 조건과 조인 조건이 섞이는 걸 피할 수 있다.
```
SELECT Fname, Lname, Address
FROM   (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)
WHERE  Dname = 'Research';
```
- 조인된 테이블 = 첫 테이블(EMPLOYEE)의 모든 속성 + 둘째 테이블(DEPARTMENT)의 모든 속성
- WHERE에 `Dnumber = Dno`를 쓴 질의 2와 결과가 같다

## NATURAL JOIN {#natural-join-sql}

**같은 이름을 가진 속성 쌍마다 암묵적인 동등 조건**을 만든다 → 조인 조건을 쓰지 않음.
- 이름이 다르면 먼저 **이름을 바꿔서** 맞춘다
```
SELECT Fname, Lname, Address
FROM   (EMPLOYEE NATURAL JOIN
        (DEPARTMENT AS DEPT (Dname, Dno, Mssn, Msdate)))
WHERE  Dname = 'Research';
```
- DEPARTMENT의 Dnumber를 Dno로 바꿔서 EMPLOYEE.Dno와 이름을 맞춤
- 조인 속성은 결과에 **한 번만** 나온다

## INNER JOIN과 OUTER JOIN {#inner-outer}

**내부 조인 (inner join)**: 기본 조인. **다른 릴레이션에 짝이 있는 투플만** 결과에 들어감.
```
SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM   EMPLOYEE AS E, EMPLOYEE AS S
WHERE  E.Super_ssn = S.Ssn;
```
→ 7행. Super_ssn이 **NULL인 Borg는 빠진다**.

**외부 조인 (outer join)**: 짝이 없는 투플도 결과에 넣고, 상대 속성은 **NULL로 채움(padding)**.
```
SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name
FROM   (EMPLOYEE AS E LEFT OUTER JOIN EMPLOYEE AS S ON E.Super_ssn = S.Ssn);
```
→ 8행. Borg의 Supervisor_name = NULL.

| 조인 | 결과에 들어가는 투플 |
|---|---|
| INNER JOIN | 조인 조건을 만족하는 쌍만 |
| LEFT OUTER JOIN | **왼쪽 테이블의 모든 투플** (짝 없으면 오른쪽 속성 NULL) |
| RIGHT OUTER JOIN | **오른쪽 테이블의 모든 투플** |
| FULL OUTER JOIN | 양쪽 모든 투플 |

> 함정: OUTER JOIN에서 "짝 없는 것만" 고르려면 `WHERE B.KEY IS NULL`을 덧붙인다 (교안 p.14 벤다이어그램 아래줄). NULL 비교는 `= NULL`이 아니라 **IS NULL**.

@lesson L5-4 | 집계 함수 · GROUP BY · HAVING | 5-1 p.15–22, 48

## 집계 함수 {#aggregate}

**집계 함수 (aggregate function)**: 여러 투플의 정보를 **투플 하나짜리 요약**으로. 주로 SELECT나 HAVING에서 씀.
- **COUNT**: 투플 수 또는 값의 수
- **SUM, MAX, MIN, AVG**: 숫자 값의 (다중)집합에 적용

**질의 19**: 전체 사원의 급여 합·최대·최소·평균
```
SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)
FROM   EMPLOYEE;
```
→ 281000, 55000, 25000, 35125

**질의 20**: Research 부서만
```
SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)
FROM   (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)
WHERE  Dname = 'Research';
```
→ 133000, 40000, 25000, 33250

## COUNT와 NULL · 중첩 질의에서의 집계 {#count-null}

- **COUNT(*)**: 결과의 **행(투플) 수**. 질의 21 `SELECT COUNT(*) FROM EMPLOYEE;` → 8, 질의 22 Research만 → 4
- **COUNT(속성)**: 그 속성의 **값** 수. **NULL은 세지 않는다**. 예) `COUNT(Super_ssn)` → 7
- **COUNT(DISTINCT Salary)**: 서로 다른 급여 값의 수 → 6 (질의 23)
- 집계 결과는 값 하나라서 **조건의 일부**로 쓸 수 있다:
```
SELECT Lname, Fname
FROM   EMPLOYEE
WHERE  ( SELECT COUNT(*) FROM DEPENDENT WHERE Ssn = Essn ) >= 2;
```
→ 부양가족이 2명 이상: Smith(3명), Wong(3명)

## GROUP BY {#group-by}

**그룹화**: 릴레이션의 투플을 **겹치지 않는 부분집합(그룹)** 으로 나눠서 그룹마다 집계 함수를 적용.
- **그룹화 속성 (grouping attribute)**: 그룹을 나누는 기준. 같은 그룹 = 그룹화 속성 값이 같은 투플들
- **GROUP BY** 절에 지정. 그룹화 속성은 SELECT에도 나와야 결과에서 어느 그룹인지 알 수 있다

**질의 24**: 부서별 부서 번호, 사원 수, 평균 급여
```
SELECT   Dno, COUNT(*), AVG(Salary)
FROM     EMPLOYEE
GROUP BY Dno;
```
→ (5, 4, 33250), (4, 3, 31000), (1, 1, 55000)

**질의 25**: 프로젝트별 번호, 이름, 일하는 사원 수
```
SELECT   Pnumber, Pname, COUNT(*)
FROM     PROJECT, WORKS_ON
WHERE    Pnumber = Pno
GROUP BY Pnumber, Pname;
```
→ ProductX 2, ProductY 3, ProductZ 2, Computerization 3, Reorganization 3, Newbenefits 3

> 함정: GROUP BY를 쓰면 SELECT에는 **그룹화 속성과 집계 함수만** 올 수 있다. 그룹마다 값이 하나로 정해지지 않는 속성(예: Dno로 묶었는데 Lname)을 SELECT에 쓰면 안 된다.

## HAVING {#having}

**HAVING**: 그룹의 **요약 정보에 대한 조건**. GROUP BY와 함께 씀. 조건을 만족하는 **그룹만** 결과에.

**질의 26**: 사원이 **두 명 넘게** 일하는 프로젝트마다 번호, 이름, 사원 수
```
SELECT   Pnumber, Pname, COUNT(*)
FROM     PROJECT, WORKS_ON
WHERE    Pnumber = Pno
GROUP BY Pnumber, Pname
HAVING   COUNT(*) > 2;
```
→ ProductY, Computerization, Reorganization, Newbenefits (각 3명)

**연습 2**: 평균 급여가 $30,000 넘는 부서마다 부서 이름과 사원 수
```
SELECT   D.Dname, COUNT(*)
FROM     EMPLOYEE AS E, DEPARTMENT AS D
WHERE    E.Dno = D.Dnumber
GROUP BY D.Dname
HAVING   AVG(E.Salary) > 30000;
```
→ Research 4, Administration 3, Headquarters 1 (교안 풀이는 GROUP BY E.Dno로 묶음. 표준 SQL에서는 SELECT의 D.Dname도 GROUP BY에 있어야 안전)

> 시험 포인트: **WHERE = 투플 조건 (그룹 만들기 전)**, **HAVING = 그룹 조건 (집계 후)**. "평균이 3만 넘는"처럼 집계에 대한 조건은 WHERE에 못 쓴다.

**실행 순서**: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY

@lesson L5-5 | Assertion · Trigger | 5-1 p.24–29

## Assertion {#assertion}

**내장 제약(키, 개체 무결성, 참조 무결성)으로 표현할 수 없는 일반 제약**을 지정.
- 예) 사원의 급여는 그 사원이 속한 부서 관리자의 급여보다 많으면 안 된다
```
CREATE ASSERTION SALARY_CONSTRAINT
CHECK ( NOT EXISTS ( SELECT *
                     FROM   EMPLOYEE E, EMPLOYEE M, DEPARTMENT D
                     WHERE  E.Salary > M.Salary
                       AND  E.Dno = D.Dnumber
                       AND  D.Mgr_ssn = M.Ssn ) );
```
- **CHECK** 뒤 괄호 안의 조건은 **모든 DB 상태에서 참**이어야 한다
- 관례: 원하는 조건을 **위반하는 투플을 고르는 질의**를 쓰고 **NOT EXISTS**로 감싼다 → 결과가 비면 TRUE(만족), 비지 않으면 FALSE(위반)

## Trigger (ECA 규칙) {#trigger-eca}

**특정 이벤트가 일어나고 조건이 맞을 때 자동으로 실행할 동작**을 지정. **ECA (Event, Condition, Action) 규칙**.
```
CREATE TRIGGER SALARY_VIOLATION
BEFORE INSERT OR UPDATE OF SALARY, SUPERVISOR_SSN
    ON EMPLOYEE
FOR EACH ROW
    WHEN ( NEW.SALARY > ( SELECT SALARY FROM EMPLOYEE
                          WHERE SSN = NEW.SUPERVISOR_SSN ) )
        INFORM_SUPERVISOR(NEW.Supervisor_ssn, NEW.Ssn);
```
- **Event**: DB에 명시적으로 적용되는 갱신 연산 (새 사원 삽입, 급여 변경, 상사 변경). **BEFORE / AFTER**로 그 연산 전/후에 실행. 가능한 이벤트를 **모두** 고려해야 함
- **Condition**: 이벤트가 일어난 뒤 동작을 실행할지 결정. **WHEN 절**. 선택 사항. 참일 때만 동작 실행
- **Action**: 자동 실행할 동작 = SQL 문장들, DB 트랜잭션, 또는 외부 프로그램 (예: 외부 저장 프로시저 INFORM_SUPERVISOR)
- 용도: (1) DB 일관성 유지, (2) DB 갱신 모니터링, (3) 유도 데이터 자동 갱신
- 예) 사원의 출장비가 한도를 넘으면 관리자에게 알림

> 함정: Assertion = **제약** (위반하면 연산을 막음), Trigger = **동작** (조건이 맞으면 무언가를 실행). 교안 예는 둘 다 급여 비교지만 하나는 "막기", 하나는 "알리기".

@lesson L5-6 | 뷰 (View) | 5-1 p.30–47

## 뷰의 정의와 쓰임 {#view-def}

**뷰 (view)**: 기본 테이블(base table)에서 유도된 **가상 테이블**. 물리적으로 존재하지 않을 수도 있다.
- 검색: 제한 없음. 갱신: 보통 제한됨 (사실상 읽기 전용)
- 쓰는 이유: **복잡한 질의를 단순화**. 여러 테이블 조인·집계를 자주 쓰면 뷰로 만들어 두고 **단일 테이블 질의**처럼 쓴다

```
CREATE VIEW WORKS_ON1
AS SELECT Fname, Lname, Pname, Hours
   FROM   EMPLOYEE, PROJECT, WORKS_ON
   WHERE  Ssn = Essn AND Pno = Pnumber;

CREATE VIEW DEPT_INFO (Dept_name, No_of_emps, Total_sal)
AS SELECT   Dname, COUNT(*), SUM(Salary)
   FROM     DEPARTMENT, EMPLOYEE
   WHERE    Dnumber = Dno
   GROUP BY Dname;
```
- 속성 이름을 안 주면 정의 질의의 속성 이름을 그대로 씀 (WORKS_ON1), 명시할 수도 있음 (DEPT_INFO)
- 뷰 질의: `SELECT Fname, Lname FROM WORKS_ON1 WHERE Pname = 'ProductX';` → 매번 세 테이블을 조인할 필요 없음
- **DROP VIEW WORKS_ON1;** → 정의 테이블에는 영향 없음

## 뷰 구현: 질의 수정 vs 실체화 {#view-impl}

뷰는 **항상 최신(up-to-date)** 이어야 한다 → 정의 테이블이 바뀌면 DBMS가 뷰에 반영할 책임.

| 방식 | 내용 | 특징 |
|---|---|---|
| **질의 수정 (query modification)** | 뷰 질의를 **기본 테이블에 대한 질의로 변환**. 뷰를 물리적으로 유지하지 않음 | 사용자는 편하지만 DB 시스템엔 비효율 (복잡한 뷰를 매번 다시 계산) |
| **뷰 실체화 (view materialization)** | 뷰가 처음 질의될 때 **물리적으로 뷰 테이블을 만들어** 한동안 유지 | 이후 뷰 질의가 자주 온다는 가정. **추가 저장 공간**. 정의 테이블이 바뀌면 **점진적 갱신(incremental update)** |

실체화된 뷰를 **언제** 갱신하나:
- **즉시 갱신 (immediate)**: 기본 테이블이 바뀌자마자. 항상 최신이지만 불필요하고 비효율적일 때가 있음
- **주기적 갱신 (periodic)**: 주기적으로. 뷰 질의가 최신이 아닌 결과를 받을 수 있음
- **지연 갱신 (lazy)**: 뷰 질의가 필요할 때. 질의가 오기 전까진 최신이 아님

일정 기간 질의되지 않으면 실체화된 뷰를 지우고, 나중에 필요하면 처음부터 다시 계산.

## 뷰 갱신 {#view-update}

뷰에 대한 검색은 언제나 가능하지만, INSERT/DELETE/UPDATE는 많은 경우 불가능.

**갱신 가능 조건: 뷰 갱신을 이루는 기본 릴레이션 갱신이 딱 하나뿐일 때.**
- **단일 테이블 + 집계 없음** → 기본 테이블 갱신 하나로 매핑 → **허용**. 단 뷰 속성에 (1) 기본 릴레이션의 **PK**, (2) DEFAULT가 없는 **NOT NULL 속성 전부**가 들어 있어야 함 (뷰로 투플을 넣을 때 그 값들이 비면 안 되니까)
- **조인 (여러 테이블)** → 여러 방식으로 매핑될 수 있어 **일반적으로 불가**
- **그룹화·집계** → 그 갱신이 **말이 안 됨** → **불가**

예 1 (여러 해석): `UPDATE WORKS_ON1 SET Pname = 'ProductY' WHERE Lname = 'Smith' AND Fname = 'John' AND Pname = 'ProductX';`
- 해석 a: Smith가 일하는 프로젝트를 바꿈 → WORKS_ON의 Pno를 ProductY 번호로 (의도대로)
- 해석 b: PROJECT의 'ProductX' 이름을 'ProductY'로 → 뷰 결과는 같아 보이지만 **부작용**: ProductX에서 일하던 모든 투플이 바뀜

예 2 (불가능): `UPDATE DEPT_INFO SET Total_sal = 100000 WHERE Dname = 'Research';` → Total_sal은 SUM으로 **계산된 값**, 물리적으로 저장 안 됨 → 의미 없음

## 뷰를 이용한 권한 부여 {#view-auth}

뷰로 권한 없는 사용자에게 **특정 속성이나 투플을 숨길** 수 있다.
```
CREATE VIEW DEPT5EMP AS
SELECT * FROM EMPLOYEE WHERE Dno = 5;            -- 투플 제한

CREATE VIEW BASIC_EMP_DATA AS
SELECT Fname, Lname, Address FROM EMPLOYEE;      -- 속성 제한
```
- DEPT5EMP: 5번 부서 관리자는 5번 부서 사원 정보만 보게 함. 사용자에게 EMPLOYEE가 아니라 **뷰에 대한 질의 권한만** 부여
- BASIC_EMP_DATA: 일반 사원은 이름과 주소만

교안 연습 3·4 풀이:
```
CREATE VIEW DEPT_INFO (DeptName, MgrFname, MgrLname, MgrSalary)
AS SELECT D.Dname, E.Fname, E.Lname, E.Salary
   FROM   DEPARTMENT AS D, EMPLOYEE AS E
   WHERE  D.Mgr_ssn = E.Ssn;                      -- 부서와 관리자 정보

CREATE VIEW ProjectInfo (Pname, Dname, NumEmployees, TotalHours)
AS SELECT   P.Pname, D.Dname, COUNT(*), SUM(W.Hours)
   FROM     PROJECT AS P, WORKS_ON AS W, DEPARTMENT AS D
   WHERE    P.Pnumber = W.Pno AND D.Dnumber = P.Dnum
   GROUP BY P.Pnumber, P.Pname, D.Dname;          -- 프로젝트 현황
```
