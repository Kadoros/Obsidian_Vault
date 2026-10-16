from qdsl import Q
from sq import RAQ
import company as C

# ───────── L6-1 소개 · 질의 트리 ─────────
Q("6-in-1","ra-intro","mc","관계 대수와 SQL의 차이로 옳은 것은?",
  1, choices=["관계 대수는 선언적, SQL은 절차적","관계 대수는 절차적(어떻게), SQL은 선언적(무엇을)","둘 다 절차적","둘 다 선언적"])
Q("6-in-2","ra-intro","short","관계 대수가 중요한 이유 두 가지를 쓰시오.",
  "1) 관계 모델 연산(선택, 투영, 이름 바꾸기, 조인, 카티션 곱 등)의 형식적 기초이며 집합에 대한 수학 개념에 엄격하게 기반한다. 2) 결과를 얻기 위한 연산의 순서를 명시하므로 질의 처리와 최적화의 기반이 된다.",
  keys=["관계 모델 연산의 형식적 기초 (집합 기반)","질의 처리·최적화의 기반 (연산 순서)"])
Q("6-in-3","ra-intro","ox","관계 대수 연산의 결과는 항상 릴레이션이다 (닫힌 체계).",True)
Q("6-qt-1","query-tree","mc","질의 트리에서 잎 노드와 내부 노드는 각각?",
  2, choices=["연산, 릴레이션","SQL 절, 속성","입력 릴레이션, 관계 대수 연산","조건, 결과"])
Q("6-qt-2","query-tree","ox","질의 트리는 루트에서 시작해서 잎에서 끝나는 순서로 실행된다.",False,
  explain="잎(입력 릴레이션)에서 시작해 루트에서 끝난다.")
Q("6-qt-3","query-tree","short","질의 처리(query processing)란 무엇이고, 질의 트리와 어떤 관계인지 쓰시오.",
  "질의 처리는 SQL 질의를 실행할 수 있는 여러 전략(질의 트리, 실행 계획) 중 적절한 것을 고르는 과정이다. SQL 하나에 질의 트리가 여러 개 있을 수 있고, 그중 최선을 고르는 것이 질의 최적화다.",
  keys=["여러 실행 전략 중 선택","SQL 하나에 질의 트리 여러 개","최선 선택 = 최적화"])
Q("6-qt-4","query-tree","calc","다음 SQL을 질의 트리의 실행 순서대로 관계 대수 단계(중간 릴레이션)로 쓰시오.\nSELECT P.Pnumber, P.Dnum, E.Lname, E.Address, E.Bdate\nFROM   PROJECT P, DEPARTMENT D, EMPLOYEE E\nWHERE  P.Dnum = D.Dnumber AND D.Mgr_ssn = E.Ssn AND P.Plocation = 'Stafford';",
  "STAFFORD_PROJS ← σ Plocation='Stafford' (PROJECT)\nCONTR_DEPTS    ← STAFFORD_PROJS ⋈ Dnum=Dnumber DEPARTMENT\nPROJ_DEPT_MGRS ← CONTR_DEPTS ⋈ Mgr_ssn=Ssn EMPLOYEE\nRESULT         ← π Pnumber, Dnum, Lname, Address, Bdate (PROJ_DEPT_MGRS)\n(잎: PROJECT, DEPARTMENT, EMPLOYEE / 루트: π)",
  keys=["σ Plocation 먼저 (잎 쪽)","⋈ Dnum=Dnumber","⋈ Mgr_ssn=Ssn","π 루트"], code=C.COMPANY_SCHEMA)

# ───────── L6-2 σ π ρ ─────────
Q("6-sel-1","ra-select","mc","σ Dno=4 (EMPLOYEE)의 결과 차수(속성 수)는?",
  2, choices=["1","4","EMPLOYEE와 같다 (10)","조건을 만족하는 투플 수"])
Q("6-sel-2","ra-select","mc","관계 대수의 σ에 대응하는 SQL 부분은?",
  1, choices=["SELECT 절","WHERE 절","FROM 절","GROUP BY 절"])
Q("6-sel-3","ra-select","ox","σ c1(σ c2(R)) = σ c2(σ c1(R)) 이 성립한다 (교환 법칙).",True)
Q("6-sel-4","ra-select","blank","σ는 릴레이션에서 조건을 만족하는 투플을 고르는 (a) 필터링이고, π는 원하는 열만 남기는 (b) 필터링이다.",
  ["수평","수직"], accept=[["수평","horizontal","가로"],["수직","vertical","세로"]])
RAQ("6-sel-5","ra-select","4번 부서에서 급여가 25000을 넘거나, 5번 부서에서 급여가 30000을 넘는 사원 투플을 관계 대수로 쓰시오.",
  "σ (Dno=4 AND Salary>25000) OR (Dno=5 AND Salary>30000) (EMPLOYEE)",
  "SELECT Fname, Lname, Dno, Salary FROM EMPLOYEE WHERE (Dno=4 AND Salary>25000) OR (Dno=5 AND Salary>30000)", expect=3,
  keys=["σ 하나에 AND/OR 조건","(Dno=4 AND Salary>25000) OR (Dno=5 AND Salary>30000)"])
Q("6-sel-6","ra-select","short","σ의 조건(selection condition)에 쓸 수 있는 절의 형태와 비교 연산자를 쓰고, 순서가 없는 값의 경우를 쓰시오.",
  "절의 형태: <속성> <비교연산> <상수> 또는 <속성> <비교연산> <속성>, 절들은 AND, OR로 연결. 비교 연산자: =, <, ≤, >, ≥, ≠. 순서가 있는 값(숫자, 날짜)은 모두 쓸 수 있지만 순서가 없는 값(예: 색깔)은 =, ≠만.",
  keys=["<속성> op <상수/속성>","AND, OR 연결","순서 없는 값은 =, ≠만"])
Q("6-sel-7","ra-select","calc","σ Dno=5 AND Salary>=30000 (EMPLOYEE) 와 같은 결과를 내는 SQL을 쓰고, 이 σ를 두 개의 σ로 나눠 쓰시오.",
  "SQL: SELECT * FROM EMPLOYEE WHERE Dno = 5 AND Salary >= 30000;\n두 개로: σ Dno=5 (σ Salary>=30000 (EMPLOYEE))  (또는 순서를 바꿔도 같음)\n결과: Smith, Wong, Narayan",
  keys=["SELECT * ... WHERE (σ = WHERE)","σ를 중첩해 나눔 (교환 가능)"], code=C.COMPANY_SCHEMA)
