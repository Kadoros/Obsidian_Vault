from qdsl import Q
from sq import SQLQ
import company as C

# ───────── L4-1 SQL 소개 · DDL ─────────
Q("4-int-1","sql-intro","mc","SQL에 대한 설명으로 옳은 것은?",
  1, choices=["절차적 언어로, 데이터를 어떻게 가져올지 기술한다","선언적 언어로, 원래 이름은 SEQUEL이다","IBM이 아니라 Oracle이 처음 만들었다","DDL만 제공한다"])
Q("4-int-2","sql-intro","mc","다음 중 DML 명령이 '아닌' 것은?",
  2, choices=["SELECT","INSERT","ALTER TABLE","UPDATE"])
Q("4-int-3","sql-intro","short","NL2SQL이 무엇인지 쓰고, 어려운 점을 두 가지 이상 쓰시오.",
  "자연어 질의를 SQL 질의로 바꿔 DB에서 원하는 데이터를 가져오는 기술. 어려운 점: 자연어의 모호성, 스키마 이해와 연결(schema linking), 처음 보는 DB로의 일반화, 복잡한 질의 생성. (그래서 LLM 기반 방법도 완벽하지 않고 SQL을 이해하는 게 중요)",
  keys=["자연어 → SQL 변환","모호성","스키마 이해·연결","일반화 / 복잡한 질의"])
Q("4-int-4","sql-intro","blank","SQL에서 (a) 은 DB와 테이블에 대한 명령(CREATE, ALTER, DROP), (b) 은 투플에 대한 명령(SELECT, INSERT, DELETE, UPDATE)을 제공한다.",
  ["DDL","DML"], accept=[["DDL","데이터 정의어","data definition language"],["DML","데이터 조작어","data manipulation language"]])
Q("4-ct-1","create-table","mc","CREATE SCHEMA COMPANY AUTHORIZATION 'Jsmith'; 에서 'Jsmith'는?",
  0, choices=["스키마를 소유한 사용자(권한 식별자)","스키마 이름","DB 이름","비밀번호"])
Q("4-ct-2","create-table","ox","CREATE TABLE COMPANY.EMPLOYEE 처럼 테이블 이름 앞에 스키마 이름을 붙일 수 있다.",True)
Q("4-ct-3","create-table","calc","다음 릴레이션을 CREATE TABLE로 정의하시오. PK와 FK, NOT NULL을 지정할 것.\nPROJECT(Pname VARCHAR(15) 필수·고유, Pnumber INT 기본 키, Plocation VARCHAR(15), Dnum INT 필수, DEPARTMENT(Dnumber) 참조)",
  "CREATE TABLE PROJECT\n( Pname      VARCHAR(15)  NOT NULL,\n  Pnumber    INT          NOT NULL,\n  Plocation  VARCHAR(15),\n  Dnum       INT          NOT NULL,\n  PRIMARY KEY (Pnumber),\n  UNIQUE (Pname),\n  FOREIGN KEY (Dnum) REFERENCES DEPARTMENT(Dnumber) );",
  keys=["PRIMARY KEY (Pnumber)","UNIQUE (Pname)","FOREIGN KEY (Dnum) REFERENCES DEPARTMENT(Dnumber)","NOT NULL"])
Q("4-ct-4","create-table","calc","WORKS_ON(Essn CHAR(9), Pno INT, Hours DECIMAL(3,1))을 CREATE TABLE로 정의하시오. PK는 (Essn, Pno), Essn은 EMPLOYEE(Ssn), Pno는 PROJECT(Pnumber)를 참조한다.",
  "CREATE TABLE WORKS_ON\n( Essn   CHAR(9)       NOT NULL,\n  Pno    INT           NOT NULL,\n  Hours  DECIMAL(3,1),\n  PRIMARY KEY (Essn, Pno),\n  FOREIGN KEY (Essn) REFERENCES EMPLOYEE(Ssn),\n  FOREIGN KEY (Pno)  REFERENCES PROJECT(Pnumber) );",
  keys=["복합 PK (Essn, Pno)","FK 두 개","PK 속성 NOT NULL (생략해도 암묵적)"])
Q("4-ac-1","attr-constraints","mc","PK 속성에 대한 설명으로 옳은 것은?",
  1, choices=["NULL을 허용한다","NOT NULL이 암묵적으로 적용된다","DEFAULT가 반드시 필요하다","UNIQUE를 따로 써야 한다"])
