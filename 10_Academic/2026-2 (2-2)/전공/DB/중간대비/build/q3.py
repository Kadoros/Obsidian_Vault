from qdsl import Q

# ───────── L3-1 기본 개념 ─────────
Q("3-rm-1","rel-model","mc","관계 데이터 모델을 제안한 사람과 시기는?",
  1, choices=["Peter Chen, 1976","Ted Codd (IBM), 1970","Chamberlin & Boyce, 1974","Elmasri, 1994"])
Q("3-rm-2","rel-model","short","관계 데이터 모델의 장점 네 가지를 쓰시오.",
  "단순성(평평한 테이블 구조), 데이터 무결성(유효·일관·정확한 데이터 보장), 쉬운 데이터 조작(SQL 같은 고급 언어), 보안(인증, 권한, 암호화).",
  keys=["단순성","데이터 무결성","쉬운 데이터 조작 (SQL)","보안"])
Q("3-rm-3","rel-model","blank","관계 모델에서 릴레이션은 테이블, 투플은 (a), 속성은 (b) 에 해당한다.",
  ["행","열"], accept=[["행","row","레코드"],["열","column","열 헤더","컬럼"]])
Q("3-dom-1","domain-schema","mc","릴레이션 스키마의 '차수(degree)'는?",
  0, choices=["속성의 수","투플의 수","키의 수","외래 키의 수"])
Q("3-dom-2","domain-schema","mc","STUDENT(Name, Ssn, Home_phone, Address, Office_phone, Age, Gpa)에 투플이 5개 있다. 차수는?",
  2, choices=["5","6","7","35"])
Q("3-dom-3","domain-schema","blank","도메인 = 데이터 (a) + (b) 이다. 예) Employee_ages: 15~80 사이의 정수.",
  ["타입","제약조건"], accept=[["타입","type","자료형","데이터 타입"],["제약조건","제약","constraint","constraints"]])
Q("3-dom-4","domain-schema","ox","투플은 n개 값의 순서 있는 리스트이며, 각 값은 해당 속성 도메인의 원소이거나 NULL이다.",True)
Q("3-dom-5","domain-schema","short","릴레이션 스키마와 릴레이션 인스턴스(상태)를 구별해서 설명하시오.",
  "릴레이션 스키마 R(A₁, …, Aₙ): 릴레이션 이름과 속성 리스트 (구조, 잘 안 바뀜). 릴레이션 인스턴스 r(R): 어느 시점의 n-투플들의 집합 {t₁, …, tₘ} (데이터, 갱신으로 계속 바뀜).",
  keys=["스키마 = 이름 + 속성 리스트","인스턴스 = 투플의 집합 (시점에 따라 바뀜)"])
Q("3-ch-1","rel-chars","ox","관계 모델에서는 다중값 속성을 한 칸에 집합으로 저장할 수 있다.",False,
  explain="투플의 값은 원자 값이어야 한다. 다중값 속성은 별도 릴레이션으로.")
Q("3-ch-2","rel-chars","mc","관계 모델에서 복합 속성 Address(Street, City, Zip)를 표현하는 방법은?",
  1, choices=["별도 릴레이션으로","단순 구성 속성 Street, City, Zip으로","문자열 하나로 합쳐서","표현할 수 없다"])
Q("3-ch-3","rel-chars","short","NULL 값이 쓰이는 경우를 쓰시오.",
  "속성 값을 모르거나(unknown), 얻을 수 없거나(unavailable), 그 투플에 적용되지 않는(undefined / not applicable) 경우.",
  keys=["모름 (unknown)","얻을 수 없음 (unavailable)","해당 없음 (not applicable)"])
Q("3-ch-4","rel-chars","ox","릴레이션은 투플의 집합이므로 정의상 같은 투플이 두 번 나올 수 없다.",True)
Q("3-st-1","db-schema-state","mc","관계 DB 스키마 S를 이루는 것은?",
  2, choices=["릴레이션 상태들의 집합","투플들의 집합","릴레이션 스키마들의 집합 + 무결성 제약조건 집합 IC","카탈로그와 뷰"])
Q("3-st-2","db-schema-state","ox","무결성 제약을 하나라도 어기는 DB 상태는 무효(invalid) 상태이다.",True)
Q("3-st-3","db-schema-state","mc","COMPANY 관계 DB 스키마 그림에서 화살표가 나타내는 것은?",
  1, choices=["기본 키","참조 무결성 (FK → 참조되는 PK)","함수 종속","카디널리티 비"])
Q("3-st-4","db-schema-state","short","관계 DB 스키마와 관계 DB 상태를 정의하고, '유효한 상태'란 무엇인지 쓰시오.",
  "관계 DB 스키마: 릴레이션 스키마들의 집합 {R₁…Rₘ}과 무결성 제약조건 집합 IC. 관계 DB 상태: 각 Rᵢ의 상태 rᵢ들의 집합. 유효한 상태: IC에 있는 모든 무결성 제약조건을 만족하는 상태.",
  keys=["스키마 = 릴레이션 스키마 집합 + IC","상태 = 릴레이션 상태들의 집합","유효 = 모든 제약 만족"])

