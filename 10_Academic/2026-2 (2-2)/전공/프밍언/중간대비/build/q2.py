from qdsl import Q

EXPR_G = """<assign> → <id> = <expr>
<id>     → A | B | C
<expr>   → <expr> + <term> | <term>
<term>   → <term> * <factor> | <factor>
<factor> → ( <expr> ) | <id>"""

# ───────── U2 Ch.3 구문 ─────────
Q("2-ss-1","syn-sem","short","구문(syntax)과 의미론(semantics)에 대해 간략히 서술하시오.",
  "구문: 식, 문장, 프로그램 단위의 형식 또는 구조.\n의미론: 그 식, 문장, 프로그램 단위의 의미.\n예) while (bool_expr) statement 라는 형태가 구문이고, bool_expr가 참이면 statement를 실행하고 거짓이면 while 다음 문장으로 제어가 넘어간다는 것이 의미.",
  keys=["구문 = 형식/구조","의미론 = 의미","(예시가 있으면 좋음)"], slot=4, pts=3)
Q("2-ss-2","syn-sem","mc","Java의 `while (bool_expr) statement`에 대해 '조건식이 거짓이면 while 다음 문장으로 제어가 넘어간다'는 설명은?",
  1, choices=["구문","의미론","정적 의미론","어휘 구조"])
Q("2-ss-3","syn-sem","mc","언어 정의(구문+의미)를 사용하는 사람 중, '모호성·비일관성·설계 결함을 찾기 위해' 쓰는 사람은?",
  0, choices=["다른 언어 설계자","구현자","프로그래머","사용자 매뉴얼 작성자"])

Q("2-lt-1","lexeme-token","short","어휘항목(lexeme)과 토큰(token)을 간략히 서술하시오.",
  "어휘항목: 언어의 가장 낮은 수준의 구문 단위 (예: *, sum, begin).\n토큰: 어휘항목들의 범주(category) (예: identifier). 여러 어휘항목이 같은 토큰에 속할 수 있다.",
  keys=["어휘항목 = 가장 낮은 수준의 구문 단위","토큰 = 어휘항목의 범주"], slot=6, pts=3)
Q("2-lt-2","lexeme-token","short","`total = price * 3 - tax;` 를 어휘항목과 토큰으로 나누시오.",
  "total – identifier\n= – equal_sign(assign_op)\nprice – identifier\n* – mult_op\n3 – int_literal\n- – minus_op(sub_op)\ntax – identifier\n; – semicolon",
  keys=["8개 어휘항목을 빠짐없이","total/price/tax → identifier","3 → int_literal","연산자·세미콜론 토큰"])
Q("2-lt-3","lexeme-token","mc","`count = count + 1;` 에서 서로 다른 '토큰'의 개수는? (토큰: identifier, equal_sign, plus_op, int_literal, semicolon)",
  2, choices=["3","4","5","6"], explain="어휘항목은 6개(count, =, count, +, 1, ;)지만 토큰 종류는 identifier, equal_sign, plus_op, int_literal, semicolon = 5개.")
Q("2-lt-4","lexeme-token","ox","sum 과 index 는 서로 다른 어휘항목이지만 같은 토큰(identifier)에 속한다.",True)
Q("2-lt-5","lexeme-token","blank","어떤 알파벳 위의 문자열을 (a), 그것들의 집합을 (b) 라고 한다.",
  ["문장","언어"], accept=[["문장","sentence"],["언어","language"]])

Q("2-rg-1","recognizer-generator","mc","입력 문자열을 읽어 그 언어에 속하는지 판단하는 장치로, 컴파일러의 구문 분석기가 그 예인 것은?",
  0, choices=["언어 인식기","언어 생성기","메타언어","속성 문법"])
Q("2-rg-2","recognizer-generator","short","언어 인식기와 언어 생성기의 차이를 쓰시오.",
  "인식기: 입력 문자열이 그 언어에 속하는지 판단하는 장치 (예: 컴파일러의 구문 분석기).\n생성기: 그 언어의 문장을 생성하는 장치. 어떤 문장이 구문적으로 올바른지 생성기의 구조와 비교해 판단 (예: BNF 문법).",
  keys=["인식기: 속하는지 판단(구문 분석기)","생성기: 문장을 생성(문법)"])

