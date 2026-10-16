from qdsl import Q
import lr, rd

# ───────── U4 어휘 분석 ─────────
Q("4-sab-1","sa-bnf","short","구문을 BNF로 기술하는 것의 장점 3가지(구문 분석기 관점)를 쓰시오.",
  "1. 명확하고 간결한 구문 기술을 제공\n2. 파서를 BNF에 직접 기반하여 만들 수 있음\n3. BNF 기반 파서는 유지보수가 쉬움(모듈성)",
  keys=["명확·간결","파서를 직접 기반","유지보수 쉬움"])
Q("4-sab-2","sa-bnf","ox","컴파일, 해석, 혼합형 등 구현 방식과 상관없이 언어 구현 시스템은 원시 코드를 분석해야 한다.",True)

Q("4-lp-1","lex-vs-parser","mc","어휘 분석기의 수학적 모델은?",
  0, choices=["정규 문법 기반 유한 오토마타","문맥 자유 문법 기반 푸시다운 오토마타","튜링 기계","속성 문법"])
Q("4-lp-2","lex-vs-parser","blank","구문 분석기(파서)는 수학적으로 (a) 문법에 기반한 (b) 오토마타이다.",
  ["문맥 자유","푸시다운"], accept=[["문맥자유","contextfree","cfg","bnf"],["푸시다운","pushdown","pda"]])
Q("4-lp-3","lex-vs-parser","ox","어휘 분석기는 고수준 부분, 파서는 저수준 부분이다.",False,
  explain="어휘 분석기 = 저수준(문자 단위), 파서 = 고수준(토큰 → 구조).")

Q("4-sep-1","separate-why","short","어휘 분석과 구문 분석을 분리하는 이유 3가지를 쓰시오.",
  "1. 단순성: 어휘 분석에는 덜 복잡한 기법을 쓸 수 있고, 분리하면 파서가 단순해진다.\n2. 효율성: 분리하면 어휘 분석기를 따로 최적화할 수 있다.\n3. 이식성: 어휘 분석기 일부는 이식이 어려울 수 있지만 파서는 항상 이식 가능하다.",
  keys=["단순성","효율성(어휘 분석기 최적화)","이식성(파서는 항상 이식 가능)"])
Q("4-sep-2","separate-why","mc","어휘 분석과 구문 분석을 분리하는 이유 중 '파서는 항상 이식 가능하다'와 관련된 것은?",
  2, choices=["단순성","효율성","이식성","신뢰성"])
Q("4-sep-3","separate-why","mc","어휘 분석기만 따로 최적화할 수 있다는 장점은?",1,choices=["단순성","효율성","이식성","모듈성"])

Q("4-lr-1","lexer-role","mc","어휘 분석기에 대한 설명으로 틀린 것은?",
  3, choices=["문자열에 대한 패턴 매처이다","파서의 전단부(front-end)이다","보통 파서가 다음 토큰이 필요할 때 호출하는 함수이다","파스 트리를 생성한다"])
Q("4-lr-2","lexer-role","short","`result = oldsum - value / 100;` 을 어휘 분석했을 때의 (토큰, 어휘항목) 쌍을 모두 쓰시오.",
  "IDENT result / ASSIGN_OP = / IDENT oldsum / SUB_OP - / IDENT value / DIV_OP / / INT_LIT 100 / SEMICOLON ;",
  keys=["8쌍","IDENT 3개","INT_LIT 100","연산자 토큰 구분"])
Q("4-lr-3","lexer-role","short","`if (cnt >= 10) x = y;` 를 어휘 분석했을 때 어휘항목을 순서대로 모두 쓰고 각 토큰 범주를 쓰시오.",
  "if – 예약어(IF) / ( – LEFT_PAREN / cnt – IDENT / >= – 관계 연산자(GE_OP) / 10 – INT_LIT / ) – RIGHT_PAREN / x – IDENT / = – ASSIGN_OP / y – IDENT / ; – SEMICOLON",
  keys=["if는 예약어 토큰",">= 는 하나의 어휘항목","총 10개 어휘항목"])

Q("4-lb-1","lexer-build","short","어휘 분석기를 만드는 세 가지 접근 방법을 쓰시오.",
  "1. 토큰을 형식적으로 기술하고, 그 기술로부터 표 기반 어휘 분석기를 생성하는 SW 도구를 사용 (예: lex)\n2. 토큰을 기술하는 상태 다이어그램을 설계하고, 그 다이어그램을 구현하는 프로그램을 작성\n3. 상태 다이어그램을 설계하고, 그것의 표 기반 구현을 손으로 작성",
  keys=["도구(lex) 사용","상태 다이어그램 → 프로그램 작성","상태 다이어그램 → 표 기반 손 구현"])