# ───────── L3-2 키 · 무결성 ─────────
Q("3-key-1","superkey-key","mc","슈퍼키와 키의 차이는?",
  1, choices=["키는 속성이 하나뿐이다","키는 최소성(어떤 속성을 빼도 슈퍼키가 아님)을 만족한다","슈퍼키는 NULL을 허용한다","차이가 없다"])
Q("3-key-2","superkey-key","ox","모든 키는 슈퍼키이지만, 모든 슈퍼키가 키인 것은 아니다.",True)
Q("3-key-3","superkey-key","mc","EMPLOYEE(Ssn, Fname, Lname, …)에서 Ssn이 키일 때 {Ssn, Lname}은?",
  0, choices=["슈퍼키지만 키는 아님","키","후보 키","슈퍼키도 아님"])
Q("3-key-4","superkey-key","blank","키 제약: 서로 다른 두 투플 t₁, t₂에 대해 t₁[(a)] ≠ t₂[(a)] 이다. 키는 (b) 슈퍼키이다.",
  ["SK","최소"], accept=[["SK","슈퍼키","superkey","키"],["최소","minimal","최소한의"]])
Q("3-key-5","superkey-key","short","슈퍼키와 키를 정의하고, {Ssn, Home_phone}을 예로 차이를 설명하시오.",
  "슈퍼키: 각 투플을 유일하게 식별하는 속성 부분집합 (서로 다른 두 투플이 같은 값을 가질 수 없음). 키: 슈퍼키 중에서 어떤 속성을 빼도 더 이상 슈퍼키가 아닌 최소 슈퍼키. {Ssn, Home_phone}은 슈퍼키지만 Home_phone을 빼도 {Ssn}이 여전히 유일하므로 키가 아니고, {Ssn}이 키다.",
  keys=["슈퍼키 정의 (유일 식별)","키 = 최소 슈퍼키","예: Home_phone 빼도 유일 → {Ssn}이 키"])
Q("3-key-6","superkey-key","calc","R(A, B, C, D)의 상태가 다음과 같을 때, 이 상태에서 슈퍼키가 될 수 있는 속성 집합 중 '키(최소 슈퍼키)'를 모두 쓰시오.\n\nA | B | C | D\n1 | x | p | 10\n2 | x | q | 10\n3 | y | p | 20\n4 | y | q | 20",
  "{A}, {B, C}, {C, D}\n\nA는 값이 모두 달라 혼자 키. B, C, D는 각각 중복이 있음. {B,C}: (x,p),(x,q),(y,p),(y,q) 모두 다름 → 키. {C,D}: (p,10),(q,10),(p,20),(q,20) 모두 다름 → 키. {B,D}: (x,10),(x,10) 중복 → 아님.",
  keys=["{A}","{B, C}","{C, D}","{B, D}는 아님"], explain="엄밀히 키는 스키마(모든 가능한 상태)에 대한 성질이라, 상태 하나만 보고는 '키일 수 있는 것'만 판단한다.")
Q("3-key-7","superkey-key","ox","모든 릴레이션은 최소 하나의 슈퍼키를 가진다.",True,
  explain="투플은 서로 다르므로 속성 전체 집합이 기본 슈퍼키.")
Q("3-ck-1","candidate-pk","mc","CAR(License_number, Engine_serial_number, Make, Model, Year)에서 License_number와 Engine_serial_number가 각각 키라면 이 둘을 무엇이라 부르나?",
  2, choices=["슈퍼키","외래 키","후보 키","부분 키"])
Q("3-ck-2","candidate-pk","ox","기본 키는 보통 속성 하나 또는 적은 수의 속성으로 된 후보 키를 고르는 것이 좋다.",True)
Q("3-ck-3","candidate-pk","short","후보 키와 기본 키의 관계를 설명하고, SQL에서 기본 키가 아닌 후보 키를 지정하는 절을 쓰시오.",
  "릴레이션 스키마의 키가 여러 개면 각각이 후보 키이고, 그중 하나를 투플 식별에 쓰는 기본 키로 지정한다(스키마에 밑줄). 나머지 후보 키는 SQL에서 UNIQUE 절로 지정한다.",
  keys=["키 여러 개 = 후보 키","하나를 PK로 지정","나머지는 UNIQUE"])
Q("3-ck-4","candidate-pk","mc","릴레이션 스키마 그림에서 기본 키는 어떻게 표시하나?",
  0, choices=["밑줄","굵은 글씨","화살표","이중선"])
Q("3-ei-1","entity-integrity","mc","개체 무결성 제약은?",
  1, choices=["FK 값은 참조되는 PK 값이거나 NULL","기본 키 값은 NULL일 수 없다","두 투플의 키 값은 같을 수 없다","모든 속성은 NULL일 수 없다"])
Q("3-ei-2","entity-integrity","short","개체 무결성 제약이 왜 필요한지 쓰시오.",
  "PK가 NULL인 투플이 둘 이상 있으면, 다른 릴레이션에서 그 투플들을 참조하려 할 때 서로 구별할 수 없기 때문. PK는 투플을 식별하는 데 쓰이므로 NULL이면 안 된다.",
  keys=["PK가 NULL이면 투플을 구별·참조할 수 없음"])
