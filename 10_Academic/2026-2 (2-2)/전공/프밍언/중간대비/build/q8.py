from qdsl import Q, QS
from fractions import Fraction as Fr
import random, lr
rnd = random.Random(42)

# ───────── concept weights: how many questions per concept in a lesson check ─────────
W3 = "criteria orthogonality tradeoffs impl-methods lexeme-token derivation parse-tree ambiguity precedence wp-assign wp-seq wp-select invariant loop-proof topdown-bottomup left-recursion pairwise handle-howto lr-actions lr-routine var-attrs var-categories static-scope blocks dynamic-scope sem-three ag-attr-kinds".split()
W1 = "why read-why cost other-criteria preproc-env recognizer-generator ebnf-variants sem-why axiomatic-eval sa-bnf lexer-build parser-goals parse-complexity lifetime-def static-scope-eval named-const lr-trace".split()
WEIGHTS = {c:3 for c in W3}
WEIGHTS.update({c:1 for c in W1})   # everything else defaults to 2

# ───────── U1 additions ─────────
Q("1-dom-4","domain","mc","'계속 실행되므로 효율이 중요하다'는 특징을 가진 도메인과 대표 언어는?",
  3, choices=["과학 응용 – Fortran","사무 응용 – COBOL","웹 – PHP","시스템 프로그래밍 – C"])
Q("1-crit-5","criteria","mc","다음 중 언어 평가 기준 4가지에 들어가지 '않는' 것은?",
  2, choices=["판독성","비용","이식성","작성력"], explain="이식성·일반성·분명성은 '기타 기준'. 핵심 4가지 = 판독성, 작성력, 신뢰성, 비용.")
Q("1-crit-6","criteria","mc","교안 표에서 '추상화 지원'과 '표현력'이 영향을 주는 기준의 조합은?",
  1, choices=["판독성만","작성력과 신뢰성","판독성과 비용","신뢰성만"])
Q("1-crit-7","criteria","ox","단순성과 직교성은 판독성, 작성력, 신뢰성 세 기준 모두에 영향을 준다.",True)
Q("1-simp-4","simplicity","ox","같은 연산을 하는 방법이 여러 개 있으면 작성할 때는 편할 수 있지만 판독성 측면의 단순성을 해친다.",True)
Q("1-orth-5","orthogonality","blank","직교성이 높으면 규칙의 (a) 가 적어지고 규칙성이 높아져 배우고 읽기 쉽다. C에서 구조체는 반환할 수 있지만 (b) 은 반환할 수 없는 것은 직교성이 부족한 예이다.",
  ["예외","배열"], accept=[["예외","exception","exceptions","예외사항"],["배열","array","arrays"]])
Q("1-orth-6","orthogonality","short","'너무 많은 직교성'이 왜 문제가 되는지 예와 함께 설명하시오.",
  "모든 조합이 합법이 되면 이상한 조합도 허용되어 오히려 복잡해지고 오류가 탐지되지 않는다. 예) 모든 것이 값을 갖는 식이 되면 x := (if a > b then a := b else b := a fi); 같은 코드도 합법이 되어 읽기 어렵다.",
  keys=["이상한 조합까지 합법","오류 미탐지/복잡","예: if 식 안의 배정"])
Q("1-syn-4","syntax-design","mc","'의미가 구문에서 바로 드러나야 한다'는 원칙을 위반하는 C의 예약어는?",
  1, choices=["while","static","return","int"])
Q("1-wr-4","writability","mc","작성력을 '높이는' 특성이 아닌 것은?",
  3, choices=["추상화 지원","표현력","단순성과 직교성","별칭 허용"], explain="별칭은 신뢰성을 낮추는 요인으로 교안에 나온다.")
Q("1-trade-6","tradeoffs","ox","APL은 강력한 연산자로 프로그램을 짧게 쓸 수 있어 판독성과 작성력이 모두 높다.",False,
  explain="작성력은 높지만 판독성은 나쁘다 → 판독성 vs 작성력의 상충 예.")