Q("4-lb-2","lexer-build","mc","front.c는 어휘 분석기를 만드는 세 방법 중 어느 것인가?",
  1, choices=["도구로 표 기반 분석기 생성","상태 다이어그램을 구현하는 프로그램 작성","표 기반 구현을 손으로 작성","정규식 엔진 사용"])

Q("4-sd-1","state-diagram","short","어휘 분석기 상태 다이어그램을 단순화하는 두 가지 방법을 쓰시오.",
  "1. 문자 클래스 사용: 식별자 인식 시 모든 글자를 LETTER, 정수 인식 시 모든 숫자를 DIGIT 클래스로 묶어 전이를 합친다.\n2. 예약어와 식별자를 함께 인식: 예약어마다 다이어그램을 만들지 않고, 식별자로 인식한 뒤 테이블 탐색(lookup)으로 예약어인지 판별한다.",
  keys=["문자 클래스(LETTER/DIGIT)","예약어·식별자 함께 인식 + 테이블 탐색"])
Q("4-sd-2","state-diagram","ox","순진한 상태 다이어그램은 모든 상태에서 모든 문자에 대한 전이가 필요해 매우 커진다.",True)
Q("4-sd-3","state-diagram","mc","예약어 while을 식별자와 구분하는 일반적인 방법은?",
  2, choices=["while 전용 상태 다이어그램을 따로 만든다","파서가 판단한다","식별자로 인식한 후 테이블 탐색으로 예약어인지 확인한다","w로 시작하면 예약어로 본다"])

Q("4-ut-1","lexer-utils","mc","다음 입력 문자를 nextChar에 넣고 그 문자 클래스를 charClass에 저장하는 함수는?",
  0, choices=["getChar","addChar","lookup","getNonBlank"])
Q("4-ut-2","lexer-utils","mc","nextChar의 문자를 lexeme 배열에 덧붙이는 함수는?",1,choices=["getChar","addChar","lookup","lex"])
Q("4-ut-3","lexer-utils","short","getChar, addChar, lookup 의 역할을 각각 쓰시오.",
  "getChar: 입력의 다음 문자를 nextChar에 넣고, 그 문자의 클래스를 판단해 charClass에 넣는다.\naddChar: nextChar의 문자를 어휘항목을 모으는 곳(lexeme)에 추가한다.\nlookup: lexeme(문자)가 예약어/연산자인지 판단해 해당 토큰 코드를 반환한다.",
  keys=["getChar: 다음 문자 + 클래스","addChar: lexeme에 추가","lookup: 예약어/연산자 판단 → 코드"])

Q("4-fc-1","front-codes","mc","front.c에서 `(sum + 47) / total` 의 출력 중 `Next token is: 24` 에 해당하는 어휘항목은?",
  2, choices=["(","+","/",")"], explain="DIV_OP = 24. ( = 25, ) = 26, + = 21.")
Q("4-fc-2","front-codes","calc","front.c로 `count = a1 * 25` 를 분석할 때 출력되는 'Next token is: … Next lexeme is …' 줄들을 모두 쓰시오.",
  "Next token is: 11 Next lexeme is count\nNext token is: 20 Next lexeme is =\nNext token is: 11 Next lexeme is a1\nNext token is: 23 Next lexeme is *\nNext token is: 10 Next lexeme is 25\nNext token is: -1 Next lexeme is EOF",
  keys=["IDENT 11","ASSIGN_OP 20","a1은 LETTER로 시작 → IDENT","MULT_OP 23","INT_LIT 10","EOF -1"])
Q("4-fc-3","front-codes","mc","front.c에서 `a1`이 하나의 IDENT로 인식되는 이유는?",
  1, choices=["숫자가 무시되므로","LETTER로 시작한 뒤 while (charClass == LETTER || charClass == DIGIT) 동안 계속 addChar 하므로","lookup이 a1을 예약어로 보므로","getNonBlank가 1을 건너뛰므로"])
