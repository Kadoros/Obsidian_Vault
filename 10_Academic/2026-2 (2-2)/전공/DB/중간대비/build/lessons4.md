@unit U4 | Basic SQL (DDL · DML · SELECT) | 4-1_SQL.pdf + 3-2_setup-for-sql.pdf + SQL-week6-lab.pdf
@intro CREATE TABLE의 제약조건 문법, 참조 트리거 동작(ON DELETE/UPDATE), INSERT·DELETE·UPDATE가 무엇을 어기는지, 그리고 SELECT-FROM-WHERE. SQL은 직접 써봐야 늘어. 풀이 문제는 교재 COMPANY 상태(3-1 p.12)에서 실제로 돌려본 결과를 정답에 붙여놨어.

@lesson L4-1 | SQL 소개 · CREATE SCHEMA/TABLE · 제약조건 | 4-1 p.3–10

## SQL과 NL2SQL {#sql-intro}

- **SQL (Structured Query Language)**: 특수 목적 **선언적(declarative)** 언어. IBM의 첫 DBMS용으로 설계, 원래 이름 **SEQUEL** (Structured English Query Language). 'S-Q-L' 또는 'SEQUEL'로 읽음
- **DDL (Data Definition Language)**: DB와 **테이블**에 대한 명령. CREATE / ALTER / DROP (schema, table)
- **DML (Data Manipulation Language)**: 테이블 안 **투플**에 대한 명령. 검색 SELECT, 수정 INSERT / DELETE / UPDATE
- **NL2SQL**: 자연어 질의를 SQL로 바꾸는 기술. 어려움 = 자연어의 모호성, 스키마 이해·연결(schema linking), 처음 보는 DB로의 일반화, 복잡한 질의 생성. LLM 기반 방법도 아직 완벽과 거리가 멀다 → **SQL을 제대로 이해하는 게 중요**

## CREATE SCHEMA / CREATE TABLE {#create-table}

**SQL 스키마**: 테이블, 타입, 제약조건, 뷰, 도메인 등 스키마를 기술하는 요소들. 스키마 이름으로 식별.

```
CREATE SCHEMA COMPANY AUTHORIZATION 'Jsmith';
```
- **권한 식별자 (authorization identifier)**: 스키마를 소유한 사용자

**CREATE TABLE**: 이름, 속성, 초기 제약조건을 지정해 새 릴레이션 생성.
- 테이블 이름에 스키마 이름을 붙일 수 있음: `CREATE TABLE COMPANY.EMPLOYEE`
- 속성 = <속성 이름, 데이터 타입> 쌍의 리스트
- 초기 제약조건 = 속성 제약, 무결성 제약

```
CREATE TABLE EMPLOYEE
( Fname      VARCHAR(15)    NOT NULL,
  Minit      CHAR,
  Lname      VARCHAR(15)    NOT NULL,
  Ssn        CHAR(9)        NOT NULL,
  Bdate      DATE,
  Address    VARCHAR(30),
  Sex        CHAR,
  Salary     DECIMAL(10,2),
  Super_ssn  CHAR(9),
  Dno        INT            NOT NULL,
  PRIMARY KEY (Ssn) );
```

## 속성 제약: NOT NULL, DEFAULT {#attr-constraints}

- **NOT NULL**: 그 속성 값은 NULL이 될 수 없다. **PK 속성에는 항상 암묵적으로** 적용 (= 개체 무결성)
- **DEFAULT <값>**: 새 투플에 그 속성 값을 명시하지 않으면 기본값이 들어감
  - 예) 새 사원의 기본 부서: `Dno INT NOT NULL DEFAULT 1`, DEPARTMENT의 `Mgr_ssn CHAR(9) NOT NULL DEFAULT '888665555'`

## 키 제약: PRIMARY KEY, UNIQUE, FOREIGN KEY {#key-clauses}