Q("2-bnf-1","bnf","mc","BNF에 대한 설명으로 틀린 것은?",
  3, choices=["John Backus가 ALGOL 58을 기술하려고 만들었다","문맥 자유 문법과 동등하다","프로그래밍 언어를 위한 메타언어이다","문맥 자유 문법보다 표현력이 강하다"])
Q("2-bnf-2","bnf","blank","BNF 규칙의 왼쪽(LHS)은 하나의 (a) 이고, 오른쪽(RHS)은 단말과 비단말로 된 문자열이다. 유도는 특별한 비단말인 (b) 에서 시작한다.",
  ["비단말","시작 기호"], accept=[["비단말","비단말기호","nonterminal","추상화"],["시작기호","startsymbol","시작심볼"]])
Q("2-bnf-3","bnf","short","식별자 목록 `a, b, c` 같은 가변 길이 리스트를 BNF로 어떻게 표현하는지 규칙을 쓰고 설명하시오.",
  "<ident_list> → ident | ident , <ident_list>\n재귀 규칙(LHS가 RHS에 다시 나타나는 규칙)을 사용해 가변 길이 리스트를 표현한다.",
  keys=["재귀 규칙","<ident_list> → ident | ident , <ident_list> (또는 동등한 좌순환 형태)"])
Q("2-bnf-4","bnf","ox","문맥 자유 문법은 1950년대 중반 Noam Chomsky가 자연어의 구문을 기술하기 위해 개발했다.",True)
Q("2-bnf-5","bnf","mc","BNF에서 단말 기호(terminal)에 해당하는 것은?",
  1, choices=["<expr> 같은 추상화","어휘항목 또는 토큰","규칙(production)","시작 기호"])

Q("2-der-1","derivation","calc","다음 문법으로 `begin c = d - a end` 의 최좌단 유도를 쓰시오.",
  """<program> ⇒ begin <stmts> end
⇒ begin <stmt> end
⇒ begin <var> = <expr> end
⇒ begin c = <expr> end
⇒ begin c = <var> - <var> end
⇒ begin c = d - <var> end
⇒ begin c = d - a end""",
  code="""<program> → begin <stmts> end
<stmts>   → <stmt> | <stmt> ; <stmts>
<stmt>    → <var> = <expr>
<var>     → a | b | c | d
<expr>    → <var> + <var> | <var> - <var> | <var>""",
  keys=["<stmts> ⇒ <stmt> 선택","매 단계 가장 왼쪽 비단말 하나만 전개","<expr> ⇒ <var> - <var>"])
Q("2-der-2","derivation","calc","같은 문법(`<program> → begin <stmts> end` …)으로 `begin a = b ; c = a + d end` 의 최좌단 유도를 쓰시오.",
  """<program> ⇒ begin <stmts> end
⇒ begin <stmt> ; <stmts> end
⇒ begin <var> = <expr> ; <stmts> end
⇒ begin a = <expr> ; <stmts> end
⇒ begin a = <var> ; <stmts> end
⇒ begin a = b ; <stmts> end
⇒ begin a = b ; <stmt> end
⇒ begin a = b ; <var> = <expr> end
⇒ begin a = b ; c = <expr> end
⇒ begin a = b ; c = <var> + <var> end
⇒ begin a = b ; c = a + <var> end
⇒ begin a = b ; c = a + d end""",
  code="""<program> → begin <stmts> end
<stmts>   → <stmt> | <stmt> ; <stmts>
<stmt>    → <var> = <expr>
<var>     → a | b | c | d
<expr>    → <var> + <var> | <var> - <var> | <var>""",
  keys=["첫 문장 다 끝낸 뒤 두 번째 <stmts> 전개","<expr> ⇒ <var> (첫 문장)","매 줄 비단말 하나만"])