Q("1-impl-5","impl-methods","mc","'고급 언어를 해석하기 쉬운 중간 언어로 번역한 뒤 그것을 해석'하는 방식은?",
  2, choices=["컴파일","순수 해석","혼합형 구현","전처리"])
Q("1-impl-6","impl-methods","blank","순수 해석은 컴파일된 프로그램보다 실행이 (a) 배 느리고, 대신 실행 시간 오류를 (b) 수준에서 바로 보여주기 쉽다.",
  ["10~100","소스"], accept=[["10~100","10-100","10~100배","10에서100","10~100배느림"],["소스","원시","원시코드","소스코드","source"]])
Q("1-phase-4","compile-phases","mc","컴파일 과정에서 '모든 단계가 공통으로 참조하는' 것은?",
  0, choices=["심볼 테이블","파스 트리","중간 코드","적재 모듈"])

# ───────── U2 additions ─────────
Q("2-ss-4","syn-sem","ox","'변수 이름은 문자로 시작해야 한다'는 규칙은 의미론이 아니라 구문에 속한다.",True)
Q("2-lt-6","lexeme-token","mc","`x1 = x1 * 10;` 의 어휘항목 수와 토큰 종류 수는? (토큰: identifier, equal_sign, mult_op, int_literal, semicolon)",
  1, choices=["6개 / 6종류","6개 / 5종류","5개 / 5종류","7개 / 5종류"], explain="어휘항목: x1, =, x1, *, 10, ; = 6개. 토큰 종류: identifier, equal_sign, mult_op, int_literal, semicolon = 5종류.")
Q("2-der-6","derivation","mc","문법 `<expr> → <var> + <var> | <var>`, `<var> → a | b` 에서 `a + <var>` 다음의 최좌단 유도 단계로 가능한 것은?",
  0, choices=["a + b","<var> + b","a + <var> + <var>","a + b + b"])
Q("2-der-7","derivation","calc","다음 문법으로 `begin d = a + b ; a = c end` 의 최좌단 유도를 쓰시오.\n<program> → begin <stmts> end\n<stmts> → <stmt> | <stmt> ; <stmts>\n<stmt> → <var> = <expr>\n<var> → a | b | c | d\n<expr> → <var> + <var> | <var> - <var> | <var>",
  """<program> ⇒ begin <stmts> end
⇒ begin <stmt> ; <stmts> end
⇒ begin <var> = <expr> ; <stmts> end
⇒ begin d = <expr> ; <stmts> end
⇒ begin d = <var> + <var> ; <stmts> end
⇒ begin d = a + <var> ; <stmts> end
⇒ begin d = a + b ; <stmts> end
⇒ begin d = a + b ; <stmt> end
⇒ begin d = a + b ; <var> = <expr> end
⇒ begin d = a + b ; a = <expr> end
⇒ begin d = a + b ; a = <var> end
⇒ begin d = a + b ; a = c end""",
  keys=["<stmts> ⇒ <stmt> ; <stmts>","첫 문장 끝까지 먼저","매 단계 비단말 하나"])
Q("2-pt-6","parse-tree","mc","식 문법(<expr>/<term>/<factor>)으로 만든 `A = B * C + A` 의 파스 트리에서 루트 아래 <expr>의 자식은?",
  0, choices=["<expr> + <term>","<term>","<term> * <factor>","<expr> * <term>"], explain="+ 가 가장 낮은 우선순위라 최상위 <expr> → <expr> + <term>. B * C는 왼쪽 <expr> ⇒ <term> 안에 들어감.")
Q("2-amb-6","ambiguity","mc","다음 중 모호한 문법은?",
  2, choices=["<E> → <E> + <T> | <T>,  <T> → id","<E> → <T> + <E> | <T>,  <T> → id","<E> → <E> + <E> | id","<E> → id + <E> | id"])
Q("2-prec-4","precedence","mc","모호하지 않은 식 문법에서 `A = B + C * A`의 파스 트리를 그리면 트리에서 더 아래(잎 쪽)에 있는 연산자는?",
  1, choices=["+","*","둘이 같은 높이","괄호에 따라 다름"])
