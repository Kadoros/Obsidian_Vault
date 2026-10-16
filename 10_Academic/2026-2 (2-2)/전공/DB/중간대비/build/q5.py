from qdsl import Q
from sq import SQLQ
import company as C

# ───────── L5-1 중첩 질의 ─────────
Q("5-in-1","nested-in","mc","중첩 질의(nested query)에 대한 설명으로 옳은 것은?",
  1, choices=["FROM 절에만 올 수 있다","다른 질의의 WHERE 절 안에 들어간 완전한 SELECT-FROM-WHERE 블록이다","결과는 항상 값 하나다","SQL에서는 지원하지 않는다"])
Q("5-in-2","nested-in","mc","v IN V 가 TRUE가 되는 경우는?",
  0, choices=["v가 V의 원소 중 하나일 때","v가 V의 모든 원소와 같을 때","V가 비어 있을 때","v가 V의 최댓값보다 클 때"])
Q("5-in-3","nested-in","ox","= ANY는 IN과 같은 뜻이다.",True)
SQLQ("5-in-4","nested-in","'Research' 부서에서 일하는 사원의 이름을 중첩 질의(IN)로 검색하시오.",
  "SELECT Fname, Lname\nFROM   EMPLOYEE\nWHERE  Dno IN ( SELECT Dnumber\n               FROM   DEPARTMENT\n               WHERE  Dname = 'Research' );", expect=4,
  keys=["바깥 EMPLOYEE","Dno IN (안쪽 질의)","안쪽: Dname = 'Research'인 Dnumber"])
SQLQ("5-in-5","nested-in","성이 'Smith'인 사원이 일꾼으로 일하거나 관리자로 있는 부서가 통제하는 프로젝트의 번호를 IN 두 개와 OR로 검색하시오.",
  "SELECT DISTINCT Pnumber\nFROM   PROJECT\nWHERE  Pnumber IN ( SELECT Pnumber\n                    FROM   PROJECT, DEPARTMENT, EMPLOYEE\n                    WHERE  Dnum = Dnumber AND Mgr_ssn = Ssn AND Lname = 'Smith' )\n   OR  Pnumber IN ( SELECT Pno\n                    FROM   WORKS_ON, EMPLOYEE\n                    WHERE  Essn = Ssn AND Lname = 'Smith' );", expect=2,
  keys=["IN (관리자 블록)","OR","IN (일꾼 블록)"])
SQLQ("5-in-6","nested-in","'Houston'에 위치한 프로젝트 중 하나라도 일하는 사원의 Ssn과 이름을 중첩 질의로 검색하시오.",
  "SELECT Ssn, Fname, Lname\nFROM   EMPLOYEE\nWHERE  Ssn IN ( SELECT W.Essn\n                FROM   WORKS_ON AS W, PROJECT AS P\n                WHERE  W.Pno = P.Pnumber AND P.Plocation = 'Houston' );", expect=4,
  keys=["Ssn IN (안쪽)","안쪽: WORKS_ON–PROJECT 조인","Plocation = 'Houston'"])
SQLQ("5-in-7","nested-in","급여가 가장 높은 사원이 일하는 부서의 모든 사원 이름을 검색하시오. (db-exercises Q1)",
  "SELECT Fname, Minit, Lname\nFROM   EMPLOYEE\nWHERE  Dno = ( SELECT Dno\n               FROM   EMPLOYEE\n               WHERE  Salary = ( SELECT MAX(Salary)\n                                 FROM   EMPLOYEE ) );", expect=1,
  keys=["가장 안쪽: MAX(Salary)","그 급여를 받는 사원의 Dno","그 Dno의 사원들"])
SQLQ("5-in-8","nested-in","상사의 상사의 Ssn이 '888665555'인 사원의 이름을 검색하시오. (db-exercises Q2)",
  "SELECT Fname, Minit, Lname\nFROM   EMPLOYEE\nWHERE  Super_ssn IN ( SELECT Ssn\n                      FROM   EMPLOYEE\n                      WHERE  Super_ssn = '888665555' );", expect=5,
  keys=["안쪽: Super_ssn = '888665555'인 사원들 (Wong, Wallace)","바깥: 그들을 상사로 둔 사원"],
  note="교안 풀이는 = 로 썼지만 안쪽 결과가 두 명(Wong, Wallace)이라 IN이 맞다.")
Q("5-aa-1","all-any","mc","Salary > ALL (SELECT Salary FROM EMPLOYEE WHERE Dno = 5) 와 같은 뜻인 조건은?",
  2, choices=["Salary > (SELECT MIN(Salary) FROM EMPLOYEE WHERE Dno = 5)","Salary > (SELECT AVG(Salary) FROM EMPLOYEE WHERE Dno = 5)","Salary > (SELECT MAX(Salary) FROM EMPLOYEE WHERE Dno = 5)","Salary IN (SELECT Salary FROM EMPLOYEE WHERE Dno = 5)"])
Q("5-aa-2","all-any","mc","Salary > ANY (SELECT Salary FROM EMPLOYEE WHERE Dno = 5) 가 참이 되는 조건은? (5번 부서 급여 = 30000, 40000, 38000, 25000)",
  0, choices=["Salary > 25000","Salary > 40000","Salary > 33250","Salary = 30000"])
SQLQ("5-aa-3","all-any","5번 부서 모든 사원보다 급여가 많은 사원의 이름을 ALL로 검색하시오.",
  "SELECT Lname, Fname\nFROM   EMPLOYEE\nWHERE  Salary > ALL ( SELECT Salary\n                      FROM   EMPLOYEE\n                      WHERE  Dno = 5 );",
  check="SELECT Lname, Fname FROM EMPLOYEE WHERE Salary > (SELECT MAX(Salary) FROM EMPLOYEE WHERE Dno = 5)", expect=2,
  keys=["Salary > ALL","안쪽: Dno = 5인 급여"], note="SQLite에는 ALL이 없어서 검산은 > (SELECT MAX(...))로 돌렸다.")
Q("5-aa-4","all-any","ox","실습 환경의 SQLite는 ALL과 ANY를 지원하지 않는다.",True)
SQLQ("5-aa-5","all-any","4번 부서의 어떤 사원보다라도 급여가 많은 5번 부서 사원의 이름과 급여를 ANY로 검색하시오.",
  "SELECT Fname, Lname, Salary\nFROM   EMPLOYEE\nWHERE  Dno = 5\n  AND  Salary > ANY ( SELECT Salary FROM EMPLOYEE WHERE Dno = 4 );",
  check="SELECT Fname, Lname, Salary FROM EMPLOYEE WHERE Dno = 5 AND Salary > (SELECT MIN(Salary) FROM EMPLOYEE WHERE Dno = 4)", expect=3,
  keys=["Dno = 5","Salary > ANY (4번 부서 급여)"], note="> ANY = 최솟값(25000)보다 크면 참. SQLite 검산은 > (SELECT MIN(...)).")