Q("6-pro-1","ra-project","mc","COMPANY 상태에서 π Sex, Salary (EMPLOYEE)의 결과 투플 수는?",
  1, choices=["8","7","6","2"])
Q("6-pro-2","ra-project","mc","π Sex, Salary (EMPLOYEE)와 정확히 같은 결과를 내는 SQL은?",
  2, choices=["SELECT Sex, Salary FROM EMPLOYEE;","SELECT ALL Sex, Salary FROM EMPLOYEE;","SELECT DISTINCT Sex, Salary FROM EMPLOYEE;","SELECT * FROM EMPLOYEE;"])
Q("6-pro-3","ra-project","ox","π의 속성 리스트에 키 속성이 포함되면 결과에 중복 투플이 생기지 않는다.",True)
Q("6-pro-4","ra-project","short","π 연산이 중복을 제거하는 이유와, 중복이 생기는 경우를 쓰시오.",
  "관계 대수는 집합에 기반하므로 π의 결과도 서로 다른 투플의 집합이어야 한다. 속성 리스트에 비키 속성만 있으면 서로 다른 투플이 같은 값 조합을 가질 수 있어 중복이 생기는데, π는 이를 제거한다.",
  keys=["결과는 집합 (중복 제거)","비키 속성만 투영하면 중복 발생"])
RAQ("6-pro-5","ra-project","모든 사원의 성, 이름, 급여를 관계 대수로 쓰시오.",
  "π Lname, Fname, Salary (EMPLOYEE)",
  "SELECT DISTINCT Lname, Fname, Salary FROM EMPLOYEE", expect=8, keys=["π Lname, Fname, Salary"])
RAQ("6-pro-6","ra-project","5번 부서 사원들이 받는 급여 값들을 중복 없이 관계 대수로 쓰시오.",
  "π Salary (σ Dno=5 (EMPLOYEE))",
  "SELECT DISTINCT Salary FROM EMPLOYEE WHERE Dno=5", expect=4, keys=["σ Dno=5 먼저","π Salary (중복 자동 제거)"])
Q("6-pro-7","ra-project","blank","π의 결과 차수는 (a) 에 있는 속성 수와 같고, σ의 결과 차수는 (b) 의 차수와 같다.",
  ["속성 리스트","R"], accept=[["속성 리스트","attribute list","리스트","속성 목록"],["R","원래 릴레이션","입력 릴레이션","릴레이션"]])
Q("6-ren-1","ra-rename","mc","ρ S(B₁, …, Bₙ)(R) 의 뜻은?",
  0, choices=["릴레이션 이름을 S로, 속성 이름을 B₁…Bₙ으로 바꿈","S와 R을 조인","R에서 B₁…Bₙ만 투영","S를 R로 바꿈"])
Q("6-ren-2","ra-rename","ox","SQL에서 이름 바꾸기는 AS(별칭)로 한다.",True)
Q("6-ren-3","ra-rename","calc","5번 부서 사원의 이름, 성, 급여를 구하고 결과 속성 이름을 First_name, Last_name, Salary로 바꾸는 관계 대수를 쓰고, 같은 SQL을 쓰시오.",
  "TEMP ← σ Dno=5 (EMPLOYEE)\nR(First_name, Last_name, Salary) ← π Fname, Lname, Salary (TEMP)\n(또는 ρ (First_name, Last_name, Salary) (π Fname, Lname, Salary (TEMP)))\n\nSQL: SELECT E.Fname AS First_name, E.Lname AS Last_name, E.Salary AS Salary\n     FROM EMPLOYEE AS E WHERE E.Dno = 5;",
  keys=["σ Dno=5","π 후 ρ (또는 R(속성들) ←)","SQL은 AS"], code=C.COMPANY_SCHEMA)
Q("6-ren-4","ra-rename","short","관계 대수에서 RENAME이 필요한 경우를 두 가지 쓰시오.",
  "1) 자연 조인에서 조인할 속성의 이름이 서로 다를 때 이름을 맞추려고 (예: Dnumber → Dnum). 2) 합집합 등 집합 연산 결과나 중간 결과의 속성 이름을 원하는 대로 바꿀 때 (예: π Super_ssn을 Ssn으로). 같은 릴레이션을 두 번 쓸 때 구별하려고도 쓴다.",
  keys=["자연 조인 속성 이름 맞추기","집합 연산·결과 이름 맞추기 / 자기 조인"])
Q("6-seq-1","ra-sequence","mc","π Fname, Lname, Salary (σ Dno=5 (EMPLOYEE)) 를 중간 릴레이션으로 나눈 것은?",
  1, choices=["DEP5 ← π Fname (EMPLOYEE); RESULT ← σ Dno=5 (DEP5)","DEP5_EMPS ← σ Dno=5 (EMPLOYEE); RESULT ← π Fname, Lname, Salary (DEP5_EMPS)","RESULT ← EMPLOYEE × DEPARTMENT","나눌 수 없다"])
Q("6-seq-2","ra-sequence","ox","복잡한 질의는 하나의 식으로 쓰는 것보다 중간 결과 릴레이션에 이름을 붙여 단계별로 쓰는 것이 보통 더 쉽다.",True)
RAQ("6-seq-3","ra-sequence","급여가 30000 이상인 사원의 성과 급여를 (1) 하나의 중첩 식으로, (2) 중간 릴레이션으로 나눠서 쓰시오.",
  "(1) π Lname, Salary (σ Salary>=30000 (EMPLOYEE))\n(2) RICH ← σ Salary>=30000 (EMPLOYEE)\n    RESULT ← π Lname, Salary (RICH)",
  "SELECT DISTINCT Lname, Salary FROM EMPLOYEE WHERE Salary>=30000", expect=5, keys=["중첩 식","중간 릴레이션 두 줄"])
Q("6-seq-4","ra-sequence","short","관계 대수식을 여러 연산으로 쓸 때의 두 방법을 쓰시오.",
  "방법 1: 중간 릴레이션에 이름을 붙여 연산 순서를 명시한다 (DEP5_EMPS ← σ…; RESULT ← π…). 방법 2: 연산을 중첩해서 하나의 관계 대수식으로 쓴다 (π…(σ…(EMPLOYEE))).",
  keys=["중간 릴레이션 이름 붙이기","중첩해서 한 식으로"])

