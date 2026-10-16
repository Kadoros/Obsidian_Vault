from qdsl import Q

# ───────── L2-1 설계 과정 · 개체와 속성 ─────────
Q("2-proc-1","design-process","mc","DB 설계 과정에서 요구사항을 '개념 스키마'로 번역하는 단계는?",
  1, choices=["요구사항 수집·분석","개념적 설계","논리적 설계","물리적 설계"])
Q("2-proc-2","design-process","mc","구현 단계에 속하는 두 설계는?",
  2, choices=["요구사항 분석, 개념적 설계","개념적 설계, 논리적 설계","논리적 설계(DB 스키마), 물리적 설계(물리적 배치)","ER 설계, 뷰 설계"])
Q("2-ent-1","entity-attr","mc","ER 모델에서 '현실 세계에서 독립적으로 존재하며 다른 것과 구별되는 것'은?",
  0, choices=["개체 (entity)","속성 (attribute)","관계 (relationship)","도메인 (domain)"])
Q("2-ent-2","entity-attr","ox","회사(company)처럼 개념적으로만 존재하는 것도 개체가 될 수 있다.",True,
  explain="개체는 물리적 존재(사원)일 수도 개념적 존재(회사, 강좌)일 수도 있다.")
Q("2-ent-3","entity-attr","short","ER 모델에서 개체, 속성, 관계를 각각 정의하시오.",
  "개체: 현실 세계에서 독립적으로 존재하고 다른 것과 구별되는 것(물리적 또는 개념적 존재). 속성: 개체를 기술하는 특정 성질. 관계: 여러 개체 사이의 연관.",
  keys=["개체 = 독립적 존재, 구별 가능","속성 = 개체를 기술하는 성질","관계 = 개체들 사이의 연관"])
Q("2-ent-4","entity-attr","mc","다음 중 '속성'이 아닌 것은?",
  3, choices=["사원의 이름","사원의 주소","회사의 본사 위치","사원이 일하는 부서와의 연관"],
  explain="부서와의 연관은 관계(WORKS_FOR). 초기 설계에선 속성처럼 넣었다가 다듬기에서 관계로 바꾼다.")
Q("2-attr-1","attr-types","mc","Address = (Street_address, City, State, Zip)는 어떤 속성인가?",
  0, choices=["복합 속성","다중값 속성","유도 속성","키 속성"])
Q("2-attr-2","attr-types","mc","한 사원이 학위를 여러 개 가질 때 College_degrees는 어떤 속성인가?",
  1, choices=["복합 속성","다중값 속성","유도 속성","단순 속성"])
Q("2-attr-3","attr-types","mc","Birth_date에서 계산할 수 있는 Age는?",
  2, choices=["복합 속성","다중값 속성","유도 속성","키 속성"])
Q("2-attr-4","attr-types","blank","ER 다이어그램에서 다중값 속성은 (a) 타원으로, 유도 속성은 (b) 타원으로 그린다.",
  ["이중","점선"], accept=[["이중","두 줄","이중선","double"],["점선","dashed","dotted"]])
Q("2-attr-5","attr-types","short","속성의 세 가지 분류 기준을 쓰고 각각 예를 하나씩 드시오.",
  "1) 복합 vs 단순: 복합은 더 작은 부분으로 나뉨(Address = Street, City, State, Zip), 단순(원자)은 안 나뉨(City). 2) 단일값 vs 다중값: 개체마다 값 하나(Age, SSN) vs 값의 집합(Phone numbers, College degrees). 3) 저장 vs 유도: DB에 저장(Birth_date) vs 다른 속성에서 계산(Age).",
  keys=["복합/단순 + 예","단일값/다중값 + 예","저장/유도 + 예"])
Q("2-attr-6","attr-types","ox","DEPARTMENT의 Locations는 부서마다 위치가 여러 개일 수 있어서 복합 속성이다.",False,
  explain="여러 값 = 다중값 속성. 복합은 한 값이 여러 부분으로 나뉘는 것.")