Q("5-aa-6","all-any","blank","v > ALL V 는 v가 V의 (a) 보다 클 때, v > ANY V 는 v가 V의 (b) 보다 클 때 참이다.",
  ["최댓값","최솟값"], accept=[["최댓값","최대","max","최대값"],["최솟값","최소","min","최소값"]])
Q("5-co-1","correlated","mc","상관 중첩 질의(correlated nested query)란?",
  1, choices=["안쪽 질의가 바깥과 무관하게 한 번만 평가되는 질의","안쪽 질의가 바깥 질의의 속성(별칭)을 참조하는 질의","FROM 절에 있는 질의","UNION으로 연결된 질의"])
Q("5-co-2","correlated","ox","중첩 질의에서 안쪽에서 자격 없이 쓴 속성 이름은 가장 가까운(안쪽) FROM의 테이블 속성으로 해석된다.",True)
Q("5-co-3","correlated","short","중첩 질의에서 모호성이 생기는 경우와 해결 방법을 쓰시오.",
  "바깥 질의의 FROM과 안쪽 질의의 FROM에 같은 이름의 속성이 있으면 어느 테이블의 속성인지 모호해진다. 해결: 테이블마다 별칭(투플 변수)을 붙이고 E.Sex, D.Sex처럼 자격을 부여한다. 질의에 쓰는 모든 테이블에 별칭을 붙이는 것이 권장된다.",
  keys=["바깥·안쪽에 같은 이름 속성","별칭으로 자격 부여","모든 테이블에 별칭 권장"])
SQLQ("5-co-4","correlated","부양가족 중에 사원 자신과 이름(first name)과 성별이 같은 사람이 있는 사원의 이름을 검색하시오. (질의 16)",
  "SELECT E.Fname, E.Lname\nFROM   EMPLOYEE AS E\nWHERE  E.Ssn IN ( SELECT D.Essn\n                  FROM   DEPENDENT AS D\n                  WHERE  E.Fname = D.Dependent_name\n                    AND  E.Sex = D.Sex );", expect=0,
  keys=["안쪽이 바깥 E를 참조 (상관)","E.Fname = D.Dependent_name","E.Sex = D.Sex"], note="COMPANY 상태에는 그런 부양가족이 없어 결과는 비어 있다.")
SQLQ("5-co-5","correlated","자기 부서의 평균 급여보다 급여가 많은 사원의 이름, 부서 번호, 급여를 상관 중첩 질의로 검색하시오.",
  "SELECT E.Fname, E.Lname, E.Dno, E.Salary\nFROM   EMPLOYEE AS E\nWHERE  E.Salary > ( SELECT AVG(E2.Salary)\n                    FROM   EMPLOYEE AS E2\n                    WHERE  E2.Dno = E.Dno );", expect=3,
  keys=["별칭 두 개 (E, E2)","안쪽 E2.Dno = E.Dno (상관)","AVG와 비교"])

# ───────── L5-2 EXISTS · 나눗셈 ─────────
Q("5-ex-1","exists","mc","NOT EXISTS (Q) 가 TRUE인 경우는?",
  2, choices=["Q 결과에 투플이 하나라도 있을 때","Q 결과가 NULL을 포함할 때","Q 결과가 비어 있을 때","Q가 집계 함수를 쓸 때"])
Q("5-ex-2","exists","ox","EXISTS는 안쪽 질의 결과의 값이 무엇인지가 아니라 결과가 비었는지만 본다.",True)
SQLQ("5-ex-3","exists","부양가족이 없는 사원의 이름을 NOT EXISTS로 검색하시오. (질의 6)",
  "SELECT Fname, Lname\nFROM   EMPLOYEE\nWHERE  NOT EXISTS ( SELECT *\n                    FROM   DEPENDENT\n                    WHERE  Ssn = Essn );", expect=5,
  keys=["NOT EXISTS","안쪽: DEPENDENT WHERE Ssn = Essn (상관)"])
SQLQ("5-ex-4","exists","부양가족이 하나 이상 있는 관리자의 이름을 EXISTS로 검색하시오.",
  "SELECT Fname, Lname\nFROM   EMPLOYEE\nWHERE  EXISTS ( SELECT * FROM DEPENDENT  WHERE Ssn = Essn )\n  AND  EXISTS ( SELECT * FROM DEPARTMENT WHERE Ssn = Mgr_ssn );", expect=2,
  keys=["EXISTS (부양가족)","AND","EXISTS (관리하는 부서)"])
SQLQ("5-ex-5","exists","어떤 프로젝트에서도 일하지 않는 부서 관리자가 있다면 그 관리자의 이름을 검색하시오.",
  "SELECT E.Fname, E.Lname\nFROM   EMPLOYEE AS E\nWHERE  EXISTS ( SELECT * FROM DEPARTMENT AS D WHERE D.Mgr_ssn = E.Ssn )\n  AND  NOT EXISTS ( SELECT * FROM WORKS_ON AS W WHERE W.Essn = E.Ssn );", expect=0,
  keys=["EXISTS (관리자)","NOT EXISTS (WORKS_ON)"], note="관리자 셋(Wong, Wallace, Borg) 모두 WORKS_ON에 있다 (Borg는 Hours가 NULL인 투플). 결과 0행.")
SQLQ("5-ex-6","exists","직접 감독하는 부하가 한 명이라도 있는 사원의 이름을 EXISTS로 검색하시오.",
  "SELECT S.Fname, S.Lname\nFROM   EMPLOYEE AS S\nWHERE  EXISTS ( SELECT *\n                FROM   EMPLOYEE AS E\n                WHERE  E.Super_ssn = S.Ssn );", expect=3,
  keys=["EXISTS","E.Super_ssn = S.Ssn (별칭 둘)"])
SQLQ("5-ex-7","exists","A 학점이 하나도 없는 학생의 이름과 전공을 검색하시오. (UNIVERSITY, db-exercises Q2-2)",
  "SELECT S.Name, S.Major\nFROM   STUDENT AS S\nWHERE  NOT EXISTS ( SELECT *\n                    FROM   GRADE_REPORT AS G\n                    WHERE  G.Student_number = S.Student_number\n                      AND  G.Grade = 'A' );", db="univ", expect=1,
  keys=["NOT EXISTS","G.Student_number = S.Student_number","G.Grade = 'A'"])