Q("4-ac-2","attr-constraints","ox","DEFAULT 값은 INSERT에서 그 속성 값을 명시하지 않았을 때 새 투플에 들어간다.",True)
Q("4-ac-3","attr-constraints","blank","새 사원의 기본 부서를 1로 하려면 Dno INT NOT NULL (a) 1 이라고 쓴다. PK 속성에는 (b) 이 암묵적으로 적용된다.",
  ["DEFAULT","NOT NULL"], accept=[["DEFAULT","default"],["NOT NULL","not null","notnull"]])
Q("4-ac-4","attr-constraints","short","NOT NULL과 DEFAULT 제약을 각각 설명하고, 둘의 관계가 INSERT에 어떤 영향을 주는지 쓰시오.",
  "NOT NULL: 그 속성 값은 NULL일 수 없음(PK에는 암묵적). DEFAULT <값>: 값을 명시하지 않으면 기본값이 들어감. 속성 이름을 명시하는 INSERT에서는 NOT NULL이면서 DEFAULT가 없는 속성은 반드시 값을 줘야 한다 (DEFAULT가 있으면 생략 가능).",
  keys=["NOT NULL 정의","DEFAULT 정의","NOT NULL + DEFAULT 없음 → INSERT에 반드시 포함"])
Q("4-kc-1","key-clauses","mc","CREATE TABLE에서 후보 키(대체 키)를 지정하는 절은?",
  2, choices=["PRIMARY KEY","FOREIGN KEY","UNIQUE","CHECK"])
Q("4-kc-2","key-clauses","mc","참조되는 PK가 삭제·갱신되어 참조 무결성이 깨질 때 SQL의 기본 동작은?",
  0, choices=["그 연산을 거부(reject)","FK를 NULL로","참조하는 투플도 삭제","FK를 기본값으로"])
Q("4-kc-3","key-clauses","ox","CONSTRAINT DEPTPK PRIMARY KEY (Dnumber) 처럼 제약에 이름을 붙이면 나중에 ALTER TABLE ... DROP CONSTRAINT로 지울 수 있다.",True)
Q("4-kc-4","key-clauses","calc","DEPARTMENT를 CREATE TABLE로 정의하시오: Dname VARCHAR(15) 필수·고유, Dnumber INT 기본 키, Mgr_ssn CHAR(9) 필수, EMPLOYEE(Ssn) 참조, Mgr_start_date DATE. 제약마다 이름(DEPTPK, DEPTSK, DEPTMGRFK)을 붙일 것.",
  "CREATE TABLE DEPARTMENT\n( Dname           VARCHAR(15)  NOT NULL,\n  Dnumber         INT          NOT NULL,\n  Mgr_ssn         CHAR(9)      NOT NULL,\n  Mgr_start_date  DATE,\n  CONSTRAINT DEPTPK    PRIMARY KEY (Dnumber),\n  CONSTRAINT DEPTSK    UNIQUE (Dname),\n  CONSTRAINT DEPTMGRFK FOREIGN KEY (Mgr_ssn) REFERENCES EMPLOYEE(Ssn) );",
  keys=["CONSTRAINT 이름 PRIMARY KEY","UNIQUE (Dname)","FOREIGN KEY ... REFERENCES EMPLOYEE(Ssn)"])

# ───────── L4-2 참조 트리거 동작 · DROP · ALTER ─────────
Q("4-ra-1","ref-actions","mc","EMPSUPERFK FOREIGN KEY (Super_ssn) REFERENCES EMPLOYEE(Ssn) ON DELETE SET NULL 일 때, 상사 Wong이 삭제되면?",
  1, choices=["Wong의 부하들도 삭제","Wong의 부하들의 Super_ssn이 NULL로","삭제가 거부됨","Super_ssn이 기본값으로"])
Q("4-ra-2","ref-actions","mc","ON UPDATE CASCADE의 동작은?",
  2, choices=["참조하는 투플을 삭제","참조하는 FK를 NULL로","참조하는 FK를 새 PK 값으로 바꿈","갱신을 거부"])