Q("3-ei-3","entity-integrity","ox","복합 기본 키 (Essn, Pno)에서는 Essn만 NULL이 아니면 Pno는 NULL이어도 된다.",False,
  explain="PK의 어느 부분도 NULL이면 안 된다.")
Q("3-ei-4","entity-integrity","mc","NULL이 들어 있는 Office_phone 속성에 대한 설명으로 옳은 것은?",
  3, choices=["후보 키가 될 수 있다","기본 키가 될 수 있다","외래 키여야 한다","개체 무결성 때문에 기본 키가 될 수 없다"])
Q("3-ri-1","ref-integrity","mc","참조 무결성 제약으로 옳은 것은?",
  0, choices=["FK 값은 참조되는 릴레이션의 어떤 투플의 PK 값과 같거나 NULL이다","FK 값은 NULL일 수 없다","PK 값은 NULL일 수 없다","FK는 자기 릴레이션을 참조할 수 없다"])
Q("3-ri-2","ref-integrity","ox","외래 키는 같은 릴레이션을 참조할 수도 있다.",True,
  explain="EMPLOYEE.Super_ssn → EMPLOYEE.Ssn.")
Q("3-ri-3","ref-integrity","blank","EMPLOYEE.Dno가 DEPARTMENT.Dnumber를 참조할 때, EMPLOYEE는 (a) 릴레이션, DEPARTMENT는 (b) 릴레이션이다.",
  ["참조하는","참조되는"], accept=[["참조하는","referencing","참조"],["참조되는","referenced","피참조"]])
Q("3-ri-4","ref-integrity","short","참조 무결성 제약을 정의하고, 이 제약이 없으면 생기는 문제를 예로 설명하시오.",
  "릴레이션 R₁의 FK 값은 R₂의 어떤 투플의 PK 값과 같거나 NULL이어야 한다 (FK와 PK는 같은 도메인). 없으면: EMPLOYEE.Dno = 3인데 3번 부서가 DEPARTMENT에 없으면 그 사원이 어느 부서에서 일하는지 해석할 수 없다. 두 릴레이션 투플 사이의 일관성을 지키려고 필요.",
  keys=["FK = 참조되는 PK 값 또는 NULL","없는 투플을 참조하면 의미를 해석할 수 없음 (예)"])
Q("3-ri-5","ref-integrity","calc","다음 스키마의 외래 키를 모두 쓰시오 (밑줄은 PK).\nSTUDENT(Ssn, Name, Major, Bdate)\nCOURSE(Course#, Cname, Dept)\nENROLL(Ssn, Course#, Quarter, Grade)  — PK (Ssn, Course#, Quarter)\nBOOK_ADOPTION(Course#, Quarter, Book_isbn)  — PK (Course#, Quarter)\nTEXT(Book_isbn, Book_title, Publisher, Author)",
  "ENROLL.Ssn → STUDENT.Ssn\nENROLL.Course# → COURSE.Course#\nBOOK_ADOPTION.Course# → COURSE.Course#\nBOOK_ADOPTION.Book_isbn → TEXT.Book_isbn",
  keys=["ENROLL.Ssn → STUDENT","ENROLL.Course# → COURSE","BOOK_ADOPTION.Course# → COURSE","BOOK_ADOPTION.Book_isbn → TEXT"])
Q("3-ri-6","ref-integrity","calc","다음 스키마의 외래 키를 모두 쓰고, 각각 왜 필요한지 한 줄씩 쓰시오.\nSALESPERSON(Ssn, Name, Start_year, Dept_no)\nTRIP(Ssn, From_city, To_city, Departure_date, Return_date, Trip_id)  — PK Trip_id\nEXPENSE(Trip_id, Account#, Amount)  — PK (Trip_id, Account#)",
  "TRIP.Ssn → SALESPERSON.Ssn: 출장은 존재하는 영업사원에게 배정돼야 함\nEXPENSE.Trip_id → TRIP.Trip_id: 경비는 특정 출장에 대해 지급됨",
  keys=["TRIP.Ssn → SALESPERSON","EXPENSE.Trip_id → TRIP","이유 각각"])
Q("3-ri-7","ref-integrity","ox","FK와 그것이 참조하는 PK는 같은 도메인을 가져야 한다.",True)

# ───────── L3-3 갱신 연산과 위반 ─────────
Q("3-ins-1","op-insert","mc","Insert 연산이 어길 수 있는 제약은?",
  3, choices=["참조 무결성만","키 제약만","키 제약과 참조 무결성","키 제약, 개체 무결성, 참조 무결성 모두"])
Q("3-ins-2","op-insert","mc","COMPANY 상태에서 EMPLOYEE에 <'Alicia', 'J', 'Zelaya', '999887777', …, '987654321', 4>를 삽입하면?",
  0, choices=["키 제약 위반 (Ssn 999887777이 이미 있음)","개체 무결성 위반","참조 무결성 위반","위반 없음"])