SQLQ("5-ex-8","exists","모든 과목에서 A를 받은(A가 아닌 학점이 없는) 학생의 이름과 전공을 검색하시오. (UNIVERSITY, db-exercises Q2-1)",
  "SELECT S.Name, S.Major\nFROM   STUDENT AS S\nWHERE  NOT EXISTS ( SELECT *\n                    FROM   GRADE_REPORT AS G\n                    WHERE  G.Student_number = S.Student_number\n                      AND  G.Grade <> 'A' );", db="univ", expect=0,
  keys=["NOT EXISTS","G.Grade <> 'A'"], note="Brown도 B가 하나 있어서 결과는 비어 있다. (성적이 하나도 없는 학생이 있다면 그 학생도 나온다는 점 주의)")
Q("5-div-1","division-sql","mc","'5번 부서가 통제하는 모든 프로젝트에서 일하는 사원'을 찾는 SQL 패턴은?",
  3, choices=["IN","= ANY","EXISTS 하나","NOT EXISTS ((5번 부서 프로젝트) EXCEPT (그 사원의 프로젝트))"])
Q("5-div-2","division-sql","short","NOT EXISTS ((SELECT Pnumber FROM PROJECT WHERE Dnum = 5) EXCEPT (SELECT Pno FROM WORKS_ON WHERE Ssn = Essn)) 가 무엇을 확인하는지 설명하시오.",
  "첫 집합은 5번 부서가 통제하는 프로젝트 전체, 둘째는 현재 사원이 일하는 프로젝트. 차집합은 5번 부서 프로젝트 중 이 사원이 안 하는 것. 이게 비어 있으면(NOT EXISTS가 참) 사원이 5번 부서 프로젝트를 전부 하고 있다는 뜻이다.",
  keys=["첫 집합 = 5번 부서 프로젝트 전체","둘째 = 그 사원의 프로젝트","차집합이 비면 전부 수행"])
Q("5-div-3","division-sql","calc","5번 부서 프로젝트 = {1, 2, 3}이다. 사원 A는 {1, 2, 4}, B는 {1, 2, 3, 4}, C는 {3}에서 일한다. NOT EXISTS + EXCEPT 나눗셈 질의 결과에 들어가는 사원과 이유를 쓰시오.",
  "A: {1,2,3} − {1,2,4} = {3} ≠ ∅ → 탈락\nB: {1,2,3} − {1,2,3,4} = ∅ → 선택\nC: {1,2,3} − {3} = {1,2} ≠ ∅ → 탈락\n결과: B만",
  keys=["A 탈락 ({3})","B 선택 (∅)","C 탈락 ({1,2})"])
SQLQ("5-div-4","division-sql","5번 부서가 통제하는 모든 프로젝트에서 일하는 사원의 이름을 검색하시오. (교안 연습 1)",
  "SELECT Fname, Lname\nFROM   EMPLOYEE\nWHERE  NOT EXISTS ( ( SELECT Pnumber FROM PROJECT WHERE Dnum = 5 )\n                    EXCEPT\n                    ( SELECT Pno FROM WORKS_ON WHERE Ssn = Essn ) );",
  check="SELECT E.Fname, E.Lname FROM EMPLOYEE E WHERE NOT EXISTS (SELECT * FROM PROJECT P WHERE P.Dnum = 5 AND NOT EXISTS (SELECT * FROM WORKS_ON W WHERE W.Essn = E.Ssn AND W.Pno = P.Pnumber))", expect=0,
  keys=["NOT EXISTS","(5번 부서 프로젝트) EXCEPT (그 사원의 프로젝트)","안쪽 Ssn = Essn (상관)"],
  note="COMPANY 상태에서는 1, 2, 3을 모두 하는 사원이 없어서 결과가 비어 있다. NOT EXISTS 두 번 방식으로도 같은 결과.")
SQLQ("5-div-5","division-sql","'John Smith'가 일하는 모든 프로젝트에서 일하는 사원의 이름을 검색하시오 (Smith 본인 포함).",
  "SELECT E.Fname, E.Lname\nFROM   EMPLOYEE AS E\nWHERE  NOT EXISTS ( SELECT W1.Pno\n                    FROM   WORKS_ON AS W1, EMPLOYEE AS S\n                    WHERE  W1.Essn = S.Ssn AND S.Fname = 'John' AND S.Lname = 'Smith'\n                      AND  NOT EXISTS ( SELECT *\n                                        FROM   WORKS_ON AS W2\n                                        WHERE  W2.Essn = E.Ssn AND W2.Pno = W1.Pno ) );", expect=2,
  keys=["바깥 NOT EXISTS: Smith의 프로젝트 중","안쪽 NOT EXISTS: 그 사원이 안 하는 것","상관 W2.Essn = E.Ssn, W2.Pno = W1.Pno"])
SQLQ("5-div-6","division-sql","Stafford에 있는 모든 프로젝트에서 일하는 사원의 이름을 검색하시오.",
  "SELECT E.Fname, E.Lname\nFROM   EMPLOYEE AS E\nWHERE  NOT EXISTS ( SELECT *\n                    FROM   PROJECT AS P\n                    WHERE  P.Plocation = 'Stafford'\n                      AND  NOT EXISTS ( SELECT *\n                                        FROM   WORKS_ON AS W\n                                        WHERE  W.Essn = E.Ssn AND W.Pno = P.Pnumber ) );", expect=2,
  keys=["이중 NOT EXISTS","Plocation = 'Stafford'","W.Essn = E.Ssn AND W.Pno = P.Pnumber"], note="Stafford 프로젝트 = {10, 30}. 둘 다 하는 사원 = Zelaya, Jabbar.")

# ───────── L5-3 조인 테이블 ─────────
Q("5-jt-1","joined-table","mc","조인 테이블(joined table)을 쓰는 곳은?",
  1, choices=["SELECT 절","FROM 절","WHERE 절","GROUP BY 절"])
Q("5-jt-2","joined-table","ox","FROM (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber) WHERE Dname = 'Research' 는 FROM EMPLOYEE, DEPARTMENT WHERE Dname = 'Research' AND Dnumber = Dno 와 결과가 같다.",True)
SQLQ("5-jt-3","joined-table","각 프로젝트 이름과 그 프로젝트를 통제하는 부서 이름을 JOIN ... ON으로 검색하시오.",
  "SELECT P.Pname, D.Dname\nFROM   (PROJECT AS P JOIN DEPARTMENT AS D ON P.Dnum = D.Dnumber);", expect=6,
  keys=["FROM (PROJECT JOIN DEPARTMENT ON ...)","P.Dnum = D.Dnumber"])