# ───────── L6-3 집합 연산 · 카티션 곱 ─────────
Q("6-set-1","ra-setops","mc","두 릴레이션이 '타입 호환'이려면?",
  2, choices=["튜플 수가 같다","속성 이름이 같다","속성 수가 같고 대응 속성의 도메인이 같다","같은 PK를 가진다"])
Q("6-set-2","ra-setops","ox","R − S = S − R 이다.",False, explain="차집합은 교환 법칙이 성립하지 않는다.")
Q("6-set-3","ra-setops","ox","R ∪ S = S ∪ R, R ∩ S = S ∩ R 이다.",True)
RAQ("6-set-4","ra-setops","5번 부서에서 일하거나, 5번 부서에서 일하는 사원을 직접 감독하는 사원의 Ssn을 관계 대수로 쓰시오.",
  "DEP5_EMPS    ← σ Dno=5 (EMPLOYEE)\nRESULT1      ← π Ssn (DEP5_EMPS)\nRESULT2(Ssn) ← π Super_ssn (DEP5_EMPS)\nRESULT       ← RESULT1 ∪ RESULT2",
  "SELECT Ssn FROM EMPLOYEE WHERE Dno=5 UNION SELECT Super_ssn FROM EMPLOYEE WHERE Dno=5", expect=5,
  keys=["σ Dno=5","π Ssn과 π Super_ssn","이름 맞추기 RESULT2(Ssn)","∪"])
RAQ("6-set-5","ra-setops","프로젝트에서 일하는 사원 중 부양가족이 있는 사원의 Ssn을 교집합으로 쓰시오.",
  "WORKERS(Ssn)  ← π Essn (WORKS_ON)\nWITH_DEPS(Ssn) ← π Essn (DEPENDENT)\nRESULT        ← WORKERS ∩ WITH_DEPS",
  "SELECT Essn FROM WORKS_ON INTERSECT SELECT Essn FROM DEPENDENT", expect=3,
  keys=["π Essn (WORKS_ON)","π Essn (DEPENDENT)","∩"])
Q("6-set-6","ra-setops","calc","STUDENT(Fn, Ln) = {(Susan, Yao), (Ramesh, Shah), (Johnny, Kohler), (Barbara, Jones), (Amy, Ford), (Jimmy, Wang), (Ernest, Gilbert)}, INSTRUCTOR(Fname, Lname) = {(John, Smith), (Ricardo, Browne), (Susan, Yao), (Francis, Johnson), (Ramesh, Shah)}일 때 다음 결과의 투플 수를 쓰시오.\n(1) STUDENT ∪ INSTRUCTOR  (2) STUDENT ∩ INSTRUCTOR  (3) STUDENT − INSTRUCTOR  (4) INSTRUCTOR − STUDENT",
  "(1) 10 (7 + 5 − 겹치는 2)\n(2) 2 (Susan Yao, Ramesh Shah)\n(3) 5 (Johnny Kohler, Barbara Jones, Amy Ford, Jimmy Wang, Ernest Gilbert)\n(4) 3 (John Smith, Ricardo Browne, Francis Johnson)",
  keys=["(1) 10","(2) 2","(3) 5","(4) 3"])
Q("6-set-7","ra-setops","blank","합집합·교집합·차집합의 결과 속성 이름은 관례상 (a) 릴레이션을 따르고, 결과에서 (b) 은 제거된다.",
  ["첫 번째","중복"], accept=[["첫 번째","첫번째","왼쪽","R","앞"],["중복","중복 투플","duplicate","duplicates"]])
Q("6-cp-1","ra-cartesian","mc","R(3개 속성, 4개 투플) × S(2개 속성, 5개 투플)의 결과는?",
  3, choices=["5개 속성, 9개 투플","6개 속성, 20개 투플","3개 속성, 4개 투플","5개 속성, 20개 투플"])
Q("6-cp-2","ra-cartesian","ox","카티션 곱은 타입 호환이 아닌 릴레이션에도 적용할 수 있다.",True)
Q("6-cp-3","ra-cartesian","short","카티션 곱이 그 자체로는 대개 의미가 없는 이유와, 유용하게 쓰는 방법을 쓰시오.",
  "모든 투플 조합을 만들기 때문에 서로 관련 없는 투플까지 이어 붙여진다 (예: 여성 사원 3명 × 부양가족 7명 = 21행, 대부분 무관). 뒤에 SELECT로 관련 있는 투플(Ssn = Essn)만 고르면 유용하다 → 이것이 JOIN.",
  keys=["모든 조합 → 무관한 투플 포함","뒤에 σ로 관련 투플 선택 = JOIN"])
RAQ("6-cp-4","ra-cartesian","여성 사원의 부양가족 이름을, 사원 이름과 함께 카티션 곱과 σ를 써서 관계 대수로 쓰시오.",
  "FEMALE_EMPS       ← σ Sex='F' (EMPLOYEE)\nEMPNAMES          ← π Fname, Lname, Ssn (FEMALE_EMPS)\nEMP_DEPENDENTS    ← EMPNAMES × DEPENDENT\nACTUAL_DEPENDENTS ← σ Ssn=Essn (EMP_DEPENDENTS)\nRESULT            ← π Fname, Lname, Dependent_name (ACTUAL_DEPENDENTS)",
  "SELECT E.Fname, E.Lname, D.Dependent_name FROM EMPLOYEE E, DEPENDENT D WHERE E.Sex='F' AND E.Ssn=D.Essn", expect=1,
  keys=["σ Sex='F'","π로 필요한 속성만","×","σ Ssn=Essn","π 결과"])
Q("6-cp-5","ra-cartesian","mc","COMPANY 상태에서 EMPLOYEE × DEPARTMENT의 투플 수와 속성 수는?",
  1, choices=["11개, 14개","24개, 14개","24개, 10개","8개, 4개"])

# ───────── L6-4 JOIN · DIVISION ─────────
Q("6-jn-1","ra-join","mc","R ⋈<조건> S 와 같은 식은?",
  0, choices=["σ<조건>(R × S)","π<조건>(R × S)","R ∪ S","R − S"])
RAQ("6-jn-2","ra-join","각 부서의 이름과 그 부서 관리자의 성, 이름을 관계 대수로 쓰시오.",
  "DEPT_MGR ← DEPARTMENT ⋈ Mgr_ssn=Ssn EMPLOYEE\nRESULT   ← π Dname, Lname, Fname (DEPT_MGR)",
  "SELECT D.Dname, E.Lname, E.Fname FROM DEPARTMENT D, EMPLOYEE E WHERE D.Mgr_ssn=E.Ssn", expect=3,
  keys=["DEPARTMENT ⋈ Mgr_ssn=Ssn EMPLOYEE","π Dname, Lname, Fname"])