Q("4-fc-4","front-codes","mc","front.c에서 `12abc` 를 분석하면 어떻게 되는가?",
  0, choices=["INT_LIT 12 다음 IDENT abc","IDENT 12abc","INT_LIT 12abc","오류 후 종료"],
  explain="DIGIT로 시작 → while (charClass == DIGIT) → 'a'에서 멈춤 → INT_LIT 12. 다음 lex()에서 abc는 IDENT.")

Q("4-ft-1","front-trace","calc","front.c의 lex()가 `(sum + 47)` 에서 두 번째 토큰 sum을 인식하는 과정을 getChar/addChar 호출과 lexeme, nextChar 변화로 쓰시오. (첫 토큰 처리 후 nextChar = 's', charClass = LETTER 상태)",
  "lexLen = 0, getNonBlank() (s는 공백 아님)\nswitch(LETTER): addChar() → lexeme = \"s\"; getChar() → nextChar = 'u', LETTER\nwhile: addChar() → \"su\"; getChar() → 'm', LETTER\n       addChar() → \"sum\"; getChar() → ' ', UNKNOWN → while 종료\nnextToken = IDENT(11), printf \"Next token is: 11 Next lexeme is sum\"",
  keys=["addChar/getChar 교대","lexeme s → su → sum","공백에서 UNKNOWN으로 while 종료","IDENT 11 출력"])
Q("4-ft-2","front-trace","mc","front.c의 lex()가 토큰 하나를 끝낸 직후의 nextChar는?",
  1, choices=["방금 인식한 토큰의 마지막 문자","방금 인식한 토큰 바로 다음 문자 (미리 읽혀 있음)","항상 공백","EOF"])
Q("4-ft-3","front-trace","mc","front.c에서 `(` 를 처리할 때 lex()의 switch는 어느 case로 가는가?",
  2, choices=["LETTER","DIGIT","UNKNOWN (lookup 호출)","EOF"])

# ───────── U5 파싱 문제 · 하향식 ─────────
Q("5-pg-1","parser-goals","short","구문 분석기(파서)의 두 가지 목표를 쓰시오.",
  "1. 모든 구문 오류를 찾아 각각 적절한 진단 메시지를 내고 빨리 복구한다.\n2. 프로그램의 파스 트리(또는 최소한 파스 트리의 흔적)를 생성한다.",
  keys=["구문 오류 탐지·진단·복구","파스 트리 생성"])
Q("5-pg-2","parser-goals","ox","파서는 첫 번째 구문 오류를 만나면 즉시 분석을 멈추는 것이 목표다.",False,
  explain="모든 구문 오류를 찾고, 오류마다 진단 후 빨리 복구해서 계속 분석하는 것이 목표.")

Q("5-tb-1","topdown-bottomup","short","하향식(top-down) 파싱과 상향식(bottom-up) 파싱에 대해 간략히 서술하시오.",
  "하향식: 루트(시작 기호)부터 잎 방향으로 파스 트리를 만든다. 최좌단 유도 순서를 따르며(전위 순회), 다음 입력 토큰을 보고 적용할 규칙을 선택한다. 예: 재귀 하강 파서, LL 파서.\n상향식: 잎부터 루트 방향으로 파스 트리를 만든다. 최우단 유도의 역순을 따르며, 우문장 형태에서 핸들을 찾아 LHS로 환원(reduce)한다. 예: LR 파서(shift-reduce).",
  keys=["하향식: 루트부터, 최좌단 유도","상향식: 잎부터, 최우단 유도의 역순","대표 알고리즘(재귀 하강/LL vs LR)"], slot=7, pts=3)
Q("5-tb-2","topdown-bottomup","mc","상향식 파서가 따르는 유도 순서는?",
  3, choices=["최좌단 유도","최좌단 유도의 역순","최우단 유도","최우단 유도의 역순"])
Q("5-tb-3","topdown-bottomup","mc","하향식 파서가 문장 형태 xAα 에서 A-규칙을 고를 때 사용하는 정보는?",
  1, choices=["입력 전체","A가 생성하는 첫 토큰(다음 입력 토큰 하나)","스택의 상태 이력","GOTO 테이블"])
Q("5-tb-4","topdown-bottomup","mc","다음 중 하향식 파싱 알고리즘이 아닌 것은?",2,choices=["재귀 하강","LL 파서","LR 파서","테이블 기반 LL(1)"])
Q("5-tb-5","topdown-bottomup","calc","S → aAc, A → aA | b 일 때 입력 aabc를 상향식으로 파싱하는 과정(환원 순서)을 쓰고, 이것이 어떤 유도의 역순인지 쓰시오.",
  "aabc → (b를 A로 환원) aaAc → (aA를 A로 환원) aAc → (aAc를 S로 환원) S\n이는 최우단 유도 S ⇒ aAc ⇒ aaAc ⇒ aabc 의 역순이다.",
  keys=["b → A","aA → A","aAc → S","최우단 유도의 역순"])