Q("2-attr-7","attr-types","mc","EMPLOYEE의 Name = (Fname, Minit, Lname)은?",
  0, choices=["복합 속성","다중값 속성","유도 속성","약한 속성"])
Q("2-key-1","key-attr","ox","한 개체 타입은 키 속성을 둘 이상 가질 수 있다.",True,
  explain="예: CAR의 키 = Registration, Vehicle_id.")
Q("2-key-2","key-attr","mc","CAR의 Registration(Number, State)에 대한 설명으로 옳은 것은?",
  1, choices=["다중값 키","두 속성이 모여 하나의 키를 이루는 복합 키","유도 키","부분 키"])
Q("2-key-3","key-attr","short","ER 모델의 키 속성이란 무엇이고 다이어그램에 어떻게 표시하는지 쓰시오.",
  "개체마다 값이 서로 다른 속성으로, 각 개체를 유일하게 식별한다. 여러 속성이 모여 키가 될 수도 있고 키가 여러 개일 수도 있다. 다이어그램에서는 속성 이름에 밑줄.",
  keys=["개체마다 값이 다름 → 유일 식별","밑줄로 표시"])
Q("2-key-4","key-attr","blank","키 속성은 다이어그램에서 (a) 로 표시하고, 약한 개체의 부분 키는 (b) 밑줄로 표시한다.",
  ["밑줄","점선"], accept=[["밑줄","underline","실선 밑줄"],["점선","dashed","dotted"]])
Q("2-not-1","er-notation","mc","ER 다이어그램에서 이중 마름모가 나타내는 것은?",
  2, choices=["약한 개체 타입","다중값 속성","식별 관계 타입","M:N 관계"])
Q("2-not-2","er-notation","mc","E₁ — R ═ E₂ (E₂ 쪽만 이중선)의 의미는?",
  1, choices=["E₁이 R에 전체 참여","E₂가 R에 전체 참여","R이 1:N","E₂가 약한 개체"])
Q("2-not-3","er-notation","ox","이중 직사각형은 약한 개체 타입을 나타낸다.",True)
Q("2-not-4","er-notation","blank","ER 다이어그램에서 개체 타입은 (a), 관계 타입은 (b), 속성은 타원으로 그린다.",
  ["직사각형","마름모"], accept=[["직사각형","사각형","네모","rectangle"],["마름모","diamond","다이아몬드"]])
Q("2-init-1","initial-design","short","COMPANY 초기 설계에서 EMPLOYEE의 Department, Supervisor, Works_on 같은 속성은 어떤 문제가 있고, 어떻게 고치는지 쓰시오.",
  "이 속성들은 사실 다른 개체(부서, 다른 사원, 프로젝트)를 참조한다. 관계가 속성 형태로 암묵적으로 들어가 있는 것이므로, 명시적인 관계 타입(WORKS_FOR, SUPERVISION, WORKS_ON)으로 바꿔야 한다.",
  keys=["다른 개체를 참조하는 속성 = 암묵적 관계","관계 타입으로 바꿈"])
Q("2-init-2","initial-design","mc","COMPANY 초기 설계에서 DEPARTMENT의 키 속성은?",
  3, choices=["Number만","Name만","Manager","Name과 Number 둘 다 (각각 고유)"])

# ───────── L2-2 관계 타입 · 제약 ─────────
Q("2-rel-1","rel-type","mc","관계 타입의 '차수(degree)'란?",
  1, choices=["관계 인스턴스의 수","참여하는 개체 타입의 수","관계 속성의 수","카디널리티 비의 최댓값"])
Q("2-rel-2","rel-type","mc","SUPPLY(SUPPLIER, PART, PROJECT)의 차수는?",
  2, choices=["1 (단항)","2 (2진)","3 (3진)","M:N"])
Q("2-rel-3","rel-type","ox","DB 시스템에서 대부분의 관계는 2진 관계이다.",True)
Q("2-rel-4","rel-type","short","관계 타입의 '역할 이름(role name)'이 무엇이고 언제 꼭 필요한지 쓰시오.",
  "참여 개체가 관계 인스턴스에서 맡는 역할(예: WORKS_FOR에서 EMPLOYEE = worker, DEPARTMENT = employer). 관계의 의미를 이해하게 해준다. 같은 개체 타입이 두 번 이상 참여하는 순환 관계에서는 참여 개체를 구별하려고 꼭 필요하다.",
  keys=["참여 개체가 맡는 역할","순환 관계에서 필수"])