Q("3-ins-3","op-insert","mc","EMPLOYEE에 <'Cecilia', 'F', 'Kolonsky', '677678989', …, '987654321', 7>을 삽입하면? (DEPARTMENT에 Dnumber=7 없음)",
  2, choices=["키 제약 위반","개체 무결성 위반","참조 무결성 위반","위반 없음"])
Q("3-ins-4","op-insert","ox","EMPLOYEE에 <'Cecilia', 'F', 'Kolonsky', '677678989', …, NULL, 4>를 삽입하면 Super_ssn이 NULL이므로 참조 무결성을 어긴다.",False,
  explain="FK는 NULL이어도 된다. 이 삽입은 모든 제약을 만족.")
Q("3-ins-5","op-insert","calc","COMPANY 상태(교안 3-1 p.12)에서 다음 삽입 각각이 어기는 제약을 쓰시오 (없으면 '없음').\n(1) EMPLOYEE에 Ssn=NULL인 투플\n(2) EMPLOYEE에 Ssn='123456789'인 새 투플\n(3) WORKS_ON에 <'453453453', 10, 5.0>\n(4) WORKS_ON에 <'677678989', 1, 10.0>\n(5) DEPT_LOCATIONS에 <2, 'Seoul'>",
  "(1) 개체 무결성 (PK가 NULL)\n(2) 키 제약 (Smith가 이미 123456789)\n(3) 없음 (English는 있고 10번 프로젝트도 있고 (453453453, 10) 조합은 없음)\n(4) 참조 무결성 (Ssn 677678989인 사원 없음)\n(5) 참조 무결성 (Dnumber 2인 부서 없음)",
  keys=["(1) 개체 무결성","(2) 키 제약","(3) 없음","(4) 참조 무결성","(5) 참조 무결성"])
Q("3-ins-6","op-insert","blank","Insert에서 새 투플의 키 값이 이미 있으면 (a) 제약, PK의 일부가 NULL이면 (b) 제약, 참조하는 투플이 없으면 (c) 제약을 어긴다.",
  ["키","개체 무결성","참조 무결성"], accept=[["키","key","키 제약"],["개체 무결성","개체","entity","entity integrity"],["참조 무결성","참조","referential","referential integrity"]])
Q("3-del-1","op-delete","mc","Delete 연산이 어길 수 있는 제약은?",
  1, choices=["키 제약","참조 무결성만","개체 무결성","세 가지 모두"])
Q("3-del-2","op-delete","ox","WORKS_ON에서 (Essn='999887777', Pno=10) 투플을 지우면 참조 무결성을 어긴다.",False,
  explain="WORKS_ON 투플을 참조하는 투플이 없다.")
Q("3-del-3","op-delete","short","Delete가 참조 무결성 외의 제약을 어기지 않는 이유를 쓰시오.",
  "삭제는 새 값을 만들지 않으므로 키 중복(키 제약)이나 NULL PK(개체 무결성)가 생기지 않는다. 지운 투플을 다른 투플의 FK가 참조하고 있을 때만 그 FK가 존재하지 않는 투플을 가리키게 되어 참조 무결성이 깨진다.",
  keys=["새 값이 없어서 키·개체 무결성은 안 깨짐","참조되던 투플을 지우면 참조 무결성 위반"])
Q("3-del-4","op-delete","calc","COMPANY 상태에서 다음 삭제가 참조 무결성을 어기는지, 어긴다면 어느 릴레이션의 투플들이 참조하고 있는지 쓰시오.\n(1) EMPLOYEE에서 Ssn='999887777'\n(2) PROJECT에서 Pnumber=30\n(3) DEPENDENT에서 (Essn='123456789', Dependent_name='Michael')\n(4) DEPARTMENT에서 Dnumber=1",
  "(1) 위반: WORKS_ON 투플 2개 (Pno 30, 10)\n(2) 위반: WORKS_ON 투플 3개 (Zelaya, Jabbar, Wallace)\n(3) 위반 없음: DEPENDENT를 참조하는 릴레이션 없음\n(4) 위반: EMPLOYEE(Borg의 Dno=1), PROJECT(Reorganization의 Dnum=1), DEPT_LOCATIONS(1, Houston)",
  keys=["(1) WORKS_ON","(2) WORKS_ON","(3) 없음","(4) EMPLOYEE, PROJECT, DEPT_LOCATIONS"])
Q("3-upd-1","op-update","mc","Update 연산이 제약 문제를 일으키는 경우는?",
  2, choices=["어떤 속성을 바꿔도 항상","비키 속성을 바꿀 때만","PK나 FK 속성을 바꿀 때만","절대 일으키지 않음"])
Q("3-upd-2","op-update","mc","EMPLOYEE에서 Ssn='999887777'인 투플의 Ssn을 '987654321'로 바꾸면?",
  3, choices=["위반 없음","키 제약만","참조 무결성만","키 제약과 참조 무결성 둘 다"],
  explain="987654321은 Wallace의 Ssn(키 중복)이고, WORKS_ON에서 999887777을 참조하던 투플이 존재하지 않는 사원을 가리키게 됨.")