SQLQ("5-jt-4","joined-table","'Houston'에 있는 부서 위치를 가진 부서에서 일하는 사원의 이름과 부서 이름을 JOIN으로 검색하시오.",
  "SELECT E.Fname, E.Lname, D.Dname\nFROM   ((EMPLOYEE AS E JOIN DEPARTMENT AS D ON E.Dno = D.Dnumber)\n        JOIN DEPT_LOCATIONS AS L ON D.Dnumber = L.Dnumber)\nWHERE  L.Dlocation = 'Houston';", expect=5,
  keys=["JOIN 두 번 (중첩)","E.Dno = D.Dnumber, D.Dnumber = L.Dnumber","WHERE Dlocation = 'Houston'"])
Q("5-jt-5","joined-table","short","조인 테이블을 쓰면 좋은 점을 쓰시오.",
  "조인 조건을 FROM 절에 명시해서, WHERE 절에 선택 조건과 조인 조건이 섞이는 것을 피할 수 있다. 질의 구조를 이해하기 쉬워지고 조인 조건을 빠뜨리는 실수가 줄어든다.",
  keys=["조인 조건을 FROM에 명시","WHERE에 선택·조인 조건이 섞이지 않음"])
Q("5-nj-1","natural-join-sql","mc","NATURAL JOIN의 조인 조건은?",
  2, choices=["직접 ON으로 써야 한다","PK와 FK 쌍","이름이 같은 속성 쌍마다 암묵적인 동등 조건","조건 없이 카티션 곱"])
Q("5-nj-2","natural-join-sql","short","EMPLOYEE NATURAL JOIN DEPARTMENT를 바로 쓰면 Dno와 Dnumber가 조인되지 않는 이유와 해결 방법을 쓰시오.",
  "NATURAL JOIN은 이름이 같은 속성끼리만 조인하는데 EMPLOYEE는 Dno, DEPARTMENT는 Dnumber로 이름이 다르다. 그래서 DEPARTMENT AS DEPT (Dname, Dno, Mssn, Msdate)처럼 이름을 바꿔 Dno로 맞춘 뒤 NATURAL JOIN한다.",
  keys=["이름이 달라서 안 걸림","별칭으로 속성 이름 바꾸기 (Dnumber → Dno)"])
Q("5-nj-3","natural-join-sql","ox","NATURAL JOIN 결과에서 조인 속성은 한 번만 나온다.",True)
SQLQ("5-nj-4","natural-join-sql","부서 이름과 그 부서의 위치를 NATURAL JOIN으로 검색하시오.",
  "SELECT Dname, Dlocation\nFROM   (DEPARTMENT NATURAL JOIN DEPT_LOCATIONS);", expect=5,
  keys=["DEPARTMENT NATURAL JOIN DEPT_LOCATIONS","공통 속성 Dnumber로 조인"])
Q("5-io-1","inner-outer","mc","SELECT E.Lname, S.Lname FROM EMPLOYEE AS E, EMPLOYEE AS S WHERE E.Super_ssn = S.Ssn; 결과에서 빠지는 사원은? (COMPANY 상태)",
  3, choices=["Wong","Wallace","Smith","Borg (Super_ssn이 NULL)"])
Q("5-io-2","inner-outer","mc","LEFT OUTER JOIN의 결과에 반드시 들어가는 것은?",
  0, choices=["왼쪽 테이블의 모든 투플","오른쪽 테이블의 모든 투플","양쪽 모든 투플","조건을 만족하는 쌍만"])
SQLQ("5-io-3","inner-outer","모든 사원의 성과, 상사가 있다면 상사의 성을 검색하시오 (상사가 없으면 NULL).",
  "SELECT E.Lname AS Employee_name, S.Lname AS Supervisor_name\nFROM   (EMPLOYEE AS E LEFT OUTER JOIN EMPLOYEE AS S\n        ON E.Super_ssn = S.Ssn);", expect=8,
  keys=["LEFT OUTER JOIN","ON E.Super_ssn = S.Ssn","Borg의 상사 NULL"])
SQLQ("5-io-4","inner-outer","모든 사원 이름과, 그 사원이 관리하는 부서가 있으면 그 부서 이름을 검색하시오.",
  "SELECT E.Fname, E.Lname, D.Dname\nFROM   (EMPLOYEE AS E LEFT OUTER JOIN DEPARTMENT AS D\n        ON E.Ssn = D.Mgr_ssn);", expect=8,
  keys=["EMPLOYEE LEFT OUTER JOIN DEPARTMENT","ON E.Ssn = D.Mgr_ssn"])
SQLQ("5-io-5","inner-outer","모든 프로젝트의 이름과 그 프로젝트에서 일하는 사원 수를 검색하시오. 일하는 사원이 없는 프로젝트도 0으로 나와야 한다.",
  "SELECT   P.Pname, COUNT(W.Essn)\nFROM     (PROJECT AS P LEFT OUTER JOIN WORKS_ON AS W ON P.Pnumber = W.Pno)\nGROUP BY P.Pnumber, P.Pname;", expect=6,
  keys=["LEFT OUTER JOIN","COUNT(W.Essn) (NULL은 안 셈 → 0)","GROUP BY"], note="COUNT(*)를 쓰면 짝 없는 프로젝트도 1로 세진다. COMPANY 상태에선 모든 프로젝트에 사원이 있어 차이가 안 보인다.")
Q("5-io-6","inner-outer","blank","외부 조인에서 짝이 없는 투플의 상대 속성은 (a) 로 채운다. 짝 없는 것만 고르려면 WHERE B.KEY (b) 를 쓴다.",
  ["NULL","IS NULL"], accept=[["NULL","null","널"],["IS NULL","is null"]])
Q("5-io-7","inner-outer","short","내부 조인과 외부 조인(LEFT, RIGHT, FULL)의 차이를 쓰시오.",
  "내부 조인: 조인 조건을 만족하는(짝이 있는) 투플 쌍만 결과에. 외부 조인: 짝이 없는 투플도 결과에 넣고 상대 속성을 NULL로 채움. LEFT는 왼쪽 테이블의 모든 투플, RIGHT는 오른쪽 테이블의 모든 투플, FULL은 양쪽 모든 투플을 유지.",
  keys=["내부 = 짝 있는 것만","외부 = 짝 없어도 NULL 채워 포함","LEFT/RIGHT/FULL 구분"])

# ───────── L5-4 집계 · GROUP BY · HAVING ─────────
Q("5-ag-1","aggregate","mc","COMPANY 상태에서 SELECT AVG(Salary) FROM EMPLOYEE; 의 결과는?",
  2, choices=["33250","31000","35125","40000"])