Q("2-rec-1","recursive","mc","순환(recursive) 관계의 예는?",
  2, choices=["WORKS_FOR","MANAGES","SUPERVISION","CONTROLS"])
Q("2-rec-2","recursive","ox","순환 관계에서는 같은 개체 타입이 두 번 이상 참여하므로 역할 이름을 명시해야 한다.",True)
Q("2-rec-3","recursive","short","SUPERVISION 관계가 순환 관계인 이유와, 인스턴스 r = (e₁, e₂)를 해석하는 데 필요한 정보를 쓰시오.",
  "EMPLOYEE 개체 타입이 supervisor와 supervisee 두 역할로 한 관계에 참여하기 때문. r = (e₁, e₂)에서 어느 쪽이 supervisor 역할이고 어느 쪽이 supervisee 역할인지(역할 이름)를 알아야 '누가 누구의 상사인지' 해석할 수 있다.",
  keys=["같은 개체 타입이 두 역할로 참여","역할 이름으로 상사/부하 구별"])
Q("2-rec-4","recursive","blank","순환 관계 SUPERVISION에서 EMPLOYEE는 (a) 역할과 (b) 역할로 참여한다.",
  ["supervisor","supervisee"], accept=[["supervisor","상사","감독자"],["supervisee","부하","피감독자"]])
Q("2-card-1","cardinality","mc","'사원은 한 부서에서만 일하고, 부서는 사원을 몇 명이든 둘 수 있다'의 카디널리티 비는?",
  1, choices=["1:1","DEPARTMENT 1 : EMPLOYEE N","EMPLOYEE 1 : DEPARTMENT N","M:N"])
Q("2-card-2","cardinality","mc","WORKS_ON(사원은 여러 프로젝트, 프로젝트는 여러 사원)의 카디널리티 비는?",
  3, choices=["1:1","1:N","N:1","M:N"])
Q("2-card-3","cardinality","mc","MANAGES(사원은 최대 한 부서를 관리, 부서는 관리자 최대 한 명)의 카디널리티 비는?",
  0, choices=["1:1","1:N","N:1","M:N"])
Q("2-card-4","cardinality","blank","카디널리티 비는 한 개체가 참여할 수 있는 관계 인스턴스의 (a) 개수를 지정하고, 참여 제약은 개체의 존재가 관계에 (b) 하는지를 지정한다.",
  ["최대","의존"], accept=[["최대","maximum","max"],["의존","depend","dependent"]])
Q("2-card-5","cardinality","ox","1:N 관계 WORKS_FOR에서 N쪽 개체(EMPLOYEE) 하나는 1쪽 개체(DEPARTMENT) 최대 하나와 연결된다.",True)
Q("2-card-6","cardinality","short","2진 관계의 카디널리티 비 세 가지를 COMPANY 예와 함께 설명하시오.",
  "1:1 — MANAGES: 사원은 최대 한 부서를 관리, 부서는 관리자가 최대 한 명. 1:N — WORKS_FOR: 부서(1)는 사원(N)을 몇 명이든, 사원은 한 부서에서만. M:N — WORKS_ON: 사원은 여러 프로젝트, 프로젝트도 여러 사원.",
  keys=["1:1 + MANAGES","1:N + WORKS_FOR","M:N + WORKS_ON"])
Q("2-part-1","participation","mc","'모든 사원은 반드시 어떤 부서에서 일해야 한다'는 EMPLOYEE의 WORKS_FOR 참여는?",
  0, choices=["전체 참여","부분 참여","1:1 참여","약한 참여"])
Q("2-part-2","participation","mc","EMPLOYEE의 MANAGES 참여가 부분 참여인 이유는?",
  2, choices=["부서마다 관리자가 한 명이라서","관리자는 반드시 사원이라서","모든 사원이 부서를 관리하지는 않아서","MANAGES가 1:1이라서"])