Q("4-ra-3","ref-actions","ox","ON DELETE CASCADE는 참조되던 투플이 삭제되면 그것을 참조하던 투플도 삭제한다.",True)
Q("4-ra-4","ref-actions","calc","EMPSUPERFK를 ON DELETE CASCADE로 바꾼 뒤(다른 FK는 고려하지 않음) COMPANY 상태에서\nDELETE FROM EMPLOYEE WHERE Lname = 'Borg';\n를 실행하면 EMPLOYEE에서 어떤 투플들이 어떤 순서로 삭제되는지 쓰시오.",
  "1) Borg(888665555) 삭제\n2) Super_ssn = 888665555인 Wong(333445555), Wallace(987654321) 연쇄 삭제\n3) Super_ssn = 333445555인 Smith, Narayan, English와 Super_ssn = 987654321인 Zelaya, Jabbar 연쇄 삭제\n→ EMPLOYEE 8개 투플 전부 삭제 (CASCADE는 재귀적으로 전파)",
  keys=["Borg → Wong, Wallace","→ Smith, Narayan, English, Zelaya, Jabbar","결국 8개 전부 (재귀 전파)"],
  explain="실제 COMPANY에서는 WORKS_ON.Essn 등이 기본 동작(거부)이면 이 DELETE 자체가 거부된다.")
Q("4-ra-5","ref-actions","short","LIBRARY DB에서 BOOK_LOANS.Card_no → BORROWER.Card_no의 ON DELETE, ON UPDATE 동작을 고르고 이유를 쓰시오.",
  "ON DELETE REJECT: 도서관은 보통 회원이 대출한 책을 다 반납(또는 변상)하기 전엔 탈퇴를 허용하지 않으므로, 대출 기록이 있는 회원 삭제를 거부. ON UPDATE CASCADE: 회원 카드 번호가 바뀌면 대출 기록도 따라 바꿔야 누가 빌렸는지 추적할 수 있음.",
  keys=["ON DELETE REJECT + 이유","ON UPDATE CASCADE + 이유"])
Q("4-ra-6","ref-actions","short","LIBRARY DB에서 BOOK_COPIES.Branch_id → LIBRARY_BRANCH.Branch_id에 ON DELETE CASCADE가 적절한 이유를 쓰시오.",
  "LIBRARY_BRANCH 투플 삭제는 실제로 그 지점이 문을 닫는 것을 뜻하므로, 그 지점의 책 사본들을 더 이상 추적할 필요가 없다. 따라서 참조하는 BOOK_COPIES 투플도 함께 삭제하는 CASCADE가 맞다.",
  keys=["지점 삭제 = 폐점","사본 추적 불필요 → 함께 삭제"])
Q("4-ra-7","ref-actions","blank","참조 트리거 동작에서 트리거는 ON DELETE와 ON (a), 동작은 SET NULL, (b), SET DEFAULT이다.",
  ["UPDATE","CASCADE"], accept=[["UPDATE","update"],["CASCADE","cascade"]])
Q("4-ra-8","ref-actions","mc","EMPDEPTFK FOREIGN KEY (Dno) REFERENCES DEPARTMENT(Dnumber) ON DELETE SET DEFAULT 이고 Dno의 DEFAULT가 1일 때, 4번 부서가 삭제되면?",
  3, choices=["4번 부서 사원들도 삭제","4번 부서 사원들의 Dno가 NULL","삭제 거부","4번 부서 사원들의 Dno가 1로"])
Q("4-dr-1","drop","mc","DROP SCHEMA COMPANY RESTRICT; 의 동작은?",
  1, choices=["스키마의 모든 요소까지 삭제","스키마에 요소가 하나도 없을 때만 삭제","테이블만 삭제","항상 거부"])
Q("4-dr-2","drop","short","DROP TABLE EMPLOYEE와 DELETE FROM EMPLOYEE의 차이를 쓰시오.",
  "DROP TABLE은 모든 투플과 함께 카탈로그의 테이블 정의까지 제거한다(테이블이 없어짐). DELETE FROM은 투플만 지우고 테이블 정의는 남긴다.",
  keys=["DROP TABLE = 투플 + 정의 제거","DELETE = 투플만, 정의는 남음"])
Q("4-dr-3","drop","ox","DROP TABLE ... CASCADE는 그 테이블을 참조하는 제약과 요소도 자동으로 삭제한다.",True)
Q("4-alt-1","alter","mc","EMPLOYEE에 새 열 Job을 추가하는 명령은?",
  0, choices=["ALTER TABLE COMPANY.EMPLOYEE ADD COLUMN Job VARCHAR(12);","UPDATE EMPLOYEE ADD Job VARCHAR(12);","INSERT INTO EMPLOYEE (Job) VALUES ('');","CREATE COLUMN Job ON EMPLOYEE;"])