Q("2-prec-5","precedence","ox","우선순위가 높은 연산자일수록 파스 트리에서 루트에 가까워야 한다.",False,
  explain="높은 우선순위 = 먼저 계산 = 트리에서 더 낮은 곳(잎 쪽).")
Q("2-prec-6","precedence","calc","다음 문법에 거듭제곱 연산자 ^ 를 * 보다 높은 우선순위로, 우결합이 되게 추가하시오.\n<expr> → <expr> + <term> | <term>\n<term> → <term> * <factor> | <factor>\n<factor> → ( <expr> ) | <id>",
  "<expr> → <expr> + <term> | <term>\n<term> → <term> * <pow> | <pow>\n<pow> → <factor> ^ <pow> | <factor>\n<factor> → ( <expr> ) | <id>",
  keys=["새 비단말을 <term>과 <factor> 사이에","우순환 형태(<factor> ^ <pow>)로 우결합","<term>이 새 비단말을 참조"])
Q("2-de-4","dangling-else","ox","대부분의 언어에서 else는 가장 바깥쪽 if와 짝지어진다.",False,
  explain="else는 가장 가까운 짝 없는(unmatched) then과 짝지어진다.")

# ───────── U3 additions ─────────
Q("3-ss-4","static-semantics","mc","정적 의미론에 대한 설명으로 옳은 것은?",
  1, choices=["프로그램 실행 중의 상태 변화를 기술","프로그램의 적법한 형식(주로 타입 제약)에 관한 규칙으로 컴파일 시간에 검사 가능","파스 트리를 생성하는 규칙","정확성 증명을 위한 규칙"])
Q("3-ag-4","ag-def","ox","속성 문법은 문맥 자유 문법에 속성, 의미 함수, 술어 함수를 추가한 것이다.",True)
Q("3-ak-5","ag-attr-kinds","mc","상속 속성 I(Xj) = f(A(X0), …, A(Xn)) 에서 정보가 흐르는 방향은?",
  1, choices=["자식 → 부모 (위로)","부모·형제 → 자식 (아래로/옆으로)","잎에서 고정","스택으로"])
Q("3-ak-6","ag-attr-kinds","blank","속성 문법에서 잎 노드에 처음부터 정해진 속성을 (a) 속성이라 하며, 예로 심볼 테이블에서 찾은 변수의 (b) 가 있다.",
  ["내장","타입"], accept=[["내장","intrinsic","고유"],["타입","type","자료형","형"]])
Q("3-st-5","sem-three","mc","'이상적인 기계에서 실행했을 때 기계 상태(메모리, 레지스터)의 변화로 의미를 정의'하는 의미론은?",
  0, choices=["연산 의미론","표기 의미론","공리 의미론","정적 의미론"])
Q("3-st-6","sem-three","ox","표기 의미론은 언어 사용자에게 가장 유용한 의미 기술 방법이다.",False,
  explain="표기 의미론은 정밀하지만 복잡해서 사용자에겐 거의 쓸모없다. 사용자 매뉴얼엔 비형식적 연산 의미론이 적합.")
Q("3-op-4","operational","mc","고급 언어에 연산 의미론을 적용하려면 무엇이 필요한가?",
  2, choices=["재귀 함수","전조건","가상 기계 (virtual machine)","속성 문법"])
Q("3-asr-4","assertions","mc","Hoare triple {P} S {Q}에서 P는?",0,choices=["전조건","후조건","루프 불변자","문장"])

def lin(a,b,v):  # "a*v + b" pretty
    s = (f"{a} * {v}" if a not in (1,-1) else (v if a==1 else f"-{v}"))
    if b>0: s += f" + {b}"
    elif b<0: s += f" - {-b}"
    return s
def solve_gt(a,b,c,op,v):  # a*v+b op c -> v op' k
    k = Fr(c-b, a); flip = a<0
    ops={">":"<","<":">",">=":"<=","<=":">="}
    o = ops[op] if flip else op
    ks = str(k) if k.denominator==1 else f"{k.numerator}/{k.denominator}"
    return f"{{{v} {o} {ks}}}", (o,k)