RAQ("6-jn-3","ra-join","'ProductX' 프로젝트에서 일하는 사원의 이름과 근무 시간을 관계 대수로 쓰시오.",
  "PX     ← σ Pname='ProductX' (PROJECT)\nPX_W   ← PX ⋈ Pnumber=Pno WORKS_ON\nPX_E   ← PX_W ⋈ Essn=Ssn EMPLOYEE\nRESULT ← π Fname, Lname, Hours (PX_E)",
  "SELECT E.Fname, E.Lname, W.Hours FROM PROJECT P, WORKS_ON W, EMPLOYEE E WHERE P.Pname='ProductX' AND P.Pnumber=W.Pno AND W.Essn=E.Ssn", expect=2,
  keys=["σ Pname='ProductX'","⋈ Pnumber=Pno","⋈ Essn=Ssn","π"])
RAQ("6-jn-4","ra-join","'Houston'에 사는 사원이 일하는 프로젝트의 이름을 관계 대수로 쓰시오.",
  "HOU    ← σ Address LIKE '%Houston%' (EMPLOYEE)      (교재식: Address에 Houston이 들어간 사원)\nHOU_W  ← HOU ⋈ Ssn=Essn WORKS_ON\nHOU_P  ← HOU_W ⋈ Pno=Pnumber PROJECT\nRESULT ← π Pname (HOU_P)",
  "SELECT DISTINCT P.Pname FROM EMPLOYEE E, WORKS_ON W, PROJECT P WHERE E.Address LIKE '%Houston%' AND E.Ssn=W.Essn AND W.Pno=P.Pnumber", expect=6,
  keys=["σ (Houston 사원)","⋈ Ssn=Essn","⋈ Pno=Pnumber","π Pname (중복 제거)"])
Q("6-jn-5","ra-join","short","JOIN과 카티션 곱의 관계를 설명하시오.",
  "JOIN은 카티션 곱 다음에 SELECT를 적용한 것과 같다: R ⋈<조건> S = σ<조건>(R × S). 두 연산(×, σ)을 한 번의 JOIN으로 바꿀 수 있고, JOIN 결과에는 조건을 만족하는 투플 조합만 들어간다.",
  keys=["R ⋈ S = σ(R × S)","조건 만족 조합만"])
Q("6-jn-6","ra-join","ox","JOIN 결과의 속성은 R의 속성 다음에 S의 속성이 이어진 것이다 (Q(A₁…Aₙ, B₁…Bₘ)).",True)
RAQ("6-jn-7","ra-join","'Research' 부서에서 일하는 모든 사원의 이름과 주소를 관계 대수로 쓰시오. (연습 1)",
  "RESEARCH_DEPT ← σ Dname='Research' (DEPARTMENT)\nRESEARCH_EMPS ← RESEARCH_DEPT ⋈ Dnumber=Dno EMPLOYEE\nRESULT        ← π Fname, Lname, Address (RESEARCH_EMPS)",
  "SELECT E.Fname, E.Lname, E.Address FROM DEPARTMENT D, EMPLOYEE E WHERE D.Dname='Research' AND D.Dnumber=E.Dno", expect=4,
  keys=["σ Dname='Research'","⋈ Dnumber=Dno","π Fname, Lname, Address"])
Q("6-jv-1","join-variants","mc","비교 연산자로 = 만 쓰는 조인은?",
  1, choices=["세타 조인","동등 조인 (EQUIJOIN)","외부 조인","카티션 곱"])
Q("6-jv-2","join-variants","mc","자연 조인(*)에 대한 설명으로 옳은 것은?",
  2, choices=["조인 조건을 직접 써야 한다","= 이외의 연산자도 쓴다","이름이 같은 속성으로 동등 조인하고 중복 속성 하나를 없앤다","짝이 없는 투플도 남긴다"])
Q("6-jv-3","join-variants","ox","동등 조인 결과에는 값이 똑같은 속성 쌍이 생기는데, 그중 하나는 불필요하다.",True)
Q("6-jv-4","join-variants","calc","PROJECT(Pname, Pnumber, Plocation, Dnum)와 DEPARTMENT(Dname, Dnumber, Mgr_ssn, Mgr_start_date)를 자연 조인하려면 어떻게 해야 하는지 관계 대수로 쓰시오.",
  "DEPT      ← ρ (Dname, Dnum, Mgr_ssn, Mgr_start_date) (DEPARTMENT)\nPROJ_DEPT ← PROJECT * DEPT\n(조인 속성 이름이 Dnum과 Dnumber로 달라서 먼저 RENAME으로 맞춘다)",
  keys=["ρ로 Dnumber → Dnum","PROJECT * DEPT"], code=C.COMPANY_SCHEMA)
Q("6-jv-5","join-variants","short","세타 조인, 동등 조인, 자연 조인을 구별해서 설명하시오.",
  "세타 조인: 일반 조인 조건 Aᵢ θ Bⱼ (θ ∈ {=, <, ≤, >, ≥, ≠})를 AND로 연결. 동등 조인: 비교 연산자로 = 만 쓴 세타 조인, 결과에 같은 값의 속성 쌍이 생김. 자연 조인(*): 이름이 같은 속성으로 동등 조인하고 중복 속성 하나를 제거, 이름이 다르면 먼저 RENAME.",
  keys=["세타 = 일반 비교 연산","동등 = = 만","자연 = 같은 이름 + 중복 제거"])
Q("6-jv-6","join-variants","mc","DEPARTMENT * DEPT_LOCATIONS 의 조인 속성은?",
  0, choices=["Dnumber (두 릴레이션에 같은 이름)","Dname","Dlocation","조인 속성 없음 → 카티션 곱"])
Q("6-js-1","join-size","mc","|R| = 8, |S| = 3일 때 R ⋈ S 결과 투플 수의 범위는?",
  2, choices=["정확히 8","3 이상 8 이하","0 이상 24 이하","8 이상 24 이하"])
Q("6-js-2","join-size","short","조인 선택도(join selectivity)를 정의하고 어디에 쓰는지 쓰시오.",
  "조인 선택도 = 예상 조인 결과 크기 / (|R| × |S|). 질의 최적화에서 질의 계획의 비용을 추정하는 데 쓴다.",
  keys=["예상 결과 크기 / (|R| × |S|)","질의 계획 비용 추정"])