Q("4-alt-2","alter","mc","ALTER TABLE COMPANY.EMPLOYEE DROP COLUMN Address RESTRICT; 의 동작은?",
  2, choices=["Address를 참조하는 제약도 같이 삭제","항상 삭제","Address를 참조하는 스키마 요소가 없을 때만 삭제","Address 값을 NULL로"])
Q("4-alt-3","alter","ox","ALTER TABLE ... DROP CONSTRAINT EMPSUPERFK CASCADE; 로 이름 붙인 제약을 지울 수 있다.",True)
Q("4-alt-4","alter","short","ALTER TABLE로 할 수 있는 일을 세 가지 쓰시오.",
  "속성(열) 추가·삭제, 제약조건 추가·삭제, 열 정의(데이터 타입이나 제약) 변경.",
  keys=["열 추가·삭제","제약 추가·삭제","열 정의 변경"])

# ───────── L4-3 INSERT · DELETE · UPDATE ─────────
Q("4-ins-1","dml-insert","mc","INSERT INTO EMPLOYEE (Fname, Lname, Dno) VALUES ('Robert', 'Hatcher', 5); 가 거부되는 이유는?",
  1, choices=["5번 부서가 없어서","Ssn(PK, NOT NULL) 값이 없어서","Fname이 중복이라서","속성 순서가 틀려서"])
Q("4-ins-2","dml-insert","mc","INSERT INTO EMPLOYEE (Fname, Lname, Ssn, Dno) VALUES ('Robert', 'Hatcher', '980760540', 2); 가 거부되는 이유는? (COMPANY 상태)",
  2, choices=["키 제약","NOT NULL","참조 무결성 (2번 부서 없음)","위반 없음"])
Q("4-ins-3","dml-insert","ox","속성 이름을 명시하지 않는 INSERT에서는 값을 테이블 정의의 속성 순서대로 모두 나열해야 한다.",True)
Q("4-ins-4","dml-insert","calc","COMPANY에 새 프로젝트 'ProductW'(번호 40, 위치 'Houston', 5번 부서 통제)를 추가하고, Smith(123456789)가 이 프로젝트에 주 5시간 일한다는 사실을 추가하는 SQL을 쓰시오.",
  "INSERT INTO PROJECT VALUES ('ProductW', 40, 'Houston', 5);\nINSERT INTO WORKS_ON (Essn, Pno, Hours) VALUES ('123456789', 40, 5.0);\n(WORKS_ON은 PROJECT 40이 먼저 있어야 참조 무결성을 만족하므로 순서가 중요)",
  keys=["PROJECT INSERT","WORKS_ON INSERT","PROJECT를 먼저 (참조 무결성)"])
Q("4-ins-5","dml-insert","blank","속성 이름을 명시하는 INSERT에서는 (a) 이면서 (b) 이 없는 속성의 값은 반드시 포함해야 한다.",
  ["NOT NULL","DEFAULT"], accept=[["NOT NULL","not null","널 불가"],["DEFAULT","default","기본값"]])
Q("4-del-1","dml-delete-update","mc","COMPANY 상태에서 DELETE FROM EMPLOYEE WHERE Dno = 5; 로 삭제되는 투플 수는? (참조 제약은 무시)",
  2, choices=["0","1","4","8"])
Q("4-del-2","dml-delete-update","ox","DELETE FROM EMPLOYEE; 는 EMPLOYEE 테이블 정의까지 없앤다.",False,
  explain="투플만 전부 지워지고 정의는 남는다. 정의까지 지우는 건 DROP TABLE.")
Q("4-del-3","dml-delete-update","mc","DELETE 명령에 대한 설명으로 옳은 것은?",
  1, choices=["한 명령으로 여러 테이블에서 명시적으로 삭제할 수 있다","한 번에 한 테이블에서만 명시적으로 삭제하지만, CASCADE로 다른 테이블에 전파될 수 있다","WHERE가 없으면 아무것도 지우지 않는다","PK 값으로만 지울 수 있다"])