SQLQ("5-ag-2","aggregate","전체 사원 급여의 합, 최대, 최소, 평균을 검색하시오. (질의 19)",
  "SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)\nFROM   EMPLOYEE;", expect=1, keys=["SUM, MAX, MIN, AVG(Salary)"])
SQLQ("5-ag-3","aggregate","'Research' 부서 사원 급여의 합, 최대, 최소, 평균을 검색하시오. (질의 20)",
  "SELECT SUM(Salary), MAX(Salary), MIN(Salary), AVG(Salary)\nFROM   (EMPLOYEE JOIN DEPARTMENT ON Dno = Dnumber)\nWHERE  Dname = 'Research';", expect=1,
  keys=["집계 함수 4개","EMPLOYEE–DEPARTMENT 조인","Dname = 'Research'"])
Q("5-ag-4","aggregate","ox","집계 함수는 주로 SELECT 절이나 HAVING 절에서 쓴다.",True)
SQLQ("5-ag-5","aggregate","WORKS_ON에 기록된 근무 시간의 총합과 평균을 검색하시오.",
  "SELECT SUM(Hours), AVG(Hours)\nFROM   WORKS_ON;", expect=1, keys=["SUM(Hours), AVG(Hours)"],
  note="Borg의 Hours가 NULL이라 AVG는 NULL을 뺀 15개로 나눈다 (275 / 15 ≈ 18.33).")
Q("5-cn-1","count-null","mc","COMPANY 상태에서 SELECT COUNT(Super_ssn) FROM EMPLOYEE; 의 결과는?",
  1, choices=["8","7","3","1"])
Q("5-cn-2","count-null","mc","COMPANY 상태에서 SELECT COUNT(DISTINCT Salary) FROM EMPLOYEE; 의 결과는?",
  2, choices=["8","7","6","5"])
Q("5-cn-3","count-null","ox","COUNT(*)는 행 수를 세고, COUNT(속성)은 NULL이 아닌 값의 수를 센다.",True)
SQLQ("5-cn-4","count-null","부양가족이 2명 이상인 사원의 이름을 검색하시오.",
  "SELECT Lname, Fname\nFROM   EMPLOYEE\nWHERE  ( SELECT COUNT(*)\n         FROM   DEPENDENT\n         WHERE  Ssn = Essn ) >= 2;", expect=2,
  keys=["안쪽 COUNT(*) (사원마다 부양가족 수)","Ssn = Essn (상관)",">= 2"])
SQLQ("5-cn-5","count-null","'Research' 부서의 사원 수를 검색하시오. (질의 22)",
  "SELECT COUNT(*)\nFROM   EMPLOYEE, DEPARTMENT\nWHERE  Dno = Dnumber AND Dname = 'Research';", expect=1, keys=["COUNT(*)","조인 + Dname 조건"])
Q("5-cn-6","count-null","short","COUNT(*), COUNT(A), COUNT(DISTINCT A)의 차이를 COMPANY의 EMPLOYEE.Super_ssn을 예로 설명하시오.",
  "COUNT(*): 행 수 → 8. COUNT(Super_ssn): NULL이 아닌 값의 수 → 7 (Borg는 NULL). COUNT(DISTINCT Super_ssn): 서로 다른 값의 수 → 3 (333445555, 888665555, 987654321).",
  keys=["COUNT(*) = 8 (행 수)","COUNT(Super_ssn) = 7 (NULL 제외)","COUNT(DISTINCT) = 3"])
Q("5-gb-1","group-by","mc","GROUP BY Dno를 쓴 질의의 SELECT 절에 올 수 있는 것은?",
  0, choices=["Dno와 집계 함수","모든 속성","Lname","Ssn"])
SQLQ("5-gb-2","group-by","부서마다 부서 번호, 사원 수, 평균 급여를 검색하시오. (질의 24)",
  "SELECT   Dno, COUNT(*), AVG(Salary)\nFROM     EMPLOYEE\nGROUP BY Dno;", expect=3, keys=["GROUP BY Dno","COUNT(*), AVG(Salary)"])
SQLQ("5-gb-3","group-by","프로젝트마다 프로젝트 번호, 이름, 그 프로젝트에서 일하는 사원 수를 검색하시오. (질의 25)",
  "SELECT   Pnumber, Pname, COUNT(*)\nFROM     PROJECT, WORKS_ON\nWHERE    Pnumber = Pno\nGROUP BY Pnumber, Pname;", expect=6,
  keys=["PROJECT–WORKS_ON 조인","GROUP BY Pnumber, Pname","COUNT(*)"])
SQLQ("5-gb-4","group-by","부서마다 부서 이름과 그 부서가 통제하는 프로젝트 수를 검색하시오.",
  "SELECT   D.Dname, COUNT(*)\nFROM     DEPARTMENT AS D, PROJECT AS P\nWHERE    D.Dnumber = P.Dnum\nGROUP BY D.Dnumber, D.Dname;", expect=3,
  keys=["DEPARTMENT–PROJECT 조인","GROUP BY 부서","COUNT(*)"])
SQLQ("5-gb-5","group-by","사원마다 Ssn, 성, 일하는 프로젝트 수, 총 근무 시간을 검색하시오.",
  "SELECT   E.Ssn, E.Lname, COUNT(*), SUM(W.Hours)\nFROM     EMPLOYEE AS E, WORKS_ON AS W\nWHERE    E.Ssn = W.Essn\nGROUP BY E.Ssn, E.Lname;", expect=8,
  keys=["EMPLOYEE–WORKS_ON 조인","GROUP BY E.Ssn, E.Lname","COUNT(*), SUM(Hours)"])
Q("5-gb-6","group-by","ox","SELECT Dno, Lname, COUNT(*) FROM EMPLOYEE GROUP BY Dno; 는 표준 SQL에서 올바른 질의이다.",False,
  explain="Lname은 그룹마다 값이 하나로 정해지지 않는다. GROUP BY를 쓰면 SELECT엔 그룹화 속성과 집계만.")
Q("5-gb-7","group-by","short","GROUP BY와 그룹화 속성을 설명하시오.",
  "GROUP BY는 릴레이션의 투플을 겹치지 않는 부분집합(그룹)으로 나눠서 그룹마다 집계 함수를 적용하게 한다. 그룹화 속성은 그룹을 나누는 기준으로, 같은 그룹의 투플은 그룹화 속성 값이 같다.",
  keys=["겹치지 않는 그룹으로 분할","그룹마다 집계","그룹화 속성 값이 같은 투플이 한 그룹"])