Q("6-js-3","join-size","ox","조인 조건이 없으면 조인 결과는 카티션 곱과 같다.",True)
Q("6-div-1","ra-division","mc","R(Z) ÷ S(X) = T(Y)에서 Y는?",
  1, choices=["X","Z − X","Z ∪ X","Z ∩ X"])
Q("6-div-2","ra-division","calc","R(A, B) = {(a1,b1), (a2,b1), (a3,b1), (a4,b1), (a1,b2), (a3,b2), (a2,b3), (a3,b3), (a4,b3), (a1,b4), (a2,b4), (a3,b4)}, S(A) = {a1, a2, a3}일 때 T ← R ÷ S 를 구하시오.",
  "T(B) = {b1, b4}\nb1: a1, a2, a3 모두와 짝 → 포함\nb2: a1, a3만 → 제외\nb3: a2, a3만 (a1 없음) → 제외\nb4: a1, a2, a3 → 포함",
  keys=["T의 속성 = B","b1 포함","b4 포함","b2, b3 제외"])
RAQ("6-div-3","ra-division","'John Smith'가 일하는 모든 프로젝트에서 일하는 사원의 이름을 DIVISION으로 쓰시오.",
  "SMITH      ← σ Fname='John' AND Lname='Smith' (EMPLOYEE)\nSMITH_PNOS ← π Pno (WORKS_ON ⋈ Essn=Ssn SMITH)\nSSN_PNOS   ← π Essn, Pno (WORKS_ON)\nSSNS(Ssn)  ← SSN_PNOS ÷ SMITH_PNOS\nRESULT     ← π Fname, Lname (SSNS * EMPLOYEE)",
  "SELECT E.Fname, E.Lname FROM EMPLOYEE E WHERE NOT EXISTS (SELECT W1.Pno FROM WORKS_ON W1, EMPLOYEE S WHERE W1.Essn=S.Ssn AND S.Fname='John' AND S.Lname='Smith' AND NOT EXISTS (SELECT * FROM WORKS_ON W2 WHERE W2.Essn=E.Ssn AND W2.Pno=W1.Pno))", expect=2,
  keys=["SMITH_PNOS (분모)","SSN_PNOS(Essn, Pno) (분자)","÷","SSNS(Ssn)로 이름 바꿔 EMPLOYEE와 자연 조인"])
RAQ("6-div-4","ra-division","Stafford에 있는 모든 프로젝트에서 일하는 사원의 Ssn을 DIVISION으로 쓰시오.",
  "STAFF_P(Pno) ← π Pnumber (σ Plocation='Stafford' (PROJECT))\nSSN_PNOS     ← π Essn, Pno (WORKS_ON)\nRESULT       ← SSN_PNOS ÷ STAFF_P",
  "SELECT E.Ssn FROM EMPLOYEE E WHERE NOT EXISTS (SELECT * FROM PROJECT P WHERE P.Plocation='Stafford' AND NOT EXISTS (SELECT * FROM WORKS_ON W WHERE W.Essn=E.Ssn AND W.Pno=P.Pnumber))", expect=2,
  keys=["분모: Stafford 프로젝트 번호 (이름 Pno로)","분자: π Essn, Pno (WORKS_ON)","÷"])
Q("6-div-5","ra-division","short","DIVISION 연산이 필요한 질의의 특징과 SQL에서의 대응 패턴을 쓰시오.",
  "'모든 ~에 대해'(all) 조건이 들어간 질의 (예: 어떤 사원이 일하는 '모든' 프로젝트에서 일하는 사원). SQL에는 ÷가 없어서 NOT EXISTS ((분모 집합) EXCEPT (그 투플의 집합)) 또는 이중 NOT EXISTS로 쓴다.",
  keys=["'모든(all)' 조건","SQL: NOT EXISTS + EXCEPT 또는 이중 NOT EXISTS"])
Q("6-div-6","ra-division","ox","R(Z) ÷ S(X)에서 S의 속성 X는 R의 속성 Z의 부분집합이어야 한다.",True)
Q("6-cs-1","ra-complete","mc","관계 대수 연산의 완전 집합은?",
  3, choices=["{σ, π, ⋈, ∩}","{σ, π, ∪, ∩, ÷}","{σ, π, ×, ⋈, ÷, ℑ}","{σ, π, ∪, ρ, −, ×}"])
Q("6-cs-2","ra-complete","blank","교집합은 R ∩ S ≡ (R ∪ S) − ((R − S) ∪ (S − R)) 로, 조인은 R ⋈<조건> S ≡ (a)<조건>(R (b) S) 로 표현할 수 있다.",
  ["σ","×"], accept=[["σ","sigma","SELECT","시그마"],["×","x","X","CARTESIAN PRODUCT","카티션 곱"]])
Q("6-cs-3","ra-complete","short","∩와 ⋈가 완전 집합에 없는데도 별도 연산으로 두는 이유를 쓰시오.",
  "엄밀히는 ∩와 ⋈ 모두 완전 집합 {σ, π, ∪, ρ, −, ×}의 조합으로 표현할 수 있어 필요 없지만, DB 응용에서 아주 자주 쓰이기 때문에 편의상 별도 연산으로 둔다.",
  keys=["다른 연산으로 표현 가능","자주 쓰여서 편의상"])
Q("6-cs-4","ra-complete","ox","자연 조인은 RENAME, 카티션 곱, SELECT, PROJECT의 조합으로 표현할 수 있다.",True)

# ───────── L6-5 집계 · 외부 조인 ─────────
Q("6-agg-1","ra-aggregate","mc","Dno ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE)의 결과 속성 이름은? (이름 바꾸기 없음)",
  2, choices=["Dno, COUNT, AVERAGE","Dno, Ssn, Salary","Dno, Count_ssn, Average_salary","No_of_employees, Average_sal"])
Q("6-agg-2","ra-aggregate","mc","ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE) (그룹화 속성 없음)의 결과는? (COMPANY 상태)",
  0, choices=["투플 하나 (8, 35125)","투플 세 개","스칼라 숫자 두 개","투플 8개"])
RAQ("6-agg-3","ra-aggregate","부서마다 부서 번호, 사원 수, 평균 급여를 구하고 결과 속성 이름을 Dno, No_of_employees, Average_sal로 바꾸는 관계 대수를 쓰시오.",
  "ρ R(Dno, No_of_employees, Average_sal) ( Dno ℑ COUNT Ssn, AVERAGE Salary (EMPLOYEE) )",
  "SELECT Dno, COUNT(Ssn), AVG(Salary) FROM EMPLOYEE GROUP BY Dno", expect=3,
  keys=["그룹화 속성 Dno (ℑ 왼쪽)","함수 리스트 COUNT Ssn, AVERAGE Salary","ρ로 이름 바꾸기"])