def fmtk(o,k,v):
    ks = str(k) if k.denominator==1 else f"{k.numerator}/{k.denominator}"
    return f"{{{v} {o} {ks}}}"
gen=[(3,-2,"x","y",">",10),(2,5,"a","b","<",1),(-3,4,"x","y",">",1),(4,1,"s","t",">=",9),(5,-3,"b","a","<",12),(-2,6,"y","x","<=",0)]
for i,(a,b,lhs,v,op,c) in enumerate(gen):
    ans,(o,k)=solve_gt(a,b,c,op,v)
    flipo={">":"<","<":">",">=":"<=","<=":">="}[o]
    wrong=[fmtk(flipo,k,v), fmtk(o,Fr(c+b,a),v), fmtk(o,Fr(c,a),v)]
    if a<0: wrong[0]=fmtk({">":"<","<":">",">=":"<=","<=":">="}[o],k,v)
    ch=[ans]+[w for w in dict.fromkeys(wrong) if w!=ans][:3]
    while len(ch)<4: ch.append(fmtk(o,k+1,v))
    rnd.shuffle(ch)
    Q(f"3-wpa-g{i+1}","wp-assign","mc",f"다음 배정문과 후조건의 최약 전조건은?\n  {lhs} = {lin(a,b,v)} {{{lhs} {op} {c}}}",
      ch.index(ans), choices=ch, explain=f"{lin(a,b,v)} {op} {c} 를 정리 → {ans}" + (" (음수로 나눠서 부등호 반전)" if a<0 else ""))
Q("3-wpt-4","wp-theorem","mc","{x > 2} x = 2 * x - 1 {x > 5} 에 대한 판단으로 옳은 것은?",
  1, choices=["배정 공리만으로 증명된다","거짓이다 (wp = {x > 3}인데 x > 2 ⇒ x > 3 이 성립하지 않음)","결과 규칙으로 증명된다","판단할 수 없다"])
Q("3-con-4","consequence","mc","{x > 7} x = x - 3 {x > 0} 은 어떻게 증명되는가?",
  2, choices=["배정 공리만으로","시퀀스 규칙으로","배정 공리로 {x > 3}을 얻고 x > 7 ⇒ x > 3 이므로 결과 규칙으로","증명 불가"])
seqg=[(("a","2 * b - 4"),("b","a + 1"),"b > 5","① a + 1 > 5 → {a > 4}\n② 2b - 4 > 4 → {b > 4}","{b > 4}",["{b > 5}","{a > 4}","{b > 3}"]),
      (("x","y - 3"),("y","2 * x"),"y < 8","① 2x < 8 → {x < 4}\n② y - 3 < 4 → {y < 7}","{y < 7}",["{x < 4}","{y < 11}","{y < 5}"]),
      (("m","n + 2"),("n","3 * m - 1"),"n > 11","① 3m - 1 > 11 → {m > 4}\n② n + 2 > 4 → {n > 2}","{n > 2}",["{m > 4}","{n > 4}","{n > 6}"])]
for i,((v1,e1),(v2,e2),post,expl,ans,wr) in enumerate(seqg):
    ch=[ans]+wr; rnd.shuffle(ch)
    Q(f"3-seq-g{i+1}","wp-seq","mc",f"다음 시퀀스의 최약 전조건은?\n  {v1} = {e1};\n  {v2} = {e2};\n  {{{post}}}",
      ch.index(ans), choices=ch, explain="마지막 문장부터 거꾸로:\n"+expl)
Q("3-sel-7","wp-select","mc","`if (a > 0) b = a + 1 else b = 1 - a; {b > 3}` 에서 then 쪽과 else 쪽의 전조건은?",
  0, choices=["then {a > 2}, else {a < -2}","then {a > 2}, else {a > -2}","then {a > 4}, else {a < -4}","then {a > 3}, else {a < 3}"], explain="then: a + 1 > 3 → a > 2 / else: 1 - a > 3 → -a > 2 → a < -2")