Q("4-del-4","dml-delete-update","calc","5번 부서 사원 전원의 급여를 10% 올리는 SQL을 쓰고, COMPANY 상태에서 바뀌는 사원과 새 급여를 쓰시오.",
  "UPDATE EMPLOYEE\nSET    Salary = Salary * 1.1\nWHERE  Dno = 5;\n\nSmith 30000 → 33000, Wong 40000 → 44000, Narayan 38000 → 41800, English 25000 → 27500 (4개 투플)",
  keys=["UPDATE ... SET Salary = Salary * 1.1","WHERE Dno = 5","4명과 새 급여"])
Q("4-del-5","dml-delete-update","calc","프로젝트 10번의 위치를 'Bellaire'로, 통제 부서를 5번으로 바꾸는 SQL을 쓰시오.",
  "UPDATE PROJECT\nSET    Plocation = 'Bellaire', Dnum = 5\nWHERE  Pnumber = 10;",
  keys=["UPDATE PROJECT","SET 두 속성 (쉼표로)","WHERE Pnumber = 10"])
Q("4-del-6","dml-delete-update","short","UPDATE 문에서 WHERE와 SET의 역할을 쓰고, UPDATE가 다른 테이블에 영향을 줄 수 있는 경우를 쓰시오.",
  "WHERE: 한 릴레이션에서 수정할 투플을 고름. SET: 수정할 속성과 새 값 지정. PK 값을 바꿀 때 FK에 ON UPDATE CASCADE가 지정돼 있으면 참조하는 다른 테이블의 투플도 바뀐다.",
  keys=["WHERE = 투플 선택","SET = 속성과 새 값","ON UPDATE CASCADE로 전파"])

# ───────── L4-4 SELECT-FROM-WHERE ─────────
SCH = C.COMPANY_SCHEMA
Q("4-sfw-1","sfw","mc","SELECT Fname, Lname, Address FROM EMPLOYEE, DEPARTMENT WHERE Dname = 'Research' AND Dnumber = Dno; 에서 Dnumber = Dno는?",
  1, choices=["선택 조건","조인 조건","투영 속성","정렬 조건"])
Q("4-sfw-2","sfw","blank","SELECT 절의 속성은 (a) 속성이고, WHERE 절에는 선택 조건과 (b) 조건이 들어간다.",
  ["투영","조인"], accept=[["투영","projection","프로젝션"],["조인","join"]])
SQLQ("4-sfw-3","sfw","'John B. Smith'의 생일과 주소를 검색하시오.",
  "SELECT Bdate, Address\nFROM   EMPLOYEE\nWHERE  Fname = 'John' AND Minit = 'B' AND Lname = 'Smith';", expect=1,
  keys=["SELECT Bdate, Address","세 이름 조건 AND"])
SQLQ("4-sfw-4","sfw","'Research' 부서에서 일하는 모든 사원의 이름(Fname, Lname)과 주소를 검색하시오.",
  "SELECT Fname, Lname, Address\nFROM   EMPLOYEE, DEPARTMENT\nWHERE  Dname = 'Research' AND Dnumber = Dno;", expect=4,
  keys=["EMPLOYEE, DEPARTMENT","선택 조건 Dname = 'Research'","조인 조건 Dnumber = Dno"])
SQLQ("4-sfw-5","sfw","5번 부서에서 일하고 'ProductX' 프로젝트에서 주 10시간 넘게 일하는 사원의 이름을 검색하시오. (교안 연습 2)",
  "SELECT E.Fname, E.Minit, E.Lname\nFROM   EMPLOYEE AS E, PROJECT AS P, WORKS_ON AS W\nWHERE  E.Dno = 5 AND P.Pname = 'ProductX' AND W.Hours > 10\n  AND  E.Ssn = W.Essn AND W.Pno = P.Pnumber;", expect=2,
  keys=["세 테이블","선택 조건 3개 (Dno=5, Pname, Hours>10)","조인 조건 2개 (Ssn=Essn, Pno=Pnumber)"],
  note="교안 풀이의 마지막 조인 조건은 E.Dno = P.Dnum으로 적혀 있지만, 사원이 그 프로젝트에서 일하는지를 잇는 조건은 W.Pno = P.Pnumber가 맞다.")