```
CREATE TABLE DEPARTMENT
( Dname           VARCHAR(15)  NOT NULL,
  Dnumber         INT          NOT NULL,
  Mgr_ssn         CHAR(9)      NOT NULL,
  Mgr_start_date  DATE,
  PRIMARY KEY (Dnumber),
  UNIQUE (Dname),
  FOREIGN KEY (Mgr_ssn) REFERENCES EMPLOYEE(Ssn) );
CREATE TABLE DEPT_LOCATIONS
( Dnumber    INT          NOT NULL,
  Dlocation  VARCHAR(15)  NOT NULL,
  PRIMARY KEY (Dnumber, Dlocation),
  FOREIGN KEY (Dnumber) REFERENCES DEPARTMENT(Dnumber) );
```
- **PRIMARY KEY**: PK를 이루는 속성(들). 복합이면 괄호 안에 여러 개
- **UNIQUE**: 대체(alternate) 키 = **후보 키**
- **FOREIGN KEY ... REFERENCES 테이블(속성)**: 다른 릴레이션의 PK를 참조하는 FK
- 제약에 이름 붙이기: `CONSTRAINT DEPTPK PRIMARY KEY (Dnumber)` → 나중에 ALTER로 지울 때 이름이 필요

> 시험 포인트: 참조되는 PK가 갱신·삭제되면 참조 무결성이 깨질 수 있는데, **SQL의 기본 동작은 그 연산을 거부(reject)** 하는 것. 다른 방법 = 참조 트리거 동작 (L4-2).

@lesson L4-2 | 참조 트리거 동작 · DROP · ALTER | 4-1 p.11–20

## 참조 트리거 동작 (Referential Triggered Actions) {#ref-actions}

**"다른 투플이 참조하는 투플이 삭제/갱신되면?"** 에 대한 동작을 FK에 붙인다.
- **트리거**: `ON DELETE`, `ON UPDATE`
- **동작**: `SET NULL`, `CASCADE`, `SET DEFAULT` (지정 안 하면 기본 = 거부, 교안 연습에서는 REJECT라고 부름)

| 동작 | 참조되던 투플이 삭제될 때 | 갱신될 때 |
|---|---|---|
| SET NULL | 참조하던 FK를 NULL로 | FK를 NULL로 |
| SET DEFAULT | FK를 기본값으로 | FK를 기본값으로 |
| CASCADE | **참조하던 투플도 삭제** | 참조하던 FK를 **새 값으로** 바꿈 |

```
CREATE TABLE EMPLOYEE
( ...,
  Dno INT NOT NULL DEFAULT 1,
  CONSTRAINT EMPPK PRIMARY KEY (Ssn),
  CONSTRAINT EMPSUPERFK FOREIGN KEY (Super_ssn) REFERENCES EMPLOYEE(Ssn)
      ON DELETE SET NULL      ON UPDATE CASCADE,
  CONSTRAINT EMPDEPTFK  FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber)
      ON DELETE SET DEFAULT   ON UPDATE CASCADE );
```

**교안 토론 (p.13)**: EMPSUPERFK의 ON DELETE를 **CASCADE**로 바꾸고 `DELETE FROM EMPLOYEE WHERE Lname = 'Borg';` 를 실행하면?
- Borg(888665555)를 상사로 둔 Wong, Wallace가 같이 삭제 → 그들을 상사로 둔 Smith, Narayan, English, Zelaya, Jabbar도 연쇄 삭제 → **EMPLOYEE 투플 8개가 전부 사라진다**. CASCADE는 재귀적으로 전파된다는 점이 핵심
- (EMPSUPERFK만 봤을 때 얘기. 실제로는 WORKS_ON.Essn, DEPENDENT.Essn 같은 다른 FK가 기본 동작(거부)이면, 지워질 사원을 그 투플들이 참조하고 있어서 DELETE 전체가 거부된다)

**교안 연습 1 (LIBRARY)** 정답 예:
| FK | ON DELETE | ON UPDATE | 이유 |
|---|---|---|---|
| BOOK_AUTHORS.Book_id → BOOK | CASCADE | CASCADE | 책이 지워지면 저자 정보도 필요 없음 |
| BOOK.Publisher_name → PUBLISHER | REJECT | CASCADE | 그 출판사 책이 있으면 출판사 삭제 금지 |
| BOOK_COPIES.Book_id → BOOK | CASCADE | CASCADE | 책 목록에서 빼면 사본도 관리 안 함 |
| BOOK_COPIES.Branch_id → LIBRARY_BRANCH | CASCADE | CASCADE | 지점 삭제 = 폐점 |
| BOOK_LOANS.Book_id → BOOK | REJECT (또는 CASCADE) | CASCADE | 목록에서 빼도 대출된 책은 돌려받아야 함 |
| BOOK_LOANS.Branch_id → LIBRARY_BRANCH | CASCADE (또는 REJECT) | CASCADE | 폐점하면 대출을 탕감 |
| BOOK_LOANS.Card_no → BORROWER | REJECT | CASCADE | 책을 다 반납해야 회원 탈퇴 가능 |