Q("3-sel-8","wp-select","calc","다음 선택문과 후조건에 대해 최약 전조건을 계산하시오.\n  if (x > y)\n      y = x + 3\n  else\n      y = 2 * x + 1;\n  {y > 7}",
  "then: x + 3 > 7 → {x > 4}\nelse: 2x + 1 > 7 → {x > 3}\nx > 4 ⇒ x > 3 이므로 (교재 방식) 최약 전조건: {x > 4}\n(정밀하게는 {(x > y and x > 4) or (x <= y and x > 3)})",
  keys=["then {x > 4}","else {x > 3}","결론 {x > 4}"], slot=12, pts=5)
Q("3-lr-4","loop-rule","mc","불변자 조건 중 '루프 몸체를 한 번 실행해도 I가 유지된다'를 나타내는 것은?",
  1, choices=["P ⇒ I","{I and B} S {I}","(I and not B) ⇒ Q","루프 종료"])
Q("3-inv-5","invariant","mc","`while i <> n do i = i + 1 end {i = n}` (시작 시 i = 0, n >= 0) 의 적절한 루프 불변자는?",
  2, choices=["{i = n}","{i >= n}","{i <= n}","{i > 0}"])
Q("3-inv-6","invariant","mc","`while k > 0 do k = k - 2 end` 의 후조건이 {k <= 0} 일 때, I and not B ⇒ Q 를 만족하는 불변자로 가장 알맞은 것은? (k의 초기값은 정수)",
  3, choices=["{k > 0}","{k = 0}","{k < 0}","{true} (아무 조건 없음)"], explain="not B = k <= 0 자체가 Q이므로 I는 아무 조건이어도 (I and k <= 0) ⇒ k <= 0 이 성립. 가장 약한 I = true.")
Q("3-lp-5","loop-proof","calc","다음 프로그램이 올바름을 증명하시오.\n{n >= 0}\nc = 0;\nr = 1;\nwhile c <> n do\n    c = c + 1;\n    r = r * 2;\nend\n{r = 2^n}",
  "불변자 I = (r = 2^c) and (c <= n)\n1. P ⇒ I: 루프 직전 c = 0, r = 1 = 2^0, 0 <= n ✓\n2. {I and B} S {I}: c ≠ n 이고 c <= n 이므로 c < n. c = c + 1 → c <= n, r = r * 2 = 2^(c-1) * 2 = 2^c ✓\n3. (I and not B) ⇒ Q: c = n 이면 r = 2^n ✓\n4. 종료: c는 0에서 1씩 증가하고 c <= n 이므로 n에 도달",
  keys=["I = (r = 2^c) and c <= n","P ⇒ I","몸체 유지","c = n → Q","종료"], slot=19, pts=10)
Q("3-lp-6","loop-proof","mc","팩토리얼 증명에서 불변자 I = (fact = (count+1)*…*n) and (count >= 0) 일 때, (I and not B) ⇒ Q 를 확인하는 방법은? (B: count <> 0)",
  0, choices=["count = 0을 대입하면 fact = 1*2*…*n = n!","count = n을 대입하면 fact = 1","fact = 1이므로 Q 성립","count가 감소하므로 종료"])

# ───────── U4 additions ─────────
Q("4-lp-4","lex-vs-parser","mc","어휘 분석기와 구문 분석기의 짝으로 옳은 것은?",
  0, choices=["어휘: 정규 문법·유한 오토마타 / 구문: CFG·푸시다운 오토마타","어휘: CFG / 구문: 정규 문법","둘 다 튜링 기계","어휘: 푸시다운 / 구문: 유한 오토마타"])
Q("4-sep-4","separate-why","ox","어휘 분석과 구문 분석을 분리하면 파서가 공백·주석 같은 세부를 다루지 않아도 되므로 단순해진다.",True)
Q("4-lr-4","lexer-role","mc","어휘 분석기가 하는 일이 '아닌' 것은?",
  3, choices=["주석과 공백 건너뛰기","사용자 정의 이름을 심볼 테이블에 넣기","어휘 오류 탐지","모호한 문법 검출"])