Q("3-upd-3","op-update","mc","EMPLOYEE에서 Ssn='999887777'의 Dno를 7로 바꾸면? (7번 부서 없음)",
  1, choices=["키 제약","참조 무결성","개체 무결성","위반 없음"])
Q("3-upd-4","op-update","ox","EMPLOYEE의 Salary를 바꾸는 갱신은 키·개체·참조 무결성 제약을 어기지 않는다.",True,
  explain="PK도 FK도 아닌 속성. (도메인 제약은 별개)")
Q("3-upd-5","op-update","calc","COMPANY 상태에서 다음 갱신이 어기는 제약을 쓰시오 (없으면 '없음').\n(1) PROJECT Pnumber=10의 Dnum을 5로\n(2) DEPARTMENT Dnumber=5의 Mgr_ssn을 '111111111'로\n(3) WORKS_ON (Essn='123456789', Pno=1)의 Pno를 2로\n(4) EMPLOYEE Ssn='888665555'의 Ssn을 NULL로",
  "(1) 없음 (5번 부서 있음)\n(2) 참조 무결성 (Ssn 111111111인 사원 없음)\n(3) 키 제약 ((123456789, 2) 투플이 이미 있음)\n(4) 개체 무결성 (PK를 NULL로) + 다른 투플이 888665555를 참조하므로 참조 무결성도",
  keys=["(1) 없음","(2) 참조 무결성","(3) 키 제약","(4) 개체 무결성 (+참조)"])
Q("3-upd-6","op-update","short","Insert, Delete, Update가 각각 어길 수 있는 제약을 정리하시오.",
  "Insert: 키 제약, 개체 무결성, 참조 무결성 모두 가능. Delete: 참조 무결성만. Update: 키 제약과 참조 무결성 (PK나 FK를 바꿀 때만 문제).",
  keys=["Insert = 세 가지 모두","Delete = 참조 무결성만","Update = 키·참조 (PK/FK 변경 시)"])

# ───────── L3-4 매핑 ① ─────────
Q("3-me-1","map-entity","mc","정규 개체 타입을 매핑할 때 복합 속성 Name(Fname, Minit, Lname)은?",
  1, choices=["별도 릴레이션으로","단순 구성 속성 Fname, Minit, Lname만 넣는다","Name 하나로 넣는다","FK로 넣는다"])
Q("3-me-2","map-entity","ox","정규 개체 타입을 매핑할 때 다중값 속성도 같은 릴레이션에 넣는다.",False,
  explain="다중값 속성은 별도 릴레이션 (다음 단계).")
Q("3-me-3","map-entity","short","정규 개체 타입 E를 릴레이션으로 매핑하는 절차를 쓰시오.",
  "E의 단순 속성을 모두 포함하는 릴레이션 R을 만든다. 복합 속성은 단순 구성 속성만 넣는다. E의 키 속성 중 하나를 R의 기본 키로 지정한다 (다중값 속성은 다음 단계에서 별도 릴레이션).",
  keys=["단순 속성 전부 포함","복합 → 구성 속성","키 하나를 PK로"])
Q("3-me-4","map-entity","mc","DEPARTMENT(Name, Number 둘 다 키)를 매핑할 때 Number를 PK로 고르면 Name은?",
  2, choices=["버린다","FK가 된다","UNIQUE 후보 키로 둔다","별도 릴레이션으로"])
Q("3-mv-1","map-multival","mc","DEPARTMENT의 다중값 속성 Locations를 매핑한 DEPT_LOCATIONS의 기본 키는?",
  2, choices=["Dnumber","Dlocation","(Dnumber, Dlocation)","새로 만든 Loc_id"])
Q("3-mv-2","map-multival","blank","다중값 속성 A는 별도 릴레이션 R로 만들고, 원래 릴레이션의 PK K를 R의 (a) 로 넣으며, (b) 조합을 R의 PK로 한다.",
  ["외래 키","A와 K"], accept=[["외래 키","FK","foreign key","외래키"],["A와 K","(A, K)","A, K","K와 A","(K, A)"]])
Q("3-mv-3","map-multival","calc","EMPLOYEE(Ssn 키)에 다중값 속성 {Phone}과 {Skill}이 있다. 이 둘을 매핑한 릴레이션들을 PK, FK와 함께 쓰시오.",
  "EMP_PHONE(Ssn, Phone)  PK (Ssn, Phone), FK Ssn → EMPLOYEE\nEMP_SKILL(Ssn, Skill)  PK (Ssn, Skill), FK Ssn → EMPLOYEE\n(다중값 속성마다 별도 릴레이션)",
  keys=["다중값 속성마다 별도 릴레이션 2개","PK = (Ssn, 속성)","FK Ssn → EMPLOYEE"])
Q("3-mv-4","map-multival","ox","다중값 속성을 매핑한 릴레이션에서는 원래 개체의 키 값이 여러 투플에 반복된다.",True)
Q("3-mw-1","map-weak","mc","약한 개체 DEPENDENT를 매핑한 릴레이션의 기본 키는?",
  1, choices=["Dependent_name","(Essn, Dependent_name)","Essn","새 대리 키"])