> 시험 포인트: 정답이 하나가 아니라 **이유가 맞으면** 인정되는 유형. ON UPDATE는 거의 다 CASCADE (키가 바뀌면 참조도 따라가야 추적 가능).

## DROP SCHEMA / DROP TABLE {#drop}

스키마 수정 = 투플이 아니라 **스키마**를 바꾸는 것 (테이블·속성·제약 추가/삭제).

- **DROP SCHEMA**: 스키마 전체 삭제
  - `CASCADE`: 스키마의 모든 요소(테이블, 도메인 등)까지 삭제
  - `RESTRICT`: 스키마에 **요소가 하나도 없을 때만** 삭제 (사용자가 요소를 하나씩 지워야 함)
- **DROP TABLE**: 특정 테이블 삭제. 모든 투플 + **카탈로그의 테이블 정의까지** 제거
  - 투플만 지우고 정의는 남기려면 **DELETE** 명령
  - `CASCADE`: 그 테이블을 참조하는 제약과 요소도 자동으로 같이 삭제
  - `RESTRICT`: 어떤 제약이나 요소도 그 테이블을 참조하지 않을 때만 삭제

## ALTER TABLE {#alter}

테이블 정의 변경: 속성·제약 추가/삭제, 열 정의(타입, 제약) 변경.
```
ALTER TABLE COMPANY.EMPLOYEE ADD COLUMN Job VARCHAR(12);
ALTER TABLE COMPANY.EMPLOYEE DROP COLUMN Address CASCADE;
ALTER TABLE COMPANY.EMPLOYEE DROP CONSTRAINT EMPSUPERFK CASCADE;
```
- DROP COLUMN `CASCADE`: 그 열을 참조하는 제약도 자동으로 같이 삭제 / `RESTRICT`: 그 열을 참조하는 요소가 없을 때만
- ADD COLUMN으로 추가된 열은 기존 투플에서 NULL (또는 DEFAULT 값). 그래서 새 열에 NOT NULL을 걸려면 DEFAULT가 필요

@lesson L4-3 | INSERT · DELETE · UPDATE | 4-1 p.22–27

## INSERT {#dml-insert}

**사용법 1: 모든 속성 값** — 테이블을 만들 때의 속성 **순서대로** 값을 나열
```
INSERT INTO EMPLOYEE
VALUES ('Richard', 'K', 'Marini', '653298653', '1962-12-30',
        '98 Oak Forest, Katy, TX', 'M', 37000, '653298653', 4);
```
**사용법 2: 속성 이름 명시** — **NOT NULL이면서 DEFAULT가 없는 속성은 반드시** 포함
```
INSERT INTO EMPLOYEE (Fname, Lname, Dno, Ssn)
VALUES ('Richard', 'Marini', 4, '653298653');
```
**제약 위반 예 (거부됨)**
- `INSERT INTO EMPLOYEE (Fname, Lname, Ssn, Dno) VALUES ('Robert', 'Hatcher', '980760540', 2);` → Dnumber=2인 부서 없음 → **참조 무결성**
- `INSERT INTO EMPLOYEE (Fname, Lname, Dno) VALUES ('Robert', 'Hatcher', 5);` → Ssn 없음 → **NOT NULL** (PK라 개체 무결성)

## DELETE와 UPDATE {#dml-delete-update}

**DELETE**: WHERE로 **한 릴레이션**에서 지울 투플을 고름
- 한 번에 한 테이블에서만 명시적으로 삭제. 참조 트리거 동작(ON DELETE CASCADE)이 있으면 다른 릴레이션으로 전파될 수 있다
- 지워지는 투플 수는 경우마다 다름 (COMPANY 상태 기준):