Q("2-part-3","participation","ox","전체 참여는 ER 다이어그램에서 이중선으로 그린다.",True)
Q("2-part-4","participation","short","전체 참여와 부분 참여를 정의하고 EMPLOYEE를 예로 각각 설명하시오.",
  "전체 참여: 모든 개체가 그 관계에 참여해야 함(존재 의존). 예) 모든 사원은 부서에서 일하므로 EMPLOYEE는 WORKS_FOR에 전체 참여. 부분 참여: 모든 개체가 참여할 필요는 없음. 예) 일부 사원만 부서를 관리하므로 EMPLOYEE는 MANAGES에 부분 참여.",
  keys=["전체 = 모든 개체 참여 + WORKS_FOR 예","부분 = 일부만 + MANAGES 예"])
Q("2-part-5","participation","mc","약한 개체 타입의 식별 관계 참여는 항상?",
  0, choices=["전체 참여","부분 참여","M:N","1:1"])
Q("2-part-6","participation","ox","CONTROLS에서 DEPARTMENT는 전체 참여이고 PROJECT는 부분 참여이다.",False,
  explain="반대. 모든 프로젝트는 통제 부서가 있어야 하므로 PROJECT가 전체, 프로젝트가 없는 부서도 있으므로 DEPARTMENT가 부분.")
Q("2-mm-1","minmax","mc","(min, max) 표기에서 min = 0이 뜻하는 것은?",
  1, choices=["전체 참여","부분 참여","1:1 관계","약한 개체"])
Q("2-mm-2","minmax","mc","'강의는 교재를 쓸 수도 안 쓸 수도 있고, 다섯 권을 넘게 쓰지는 않는다'일 때 COURSE의 USES 참여는?",
  2, choices=["(1, 5)","(0, N)","(0, 5)","(5, N)"])
Q("2-mm-3","minmax","mc","'강사는 2개 이상 4개 이하의 강의를 가르친다'일 때 INSTRUCTOR의 TEACHES 참여는?",
  3, choices=["(0, 4)","(1, 4)","(2, N)","(2, 4)"])
Q("2-mm-4","minmax","blank","MANAGES 관계를 (min, max)로 나타내면 EMPLOYEE 쪽은 (a), DEPARTMENT 쪽은 (b) 이다.",
  ["(0,1)","(1,1)"], accept=[["(0,1)","0,1","(0, 1)"],["(1,1)","1,1","(1, 1)"]])
Q("2-mm-5","minmax","calc","다음 요구사항을 보고 각 참여의 (min, max)를 쓰시오.\n• 강의(COURSE)는 교재를 쓸 수도 안 쓸 수도 있고, 다섯 권을 넘게 쓰지 않는다.\n• 강의는 최소 1명, 최대 4명의 강사가 가르친다.\n• 교재(TEXT)는 어떤 강의들에서 쓰인다 (안 쓰이는 교재는 기록 안 함).\n• 강사는 2~4개의 강의를 가르친다.\n\nINSTRUCTOR —(①)— TEACHES —(②)— COURSE —(③)— USES —(④)— TEXT",
  "① INSTRUCTOR의 TEACHES 참여: (2, 4)\n② COURSE의 TEACHES 참여: (1, 4)\n③ COURSE의 USES 참여: (0, 5)\n④ TEXT의 USES 참여: (1, N)",
  keys=["① (2,4)","② (1,4)","③ (0,5)","④ (1,N)"], explain="(min,max)는 그 개체 하나가 관계에 몇 번 참여하는지. min 0 = 부분, min ≥ 1 = 전체.")
Q("2-mm-6","minmax","ox","WORKS_FOR(DEPARTMENT 1 : EMPLOYEE N)를 (min, max)로 나타내면 EMPLOYEE 쪽에 (1, 1)이 붙는다.",True,
  explain="사원 하나는 WORKS_FOR 인스턴스에 정확히 1번 참여. 1:N 표기의 '1'이 DEPARTMENT 쪽에 붙는 것과 위치가 반대로 보이는 게 함정.")