RAQ("6-agg-4","ra-aggregate","프로젝트마다 프로젝트 번호와 총 근무 시간을 관계 대수로 쓰시오.",
  "Pno ℑ SUM Hours (WORKS_ON)",
  "SELECT Pno, SUM(Hours) FROM WORKS_ON GROUP BY Pno", expect=6, keys=["그룹화 속성 Pno","SUM Hours"])
Q("6-agg-5","ra-aggregate","short","기본 관계 대수 연산만으로 표현할 수 없는 요청 세 가지를 쓰시오.",
  "1) 집계 함수(SUM, AVERAGE, MAXIMUM, MINIMUM, COUNT)를 쓰는 요청. 2) 속성 값으로 투플을 그룹화하고 그룹마다 집계를 적용하는 요청. 3) 외부 조인 요청.",
  keys=["집계","그룹별 집계","외부 조인"])
Q("6-agg-6","ra-aggregate","blank","<그룹화 속성> ℑ <함수 리스트> (R)의 결과는 (a) 속성과 함수 리스트 원소마다 속성 하나로 이루어진다. 그룹화 속성이 없으면 결과는 투플 (b) 개다.",
  ["그룹화","1"], accept=[["그룹화","grouping","그룹화 속성","그룹"],["1","하나","한","one"]])
Q("6-ap-1","ra-agg-props","ox","관계 대수의 집계 함수는 적용할 때 중복을 제거한다.",False,
  explain="중복을 제거하지 않는다 (급여 합·평균을 제대로 구하려고).")
Q("6-ap-2","ra-agg-props","mc","관계 대수 집계에서 NULL 값은?",
  1, choices=["0으로 취급","고려하지 않는다","오류를 낸다","가장 작은 값으로 취급"])
Q("6-ap-3","ra-agg-props","short","'관계 대수는 닫힌 수학 체계'라는 말이 집계 함수에 대해 뜻하는 바를 쓰시오.",
  "집계 결과도 스칼라 숫자가 아니라 릴레이션이다. 값이 하나, 투플이 하나뿐이어도 릴레이션이라서 다른 관계 대수 연산의 입력으로 쓸 수 있다.",
  keys=["결과도 릴레이션 (스칼라 아님)","값·투플 하나여도"])
Q("6-oj-1","ra-outer","mc","EMPLOYEE ⟕ Ssn=Mgr_ssn DEPARTMENT 결과에 대한 설명으로 옳은 것은? (COMPANY 상태)",
  2, choices=["관리자 3명만 나온다","부서 3개만 나온다","사원 8명 모두 나오고, 관리하지 않는 사원의 부서 속성은 NULL","결과가 비어 있다"])
Q("6-oj-2","ra-outer","blank","⟕는 (a) 외부 조인, ⟖는 (b) 외부 조인, ⟗는 (c) 외부 조인이다.",
  ["LEFT","RIGHT","FULL"], accept=[["LEFT","left","왼쪽"],["RIGHT","right","오른쪽"],["FULL","full","완전","양쪽"]])
RAQ("6-oj-3","ra-outer","모든 사원의 이름과, 그 사원이 부서를 관리하면 그 부서 이름(관리하지 않으면 NULL)을 관계 대수로 쓰시오.",
  "TEMP   ← EMPLOYEE ⟕ Ssn=Mgr_ssn DEPARTMENT\nRESULT ← π Fname, Minit, Lname, Dname (TEMP)",
  "SELECT E.Fname, E.Minit, E.Lname, D.Dname FROM EMPLOYEE E LEFT OUTER JOIN DEPARTMENT D ON E.Ssn=D.Mgr_ssn", expect=8,
  keys=["⟕ (LEFT OUTER JOIN) Ssn=Mgr_ssn","π Fname, Minit, Lname, Dname"])
Q("6-oj-4","ra-outer","short","내부 조인(EQUIJOIN, NATURAL JOIN)으로는 안 되고 외부 조인이 필요한 상황을 예와 함께 쓰시오.",
  "내부 조인은 조건을 만족하는 투플만 남겨서 짝이 없는 투플이 결과에서 빠진다. 짝이 없어도 한쪽 릴레이션의 투플을 모두 남기고 싶을 때 외부 조인을 쓴다. 예: 모든 사원 목록에 관리하는 부서 이름을 붙이되, 관리하지 않는 사원도 NULL로 포함.",
  keys=["내부 조인은 짝 없는 투플이 빠짐","외부 조인은 모두 남기고 NULL로 채움","예"])
RAQ("6-oj-5","ra-outer","모든 부서의 이름과, 그 부서가 통제하는 프로젝트가 있으면 프로젝트 이름을 관계 대수로 쓰시오 (프로젝트가 없는 부서도 포함).",
  "TEMP   ← DEPARTMENT ⟕ Dnumber=Dnum PROJECT\nRESULT ← π Dname, Pname (TEMP)",
  "SELECT D.Dname, P.Pname FROM DEPARTMENT D LEFT OUTER JOIN PROJECT P ON D.Dnumber=P.Dnum", expect=6,
  keys=["DEPARTMENT ⟕ PROJECT","Dnumber=Dnum","π Dname, Pname"], note="COMPANY 상태에서는 모든 부서가 프로젝트를 통제해서 NULL 행이 없다.")

# ───────── L6-6 작성 연습 ─────────
RAQ("6-pj-1","ra-practice-join","'Stafford'에 있는 모든 프로젝트에 대해 프로젝트 번호, 통제 부서 번호, 부서 관리자의 성, 주소, 생일을 관계 대수로 쓰시오. (연습 2)",
  "STAFFORD_PROJS ← σ Plocation='Stafford' (PROJECT)\nCONTR_DEPTS    ← STAFFORD_PROJS ⋈ Dnum=Dnumber DEPARTMENT\nPROJ_DEPT_MGRS ← CONTR_DEPTS ⋈ Mgr_ssn=Ssn EMPLOYEE\nRESULT         ← π Pnumber, Dnum, Lname, Address, Bdate (PROJ_DEPT_MGRS)",
  "SELECT P.Pnumber, P.Dnum, E.Lname, E.Address, E.Bdate FROM PROJECT P, DEPARTMENT D, EMPLOYEE E WHERE P.Plocation='Stafford' AND P.Dnum=D.Dnumber AND D.Mgr_ssn=E.Ssn", expect=2,
  keys=["σ Plocation='Stafford'","⋈ Dnum=Dnumber","⋈ Mgr_ssn=Ssn","π 5개 속성"])