```
DELETE FROM EMPLOYEE WHERE Lname = 'Brown';        -- 0개
DELETE FROM EMPLOYEE WHERE Ssn = '123456789';      -- 1개
DELETE FROM EMPLOYEE WHERE Dno = 5;                -- 4개
DELETE FROM EMPLOYEE;                              -- 전부!
```
> 주의: **WHERE를 빼면 모든 투플이 삭제된다.** 테이블 정의는 남음 (DROP TABLE과 다름).

**UPDATE**: WHERE로 **한 릴레이션**에서 고친 투플을 고르고, **SET**으로 바꿀 속성과 새 값 지정
```
UPDATE PROJECT  SET Plocation = 'Bellaire', Dnum = 5  WHERE Pnumber = 10;
UPDATE EMPLOYEE SET Salary = Salary * 1.1             WHERE Dno = 5;
```
- UPDATE 하나로 여러 투플을 고칠 수 있다 (Dno=5인 4명이 한꺼번에 10% 인상)
- ON UPDATE CASCADE가 있으면 다른 릴레이션으로 전파

@lesson L4-4 | SELECT-FROM-WHERE · 별칭 | 4-1 p.28–34

## SELECT-FROM-WHERE 블록 {#sfw}

```
SELECT  <attribute list>      -- 투영 속성 (projection attributes)
FROM    <table list>          -- 질의에 필요한 릴레이션
WHERE   <condition>;          -- 선택 조건 + 조인 조건
```
**질의 1**: 'John B. Smith'의 생일과 주소
```
SELECT Bdate, Address
FROM   EMPLOYEE
WHERE  Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';
```
→ 1965-01-09, 731 Fondren, Houston, TX

**질의 2**: 'Research' 부서에서 일하는 모든 사원의 이름과 주소
```
SELECT Fname, Lname, Address
FROM   EMPLOYEE, DEPARTMENT
WHERE  Dname = 'Research' AND Dnumber = Dno;
```
- `Dname = 'Research'` = **선택 조건** (한 테이블에서 관심 있는 투플 고르기)
- `Dnumber = Dno` = **조인 조건** (DEPARTMENT 투플과 EMPLOYEE 투플을 결합)
- 결과: Smith, Wong, Narayan, English (4명)

## 모호한 속성 이름과 별칭 {#qualify-alias}

**자격 부여 (qualify)**: 다른 릴레이션에 같은 이름의 속성이 있으면 `릴레이션이름.속성`으로 구분.
```
SELECT Fname, EMPLOYEE.Name, Address
FROM   EMPLOYEE, DEPARTMENT
WHERE  DEPARTMENT.Name = 'Research' AND DEPARTMENT.Dnumber = EMPLOYEE.Dnumber;
```
**별칭 (alias, 투플 변수)**: 긴 이름 반복을 줄이고, **같은 릴레이션을 두 번** 참조할 때 필수.
```
SELECT E.Fname, E.Lname, S.Fname, S.Lname
FROM   EMPLOYEE AS E, EMPLOYEE AS S
WHERE  E.Super_ssn = S.Ssn;
```
→ 사원과 그 직속 상사의 이름. E = 사원 역할, S = 상사 역할. 상사가 없는 Borg는 결과에 없다 (7행).

> 함정: 교안 p.32의 `FROM EMPLOYEE AS E WHERE E.Super_ssn = E.Ssn` 은 별칭이 하나라서 "자기 자신이 자기 상사인 사원"을 찾는 질의가 된다 (결과 0행). 같은 테이블을 두 역할로 쓰려면 별칭이 **두 개** 필요하다는 걸 보여주는 예.

## WHERE 생략과 * {#missing-where-star}

**WHERE 생략**: 투플 선택 조건이 없음 → FROM의 릴레이션 투플을 전부 검색.
- 릴레이션이 둘 이상이면 **가능한 모든 투플 조합 (카티션 곱)** 이 나온다
- `SELECT Ssn, Dname FROM EMPLOYEE, DEPARTMENT;` → 8 × 3 = **24행**
- 조건 하나라도 빠뜨리면 틀리고 아주 큰 결과가 나오니 **WHERE에 모든 조건을 다 써야** 한다