SQLQ("4-sfw-6","sfw","'Stafford'에 있는 모든 프로젝트에 대해 프로젝트 번호, 통제 부서 번호, 부서 관리자의 성, 주소, 생일을 검색하시오.",
  "SELECT P.Pnumber, P.Dnum, E.Lname, E.Address, E.Bdate\nFROM   PROJECT AS P, DEPARTMENT AS D, EMPLOYEE AS E\nWHERE  P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn\n  AND  P.Plocation = 'Stafford';", expect=2,
  keys=["조인 P.Dnum = D.Dnumber","조인 D.Mgr_ssn = E.Ssn","선택 Plocation = 'Stafford'"])
SQLQ("4-sfw-7","sfw","Houston에 사는 사원 중 급여가 30000 이상인 사원의 이름과 급여를 검색하시오. (Address에 'Houston'이 들어 있으면 Houston에 사는 것으로 본다)",
  "SELECT Fname, Lname, Salary\nFROM   EMPLOYEE\nWHERE  Address LIKE '%Houston%' AND Salary >= 30000;", expect=3,
  keys=["LIKE '%Houston%'","Salary >= 30000"])
SQLQ("4-sfw-8","sfw","'Administration' 부서가 통제하는 프로젝트의 이름과 위치를 검색하시오.",
  "SELECT P.Pname, P.Plocation\nFROM   PROJECT AS P, DEPARTMENT AS D\nWHERE  P.Dnum = D.Dnumber AND D.Dname = 'Administration';", expect=2,
  keys=["조인 Dnum = Dnumber","선택 Dname = 'Administration'"])
Q("4-qa-1","qualify-alias","mc","같은 릴레이션을 한 질의에서 두 역할(사원, 상사)로 참조하려면?",
  2, choices=["DISTINCT를 쓴다","테이블을 두 번 만든다","별칭(투플 변수)을 두 개 쓴다","UNION을 쓴다"])
Q("4-qa-2","qualify-alias","ox","SELECT E.Fname, E.Lname, E.Fname, E.Lname FROM EMPLOYEE AS E WHERE E.Super_ssn = E.Ssn; 은 사원과 그 상사의 이름을 검색한다.",False,
  explain="별칭이 하나라 '자기 자신이 자기 상사'인 사원을 찾는 질의가 된다(0행). 상사용 별칭 S가 따로 필요.")
SQLQ("4-qa-3","qualify-alias","각 사원의 이름(Fname, Lname)과 그 사원의 직속 상사의 이름(Fname, Lname)을 검색하시오.",
  "SELECT E.Fname, E.Lname, S.Fname, S.Lname\nFROM   EMPLOYEE AS E, EMPLOYEE AS S\nWHERE  E.Super_ssn = S.Ssn;", expect=7,
  keys=["EMPLOYEE 별칭 두 개 (E, S)","E.Super_ssn = S.Ssn","E.이름, S.이름"], note="상사가 없는(Super_ssn NULL) Borg는 결과에 없다.")
Q("4-qa-4","qualify-alias","short","SQL에서 속성 이름에 릴레이션 이름을 붙여야(qualify) 하는 두 가지 경우를 쓰시오.",
  "1) 서로 다른 릴레이션에 같은 이름의 속성이 있을 때 (예: EMPLOYEE.Name과 DEPARTMENT.Name). 2) 같은 릴레이션을 한 질의에서 두 번 이상 참조할 때 → 별칭으로 구별 (EMPLOYEE AS E, EMPLOYEE AS S).",
  keys=["다른 릴레이션의 같은 이름 속성","같은 릴레이션을 두 번 참조 (별칭)"])
SQLQ("4-qa-5","qualify-alias","직속 상사와 다른 부서에서 일하는 사원의 성과 부서 번호, 그 상사의 성과 부서 번호를 검색하시오.",
  "SELECT E.Lname, E.Dno, S.Lname, S.Dno\nFROM   EMPLOYEE AS E, EMPLOYEE AS S\nWHERE  E.Super_ssn = S.Ssn AND E.Dno <> S.Dno;", expect=2,
  keys=["별칭 E, S","E.Super_ssn = S.Ssn","E.Dno <> S.Dno"])
Q("4-mw-1","missing-where-star","mc","SELECT Ssn, Dname FROM EMPLOYEE, DEPARTMENT; 의 결과 행 수는? (COMPANY 상태)",
  3, choices=["3","8","11","24"])