Q("5-pc-1","parse-complexity","mc","모든 모호하지 않은 문법에 대해 동작하는 일반 파서의 시간 복잡도는?",
  2, choices=["O(n)","O(n log n)","O(n³)","O(2ⁿ)"])
Q("5-pc-2","parse-complexity","short","컴파일러가 모든 문법에 동작하는 파서 대신 일부 문법에만 동작하는 파서를 쓰는 이유를 쓰시오.",
  "모든 모호하지 않은 문법에 동작하는 파서는 복잡하고 비효율적(O(n³))이다. 컴파일러는 문법의 부분 집합(LL, LR 등)에서만 동작하지만 선형 시간 O(n)에 파싱하는 파서를 사용한다.",
  keys=["일반 파서 O(n³)","부분 집합만 지원하지만 O(n)"])

Q("5-rds-1","rd-structure","short","재귀 하강 파서의 구조를 설명하고, EBNF가 재귀 하강 파서에 적합한 이유를 쓰시오.",
  "문법의 각 비단말마다 그 비단말이 생성하는 문장을 파싱하는 부프로그램을 하나씩 둔, 재귀적 부프로그램들의 모음이다. 파스 트리를 하향식으로 만든다.\nEBNF는 비단말의 수를 최소화하므로(반복을 {}로 표현) 재귀 하강 파서의 기반으로 적합하다.",
  keys=["비단말마다 부프로그램","재귀적, 하향식","EBNF는 비단말 수 최소화"])
Q("5-rds-2","rd-structure","mc","재귀 하강 파서에 재귀가 쓰이는 이유로 교안이 든 것은?",
  0, choices=["프로그래밍 언어의 중첩 구조를 반영","속도가 빠르므로","스택이 필요 없으므로","좌순환을 처리하기 위해"])
Q("5-rds-3","rd-structure","ox","재귀 하강 파서는 LL 파서의 일종이다.",True)

Q("5-rdc-1","rd-coding","short","재귀 하강 파서에서 RHS가 하나인 규칙의 파싱 부프로그램을 코딩하는 규칙 2가지를 쓰시오.",
  "1. RHS의 각 단말 기호는 다음 입력 토큰과 비교해 같으면 계속(lex 호출), 다르면 오류.\n2. RHS의 각 비단말 기호는 그 비단말의 파싱 부프로그램을 호출.",
  keys=["단말: 다음 토큰과 비교","비단말: 해당 부프로그램 호출"])
Q("5-rdc-2","rd-coding","mc","재귀 하강 파서의 관례로 옳은 것은?",
  1, choices=["각 파싱 루틴은 시작할 때 lex()를 호출한다","모든 파싱 루틴은 끝날 때 다음 토큰을 nextToken에 남겨둔다","factor는 expr을 호출하지 않는다","오류 시 항상 프로그램을 종료한다"])
Q("5-rdc-3","rd-coding","calc","재귀 하강 파서에서 `<term> → <factor> {(* | /) <factor>}` 에 대한 함수 term()을 C로 작성하시오.",
  "void term() {\n    printf(\"Enter <term>\\n\");\n    factor();\n    while (nextToken == MULT_OP || nextToken == DIV_OP) {\n        lex();\n        factor();\n    }\n    printf(\"Exit <term>\\n\");\n}",
  keys=["factor() 먼저 호출","while (MULT_OP || DIV_OP)","루프 안에서 lex() 후 factor()"])
Q("5-rdc-4","rd-coding","mc","RHS가 여러 개인 비단말(<factor>)의 파싱 함수가 RHS를 고르는 방법은?",
  2, choices=["모두 시도해 보고 되돌아감(backtracking)","항상 첫 번째 RHS","다음 입력 토큰(lookahead)을 각 RHS가 생성할 수 있는 첫 토큰과 비교","GOTO 테이블 참조"])