Q("2-der-3","derivation","mc","유도 과정에서 나오는 모든 기호열을 무엇이라 하는가?",
  1, choices=["문장 (sentence)","문장 형태 (sentential form)","어휘항목","핸들"])
Q("2-der-4","derivation","ox","최좌단 유도를 쓰느냐 최우단 유도를 쓰느냐에 따라 문법이 생성하는 언어가 달라진다.",
  False, explain="유도 순서는 생성되는 언어에 영향을 주지 않는다.")
Q("2-der-5","derivation","mc","`A = <id> + <term> * <factor>` 에서 최좌단 유도의 다음 단계로 전개할 비단말은?",
  0, choices=["<id>","<term>","<factor>","아무거나"])

Q("2-pt-1","parse-tree","calc","다음 문법을 사용하여 `B = C * (A + B)` 의 파스 트리와 최좌단 유도를 보이시오.",
  """<assign> ⇒ <id> = <expr>
⇒ B = <expr>
⇒ B = <term>
⇒ B = <term> * <factor>
⇒ B = <factor> * <factor>
⇒ B = <id> * <factor>
⇒ B = C * <factor>
⇒ B = C * ( <expr> )
⇒ B = C * ( <expr> + <term> )
⇒ B = C * ( <term> + <term> )
⇒ B = C * ( <factor> + <term> )
⇒ B = C * ( <id> + <term> )
⇒ B = C * ( A + <term> )
⇒ B = C * ( A + <factor> )
⇒ B = C * ( A + <id> )
⇒ B = C * ( A + B )

파스 트리:
<assign>
├─ <id> ─ B
├─ =
└─ <expr>
   └─ <term>
      ├─ <term> ─ <factor> ─ <id> ─ C
      ├─ *
      └─ <factor>
         ├─ (
         ├─ <expr>
         │  ├─ <expr> ─ <term> ─ <factor> ─ <id> ─ A
         │  ├─ +
         │  └─ <term> ─ <factor> ─ <id> ─ B
         └─ )""",
  code=EXPR_G, keys=["<expr> ⇒ <term> ⇒ <term> * <factor> (곱셈이 위)","괄호는 <factor> → ( <expr> )","최좌단 순서","파스 트리 구조"], slot=10, pts=3)
Q("2-pt-2","parse-tree","calc","다음 문법을 사용하여 `A = (B + C) * A` 의 파스 트리와 최좌단 유도를 보이시오.",
  """<assign> ⇒ <id> = <expr>
⇒ A = <expr>
⇒ A = <term>
⇒ A = <term> * <factor>
⇒ A = <factor> * <factor>
⇒ A = ( <expr> ) * <factor>
⇒ A = ( <expr> + <term> ) * <factor>
⇒ A = ( <term> + <term> ) * <factor>
⇒ A = ( <factor> + <term> ) * <factor>
⇒ A = ( <id> + <term> ) * <factor>
⇒ A = ( B + <term> ) * <factor>
⇒ A = ( B + <factor> ) * <factor>
⇒ A = ( B + <id> ) * <factor>
⇒ A = ( B + C ) * <factor>
⇒ A = ( B + C ) * <id>
⇒ A = ( B + C ) * A

파스 트리:
<assign>
├─ <id> ─ A
├─ =
└─ <expr>
   └─ <term>
      ├─ <term> ─ <factor>
      │           ├─ (
      │           ├─ <expr>
      │           │  ├─ <expr> ─ <term> ─ <factor> ─ <id> ─ B
      │           │  ├─ +
      │           │  └─ <term> ─ <factor> ─ <id> ─ C
      │           └─ )
      ├─ *
      └─ <factor> ─ <id> ─ A""",
  code=EXPR_G, keys=["<term> * <factor>가 최상위","왼쪽 <factor> ⇒ ( <expr> )","괄호 안 <expr> + <term>","최좌단 순서 유지"], slot=10, pts=3)