Q("4-mw-2","missing-where-star","ox","FROM에 테이블이 둘 이상인데 조인 조건을 빠뜨리면 카티션 곱이 나와 결과가 틀리고 매우 커진다.",True)
SQLQ("4-mw-3","missing-where-star","5번 부서에서 일하는 사원의 모든 속성을 검색하시오.",
  "SELECT *\nFROM   EMPLOYEE\nWHERE  Dno = 5;", expect=4, keys=["SELECT *","WHERE Dno = 5"])
Q("4-mw-4","missing-where-star","short","SELECT 질의에서 WHERE 절을 생략하면 어떻게 되는지, FROM에 테이블이 하나일 때와 둘일 때로 나눠 쓰시오.",
  "투플 선택 조건이 없으므로 FROM에 있는 릴레이션의 투플을 모두 검색한다. 테이블이 하나면 그 테이블의 모든 투플, 둘 이상이면 가능한 모든 투플 조합(카티션 곱, 예: 8 × 3 = 24행)이 나온다.",
  keys=["조건 없음 → 모든 투플","둘 이상이면 카티션 곱"])

# ───────── L4-5 다중집합 · 집합 연산 · ORDER BY ─────────
Q("4-ms-1","multiset-distinct","mc","SQL이 질의 결과에서 중복 투플을 자동으로 제거하지 않는 이유가 '아닌' 것은?",
  3, choices=["중복 제거는 비싼 연산이라서","사용자가 중복을 보고 싶을 때가 있어서","집계 함수에 중복이 필요해서","SQL 테이블은 집합이라 중복이 원래 없어서"])
Q("4-ms-2","multiset-distinct","mc","COMPANY 상태에서 SELECT DISTINCT Salary FROM EMPLOYEE; 의 결과 행 수는?",
  1, choices=["5","6","7","8"])
Q("4-ms-3","multiset-distinct","ox","SQL은 테이블을 집합이 아니라 다중집합으로 취급한다.",True)
Q("4-ms-4","multiset-distinct","short","SQL이 테이블을 다중집합으로 다루는 이유를 세 가지 쓰시오.",
  "1) 중복 제거는 비싼 연산이다 (투플을 정렬한 뒤 중복을 지워야 함). 2) 사용자가 결과에서 중복 투플을 보고 싶을 때가 있다. 3) 집계 함수를 적용할 때 중복이 필요하다 (예: 급여 합·평균).",
  keys=["중복 제거 비용","사용자가 중복을 원할 수 있음","집계 함수"])
SQLQ("4-ms-5","multiset-distinct","사원들이 일하는 프로젝트 번호를 중복 없이 검색하시오.",
  "SELECT DISTINCT Pno\nFROM   WORKS_ON;", expect=6, keys=["DISTINCT","WORKS_ON"])
Q("4-ms-6","multiset-distinct","blank","SELECT (a) Salary 는 중복을 유지하고(기본), SELECT (b) Salary 는 중복을 제거한다.",
  ["ALL","DISTINCT"], accept=[["ALL","all"],["DISTINCT","distinct"]])
Q("4-so-1","set-ops","mc","UNION, EXCEPT, INTERSECT의 결과에 대한 설명으로 옳은 것은?",
  0, choices=["중복이 제거된 집합","항상 중복이 유지된 다중집합","정렬된 리스트","타입 호환이 아니어도 된다"])
Q("4-so-2","set-ops","calc","R(A) = {a1, a2, a2, a3}, S(A) = {a1, a2, a4, a5}일 때 다음 결과를 쓰시오.\n(1) R UNION ALL S  (2) R EXCEPT ALL S  (3) R INTERSECT ALL S  (4) R UNION S  (5) R EXCEPT S",
  "(1) {a1, a1, a2, a2, a2, a3, a4, a5}\n(2) {a2, a3}\n(3) {a1, a2}\n(4) {a1, a2, a3, a4, a5}\n(5) {a3}",
  keys=["(1) 8개 다중집합","(2) {a2, a3}","(3) {a1, a2}","(4) 중복 제거 합집합","(5) {a3}"])