for i,(s,keys) in enumerate([("x * (y - 2)",["x에서 factor 즉시 Exit","* 보고 term이 factor 다시 호출","( 에서 expr 재귀 진입","EOF 후 Exit 순서"]),
                              ("a + b * 3",["a 후 Exit <factor>, Exit <term>","+ 후 Enter <term>","* 처리는 term 안에서","마지막 Exit 3개"])]):
    tr="\n".join(rd.trace(s))
    Q(f"5-rdt-{i+1}","rd-trace","calc",f"교안의 재귀 하강 파서(expr/term/factor + lex)로 `{s}` 를 파싱할 때의 출력(Next token… / Enter… / Exit…)을 순서대로 쓰시오.",
      tr, keys=keys)
Q("5-rdt-3","rd-trace","mc","`(sum + 47) / total` 파싱에서 `)` 를 확인한 뒤 바로 다음 출력은?",
  1, choices=["Exit <expr>","Next token is: 24 Next lexeme is /","Enter <factor>","Exit <term>"],
  explain="factor가 ) 를 확인하면 lex()를 호출해 다음 토큰 /(24)를 읽는다. 그 다음 Exit <factor>.")
Q("5-rdt-4","rd-trace","mc","`a + b * 3` 파싱에서 `Enter <term>` 은 총 몇 번 출력되는가?",
  1, choices=["1번","2번","3번","4번"], explain="expr에서 a 쪽 term 1번, + 뒤 b * 3 쪽 term 1번 = 2번.")

Q("5-ll-1","ll-parsing","blank","LL 파싱의 첫 L은 입력을 (a)에서 (b)로 스캔한다는 뜻이고, 두 번째 L은 (c) 유도를 구성한다는 뜻이다.",
  ["왼쪽","오른쪽","최좌단"], accept=[["왼쪽","left","좌"],["오른쪽","right","우"],["최좌단","leftmost","좌단"]])
Q("5-ll-2","ll-parsing","mc","교안의 LL(1) 테이블(S → aAB, A → bA | ε, B → c)에서 A 행, c 열의 항목은?",
  2, choices=["A → bA","error","A → ε","B → c"], explain="A 다음에 B가 오고 B는 c로 시작 → A가 ε이 되어야 c를 만날 수 있음.")
Q("5-ll-3","ll-parsing","calc","S → aAB, A → bA | ε, B → c 와 LL(1) 테이블로 입력 abbc를 파싱할 때 적용되는 규칙을 순서대로 쓰시오.",
  "S → aAB (a 매치) → A → bA (b 매치) → A → bA (b 매치) → A → ε (다음 토큰 c) → B → c (c 매치) → 성공\n최좌단 유도: S ⇒ aAB ⇒ abAB ⇒ abbAB ⇒ abbB ⇒ abbc",
  keys=["S → aAB","A → bA 두 번","c를 보고 A → ε","B → c"])

Q("5-lrc-1","left-recursion","calc","다음 문법에서 좌순환을 제거하시오.\nE → E + T | T\nT → T * F | F\nF → (E) | id",
  "E  → T E'\nE' → + T E' | ε\nT  → F T'\nT' → * F T' | ε\nF  → (E) | id",
  keys=["E → T E'","E' → + T E' | ε","T → F T'","T' → * F T' | ε","F 그대로"])
Q("5-lrc-2","left-recursion","calc","다음 규칙에서 직접 좌순환을 제거하시오.\nA → Aa | Ab | c | d",
  "A  → cA' | dA'\nA' → aA' | bA' | ε",
  keys=["β(c, d)에 A' 붙이기","α(a, b)는 A' → αA'","A' → ε 포함"])
Q("5-lrc-3","left-recursion","mc","좌순환 문법이 하향식 파서의 기반이 될 수 없는 이유는?",
  1, choices=["모호하기 때문","A의 파싱 함수가 토큰을 소비하지 않고 자기 자신을 다시 호출해 무한 재귀에 빠지므로","FIRST 집합이 비어서","상향식으로만 표현되므로"])
Q("5-lrc-4","left-recursion","calc","다음 규칙에서 직접 좌순환을 제거하시오.\nS → S , x | S ; y | z",
  "S  → z S'\nS' → , x S' | ; y S' | ε",
  keys=["S → z S'","S' → , x S' | ; y S' | ε"])
Q("5-lrc-5","left-recursion","ox","간접 좌순환(A → Bα, B → Aβ)이 있어도 하향식 파서의 기반이 될 수 있다.",False,
  explain="직접이든 간접이든 좌순환이 있으면 하향식 파서의 기반이 될 수 없다.")