Q("2-pt-3","parse-tree","calc","다음 문법을 사용하여 `C = A + B * C` 의 파스 트리와 최좌단 유도를 보이시오.",
  """<assign> ⇒ <id> = <expr>
⇒ C = <expr>
⇒ C = <expr> + <term>
⇒ C = <term> + <term>
⇒ C = <factor> + <term>
⇒ C = <id> + <term>
⇒ C = A + <term>
⇒ C = A + <term> * <factor>
⇒ C = A + <factor> * <factor>
⇒ C = A + <id> * <factor>
⇒ C = A + B * <factor>
⇒ C = A + B * <id>
⇒ C = A + B * C

파스 트리:
<assign>
├─ <id> ─ C
├─ =
└─ <expr>
   ├─ <expr> ─ <term> ─ <factor> ─ <id> ─ A
   ├─ +
   └─ <term>
      ├─ <term> ─ <factor> ─ <id> ─ B
      ├─ *
      └─ <factor> ─ <id> ─ C""",
  code=EXPR_G, keys=["+가 위(<expr> + <term>)","*는 <term> 안(아래)","최좌단 순서"], slot=10, pts=3)
Q("2-pt-4","parse-tree","mc","파스 트리에서 잎(leaf) 노드가 될 수 '없는' 것은? (완전한 문장의 파스 트리라고 가정)",
  2, choices=["단말 기호","어휘항목","비단말 기호","토큰"], explain="완전한 문장의 파스 트리에서 내부 노드 = 비단말, 잎 = 단말.")
Q("2-pt-5","parse-tree","ox","파스 트리의 한 노드의 자식들은 그 노드에 적용한 규칙의 RHS 기호들을 왼쪽부터 순서대로 나타낸다.",True)

Q("2-amb-1","ambiguity","calc","다음 문법이 모호함을 증명하시오.\n<S> → <A>\n<A> → <A> - <A> | <id>\n<id> → a | b | c",
  """문장 a - b - c 에 대해 서로 다른 최좌단 유도가 2개 존재한다.
유도 1 ((a - b) - c):
<S> ⇒ <A> ⇒ <A> - <A> ⇒ <A> - <A> - <A> ⇒ <id> - <A> - <A> ⇒ a - <A> - <A>
⇒ a - <id> - <A> ⇒ a - b - <A> ⇒ a - b - <id> ⇒ a - b - c
(첫 <A> - <A>에서 왼쪽 <A>를 <A> - <A>로 전개)
유도 2 (a - (b - c)):
<S> ⇒ <A> ⇒ <A> - <A> ⇒ <id> - <A> ⇒ a - <A> ⇒ a - <A> - <A>
⇒ a - <id> - <A> ⇒ a - b - <A> ⇒ a - b - <id> ⇒ a - b - c
(오른쪽 <A>를 <A> - <A>로 전개)
같은 문장에 대해 파스 트리가 2개이므로 이 문법은 모호하다.""",
  keys=["구체적 문장 선택 (a - b - c 등)","서로 다른 최좌단 유도(또는 파스 트리) 2개","결론: 파스 트리 2개 → 모호"], slot=8, pts=3)
Q("2-amb-2","ambiguity","calc","다음 문법이 모호함을 증명하시오.\n<S> → <S> <S> | a",
  """문장 aaa 에 대해 서로 다른 최좌단 유도 2개:
유도 1: <S> ⇒ <S><S> ⇒ <S><S><S> ⇒ a<S><S> ⇒ aa<S> ⇒ aaa   (왼쪽 <S>를 <S><S>로: (aa)a)
유도 2: <S> ⇒ <S><S> ⇒ a<S> ⇒ a<S><S> ⇒ aa<S> ⇒ aaa       (오른쪽 <S>를 <S><S>로: a(aa))
같은 문장에 서로 다른 파스 트리가 2개 존재하므로 모호하다.""",
  keys=["문장 aaa","두 최좌단 유도가 실제로 다름","결론"], slot=8, pts=3)