**별표 (*)**: 선택된 투플의 **모든 속성** 값. `SELECT * FROM EMPLOYEE WHERE Dno = 5;` → 4행, 10열.

@lesson L4-5 | 다중집합 · 집합 연산 · ORDER BY · 연산자 | 4-1 p.35–41

## 다중집합과 DISTINCT {#multiset-distinct}

**SQL은 테이블을 집합이 아니라 다중집합(multiset)으로 다룬다** → 테이블이나 질의 결과에 **중복 투플**이 있을 수 있고, SQL은 **중복을 자동으로 제거하지 않는다**.

왜?
- 중복 제거는 **비싼** 연산 (투플을 정렬한 다음 중복을 지워야 함)
- 사용자가 중복을 보고 싶을 때도 있음
- 집계 함수를 쓸 때 중복이 필요 (예: 급여 평균) → 5주차

키워드
- **ALL** (기본): 중복 유지. `SELECT ALL Salary FROM EMPLOYEE;` → 8행 (25000이 3번)
- **DISTINCT**: 중복 제거. `SELECT DISTINCT Salary FROM EMPLOYEE;` → 6행

## 집합 연산 UNION / EXCEPT / INTERSECT {#set-ops}

- **UNION**(합), **EXCEPT**(차), **INTERSECT**(교). 결과는 투플의 **집합** → **중복 제거됨**
- **타입 호환(type-compatible)** 되는 릴레이션에만 적용 (속성 수가 같고 대응 속성의 도메인이 같음)
- 다중집합 버전: **UNION ALL, EXCEPT ALL, INTERSECT ALL** (중복 유지)
  - R(A) = {a1, a2, a2, a3}, S(A) = {a1, a2, a4, a5}
  - R UNION ALL S = {a1, a1, a2, a2, a2, a3, a4, a5}
  - R EXCEPT ALL S = {a2, a3}
  - R INTERSECT ALL S = {a1, a2}

**질의 4**: 성이 'Smith'인 사원이 **일꾼**으로든 그 프로젝트를 통제하는 부서의 **관리자**로든 관련된 프로젝트 번호
```
( SELECT DISTINCT Pnumber
  FROM   PROJECT, DEPARTMENT, EMPLOYEE
  WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )
UNION
( SELECT DISTINCT Pnumber
  FROM   PROJECT, WORKS_ON, EMPLOYEE
  WHERE  Pnumber = Pno AND Essn = Ssn AND Lname = 'Smith' );
```
→ Smith는 관리자가 아니라 첫 블록은 비고, 일꾼으로 1, 2 → 결과 {1, 2}

## ORDER BY · 산술 연산 · BETWEEN {#order-arith}

**ORDER BY**: 결과 투플을 속성 값 기준으로 정렬. **기본은 오름차순(ASC)**, 내림차순은 DESC.
```
SELECT   D.Dname, E.Lname, E.Fname, P.Pname
FROM     DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE    D.Dnumber = E.Dno AND E.Ssn = W.Essn AND W.Pno = P.Pnumber
ORDER BY D.Dname DESC, E.Lname ASC, E.Fname ASC;
```
**산술 연산자** + − * /: 숫자 속성에 적용. **릴레이션 상태는 바뀌지 않는다** (결과에만 반영)
```
SELECT E.Fname, E.Lname, 1.1 * E.Salary AS Increased_sal
FROM   EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P
WHERE  E.Ssn = W.Essn AND W.Pno = P.Pnumber AND P.Pname = 'ProductX';
```
→ Smith 33000, English 27500

**BETWEEN**: 범위 조건. `(Salary BETWEEN 30000 AND 40000)` = `((Salary >= 30000) AND (Salary <= 40000))` → **양 끝 포함**
```
SELECT * FROM EMPLOYEE WHERE (Salary BETWEEN 30000 AND 40000) AND Dno = 5;
```
→ Smith(30000), Wong(40000), Narayan(38000)

> 실습 메모 (3-2, week6 lab): 실습은 SQLite + Python(pandas, sqlglot). NL_queries.txt를 보고 mysql.py에 SQL을 쓰고 test.py로 결과 CSV를 만든다. 제출 압축 파일 이름은 반드시 학번. **SQLite는 ALL, ANY를 지원하지 않는다.**