Q("2-mm-7","minmax","calc","COMPANY 다듬은 ER 다이어그램에서 다음 참여의 (min, max)를 쓰시오.\n(1) EMPLOYEE의 WORKS_FOR 참여  (2) EMPLOYEE의 MANAGES 참여  (3) PROJECT의 CONTROLS 참여  (4) supervisee 역할 EMPLOYEE의 SUPERVISION 참여  (5) DEPENDENT의 DEPENDENTS_OF 참여",
  "(1) (1, 1)  (2) (0, 1)  (3) (1, 1)  (4) (0, 1)  (5) (1, 1)",
  keys=["(1) (1,1)","(2) (0,1)","(3) (1,1)","(4) (0,1)","(5) (1,1)"],
  explain="사원은 정확히 한 부서, 관리는 최대 한 부서(안 할 수도), 프로젝트는 정확히 한 통제 부서, 상사는 최대 한 명(Borg는 없음), 부양가족은 정확히 한 사원에 딸림.")

# ───────── L2-3 관계 속성 · 약한 개체 ─────────
Q("2-ra-1","rel-attr","mc","M:N 관계 WORKS_ON의 속성 Hours를 개체 타입으로 옮길 수 없는 이유는?",
  1, choices=["Hours가 다중값이라서","Hours는 사원–프로젝트 조합으로만 결정되어서","Hours가 유도 속성이라서","WORKS_ON이 식별 관계라서"])
Q("2-ra-2","rel-attr","mc","1:N 관계 WORKS_FOR의 속성 StartDate는 어디로 옮길 수 있나?",
  2, choices=["DEPARTMENT로만","어느 쪽이든","EMPLOYEE(N쪽)로만","옮길 수 없음"])
Q("2-ra-3","rel-attr","ox","1:1 관계 MANAGES의 StartDate는 EMPLOYEE와 DEPARTMENT 중 어느 쪽으로든 옮길 수 있다.",True)
Q("2-ra-4","rel-attr","short","관계 타입의 속성을 참여 개체로 옮길(migrate) 수 있는지를 1:1, 1:N, M:N 각각에 대해 설명하시오.",
  "1:1: 어느 참여 개체로든 옮길 수 있음 (MANAGES.StartDate). 1:N: N쪽 개체로만 옮길 수 있음. N쪽 개체 하나는 인스턴스에 최대 1번 참여해서 값이 하나로 정해지기 때문 (WORKS_FOR.StartDate → EMPLOYEE). M:N: 어느 개체로도 못 옮김. 속성 값이 참여 개체 조합으로만 결정되기 때문 (WORKS_ON.Hours).",
  keys=["1:1 = 어느 쪽이든","1:N = N쪽만 (이유)","M:N = 못 옮김 (조합으로 결정)"])
Q("2-ra-5","rel-attr","blank","1:N 관계의 속성은 (a) 쪽 개체로만 옮길 수 있고, M:N 관계의 속성은 참여 개체의 (b) 으로 결정되어 옮길 수 없다.",
  ["N","조합"], accept=[["N","n","N쪽","다(N)"],["조합","combination","조합으로"]])
Q("2-weak-1","weak-entity","mc","약한 개체 타입의 정의로 옳은 것은?",
  0, choices=["자신의 키 속성이 없는 개체 타입","속성이 하나뿐인 개체 타입","부분 참여만 하는 개체 타입","다른 개체가 참조하지 않는 개체 타입"])
Q("2-weak-2","weak-entity","mc","DEPENDENT의 Dependent_name 같은, 같은 소유자에 딸린 약한 개체끼리 구별하는 속성은?",
  2, choices=["기본 키","후보 키","부분 키","외래 키"])
Q("2-weak-3","weak-entity","ox","부분 키만으로 약한 개체를 유일하게 식별할 수 있다.",False,
  explain="다른 사원에게도 같은 이름의 부양가족(Tom)이 있을 수 있다. 소유자의 키 + 부분 키로 식별.")