RAQ("6-pj-2","ra-practice-join","'Administration' 부서에서 일하는 사원이 일하는 프로젝트의 이름과 그 사원의 성을 관계 대수로 쓰시오.",
  "ADMIN    ← σ Dname='Administration' (DEPARTMENT)\nADMIN_E  ← ADMIN ⋈ Dnumber=Dno EMPLOYEE\nADMIN_W  ← ADMIN_E ⋈ Ssn=Essn WORKS_ON\nADMIN_P  ← ADMIN_W ⋈ Pno=Pnumber PROJECT\nRESULT   ← π Lname, Pname (ADMIN_P)",
  "SELECT DISTINCT E.Lname, P.Pname FROM DEPARTMENT D, EMPLOYEE E, WORKS_ON W, PROJECT P WHERE D.Dname='Administration' AND D.Dnumber=E.Dno AND E.Ssn=W.Essn AND W.Pno=P.Pnumber", expect=6,
  keys=["σ Dname","⋈ Dnumber=Dno","⋈ Ssn=Essn","⋈ Pno=Pnumber","π"])
RAQ("6-pj-3","ra-practice-join","부양가족 중 배우자(Relationship='Spouse')가 있는 사원의 이름과 배우자 이름을 관계 대수로 쓰시오.",
  "SPOUSES ← σ Relationship='Spouse' (DEPENDENT)\nES      ← EMPLOYEE ⋈ Ssn=Essn SPOUSES\nRESULT  ← π Fname, Lname, Dependent_name (ES)",
  "SELECT E.Fname, E.Lname, D.Dependent_name FROM EMPLOYEE E, DEPENDENT D WHERE D.Relationship='Spouse' AND E.Ssn=D.Essn", expect=3,
  keys=["σ Relationship='Spouse'","⋈ Ssn=Essn","π"])
RAQ("6-pj-4","ra-practice-join","Houston에 위치(DEPT_LOCATIONS)가 있는 부서의 이름과 그 부서 관리자의 성을 관계 대수로 쓰시오.",
  "HLOC   ← σ Dlocation='Houston' (DEPT_LOCATIONS)\nHDEPT  ← HLOC * DEPARTMENT                    (공통 속성 Dnumber로 자연 조인)\nHMGR   ← HDEPT ⋈ Mgr_ssn=Ssn EMPLOYEE\nRESULT ← π Dname, Lname (HMGR)",
  "SELECT D.Dname, E.Lname FROM DEPT_LOCATIONS L, DEPARTMENT D, EMPLOYEE E WHERE L.Dlocation='Houston' AND L.Dnumber=D.Dnumber AND D.Mgr_ssn=E.Ssn", expect=2,
  keys=["σ Dlocation='Houston'","* DEPARTMENT (Dnumber)","⋈ Mgr_ssn=Ssn","π Dname, Lname"])
Q("6-pj-5","ra-practice-join","short","관계 대수 질의를 작성할 때의 일반적인 순서(요령)를 쓰시오.",
  "조건이 걸린 릴레이션에 먼저 σ를 적용해 투플 수를 줄이고, FK–PK 관계를 따라 ⋈로 필요한 릴레이션을 잇고, 마지막에 π로 원하는 속성만 남긴다. 각 단계를 중간 릴레이션 이름으로 나눠 쓴다.",
  keys=["σ 먼저","FK–PK 따라 ⋈","마지막에 π","중간 릴레이션으로 나눔"])
Q("6-pj-6","ra-practice-join","ox","관계 대수에서 σ를 조인보다 먼저 적용하면 중간 결과가 작아져 효율적이다.",True)
RAQ("6-pu-1","ra-practice-union","성이 'Smith'인 사원이 일꾼으로든, 그 프로젝트를 통제하는 부서의 관리자로든 관련된 프로젝트 번호를 관계 대수로 쓰시오. (연습 3)",
  "SMITHS(Essn)             ← π Ssn (σ Lname='Smith' (EMPLOYEE))\nSMITH_WORKER_PROJS       ← π Pno (WORKS_ON * SMITHS)\nMGRS                     ← π Lname, Dnumber (EMPLOYEE ⋈ Ssn=Mgr_ssn DEPARTMENT)\nSMITH_MANAGED_DEPTS(Dnum) ← π Dnumber (σ Lname='Smith' (MGRS))\nSMITH_MGR_PROJS(Pno)     ← π Pnumber (SMITH_MANAGED_DEPTS * PROJECT)\nRESULT                   ← SMITH_WORKER_PROJS ∪ SMITH_MGR_PROJS",
  "SELECT W.Pno FROM WORKS_ON W, EMPLOYEE E WHERE W.Essn=E.Ssn AND E.Lname='Smith' UNION SELECT P.Pnumber FROM PROJECT P, DEPARTMENT D, EMPLOYEE E WHERE P.Dnum=D.Dnumber AND D.Mgr_ssn=E.Ssn AND E.Lname='Smith'", expect=2,
  keys=["일꾼 쪽: SMITHS(Essn) * WORKS_ON","관리자 쪽: Mgr_ssn 조인 → Dnum → PROJECT","속성 이름을 Pno로 맞춤","∪"])
RAQ("6-pu-2","ra-practice-union","4번 부서가 통제하는 프로젝트이거나, 'Wong'이 일하는 프로젝트의 번호를 관계 대수로 쓰시오.",
  "D4_PROJS(Pno) ← π Pnumber (σ Dnum=4 (PROJECT))\nWONG(Essn)    ← π Ssn (σ Lname='Wong' (EMPLOYEE))\nWONG_PROJS    ← π Pno (WORKS_ON * WONG)\nRESULT        ← D4_PROJS ∪ WONG_PROJS",
  "SELECT Pnumber FROM PROJECT WHERE Dnum=4 UNION SELECT W.Pno FROM WORKS_ON W, EMPLOYEE E WHERE W.Essn=E.Ssn AND E.Lname='Wong'", expect=5,
  keys=["σ Dnum=4 → π (이름 Pno)","Wong의 프로젝트","∪ (타입 호환)"])