Q("4-sd-4","state-diagram","mc","상태 다이어그램에서 'LETTER', 'DIGIT' 클래스를 쓰는 목적은?",
  1, choices=["예약어 구분","같은 전이를 하는 문자들을 묶어 다이어그램을 단순화","토큰 코드 결정","오류 복구"])
Q("4-ut-4","lexer-utils","mc","front.c의 lex()에서 공백이 아닌 문자가 나올 때까지 getChar를 반복 호출하는 함수는?",
  2, choices=["addChar","lookup","getNonBlank","getChar"])
Q("4-ft-4","front-trace","mc","front.c로 `(sum + 47)` 을 분석할 때, sum 다음의 공백을 지나 '+' 를 읽는 것은 언제인가?",
  1, choices=["sum을 인식하는 while 안에서","다음 lex() 호출의 getNonBlank()에서","lookup에서","addChar에서"])

# ───────── U5 additions ─────────
Q("5-tb-6","topdown-bottomup","ox","상향식 파서는 파스 트리를 잎에서 루트 방향으로 만들며, 최우단 유도를 역순으로 따른다.",True)
Q("5-rds-4","rd-structure","mc","재귀 하강 파서에서 부프로그램은 무엇마다 하나씩 만드는가?",
  1, choices=["단말 기호","비단말 기호","토큰 코드","파싱 테이블 행"])
Q("5-rdt-5","rd-trace","mc","`x * (y - 2)` 를 재귀 하강 파서로 파싱할 때, 출력에 'Enter <expr>' 는 몇 번 나오는가?",
  1, choices=["1번","2번","3번","4번"], explain="처음 expr 1번 + 괄호 안에서 factor가 expr을 재귀 호출 1번 = 2번.")
Q("5-ll-4","ll-parsing","mc","LL(1)의 괄호 안 숫자 1의 의미는?",
  2, choices=["한 번만 파싱","규칙이 1개","lookahead(미리 보는) 토큰이 1개","스택 깊이 1"])
Q("5-lrc-6","left-recursion","mc","A → Ab | c 에서 좌순환을 제거한 결과는?",
  0, choices=["A → cA',  A' → bA' | ε","A → bA | c","A → cA,  A → b","A → A'b,  A' → c"])
Q("5-pd-9","pairwise","mc","다음 중 집합쌍 공통 테스트를 '통과'하는 규칙은? (B → bB | c)",
  3, choices=["A → aB | aC","A → Bc | bA","A → cA | Bd","A → aB | dA | Bb"], explain="① a,a 겹침 ② FIRST(Bc)={b,c}와 b 겹침 ③ FIRST(Bd)={b,c}와 c 겹침 ④ {a}, {d}, {b,c} 서로소.")
Q("5-pd-10","pairwise","mc","A → bC | Dc, D → aD | b 에서 FIRST(Dc)와 판정은?",
  1, choices=["{c}, 통과","{a, b}, 실패 (b 공통)","{a}, 통과","{a, b, c}, 실패"])
Q("5-lf-4","left-factoring","mc","A → xyB | xyC 를 좌추출한 결과는?",
  0, choices=["A → xyA',  A' → B | C","A → xA',  A' → yB | yC 만 가능","A → B | C","A → xyBC"], explain="공통 접두부 xy 전체를 뽑는 게 일반형. (x만 뽑으면 A' 에서 다시 공통 y가 남음)")

# ───────── U6 additions ─────────
Q("6-bp-3","bu-problem","mc","상향식 파서가 우문장 형태에서 찾아 LHS로 환원해야 하는 부분 문자열을 무엇이라 하는가?",
  0, choices=["핸들","어구","토큰","FIRST"])