Q("5-hv-1","having","mc","'평균 급여가 30000을 넘는 부서'의 조건을 쓰는 곳은?",
  2, choices=["WHERE AVG(Salary) > 30000","SELECT 절","HAVING AVG(Salary) > 30000","ORDER BY"])
SQLQ("5-hv-2","having","사원이 두 명 넘게 일하는 프로젝트마다 번호, 이름, 사원 수를 검색하시오. (질의 26)",
  "SELECT   Pnumber, Pname, COUNT(*)\nFROM     PROJECT, WORKS_ON\nWHERE    Pnumber = Pno\nGROUP BY Pnumber, Pname\nHAVING   COUNT(*) > 2;", expect=4,
  keys=["GROUP BY Pnumber, Pname","HAVING COUNT(*) > 2"])
SQLQ("5-hv-3","having","평균 급여가 $30,000를 넘는 부서마다 부서 이름과 그 부서 사원 수를 검색하시오. (교안 연습 2)",
  "SELECT   D.Dname, COUNT(*)\nFROM     EMPLOYEE AS E, DEPARTMENT AS D\nWHERE    E.Dno = D.Dnumber\nGROUP BY D.Dname\nHAVING   AVG(E.Salary) > 30000;", expect=3,
  keys=["EMPLOYEE–DEPARTMENT 조인 (부서 이름 때문)","GROUP BY 부서","HAVING AVG(Salary) > 30000"])
SQLQ("5-hv-4","having","사원이 5명 이상인 부서마다 부서 번호와, 그 부서에서 급여가 40000 넘는 사원 수를 검색하시오. (WHERE와 HAVING의 차이에 주의)",
  "SELECT   Dno, COUNT(*)\nFROM     EMPLOYEE\nWHERE    Salary > 40000\n  AND    Dno IN ( SELECT   Dno\n                  FROM     EMPLOYEE\n                  GROUP BY Dno\n                  HAVING   COUNT(*) >= 5 )\nGROUP BY Dno;", expect=0,
  keys=["사원 5명 이상 조건은 그룹 전체 기준 → 중첩 질의에서 HAVING","급여 > 40000은 WHERE","바깥 GROUP BY Dno"],
  note="WHERE Salary > 40000 ... GROUP BY Dno HAVING COUNT(*) >= 5 로 쓰면 '급여 40000 넘는 사원이 5명 이상'이 되어 뜻이 달라진다 (교재 질의 28의 함정). COMPANY 상태에는 5명 이상인 부서가 없어 결과가 비어 있다.")
SQLQ("5-hv-5","having","총 근무 시간이 50시간 이상인 프로젝트의 이름과 총 근무 시간을 검색하시오.",
  "SELECT   P.Pname, SUM(W.Hours)\nFROM     PROJECT AS P, WORKS_ON AS W\nWHERE    P.Pnumber = W.Pno\nGROUP BY P.Pnumber, P.Pname\nHAVING   SUM(W.Hours) >= 50;", expect=4,
  keys=["GROUP BY 프로젝트","HAVING SUM(Hours) >= 50"])
Q("5-hv-6","having","blank","SQL 질의의 실행 순서: FROM → (a) → GROUP BY → (b) → SELECT → ORDER BY",
  ["WHERE","HAVING"], accept=[["WHERE","where"],["HAVING","having"]])
Q("5-hv-7","having","short","WHERE 절과 HAVING 절의 차이를 쓰시오.",
  "WHERE는 그룹을 만들기 전에 개별 투플에 대한 조건으로 투플을 거른다. HAVING은 GROUP BY로 만든 그룹의 요약 정보(집계)에 대한 조건으로 그룹을 거른다. 집계 함수 조건은 WHERE에 쓸 수 없고 HAVING에 쓴다.",
  keys=["WHERE = 투플 조건 (그룹 전)","HAVING = 그룹 조건 (집계 후)","집계 조건은 HAVING에"])
Q("5-hv-8","having","ox","HAVING은 GROUP BY와 함께 쓰여서 조건을 만족하는 그룹만 결과에 남긴다.",True)

# ───────── L5-5 Assertion · Trigger ─────────
Q("5-as-1","assertion","mc","CREATE ASSERTION이 필요한 경우는?",
  1, choices=["PK를 지정할 때","키·개체·참조 무결성으로 표현할 수 없는 일반 제약을 지정할 때","뷰를 만들 때","인덱스를 만들 때"])
Q("5-as-2","assertion","short","CREATE ASSERTION에서 조건을 보통 NOT EXISTS로 쓰는 이유를 설명하시오.",
  "원하는 조건을 '위반하는 투플을 고르는 질의'로 쓰고 NOT EXISTS로 감싸면, 위반 투플이 없을 때(결과가 비었을 때) 참이 되어 제약이 만족되고, 하나라도 있으면 거짓이 되어 위반이다. CHECK 조건은 모든 DB 상태에서 참이어야 한다.",
  keys=["위반 투플을 찾는 질의","NOT EXISTS → 비면 참(만족)","CHECK는 모든 상태에서 참이어야"])
Q("5-as-3","assertion","calc","'사원의 급여는 그가 일하는 부서 관리자의 급여보다 많으면 안 된다'를 CREATE ASSERTION으로 쓰시오.",
  "CREATE ASSERTION SALARY_CONSTRAINT\nCHECK ( NOT EXISTS ( SELECT *\n                     FROM   EMPLOYEE E, EMPLOYEE M, DEPARTMENT D\n                     WHERE  E.Salary > M.Salary\n                       AND  E.Dno = D.Dnumber\n                       AND  D.Mgr_ssn = M.Ssn ) );",
  keys=["CREATE ASSERTION ... CHECK","NOT EXISTS (위반 질의)","E.Salary > M.Salary, E.Dno = D.Dnumber, D.Mgr_ssn = M.Ssn"], code=C.COMPANY_SCHEMA)
Q("5-as-4","assertion","calc","'모든 부서는 사원이 최소 1명 있어야 한다'를 CREATE ASSERTION으로 쓰시오.",
  "CREATE ASSERTION DEPT_HAS_EMP\nCHECK ( NOT EXISTS ( SELECT *\n                     FROM   DEPARTMENT D\n                     WHERE  NOT EXISTS ( SELECT *\n                                         FROM   EMPLOYEE E\n                                         WHERE  E.Dno = D.Dnumber ) ) );",
  keys=["CHECK ( NOT EXISTS (위반 = 사원 없는 부서) )","안쪽 NOT EXISTS (그 부서 사원)"], code=C.COMPANY_SCHEMA)