Q("6-pu-3","ra-practice-union","short","연습 3에서 SMITHS(Essn), SMITH_MGR_PROJS(Pno)처럼 속성 이름을 바꾸는 이유를 쓰시오.",
  "SMITHS(Essn)은 WORKS_ON과 자연 조인할 때 Essn으로 조인되게 하려고, SMITH_MGR_PROJS(Pno)는 SMITH_WORKER_PROJS(Pno)와 ∪할 때 두 결과의 속성 이름을 맞추려고(타입 호환, 결과 속성 이름 통일) 바꾼다.",
  keys=["자연 조인 속성 맞추기","∪를 위한 이름 맞추기"])
RAQ("6-pu-4","ra-practice-union","Houston에 사는 사원이거나 Houston에 있는 프로젝트에서 일하는 사원의 Ssn을 관계 대수로 쓰시오.",
  "LIVE(Ssn)  ← π Ssn (σ Address LIKE '%Houston%' (EMPLOYEE))\nHP(Pno)    ← π Pnumber (σ Plocation='Houston' (PROJECT))\nWORK(Ssn)  ← π Essn (WORKS_ON * HP)\nRESULT     ← LIVE ∪ WORK",
  "SELECT Ssn FROM EMPLOYEE WHERE Address LIKE '%Houston%' UNION SELECT W.Essn FROM WORKS_ON W, PROJECT P WHERE W.Pno=P.Pnumber AND P.Plocation='Houston'", expect=7,
  keys=["사는 곳 σ → π Ssn","Houston 프로젝트 → WORKS_ON → π Essn (이름 Ssn)","∪"])
RAQ("6-pd-1","ra-practice-diff","부양가족이 없는 사원의 이름을 관계 대수로 쓰시오. (연습 4)",
  "ALL_EMPS            ← π Ssn (EMPLOYEE)\nEMPS_WITH_DEPS(Ssn) ← π Essn (DEPENDENT)\nEMPS_WITHOUT_DEPS   ← ALL_EMPS − EMPS_WITH_DEPS\nRESULT              ← π Lname, Fname (EMPS_WITHOUT_DEPS * EMPLOYEE)",
  "SELECT Lname, Fname FROM EMPLOYEE WHERE Ssn NOT IN (SELECT Essn FROM DEPENDENT)", expect=5,
  keys=["π Ssn (EMPLOYEE)","π Essn (DEPENDENT), 이름 Ssn","−","EMPLOYEE와 자연 조인 후 π"])
RAQ("6-pd-2","ra-practice-diff","부양가족이 하나 이상 있는 관리자의 이름을 관계 대수로 쓰시오. (연습 5)",
  "MGRS(Ssn)           ← π Mgr_ssn (DEPARTMENT)\nEMPS_WITH_DEPS(Ssn) ← π Essn (DEPENDENT)\nMGRS_WITH_DEPS      ← MGRS ∩ EMPS_WITH_DEPS\nRESULT              ← π Lname, Fname (MGRS_WITH_DEPS * EMPLOYEE)",
  "SELECT Lname, Fname FROM EMPLOYEE WHERE Ssn IN (SELECT Mgr_ssn FROM DEPARTMENT) AND Ssn IN (SELECT Essn FROM DEPENDENT)", expect=2,
  keys=["π Mgr_ssn → Ssn","π Essn → Ssn","∩","자연 조인 후 π"])
RAQ("6-pd-3","ra-practice-diff","어떤 프로젝트에서도 일하지 않는 사원의 이름을 관계 대수로 쓰시오.",
  "ALL_EMPS     ← π Ssn (EMPLOYEE)\nWORKERS(Ssn) ← π Essn (WORKS_ON)\nIDLE         ← ALL_EMPS − WORKERS\nRESULT       ← π Fname, Lname (IDLE * EMPLOYEE)",
  "SELECT Fname, Lname FROM EMPLOYEE WHERE Ssn NOT IN (SELECT Essn FROM WORKS_ON)", expect=0,
  keys=["π Ssn (EMPLOYEE)","π Essn (WORKS_ON)","−"], note="COMPANY 상태에선 모든 사원이 WORKS_ON에 있어 결과가 비어 있다.")
RAQ("6-pd-4","ra-practice-diff","부하가 없는(아무도 감독하지 않는) 사원의 이름을 관계 대수로 쓰시오.",
  "ALL_EMPS   ← π Ssn (EMPLOYEE)\nSUPS(Ssn)  ← π Super_ssn (EMPLOYEE)\nNON_SUPS   ← ALL_EMPS − SUPS\nRESULT     ← π Fname, Lname (NON_SUPS * EMPLOYEE)",
  "SELECT Fname, Lname FROM EMPLOYEE WHERE Ssn NOT IN (SELECT Super_ssn FROM EMPLOYEE WHERE Super_ssn IS NOT NULL)", expect=5,
  keys=["π Super_ssn을 Ssn으로 이름 바꿈","ALL_EMPS − SUPS","자연 조인 후 π"])
RAQ("6-pd-5","ra-practice-diff","4번 부서 사원이면서 Stafford에 있는 프로젝트에서 일하는 사원의 Ssn을 교집합으로 쓰시오.",
  "D4(Ssn)     ← π Ssn (σ Dno=4 (EMPLOYEE))\nSP(Pno)     ← π Pnumber (σ Plocation='Stafford' (PROJECT))\nSW(Ssn)     ← π Essn (WORKS_ON * SP)\nRESULT      ← D4 ∩ SW",
  "SELECT Ssn FROM EMPLOYEE WHERE Dno=4 INTERSECT SELECT W.Essn FROM WORKS_ON W, PROJECT P WHERE W.Pno=P.Pnumber AND P.Plocation='Stafford'", expect=3,
  keys=["4번 부서 Ssn","Stafford 프로젝트 → 일하는 Essn (이름 Ssn)","∩"])
Q("6-pd-6","ra-practice-diff","mc","'~가 없는' 질의를 관계 대수로 쓸 때 주로 쓰는 연산은?",
  2, choices=["∪","∩","−","×"])
Q("6-pd-7","ra-practice-diff","short","SQL의 NOT EXISTS, EXISTS AND EXISTS, UNION, NOT EXISTS(EXCEPT)가 관계 대수의 어떤 연산에 대응하는지 쓰시오.",
  "'~가 없는' (NOT EXISTS / NOT IN) → 차집합 −. 'A이면서 B' (EXISTS AND EXISTS / INTERSECT) → 교집합 ∩. 'A이거나 B' (UNION) → 합집합 ∪. '모든 ~' (NOT EXISTS + EXCEPT) → 나눗셈 ÷.",
  keys=["없는 = −","이면서 = ∩","이거나 = ∪","모든 = ÷"])