Q("3-mw-2","map-weak","ox","약한 개체를 매핑할 때 식별 관계 타입(DEPENDENTS_OF)은 별도 릴레이션으로 만든다.",False,
  explain="소유자 PK를 FK로 넣는 것 자체가 식별 관계의 매핑.")
Q("3-mw-3","map-weak","short","약한 개체 타입 W를 매핑하는 절차를 쓰시오.",
  "W의 단순 속성(복합은 구성 속성)을 모두 포함하는 릴레이션 R을 만든다. 소유 개체 타입의 PK를 R에 FK로 넣는다(식별 관계의 매핑). 소유자 PK와 W의 부분 키를 합쳐 R의 PK로 한다.",
  keys=["단순 속성 포함","소유자 PK를 FK로 (식별 관계 매핑)","PK = 소유자 PK + 부분 키"])
Q("3-mw-4","map-weak","calc","BUILDING(Bname 키, Address)과 약한 개체 ROOM(부분 키 Room_no, Capacity, {Equipment})이 식별 관계 HAS로 연결되어 있다. 관계 스키마로 매핑하시오 (PK, FK 표시).",
  "BUILDING(Bname, Address)  PK Bname\nROOM(Bname, Room_no, Capacity)  PK (Bname, Room_no), FK Bname → BUILDING\nROOM_EQUIPMENT(Bname, Room_no, Equipment)  PK (Bname, Room_no, Equipment), FK (Bname, Room_no) → ROOM",
  keys=["ROOM PK (Bname, Room_no)","ROOM.Bname FK","다중값 Equipment는 별도 릴레이션, PK에 ROOM의 PK 전체 포함"])

# ───────── L3-5 매핑 ② ─────────
Q("3-m11-1","map-11","mc","1:1 관계 MANAGES를 외래 키 방식으로 매핑할 때 FK를 넣기 좋은 쪽은?",
  1, choices=["부분 참여하는 EMPLOYEE","전체 참여하는 DEPARTMENT","어느 쪽이든 상관없음","별도 릴레이션"])
Q("3-m11-2","map-11","short","1:1 관계를 외래 키 방식으로 매핑할 때 전체 참여 쪽에 FK를 넣는 게 나은 이유를 MANAGES 예로 쓰시오.",
  "전체 참여 쪽(DEPARTMENT)은 모든 투플이 관계에 참여하므로 FK(Mgr_ssn)에 항상 값이 있다. 반대로 부분 참여 쪽(EMPLOYEE)에 D_managed, Mgr_start_date를 넣으면 부서를 관리하지 않는 대부분의 사원이 NULL을 가져 낭비가 생긴다.",
  keys=["전체 참여 쪽은 NULL이 안 생김","부분 참여 쪽에 넣으면 NULL이 많아짐"])
Q("3-m11-3","map-11","mc","1:1 관계를 매핑하는 세 가지 방법이 아닌 것은?",
  3, choices=["외래 키 방식","합병 릴레이션 방식","교차 참조(관계 릴레이션) 방식","다중값 속성 방식"])
Q("3-m11-4","map-11","ox","1:1 관계의 속성(예: Mgr_start_date)은 FK를 넣은 쪽 릴레이션에 함께 넣는다.",True)
Q("3-m11-5","map-11","calc","PERSON(Pid 키, Name)과 PASSPORT(Passport_no 키, Issue_date)가 1:1 관계 HOLDS로 연결된다. 모든 여권은 사람에게 속하지만(전체), 여권이 없는 사람도 있다(부분). 관계 속성 Since가 있다. 외래 키 방식으로 매핑하시오.",
  "PERSON(Pid, Name)\nPASSPORT(Passport_no, Issue_date, Pid, Since)  FK Pid → PERSON, Pid는 UNIQUE (1:1)\n전체 참여 쪽 PASSPORT에 FK를 넣어 NULL을 피한다.",
  keys=["FK를 PASSPORT(전체 참여)에","관계 속성 Since도 PASSPORT에","1:1이므로 FK에 UNIQUE"])
Q("3-m11-6","map-11","blank","1:1 관계 외래 키 방식: 한쪽 릴레이션 S를 골라 상대 T의 (a) 를 FK로 넣는다. S는 (b) 참여 쪽으로 고르는 게 좋다.",
  ["PK","전체"], accept=[["PK","기본 키","primary key","기본키"],["전체","total","전체 참여"]])
Q("3-m1n-1","map-1n","mc","1:N 관계 WORKS_FOR(DEPARTMENT 1 : EMPLOYEE N)를 매핑하면 FK는 어디에?",
  0, choices=["EMPLOYEE에 Dno","DEPARTMENT에 Essn","별도 릴레이션에만","둘 다"])
Q("3-m1n-2","map-1n","short","1:N 관계를 매핑할 때 FK를 N쪽 릴레이션에 넣는 이유를 쓰시오.",
  "N쪽 개체 하나는 1쪽 개체 최대 하나와 연결되므로 FK 값 하나로 표현된다. 1쪽에 넣으면 한 투플이 여러 N쪽 개체를 참조해야 해서 다중값이 되고, 원자 값 원칙을 어긴다.",
  keys=["N쪽은 상대가 최대 하나 → FK 하나","1쪽에 넣으면 다중값"])