Q("5-as-5","assertion","ox","Assertion의 CHECK 조건은 모든 DB 상태에서 참이어야 한다.",True)
Q("5-tr-1","trigger-eca","mc","트리거의 ECA가 뜻하는 것은?",
  0, choices=["Event, Condition, Action","Entity, Constraint, Attribute","Execute, Check, Abort","Event, Cascade, Assertion"])
Q("5-tr-2","trigger-eca","mc","트리거에서 조건(Condition)을 지정하는 절은?",
  2, choices=["CHECK","IF","WHEN","WHERE"])
Q("5-tr-3","trigger-eca","short","트리거의 세 구성 요소를 SALARY_VIOLATION 예로 설명하시오.",
  "Event: 조건을 깰 수 있는 갱신 연산 — 사원 삽입, 급여 변경, 상사 변경 (BEFORE INSERT OR UPDATE OF SALARY, SUPERVISOR_SSN ON EMPLOYEE). Condition: WHEN 절 — 새 급여가 직속 상사의 급여보다 큰가. Action: 조건이 참이면 실행 — 외부 프로시저 INFORM_SUPERVISOR로 상사에게 알림.",
  keys=["Event = 갱신 연산 (BEFORE/AFTER)","Condition = WHEN 절","Action = SQL/트랜잭션/외부 프로그램"])
Q("5-tr-4","trigger-eca","ox","트리거의 Condition은 선택 사항이며, 참일 때만 Action이 실행된다.",True)
Q("5-tr-5","trigger-eca","short","Assertion과 Trigger의 차이를 쓰시오.",
  "Assertion은 항상 만족해야 하는 일반 제약을 선언하고, 위반하는 갱신을 막는다. Trigger는 특정 이벤트가 일어나고 조건이 맞으면 자동으로 실행할 동작(SQL, 트랜잭션, 외부 프로그램)을 지정한다 (예: 알림, 유도 데이터 갱신).",
  keys=["Assertion = 제약 (위반 막음)","Trigger = 이벤트–조건–동작 (자동 실행)"])
Q("5-tr-6","trigger-eca","mc","트리거의 용도로 교안에 나온 것이 '아닌' 것은?",
  3, choices=["DB 일관성 유지","DB 갱신 모니터링","유도 데이터 자동 갱신","질의 최적화"])
Q("5-tr-7","trigger-eca","blank","트리거의 Event는 (a) 또는 AFTER 키워드로 갱신 연산 전/후 실행을 지정하고, FOR EACH (b) 는 영향받은 투플마다 실행함을 뜻한다.",
  ["BEFORE","ROW"], accept=[["BEFORE","before"],["ROW","row"]])

# ───────── L5-6 뷰 ─────────
Q("5-vd-1","view-def","mc","뷰(view)에 대한 설명으로 옳은 것은?",
  1, choices=["항상 물리적으로 저장된 테이블","기본 테이블에서 유도된 가상 테이블","DB 사본","인덱스의 한 종류"])
Q("5-vd-2","view-def","ox","DROP VIEW로 뷰를 지우면 정의 테이블(기본 테이블)의 투플도 삭제된다.",False)
Q("5-vd-3","view-def","calc","사원 이름(Fname, Lname), 프로젝트 이름, 근무 시간으로 된 뷰 WORKS_ON1을 정의하고, 그 뷰로 'ProductX'에서 일하는 사원의 이름을 검색하시오.",
  "CREATE VIEW WORKS_ON1\nAS SELECT Fname, Lname, Pname, Hours\n   FROM   EMPLOYEE, PROJECT, WORKS_ON\n   WHERE  Ssn = Essn AND Pno = Pnumber;\n\nSELECT Fname, Lname\nFROM   WORKS_ON1\nWHERE  Pname = 'ProductX';\n→ John Smith, Joyce English",
  keys=["CREATE VIEW ... AS SELECT","세 테이블 조인","뷰 질의는 단일 테이블처럼"], code=C.COMPANY_SCHEMA)
Q("5-vd-4","view-def","calc","부서 이름, 사원 수, 급여 합으로 된 뷰 DEPT_INFO(Dept_name, No_of_emps, Total_sal)를 정의하시오.",
  "CREATE VIEW DEPT_INFO (Dept_name, No_of_emps, Total_sal)\nAS SELECT   Dname, COUNT(*), SUM(Salary)\n   FROM     DEPARTMENT, EMPLOYEE\n   WHERE    Dnumber = Dno\n   GROUP BY Dname;",
  keys=["속성 이름 명시","COUNT(*), SUM(Salary)","GROUP BY Dname"], code=C.COMPANY_SCHEMA)
Q("5-vd-5","view-def","short","뷰를 쓰는 이유를 쓰시오.",
  "자주 쓰는 질의가 여러 테이블 조인이나 집계 같은 복잡한 조건을 포함할 때, 그걸 뷰로 정의해 두면 단일 테이블 질의처럼 간단하게 쓸 수 있다 (복잡한 질의 단순화). 또 특정 속성·투플만 보여주는 권한 부여에도 쓴다.",
  keys=["복잡한 질의 단순화 (단일 테이블처럼)","권한 부여 (보안)"])
Q("5-vd-6","view-def","calc","각 부서의 이름, 관리자의 이름과 급여로 된 뷰를 정의하고 쓸모를 쓰시오. (교안 연습 3)",
  "CREATE VIEW DEPT_INFO (DeptName, MgrFname, MgrLname, MgrSalary)\nAS SELECT D.Dname, E.Fname, E.Lname, E.Salary\n   FROM   DEPARTMENT AS D, EMPLOYEE AS E\n   WHERE  D.Mgr_ssn = E.Ssn;\n쓸모: 부서와 그 관리자 정보를 한 번에 보기 (Research–Franklin Wong 40000, …)",
  keys=["D.Mgr_ssn = E.Ssn 조인","속성 이름 명시","용도: 부서별 관리자 정보"], code=C.COMPANY_SCHEMA)
Q("5-vi-1","view-impl","mc","뷰 질의를 기본 테이블에 대한 질의로 바꿔서 처리하고 뷰를 물리적으로 유지하지 않는 방식은?",
  0, choices=["질의 수정 (query modification)","뷰 실체화 (view materialization)","즉시 갱신","지연 갱신"])
Q("5-vi-2","view-impl","mc","실체화된 뷰를 '뷰 질의가 필요할 때' 갱신하는 방식은?",
  2, choices=["즉시 갱신","주기적 갱신","지연 갱신 (lazy)","점진적 삭제"])