SQLQ("4-so-3","set-ops","성이 'Smith'인 사원이 일꾼으로 일하거나, 그 프로젝트를 통제하는 부서의 관리자인 프로젝트의 번호를 UNION으로 검색하시오.",
  "( SELECT DISTINCT Pnumber\n  FROM   PROJECT, DEPARTMENT, EMPLOYEE\n  WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )\nUNION\n( SELECT DISTINCT Pnumber\n  FROM   PROJECT, WORKS_ON, EMPLOYEE\n  WHERE  Pnumber = Pno AND Essn = Ssn AND Lname = 'Smith' );",
  check="SELECT Pnumber FROM PROJECT, DEPARTMENT, EMPLOYEE WHERE Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' UNION SELECT Pnumber FROM PROJECT, WORKS_ON, EMPLOYEE WHERE Pnumber = Pno AND Essn = Ssn AND Lname = 'Smith'",
  expect=2, keys=["관리자 블록 (PROJECT–DEPARTMENT–EMPLOYEE)","일꾼 블록 (PROJECT–WORKS_ON–EMPLOYEE)","UNION"])
SQLQ("4-so-4","set-ops","프로젝트에서 일하기는 하지만 부양가족은 없는 사원의 Ssn을 EXCEPT로 검색하시오.",
  "( SELECT Essn FROM WORKS_ON )\nEXCEPT\n( SELECT Essn FROM DEPENDENT );",
  check="SELECT Essn FROM WORKS_ON EXCEPT SELECT Essn FROM DEPENDENT", expect=5,
  keys=["WORKS_ON.Essn","EXCEPT","DEPENDENT.Essn"])
Q("4-so-5","set-ops","ox","SELECT Ssn FROM EMPLOYEE UNION SELECT Dname FROM DEPARTMENT; 는 타입 호환이 아니라서 의미상 잘못된 질의이다.",True,
  explain="대응 속성의 도메인이 다르다 (사원 번호 vs 부서 이름).")
SQLQ("4-ob-1","order-arith","사원과 그가 일하는 프로젝트 목록을 부서 이름 순, 같은 부서 안에서는 성·이름 순으로 정렬해 검색하시오 (부서 이름, 성, 이름, 프로젝트 이름).",
  "SELECT   D.Dname, E.Lname, E.Fname, P.Pname\nFROM     DEPARTMENT AS D, EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P\nWHERE    D.Dnumber = E.Dno AND E.Ssn = W.Essn AND W.Pno = P.Pnumber\nORDER BY D.Dname, E.Lname, E.Fname;", expect=16,
  keys=["네 테이블 조인 조건 3개","ORDER BY D.Dname, E.Lname, E.Fname"])
SQLQ("4-ob-2","order-arith","'ProductX'에서 일하는 사원 모두에게 10% 인상을 해주면 급여가 얼마가 되는지 이름과 함께 보이시오 (릴레이션은 바꾸지 말 것).",
  "SELECT E.Fname, E.Lname, 1.1 * E.Salary AS Increased_sal\nFROM   EMPLOYEE AS E, WORKS_ON AS W, PROJECT AS P\nWHERE  E.Ssn = W.Essn AND W.Pno = P.Pnumber AND P.Pname = 'ProductX';", expect=2,
  keys=["1.1 * Salary (AS 별칭)","조인 조건 2개 + Pname 조건","UPDATE가 아니라 SELECT"])
SQLQ("4-ob-3","order-arith","5번 부서에서 급여가 30000 이상 40000 이하인 사원을 BETWEEN으로 검색하시오.",
  "SELECT *\nFROM   EMPLOYEE\nWHERE  (Salary BETWEEN 30000 AND 40000) AND Dno = 5;", expect=3,
  keys=["BETWEEN 30000 AND 40000 (양 끝 포함)","AND Dno = 5"])
Q("4-ob-4","order-arith","mc","ORDER BY의 기본 정렬 순서는?",
  0, choices=["오름차순 (ASC)","내림차순 (DESC)","삽입 순서","PK 순서"])
Q("4-ob-5","order-arith","ox","SELECT 절에서 1.1 * Salary를 쓰면 EMPLOYEE 릴레이션의 Salary 값도 바뀐다.",False,
  explain="결과에만 반영되고 릴레이션 상태는 그대로. 바꾸려면 UPDATE.")
SQLQ("4-ob-6","order-arith","급여가 가장 높은 사원부터 차례로 이름과 급여를 검색하시오. 급여가 같으면 성의 알파벳 순.",
  "SELECT   Fname, Lname, Salary\nFROM     EMPLOYEE\nORDER BY Salary DESC, Lname ASC;", expect=8,
  keys=["ORDER BY Salary DESC","두 번째 기준 Lname ASC"])