Q("3-m1n-3","map-1n","mc","SUPERVISION(순환 1:N)을 매핑한 결과는?",
  2, choices=["별도 릴레이션 SUPERVISION(Ssn, Super_ssn)이 꼭 필요","DEPARTMENT에 Super_ssn","EMPLOYEE에 Super_ssn (자기 참조 FK)","매핑 불가"])
Q("3-m1n-4","map-1n","ox","1:N 관계는 교차 참조(관계 릴레이션) 방식으로도 매핑할 수 있지만, 릴레이션 수가 줄어드는 외래 키 방식을 선호한다.",True)
Q("3-m1n-5","map-1n","calc","DEPARTMENT(Dnumber 키)와 PROJECT(Pnumber 키)가 1:N 관계 CONTROLS(부서 1 : 프로젝트 N)로, PROJECT의 CONTROLS 참여는 전체이고 관계 속성 Since가 있다. 매핑 결과를 쓰시오.",
  "DEPARTMENT(Dname, Dnumber, …)\nPROJECT(Pname, Pnumber, Plocation, Dnum, Since)  FK Dnum → DEPARTMENT.Dnumber, Dnum NOT NULL (전체 참여)\n관계 속성 Since도 N쪽 PROJECT에.",
  keys=["FK Dnum을 PROJECT(N쪽)에","Since도 PROJECT에","전체 참여 → NOT NULL (선택)"])
Q("3-m1n-6","map-1n","blank","1:N 관계 외래 키 방식: (a) 쪽 릴레이션 S에 상대 릴레이션의 PK를 FK로 넣고, 관계의 단순 속성도 (b) 에 넣는다.",
  ["N","S"], accept=[["N","n","N쪽","다"],["S","N쪽","N쪽 릴레이션","s"]])
Q("3-mmn-1","map-mn","mc","M:N 관계를 매핑하는 방법은?",
  2, choices=["외래 키 방식","합병 릴레이션 방식","교차 참조(관계 릴레이션) 방식만","다중값 속성으로"])
Q("3-mmn-2","map-mn","mc","WORKS_ON(EMPLOYEE M : PROJECT N, 속성 Hours)을 매핑한 릴레이션의 PK는?",
  1, choices=["Essn","(Essn, Pno)","(Essn, Pno, Hours)","Pno"])
Q("3-mmn-3","map-mn","short","M:N 관계를 외래 키 하나로 표현할 수 없는 이유와 매핑 절차를 쓰시오.",
  "양쪽 개체 모두 상대 개체 여러 개와 연결되므로 어느 쪽에 FK를 넣어도 다중값이 된다. 그래서 별도 관계 릴레이션 S를 만들고, 참여 개체 릴레이션들의 PK를 FK로 넣고, FK들의 조합을 PK로 하며, 관계의 단순 속성도 S에 넣는다.",
  keys=["양쪽 다 여러 개 → FK 하나로 불가","별도 관계 릴레이션","PK = FK들의 조합","관계 속성 포함"])
Q("3-mmn-4","map-mn","calc","STUDENT(Sid 키)와 COURSE(Cid 키)가 M:N 관계 ENROLLS(속성 Grade, Semester)로 연결된다. 한 학생이 같은 과목을 다른 학기에 다시 들을 수 있다. 매핑하시오.",
  "STUDENT(Sid, …), COURSE(Cid, …)\nENROLLS(Sid, Cid, Semester, Grade)  FK Sid → STUDENT, FK Cid → COURSE\nPK (Sid, Cid, Semester): 재수강 때문에 (Sid, Cid)만으로는 유일하지 않아 Semester까지 포함",
  keys=["별도 릴레이션 ENROLLS","FK 2개","PK에 Semester 포함 (재수강)","Grade 포함"])
Q("3-mmn-5","map-mn","ox","M:N 관계 릴레이션(예: WORKS_ON)을 lookup table이라고도 부른다.",True)
Q("3-mmn-6","map-mn","blank","M:N 관계 매핑: 별도 릴레이션 S를 만들고, 참여 릴레이션의 (a) 들을 FK로 넣으며, 그 FK들의 (b) 을 S의 PK로 한다.",
  ["PK","조합"], accept=[["PK","기본 키","기본키","primary key"],["조합","combination","결합"]])
Q("3-mna-1","map-nary","mc","3진 관계 SUPPLY(SUPPLIER, PROJECT, PART, 속성 Quantity)를 매핑한 결과는?",
  1, choices=["SUPPLIER에 FK 두 개","SUPPLY(Sname, Proj_name, Part_no, Quantity), PK = 세 FK의 조합","PART에 FK","매핑 불가"])