Q("5-vi-3","view-impl","short","뷰를 구현하는 두 방식(질의 수정, 뷰 실체화)을 비교하시오.",
  "질의 수정: 뷰 질의를 기본 테이블에 대한 질의로 변환해서 처리, 뷰를 물리적으로 유지하지 않음. 사용자는 편하지만 복잡한 뷰를 매번 다시 계산해서 비효율적. 뷰 실체화: 뷰가 처음 질의될 때 물리적인 뷰 테이블을 만들어 한동안 유지(이후 질의가 자주 올 거라 가정). 추가 저장 공간이 필요하고, 기본 테이블이 바뀌면 점진적 갱신으로 반영해야 한다.",
  keys=["질의 수정 = 변환, 저장 안 함, 매번 계산","실체화 = 물리 테이블 유지, 저장 공간, 점진적 갱신"])
Q("5-vi-4","view-impl","short","실체화된 뷰의 갱신 시점 세 가지(즉시, 주기적, 지연)를 장단점과 함께 쓰시오.",
  "즉시 갱신: 기본 테이블이 바뀌자마자 갱신. 항상 최신이지만 불필요하고 비효율적일 수 있음. 주기적 갱신: 주기적으로 갱신. 뷰 질의가 최신이 아닌 결과를 받을 수 있음. 지연 갱신: 뷰 질의가 필요할 때 갱신. 질의가 오기 전까지는 최신이 아님.",
  keys=["즉시 = 항상 최신, 비효율","주기적 = 최신 아닐 수 있음","지연 = 필요할 때"])
Q("5-vi-5","view-impl","ox","DBMS는 정의 테이블이 바뀌면 뷰에 반영해서 뷰를 최신 상태로 유지할 책임이 있다.",True)
Q("5-vu-1","view-update","mc","갱신이 허용되는 뷰는?",
  1, choices=["여러 테이블을 조인한 뷰","단일 테이블에서 집계 없이 정의되고, PK와 DEFAULT 없는 NOT NULL 속성을 모두 포함한 뷰","GROUP BY와 SUM을 쓴 뷰","모든 뷰"])
Q("5-vu-2","view-update","short","UPDATE DEPT_INFO SET Total_sal = 100000 WHERE Dname = 'Research'; 가 불가능한 이유를 쓰시오.",
  "Total_sal은 SUM(Salary)로 계산된 집계 값이고 물리적으로 저장되지 않는다. 그 값을 100000으로 바꾸려면 Research 사원들의 급여를 어떻게 바꿔야 할지 정할 수 없으므로 의미가 없는 갱신이다.",
  keys=["집계로 계산된 값, 저장 안 됨","기본 테이블 갱신으로 바꿀 방법이 없음 (의미 없음)"])
Q("5-vu-3","view-update","short","WORKS_ON1 뷰(EMPLOYEE, PROJECT, WORKS_ON 조인)에 UPDATE WORKS_ON1 SET Pname = 'ProductY' WHERE Lname = 'Smith' AND Fname = 'John' AND Pname = 'ProductX'; 를 하면 생기는 문제를 쓰시오.",
  "이 갱신은 기본 테이블 갱신으로 여러 가지로 해석된다. (a) Smith의 WORKS_ON 투플의 Pno를 ProductY의 번호로 바꾸기 (Smith가 일하는 프로젝트를 바꿈, 의도에 맞음). (b) PROJECT에서 'ProductX'의 이름을 'ProductY'로 바꾸기 (뷰 결과는 같아 보이지만 ProductX에서 일하던 다른 모든 투플까지 바뀌는 부작용). 어느 쪽이 맞는지 정할 수 없어서 조인 뷰는 일반적으로 갱신할 수 없다.",
  keys=["해석 a: WORKS_ON의 Pno 변경","해석 b: PROJECT의 Pname 변경 (부작용)","여러 해석 → 갱신 불가"])
Q("5-vu-4","view-update","ox","뷰 갱신은 그 갱신을 이루는 기본 릴레이션 갱신이 딱 하나뿐일 때 가능하다.",True)
Q("5-vu-5","view-update","mc","단일 테이블 뷰가 갱신 가능하려면 뷰 속성에 반드시 포함되어야 하는 것은?",
  3, choices=["모든 속성","FK 속성","집계 속성","기본 키와, DEFAULT가 없는 NOT NULL 속성 전부"])
Q("5-vu-6","view-update","short","단일 테이블 뷰가 갱신 가능하려면 왜 기본 키와 DEFAULT 없는 NOT NULL 속성을 모두 포함해야 하는지 쓰시오.",
  "뷰를 통해 투플을 삽입하면 뷰에 없는 속성은 기본 테이블에서 NULL(또는 DEFAULT)이 된다. PK가 빠지면 개체 무결성을, DEFAULT 없는 NOT NULL 속성이 빠지면 NOT NULL 제약을 어기게 된다. 또 PK가 있어야 뷰의 투플이 기본 테이블의 어느 투플인지 하나로 정해진다.",
  keys=["뷰에 없는 속성은 NULL로 들어감","PK·NOT NULL 위반 방지","PK로 대응 투플을 하나로 특정"])
Q("5-vu-7","view-update","mc","갱신이 일반적으로 불가능한 뷰가 '아닌' 것은?",
  2, choices=["두 테이블을 조인한 뷰","AVG를 쓴 뷰","SELECT Ssn, Fname, Lname, Dno FROM EMPLOYEE WHERE Dno = 5 로 정의한 뷰 (Ssn이 PK, 나머지 NOT NULL 속성 포함)","GROUP BY를 쓴 뷰"])
Q("5-va-1","view-auth","mc","5번 부서 관리자가 5번 부서 사원 정보만 보게 하는 방법은?",
  0, choices=["DEPT5EMP 뷰를 만들고 그 뷰에 대한 질의 권한만 부여","EMPLOYEE에서 다른 부서 투플을 삭제","EMPLOYEE 사본을 만듦","트리거로 알림"])
Q("5-va-2","view-auth","calc","일반 사원이 다른 사원의 이름과 주소만 볼 수 있게 하는 뷰 BASIC_EMP_DATA를 정의하시오.",
  "CREATE VIEW BASIC_EMP_DATA AS\nSELECT Fname, Lname, Address\nFROM   EMPLOYEE;\n(사용자에게 EMPLOYEE가 아니라 이 뷰에 대한 질의 권한만 준다)",
  keys=["CREATE VIEW","이름, 주소만 (속성 제한)"], code=C.COMPANY_SCHEMA)
Q("5-va-3","view-auth","ox","뷰는 권한 없는 사용자에게 특정 속성이나 특정 투플을 숨기는 데 쓸 수 있다.",True)