Q("2-amb-3","ambiguity","calc","다음 문법이 모호함을 증명하시오.\n<E> → <E> + <E> | <E> * <E> | id",
  """문장 id + id * id 에 대해:
유도 1 (+가 루트): <E> ⇒ <E> + <E> ⇒ id + <E> ⇒ id + <E> * <E> ⇒ id + id * <E> ⇒ id + id * id
유도 2 (*가 루트): <E> ⇒ <E> * <E> ⇒ <E> + <E> * <E> ⇒ id + <E> * <E> ⇒ id + id * <E> ⇒ id + id * id
두 최좌단 유도(파스 트리)가 다르므로 모호하다.""",
  keys=["문장 선택","두 최좌단 유도 (+ 루트 / * 루트)","결론"], slot=8, pts=3)
Q("2-amb-4","ambiguity","mc","문법이 모호하다는 것과 동치가 '아닌' 것은?",
  3, choices=["어떤 문장 형태에 대해 서로 다른 파스 트리가 2개 이상","어떤 문장에 대해 최좌단 유도가 2개 이상","어떤 문장에 대해 최우단 유도가 2개 이상","어떤 문장에 대해 최좌단 유도와 최우단 유도가 서로 다름"],
  explain="모호하지 않은 문법도 최좌단 유도와 최우단 유도는 보통 다르다. 같은 '종류'의 유도가 2개 이상이어야 모호.")
Q("2-amb-5","ambiguity","ox","'A = B + C * A 는 (B+C)*A로도 B+(C*A)로도 해석될 수 있다'라고 말로만 쓰면 모호성 증명으로 충분하다.",
  False, explain="같은 문장에 대한 서로 다른 파스 트리 2개(또는 최좌단 유도 2개)를 실제로 보여야 한다.")

Q("2-prec-1","precedence","short","모호한 식 문법을 우선순위를 반영해 모호하지 않게 만드는 원리를 설명하시오.",
  "연산자 우선순위 수준마다 별도의 비단말(<expr>, <term>, <factor>)을 둔다. 우선순위가 높은 연산자일수록 파스 트리에서 더 낮은 곳에 나타나도록 문법을 구성한다(예: *는 <term>, +는 <expr>).",
  keys=["별도 비단말 사용","높은 우선순위 = 트리의 낮은 곳"])
Q("2-prec-2","precedence","mc","모호하지 않은 식 문법(<expr>/<term>/<factor>)에서 `*`가 `+`보다 먼저 계산되는 이유는?",
  1, choices=["*가 문법에서 먼저 나오므로","*가 <term> 수준에 있어 파스 트리에서 항상 +보다 아래에 오므로","*가 좌결합이므로","*가 단말이므로"])
Q("2-prec-3","precedence","calc","나눗셈 `/`를 곱셈과 같은 우선순위, 뺄셈 `-`를 덧셈과 같은 우선순위로 추가하도록 아래 문법을 수정하시오.\n<expr> → <expr> + <term> | <term>\n<term> → <term> * <factor> | <factor>\n<factor> → ( <expr> ) | <id>",
  "<expr> → <expr> + <term> | <expr> - <term> | <term>\n<term> → <term> * <factor> | <term> / <factor> | <factor>\n<factor> → ( <expr> ) | <id>",
  keys=["- 는 <expr> 수준에 추가","/ 는 <term> 수준에 추가","좌순환 형태 유지(좌결합)"])

Q("2-assoc-1","associativity","mc","`<expr> → <expr> + const | const` 는 + 를 어떻게 결합시키는가?",
  0, choices=["좌결합","우결합","결합성 없음","모호함"], explain="LHS가 RHS의 맨 왼쪽에 나오는 좌순환 → 좌결합.")
Q("2-assoc-2","associativity","short","거듭제곱 연산자 ** 를 우결합으로 만드는 문법 규칙을 쓰고 이유를 설명하시오.",
  "<factor> → <exp> ** <factor> | <exp>\n<exp> → ( <expr> ) | id\n우순환(LHS가 RHS의 맨 오른쪽에 나타남)으로 만들면 오른쪽 피연산자 쪽으로 트리가 깊어져 a ** b ** c = a ** (b ** c)가 된다.",
  keys=["우순환 규칙 (<factor> → <exp> ** <factor> | <exp>)","우순환 → 우결합"])