Q("2-weak-4","weak-entity","short","약한 개체 타입, 식별 관계, 부분 키를 DEPENDENT 예로 설명하시오.",
  "약한 개체 타입: 자기 키 속성이 없어 식별(소유) 개체 타입에 의존하는 개체 타입 (DEPENDENT는 EMPLOYEE에 의존). 식별 관계: 약한 개체와 소유 개체를 잇는 관계(DEPENDENTS_OF), 이중 마름모, 약한 개체는 항상 전체 참여. 부분 키: 같은 소유자에 딸린 약한 개체끼리 구별하는 속성(Dependent_name). 소유자 키(Ssn) + 부분 키로 식별.",
  keys=["약한 개체 = 자기 키 없음, 소유자에 의존","식별 관계 = 소유자와 연결, 전체 참여","부분 키 + 소유자 키로 식별"])
Q("2-weak-5","weak-entity","blank","약한 개체는 (a) 관계를 통해 소유 개체와 연결되며, 이 관계에 항상 (b) 참여한다.",
  ["식별","전체"], accept=[["식별","identifying"],["전체","total","전체 참여"]])
Q("2-weak-6","weak-entity","mc","약한 개체 타입을 ER 다이어그램에 그리는 방법은?",
  1, choices=["점선 직사각형","이중 직사각형 + 이중 마름모(식별 관계)","타원","이중 타원"])

# ───────── L2-4 다듬기 · 실습 ─────────
Q("2-ref-1","refine","mc","COMPANY 다듬기에서 PROJECT의 Controlling_department 속성은 어떤 관계 타입이 되나?",
  2, choices=["MANAGES","WORKS_FOR","CONTROLS","WORKS_ON"])
Q("2-ref-2","refine","mc","COMPANY의 WORKS_ON 관계에 대한 설명으로 옳은 것은?",
  3, choices=["1:N, 속성 없음","1:1, StartDate","M:N, 양쪽 부분 참여","M:N, 양쪽 전체 참여, 속성 Hours"])
Q("2-ref-3","refine","short","ER 스키마 설계 과정 3단계를 쓰시오.",
  "(1) 요구사항을 바탕으로 개체 타입과 속성을 기술한다. (2) 관계 타입과 그 제약조건(카디널리티 비, 참여 제약)을 지정한다. (3) 관계를 표현하던 속성을 관계 타입으로 바꾼다.",
  keys=["개체 타입·속성","관계 타입·제약조건","관계를 나타내던 속성 → 관계 타입"])
Q("2-ref-4","refine","ox","MANAGES에서 EMPLOYEE는 부분 참여, DEPARTMENT는 전체 참여이다.",True)
Q("2-ref-5","refine","calc","COMPANY 다듬은 설계의 관계 타입 6개를 쓰고, 각각의 카디널리티 비를 쓰시오.",
  "MANAGES 1:1 (EMPLOYEE–DEPARTMENT)\nWORKS_FOR 1:N (DEPARTMENT 1, EMPLOYEE N)\nCONTROLS 1:N (DEPARTMENT 1, PROJECT N)\nSUPERVISION 1:N (supervisor 1, supervisee N)\nWORKS_ON M:N (EMPLOYEE–PROJECT, 속성 Hours)\nDEPENDENTS_OF 1:N (EMPLOYEE 1, DEPENDENT N, 식별 관계)",
  keys=["MANAGES 1:1","WORKS_FOR 1:N","CONTROLS 1:N","SUPERVISION 1:N","WORKS_ON M:N","DEPENDENTS_OF 1:N"])
Q("2-ref-6","refine","mc","DEPENDENTS_OF에서 EMPLOYEE와 DEPENDENT의 참여는?",
  1, choices=["둘 다 전체","EMPLOYEE 부분, DEPENDENT 전체","EMPLOYEE 전체, DEPENDENT 부분","둘 다 부분"],
  explain="사원은 부양가족이 없을 수 있고, 부양가족은 반드시 사원에 딸린다.")