Q("6-bp-4","bu-problem","ox","상향식 파서는 최좌단 유도를 처음부터 순서대로 재현한다.",False, explain="최우단 유도를 역순으로 재현한다.")
Q("6-sr-3","shift-reduce","mc","입력 `id + id` 에서 첫 id를 스택에 옮기는 행동은?",0,choices=["shift","reduce","accept","goto"])
Q("6-sr-4","shift-reduce","ox","reduce 행동은 입력 문자열을 하나 소비한다.",False, explain="reduce는 스택만 바꾸고 입력은 그대로.")
Q("6-ls-4","lr-structure","mc","GOTO 테이블은 언제 참조하는가?",2,choices=["shift 직후","파싱 시작 시","reduce 직후 LHS를 push한 다음","accept 시"])
Q("6-tb-4","lr-table","mc","교안 LR 테이블에서 ACTION[9, *]와 ACTION[9, +]는?",
  1, choices=["둘 다 R1","S7 / R1","R1 / S6","S7 / S6"], explain="상태 9 = E+T 를 본 상태. *가 오면 T*F를 위해 shift, +가 오면 E+T를 먼저 환원.")

# lr-actions: "reduce 후 스택은?" generated from traces
k=0
for s in ["id * id + id","( id + id ) * id","id + id * id"]:
    rows=lr.run(s)
    for j,(st,inp,act) in enumerate(rows):
        if not act.startswith("Reduce 3") and not act.startswith("Reduce 1") and not act.startswith("Reduce 5"): continue
        k+=1
        nxt=rows[j+1][0]
        cand=[nxt]
        rule=act.split(" (")[0]
        # distractors: forget goto, wrong goto, pop too few
        lhs=act.split("(")[1][0]
        base=nxt[:-len(nxt.rstrip("0123456789"))] if False else nxt
        import re
        m=re.match(r'^(.*?)([A-Z])(\d+)$', nxt)
        pre,L_,g=m.group(1),m.group(2),m.group(3)
        wrongs=[pre+L_, pre+L_+str({'1':'8','2':'9','9':'2','8':'1','10':'3','3':'10'}.get(g,'5')), st[:len(st)//2]+L_+g]
        ch=[nxt]+[w for w in dict.fromkeys(wrongs) if w!=nxt][:3]
        while len(ch)<4: ch.append(pre+L_+"0")
        rnd.shuffle(ch)
        Q(f"6-la-g{k}","lr-actions","mc",f"LR 파싱(교안 테이블) 중\n스택: {st}\n입력: {inp}\n행동: {rule}\n이 행동을 수행한 뒤의 스택은?",
          ch.index(nxt), choices=ch, explain=f"{act}. RHS 기호 3개(상태 포함 6칸)를 pop하고 LHS와 GOTO 상태를 push.")
        if k>=4: break
    if k>=4: break

# ───────── U7 additions ─────────
Q("7-nm-4","names","mc","COBOL이 이름 짓기가 어렵다는 비판을 받는 이유는?",
  2, choices=["대소문자를 구분해서","이름 길이가 1자로 제한돼서","예약어가 300개 정도로 너무 많아서","특수 문자가 필요해서"])
Q("7-va-6","var-attrs","mc","재귀 함수의 지역 변수처럼 '같은 이름이 실행 중 다른 시점에 다른 주소'를 가질 수 있는 속성은?",
  1, choices=["이름","주소","타입","영역"])
Q("7-sdb-3","static-dynamic-binding","mc","C 변수의 타입 바인딩은 어떤 종류인가?",0,choices=["정적 바인딩 (컴파일 시간)","동적 바인딩","적재 시간 동적 바인딩","실행 시간 바인딩"])
Q("7-sdb-4","static-dynamic-binding","mc","Python 변수의 타입 바인딩은?",1,choices=["정적 바인딩","동적 바인딩","언어 설계 시간 바인딩","명시적 선언"])
Q("7-st-3","scope-terms","mc","함수 안에서 사용되지만 그 함수 밖에서 선언된, 가시적인 변수는?",
  2, choices=["지역 변수","정적 변수","비지역 변수","이름 상수"])
Q("7-st-4","scope-terms","blank","변수가 참조될 수 있는 문장들의 범위를 그 변수의 (a) 이라 하고, 그 범위 안에서 변수는 (b) 하다고 한다.",
  ["영역","가시적"], accept=[["영역","scope","유효범위","범위"],["가시적","visible","보인다","가시"]])
Q("7-ss-6","static-scope","mc","정적 영역 언어에서 sub2가 sub1 안에 중첩되어 있고 둘 다 x를 선언하지 않았으며 main에 x가 있다. sub3(최상위)이 sub2를 호출할 수 있다고 할 때, sub2의 x는?",
  0, choices=["main의 x (정적 조상)","sub3의 x","호출 순서에 따라 다름","오류"])
Q("7-gs-4","global-scope","ox","C에서 `extern int sum;` 은 sum을 위한 기억장소를 할당한다.",False, explain="extern은 선언(속성만), 기억장소 할당은 정의에서.")
Q("7-sl-3","scope-vs-lifetime","mc","C 함수 안의 `static int count;` 에 대해 옳은 것은?",
  1, choices=["영역 = 프로그램 전체, 생존 기간 = 함수 실행 중","영역 = 함수 안, 생존 기간 = 프로그램 실행 전체","영역과 생존 기간 모두 함수 실행 중","영역과 생존 기간 모두 프로그램 전체"])
Q("7-sl-4","scope-vs-lifetime","ox","compute()가 지역 변수 sum을 가진 채 printheader()를 호출하면, printheader 실행 중 sum은 영역 밖이지만 여전히 살아 있다.",True)
Q("7-re-3","ref-env","mc","동적 영역 언어에서 어떤 문장의 참조 환경은?",
  2, choices=["지역 변수만","지역 변수 + 정적 조상의 변수","지역 변수 + 현재 활성화된 모든 부프로그램의 가시 변수","전역 변수만"])
Q("7-re-4","ref-env","ox","정적 영역 언어에서 참조 환경은 지역 변수와 모든 정적 조상에서 선언된 가시 변수로 이루어진다.",True)

# dynamic / static scope MCs on a shared program
DYN = """// main
var a, b, c;
function sub1() { var b, d; ... }
function sub2() { var c, d, e; ... }
function sub3() { var a, e, f; ... }"""
decl={"main":["a","b","c"],"sub1":["b","d"],"sub2":["c","d","e"],"sub3":["a","e","f"]}
def owner(chain, v):
    for fn in reversed(chain):
        if v in decl[fn]: return fn
for i,(chain,v) in enumerate([(["main","sub2","sub1"],"c"),(["main","sub3","sub2"],"a"),(["main","sub1","sub3"],"d"),(["main","sub2","sub3","sub1"],"e")]):
    ans=owner(chain,v); ch=["main","sub1","sub2","sub3"]
    Q(f"7-ds-g{i+1}","dynamic-scope","mc",f"아래 프로그램(동적 영역)에서 호출 순서가 {' → '.join(chain)} 일 때, 마지막 함수({chain[-1]}) 실행 중 변수 {v}는 어느 함수에 선언된 것인가?",
      ch.index(ans), choices=ch, code=DYN, explain=f"{chain[-1]}부터 호출 체인을 거꾸로 따라가며 {v}를 처음 선언한 함수 = {ans}")
BLK = """1  void h(void) {
2      int p, q;              /* 정의 1 */
3      while (...) {
4          int q, r;          /* 정의 2 */
5          for (...) {
6              int p, s;      /* 정의 3 */
7              ...  <-------- (A)
8          }
9          ...  <------------ (B)
10     }
11     ...  <---------------- (C)
12 }"""
Q("7-bl-7","blocks","mc","다음 C 함수의 지점 (A)에서 가시적인 변수와 정의 번호로 옳은 것은?",
  2, choices=["p(1), q(1), r(2), s(3)","p(3), q(1), r(2), s(3)","p(3), s(3), q(2), r(2)","p(3), s(3)"], code=BLK)
Q("7-bl-8","blocks","mc","같은 함수의 지점 (B)에서 가시적인 변수는?",
  0, choices=["p(1), q(2), r(2)","p(3), q(2), r(2), s(3)","p(1), q(1)","q(2), r(2)"], code=BLK)
Q("7-bl-9","blocks","mc","같은 함수의 지점 (C)에서 가시적인 변수는?",
  3, choices=["p(1), q(2), r(2)","p(3), q(1)","모든 변수","p(1), q(1)"], code=BLK)