Q("2-assoc-3","associativity","mc","`<expr> → <expr> + <expr> | const` 의 문제점은?",
  2, choices=["좌결합만 표현됨","우결합만 표현됨","모호함 (결합 방향이 정해지지 않음)","const를 생성할 수 없음"])
Q("2-assoc-4","associativity","ox","좌순환 규칙은 좌결합을 표현하기 좋지만, 하향식 파서의 기반으로는 사용할 수 없다.",True)

Q("2-de-1","dangling-else","short","if-then-else 문법이 모호해지는 이유를 예를 들어 설명하고, 대부분 언어의 해결 규칙을 쓰시오.",
  "<if_stmt> → if (<logic_expr>) then <stmt> | if (<logic_expr>) then <stmt> else <stmt> 일 때, if C1 then if C2 then S1 else S2 에서 else가 바깥 if와 짝인지 안쪽 if와 짝인지 두 가지 파스 트리가 생긴다(모호).\n해결 규칙: else는 가장 가까운 짝 없는(unmatched) then과 짝지어진다. 문법적으로는 <matched>/<unmatched> 비단말을 나눠 then과 else 사이에는 matched 문장만 오게 한다.",
  keys=["중첩 if에서 else의 짝이 두 가지","else는 가장 가까운 짝 없는 then과","matched/unmatched 문법"])
Q("2-de-2","dangling-else","mc","모호하지 않은 if 문법에서 `then`과 `else` 사이에 올 수 있는 것은?",
  1, choices=["<unmatched>","<matched>","<stmt>","아무 문장"])
Q("2-de-3","dangling-else","blank","<matched> → if (<logic_expr>) then (a) else (b) | a non-if statement",
  ["<matched>","<matched>"], accept=[["<matched>","matched"],["<matched>","matched"]])

Q("2-ebnf-1","ebnf","calc","다음 BNF를 EBNF로 바꾸시오.\n<expr> → <expr> + <term> | <expr> - <term> | <term>\n<term> → <term> * <factor> | <term> / <factor> | <factor>",
  "<expr> → <term> {(+ | -) <term>}\n<term> → <factor> {(* | /) <factor>}",
  keys=["{ } 반복 사용","( | ) 대안 사용","좌순환 제거된 형태"])
Q("2-ebnf-2","ebnf","mc","EBNF에서 0번 이상 반복을 나타내는 기호는?",2,choices=["[ ]","( )","{ }","< >"])
Q("2-ebnf-3","ebnf","mc","`<if_stmt> → if (<expr>) <stmt> [else <stmt>]` 에서 [ ] 의 의미는?",
  0, choices=["선택적 부분 (0 또는 1번)","0번 이상 반복","대안 중 하나","비단말"])
Q("2-ebnf-4","ebnf","calc","다음 EBNF를 BNF로 바꾸시오.\n<ident> → letter {letter | digit}",
  "<ident> → letter | letter <rest>\n<rest> → <char> | <char> <rest>\n<char> → letter | digit\n(또는 <ident> → letter | <ident> letter | <ident> digit)",
  keys=["반복을 재귀 규칙으로","letter로 시작","letter/digit 반복"])
Q("2-ebnf-5","ebnf","ox","EBNF는 BNF보다 표현할 수 있는 언어의 범위가 넓다.",
  False, explain="EBNF는 가독성·간결성을 위한 확장일 뿐 표현력은 BNF와 같다.")

Q("2-ebv-1","ebnf-variants","mc","최근 EBNF 변형에서 `AssignmentOperator → one of = *= /= %=` 의 'one of'는?",
  1, choices=["선택적 부분","나열된 것 중 하나를 선택","반복","단말 기호 표시"])
Q("2-ebv-2","ebnf-variants","mc","`SimpleName (FormalParameterList_opt)` 의 opt 아래첨자의 의미는?",
  0, choices=["선택적(생략 가능)","최적화","연산자","반복"])