Q("2-prac-1","er-practice","mc","MOVIE DB에서 '각 영화는 제작사 하나가 만들고, 제작사는 영화 여러 편을 만든다'의 관계 PRODUCES는?",
  0, choices=["PRODUCTION 1 : MOVIE N, MOVIE 전체 참여","M:N","1:1","MOVIE 1 : PRODUCTION N"])
Q("2-prac-2","er-practice","mc","MOVIE DB의 ACTS 관계에서 Role과 {Quotes}는?",
  2, choices=["ACTOR의 속성","MOVIE의 속성","ACTS(M:N) 관계의 속성","약한 개체"],
  explain="배우가 그 영화에서 맡은 역할·대사는 배우–영화 조합으로 정해지므로 M:N 관계 속성.")
Q("2-prac-3","er-practice","short","CONF_REVIEW DB에서 SUBMITS(AUTHOR–PAPER, M:N) 관계만으로는 어떤 요구사항을 표현할 수 없고, 어떻게 해결했는지 쓰시오.",
  "'논문마다 저자 중 한 명을 연락 저자(contact author)로 지정한다'는 요구. SUBMITS는 여러 저자를 연결할 뿐 그중 누가 연락 저자인지 못 나타낸다. 그래서 별도 관계 IS_CONTACT(AUTHOR (0,N) – PAPER (1,1))를 둔다. (또는 SUBMITS에 Is_contact 속성)",
  keys=["연락 저자 지정 요구","IS_CONTACT 관계 추가, PAPER (1,1)"])
Q("2-prac-4","er-practice","calc","다음 요구사항으로 REVIEWER–REVIEWS–PAPER 부분을 설계하시오. 개체 키, 관계의 (min, max), 관계 속성을 쓰시오.\n• 리뷰어는 e-mail로 식별, 리뷰를 최소 하나 해야 기록되고 여러 편을 리뷰할 수 있다.\n• 논문은 시스템이 준 id로 식별, 리뷰어가 최소 2명 최대 4명 배정된다.\n• 리뷰어는 배정된 논문마다 네 항목(기술성, 가독성, 독창성, 관련성)을 1~10점으로 평가하고, 종합 추천과, 위원회용·저자용 두 가지 코멘트를 남긴다.",
  "REVIEWER(키 R_email) —(1,N)— REVIEWS —(2,4)— PAPER(키 P_id)\nREVIEWS의 속성: Recommendation, Comments(For_committee, Feedback) 복합, Rating(C1 Technical_merit, C2 Readability, C3 Originality, C4 Relevance) 복합\n양쪽 모두 전체 참여(min ≥ 1).",
  keys=["REVIEWER 키 R_email, PAPER 키 P_id","REVIEWER (1,N)","PAPER (2,4)","관계 속성: Recommendation, Comments 복합, Rating 복합"])
Q("2-prac-5","er-practice","ox","MOVIE DB에서 MOVIE의 키는 (Title, Year)로 된 복합 키이다.",True)
Q("2-prac-6","er-practice","calc","다음 요구사항을 ER로 설계하시오 (개체, 키, 관계, 카디널리티, 참여).\n• 도서관 회원(MEMBER)은 회원 번호로 식별되고 이름이 있다.\n• 책(BOOK)은 ISBN으로 식별되고 제목, 저자(여러 명 가능)가 있다.\n• 회원은 책을 여러 권 빌릴 수 있고, 한 책은 여러 회원이 빌린 기록이 남는다. 대출마다 대출일과 반납일을 기록한다.\n• 책을 한 번도 안 빌린 회원도 있다.",
  "MEMBER(키 Member_no, Name) — BORROWS — BOOK(키 ISBN, Title, {Author} 다중값)\nBORROWS: M:N, 관계 속성 Borrow_date, Return_date\nMEMBER는 BORROWS에 부분 참여 (min 0), BOOK의 참여는 요구사항에 없으므로 부분으로 둠.",
  keys=["MEMBER 키 Member_no, BOOK 키 ISBN","Author 다중값","BORROWS M:N + 대출일·반납일은 관계 속성","MEMBER 부분 참여"])