Q("3-mna-2","map-nary","ox","n진 관계는 M:N과 같은 교차 참조 방식으로 매핑한다.",True)
Q("3-mna-3","map-nary","short","n진 관계 타입의 매핑 절차를 쓰시오.",
  "관계를 나타내는 별도 릴레이션 S를 만들고, n개 참여 개체 릴레이션의 PK를 FK로 넣으며, 보통 FK 전부의 조합을 PK로 하고, 관계의 단순 속성도 S에 넣는다.",
  keys=["별도 릴레이션","n개 PK를 FK로","FK 조합을 PK로","관계 속성 포함"])
Q("3-mna-4","map-nary","calc","DOCTOR(Did), PATIENT(Pid), DRUG(Drug_code)가 3진 관계 PRESCRIBES(속성 Date, Dosage)로 연결된다. 매핑하시오.",
  "PRESCRIBES(Did, Pid, Drug_code, Date, Dosage)\nFK Did → DOCTOR, Pid → PATIENT, Drug_code → DRUG\nPK (Did, Pid, Drug_code) (같은 처방을 여러 날 하면 Date까지 포함)",
  keys=["별도 릴레이션 PRESCRIBES","FK 3개","PK = 세 FK 조합","Date, Dosage 포함"])
Q("3-ms-1","map-summary","mc","ER→관계 대응에서 '다중값 속성'에 해당하는 것은?",
  2, choices=["속성","도메인","릴레이션과 외래 키","기본 키"])
Q("3-ms-2","map-summary","mc","ER→관계 대응에서 '값 집합(value set)'에 해당하는 것은?",
  1, choices=["릴레이션","도메인","외래 키","후보 키"])
Q("3-ms-3","map-summary","blank","M:N 관계 타입은 관계 릴레이션과 FK (a) 개로, n진 관계 타입은 관계 릴레이션과 FK (b) 개로 대응된다.",
  ["2","n"], accept=[["2","두","둘","two"],["n","N","n개"]])
Q("3-ms-4","map-summary","calc","다음 ER 스키마를 관계 스키마로 매핑하시오 (PK, FK 표시).\n• COLLEGE(CName 키, COffice, CPhone)\n• INSTRUCTOR(Id 키, IName, Rank)\n• DEAN: COLLEGE (1,1) — INSTRUCTOR (0,1), 1:1\n• DEPT(DCode 키, DName)\n• ADMINS: COLLEGE (0,N) — DEPT (1,1), 1:N\n• EMPLOYS: DEPT (0,N) — INSTRUCTOR (1,1), 1:N\n• STUDENT(Sid 키, SName, {Phone})\n• TAKES: STUDENT M:N SECTION(SecId 키), 속성 Grade",
  "COLLEGE(CName, COffice, CPhone, DeanId)  FK DeanId → INSTRUCTOR.Id (1:1, 전체 참여 쪽 COLLEGE에)\nINSTRUCTOR(Id, IName, Rank, DCode)  FK DCode → DEPT (EMPLOYS, N쪽)\nDEPT(DCode, DName, CName)  FK CName → COLLEGE (ADMINS, N쪽)\nSTUDENT(Sid, SName)\nSTUDENT_PHONE(Sid, Phone)  PK (Sid, Phone), FK Sid → STUDENT\nSECTION(SecId, …)\nTAKES(Sid, SecId, Grade)  PK (Sid, SecId), FK Sid → STUDENT, SecId → SECTION",
  keys=["DEAN → COLLEGE에 FK","EMPLOYS → INSTRUCTOR에 DCode","ADMINS → DEPT에 CName","Phone → 별도 릴레이션","TAKES 관계 릴레이션, PK (Sid, SecId), Grade"])
Q("3-ms-5","map-summary","calc","COMPANY ER 다이어그램(교안 2 p.45)을 관계 스키마로 매핑한 결과 6개 릴레이션을 쓰고, 각 관계 타입·다중값 속성·약한 개체가 어디로 갔는지 쓰시오.",
  "EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Super_ssn, Dno)\nDEPARTMENT(Dname, Dnumber, Mgr_ssn, Mgr_start_date)\nDEPT_LOCATIONS(Dnumber, Dlocation)\nPROJECT(Pname, Pnumber, Plocation, Dnum)\nWORKS_ON(Essn, Pno, Hours)\nDEPENDENT(Essn, Dependent_name, Sex, Bdate, Relationship)\n\nMANAGES(1:1) → DEPARTMENT.Mgr_ssn, Mgr_start_date / WORKS_FOR(1:N) → EMPLOYEE.Dno / SUPERVISION(1:N) → EMPLOYEE.Super_ssn / CONTROLS(1:N) → PROJECT.Dnum / WORKS_ON(M:N) → 관계 릴레이션 WORKS_ON / 다중값 Locations → DEPT_LOCATIONS / 약한 개체 DEPENDENT → PK (Essn, Dependent_name)",
  keys=["6개 릴레이션","1:1, 1:N은 FK로 (Mgr_ssn, Dno, Super_ssn, Dnum)","WORKS_ON 관계 릴레이션","DEPT_LOCATIONS","DEPENDENT PK (Essn, Dependent_name)"])
Q("3-ms-6","map-summary","ox","ER 모델의 키 속성은 관계 모델에서 기본 키(또는 보조 키)가 된다.",True)
