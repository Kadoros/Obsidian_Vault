@unit U2 | Ch.3 구문 기술 (BNF · 파스 트리 · 모호성) | L03 Describing Syntax and Semantics.pdf (p.1–30)
@intro 시험에서 손으로 그려야 하는 파트. 최좌단 유도, 파스 트리, 모호성 증명은 "읽기"보다 "직접 써보기"로 익혀. 퀴즈에서 실제로 유도를 쓰게 할 거야.

@lesson L2-1 | 구문 vs 의미론 · 기본 용어 | L03 p.3–8

## 구문과 의미론 {#syn-sem}

- **구문** (syntax): 식(expression), 문장(statement), 프로그램 단위(program unit)의 **형식 또는 구조**.
- **의미론** (semantics): 그 식·문장·프로그램 단위의 **의미**.

예) Java `while (bool_expr) statement`
- 구문: 위와 같은 형태로 써야 한다.
- 의미: bool_expr의 현재 값이 참이면 내포된 문장을 실행하고, 거짓이면 while 다음 문장으로 제어가 넘어간다.

언어 정의(구문+의미)를 쓰는 사람: **다른 언어 설계자**(모호성·비일관성 발견), **구현자**(올바른 구현), **프로그래머**(올바르게 사용).

> 시험 포인트: 24 중간 4번 "구문과 의미론을 간략히". 형식/구조 vs 의미, 그리고 while 예 하나면 충분.

## 문장 · 언어 · 어휘항목 · 토큰 {#lexeme-token}

- **문장** (sentence): 어떤 알파벳(Σ) 위의 문자열
- **언어** (language): 문장들의 집합
- **어휘항목** (lexeme): 언어의 **가장 낮은 수준의 구문 단위**. 예) `*`, `sum`, `begin`
- **토큰** (token): **어휘항목들의 범주(category)**. 예) identifier

`index = 2 * count + 17;` 를 쪼개면:

| 어휘항목 (lexeme) | 토큰 (token) |
|---|---|
| index | identifier |
| = | equal_sign |
| 2 | int_literal |
| * | mult_op |
| count | identifier |
| + | plus_op |
| 17 | int_literal |
| ; | semicolon |

> 시험 포인트: 24 중간 6번. "어휘항목 = 가장 낮은 수준의 구문 단위(실제 문자열), 토큰 = 어휘항목의 범주(종류)". `index`와 `count`는 다른 lexeme인데 같은 token.

## 인식기와 생성기 {#recognizer-generator}

언어를 형식적으로 정의하는 두 방법:

- **언어 인식기** (recognizer): 입력 문자열을 읽고 그 언어에 속하는지 판단하는 장치. 예) 컴파일러의 **구문 분석기** (Ch.4).
- **언어 생성기** (generator): 언어의 문장을 생성하는 장치. 어떤 문장이 구문적으로 맞는지를 생성기의 구조와 비교해 판단. (BNF 문법이 생성기 역할)

@lesson L2-2 | BNF와 유도 | L03 p.8–15

## BNF와 문맥 자유 문법 {#bnf}

- **문맥 자유 문법 (CFG)**: Noam Chomsky, 1950년대 중반. 자연어 구문 기술용 언어 생성기. 문맥 자유 언어 클래스를 정의.
- **BNF** (Backus-Naur Form): John Backus, 1959, ALGOL 58 기술용. **BNF는 CFG와 동등**하다.
- **메타언어** (metalanguage): 다른 언어를 기술하는 언어. BNF는 프로그래밍 언어를 위한 메타언어.

BNF 구성 요소:
- **추상화 = 비단말 기호** (nonterminal): 구문 구조의 클래스, `<assign>`처럼 꺾쇠로 감쌈
- **단말 기호** (terminal): 어휘항목 또는 토큰
- **규칙 / 생성 규칙** (rule, production): `LHS → RHS`. LHS는 비단말 하나, RHS는 단말·비단말 문자열
- 한 비단말이 여러 RHS를 가지면 `|`로 묶음
- **문법** (grammar): 규칙들의 유한·비어있지 않은 집합
- **시작 기호** (start symbol): 유도를 시작하는 특별한 비단말

```
<if_stmt> → if (<logic_expr>) <stmt>
          | if (<logic_expr>) <stmt> else <stmt>
```

**리스트는 재귀로** 표현: LHS가 RHS에 다시 나오면 재귀 규칙.
```
<ident_list> → ident
             | ident , <ident_list>
```

## 유도 · 문장 형태 · 최좌단 유도 {#derivation}

- **유도** (derivation): 시작 기호에서 출발해 규칙을 반복 적용, 단말로만 된 문장에서 끝남.
- **문장 형태** (sentential form): 유도 중에 나오는 모든 기호열.
- **문장** (sentence): 단말 기호만 있는 문장 형태.
- **최좌단 유도** (leftmost derivation): 매 단계에서 **가장 왼쪽 비단말**을 전개.
- 유도 순서(최좌단/최우단/그 외)는 **생성되는 언어에 영향 없음**.

예제 문법:
```
<program> → begin <stmts> end
<stmts>   → <stmt> | <stmt> ; <stmts>
<stmt>    → <var> = <expr>
<var>     → a | b | c | d
<expr>    → <var> + <var> | <var> - <var> | <var>
```
`begin a = b + c; b = c end` 의 최좌단 유도:
```
<program> ⇒ begin <stmts> end
          ⇒ begin <stmt> ; <stmts> end
          ⇒ begin <var> = <expr> ; <stmts> end
          ⇒ begin a = <expr> ; <stmts> end
          ⇒ begin a = <var> + <var> ; <stmts> end
          ⇒ begin a = b + <var> ; <stmts> end
          ⇒ begin a = b + c ; <stmts> end
          ⇒ begin a = b + c ; <stmt> end
          ⇒ begin a = b + c ; <var> = <expr> end
          ⇒ begin a = b + c ; b = <expr> end
          ⇒ begin a = b + c ; b = <var> end
          ⇒ begin a = b + c ; b = c end
```

> 쓰는 요령: 매 줄마다 "지금 가장 왼쪽 비단말이 뭐지?"만 보고 그거 하나만 바꿔. 두 개 동시에 바꾸면 감점.

@lesson L2-3 | 파스 트리 · 모호성 | L03 p.16–22

## 파스 트리 {#parse-tree}

**파스 트리**: 문장이 시작 기호에서 어떻게 유도되는지를 계층 구조(트리)로 보여줌.
- 내부 노드 = 비단말, 잎 = 단말, 루트 = 시작 기호
- 노드의 자식들 = 그 노드에 적용한 규칙의 RHS (왼→오 순서)

문법 (교안 p.17):
```
<assign> → <id> = <expr>
<id>     → A | B | C
<expr>   → <id> + <expr> | <id> * <expr> | ( <expr> ) | <id>
```
`A = B * (A + C)` 의 파스 트리:
```
            <assign>
         /     |      \
      <id>     =      <expr>
       |            /   |    \
       A         <id>   *    <expr>
                  |        /   |   \
                  B       (  <expr>  )
                           /   |   \
                        <id>   +   <expr>
                         |           |
                         A         <id>
                                     |
                                     C
```

## 모호성 (Ambiguity) {#ambiguity}

**문법이 모호하다 ⟺ 어떤 문장 형태에 대해 서로 다른 파스 트리가 2개 이상 존재.**
동치 조건: 어떤 문장에 대해 **최좌단 유도가 2개 이상** (또는 최우단 유도가 2개 이상).

모호한 문법:
```
<assign> → <id> = <expr>
<id>     → A | B | C
<expr>   → <expr> + <expr> | <expr> * <expr> | ( <expr> ) | <id>
```
`A = B + C * A` 에 대해 두 트리가 생긴다:
```
(1) + 가 위:  <expr> ⇒ <expr> + <expr>, 오른쪽 <expr> ⇒ <expr> * <expr>    → B + (C * A)
(2) * 가 위:  <expr> ⇒ <expr> * <expr>, 왼쪽  <expr> ⇒ <expr> + <expr>    → (B + C) * A
```

**모호성 증명하는 법 (시험 답안 형식)**:
1. 문장 하나를 고른다 (짧을수록 좋음).
2. 그 문장에 대한 **서로 다른 최좌단 유도 2개** (또는 파스 트리 2개)를 쓴다.
3. "같은 문장에 대해 서로 다른 파스 트리가 2개 존재하므로 모호하다"로 마무리.

예) `<S> → <A>`, `<A> → <A> + <A> | <id>`, `<id> → a | b | c` 에서 `a + b + c`:
```
유도 1: <S> ⇒ <A> ⇒ <A> + <A> ⇒ <A> + <A> + <A> ⇒ <id> + <A> + <A>
        ⇒ a + <A> + <A> ⇒ a + <id> + <A> ⇒ a + b + <A> ⇒ a + b + <id> ⇒ a + b + c
        (첫 <A> + <A> 중 "왼쪽" <A>를 다시 <A> + <A>로 전개 → (a+b)+c)
유도 2: <S> ⇒ <A> ⇒ <A> + <A> ⇒ <id> + <A> ⇒ a + <A> ⇒ a + <A> + <A>
        ⇒ a + <id> + <A> ⇒ a + b + <A> ⇒ a + b + <id> ⇒ a + b + c
        (오른쪽 <A>를 전개 → a+(b+c))
```

> 시험 포인트: 24 중간 8번이 이 유형(3점). "두 개의 서로 다른 최좌단 유도 또는 파스 트리"를 반드시 보여야 함. 말로만 "두 가지로 해석된다"는 감점.

@lesson L2-4 | 우선순위 · 결합성 · if-else 모호성 | L03 p.23–27

## 연산자 우선순위를 문법으로 {#precedence}

연산자마다 **별도의 비단말**을 두면 모호성이 사라진다.
규칙: **우선순위가 높은 연산자일수록 파스 트리에서 더 낮은 곳(잎 쪽)** 에 나타나야 한다.

모호하지 않은 식 문법 (**시험에 자주 주어지는 문법**):
```
<assign> → <id> = <expr>
<id>     → A | B | C
<expr>   → <expr> + <term>   | <term>
<term>   → <term> * <factor> | <factor>
<factor> → ( <expr> )        | <id>
```
`*`는 `<term>` 단계, `+`는 `<expr>` 단계 → `*`가 항상 아래 → 먼저 계산.

`A = B + C * A` 의 최좌단 유도 (L04 p.37에도 나옴):
```
<assign> ⇒ <id> = <expr>
         ⇒ A = <expr>
         ⇒ A = <expr> + <term>
         ⇒ A = <term> + <term>
         ⇒ A = <factor> + <term>
         ⇒ A = <id> + <term>
         ⇒ A = B + <term>
         ⇒ A = B + <term> * <factor>
         ⇒ A = B + <factor> * <factor>
         ⇒ A = B + <id> * <factor>
         ⇒ A = B + C * <factor>
         ⇒ A = B + C * <id>
         ⇒ A = B + C * A
```
파스 트리:
```
          <assign>
        /    |     \
     <id>    =     <expr>
      |          /   |    \
      A      <expr>  +    <term>
               |         /  |   \
            <term>   <term> *  <factor>
               |        |         |
           <factor>  <factor>   <id>
               |        |         |
             <id>     <id>        A
               |        |
               B        C
```

> 괄호가 있으면 `<factor> → ( <expr> )`를 써서 다시 `<expr>`로 올라간다. 24 중간 10번이 이 문법으로 괄호 있는 문장 2개를 유도하는 문제였어.

## 결합성 (Associativity) {#associativity}

같은 우선순위 연산자가 연속될 때 어느 쪽부터 묶을지도 문법으로 표현한다.

```
<expr> → <expr> + <expr> | const    (모호)
<expr> → <expr> + const  | const    (모호하지 않음)
```
- **좌순환** 규칙 (LHS가 RHS의 **맨 왼쪽**에 나옴) → **좌결합**. `const + const + const` = `(const + const) + const`.
- **우순환** 규칙 (LHS가 RHS의 맨 오른쪽) → **우결합**. 예) 거듭제곱 `<factor> → <exp> ** <factor> | <exp>`.

> 함정: 좌순환 = 좌결합에 좋지만, Ch.4에서 배우는 **하향식 파서는 좌순환을 못 다룬다**. 이 연결고리가 시험에 나오기 좋다.

## if-then-else 모호성 (dangling else) {#dangling-else}

```
<if_stmt> → if (<logic_expr>) then <stmt>
          | if (<logic_expr>) then <stmt> else <stmt>
```
`if C1 then if C2 then S1 else S2` 에서 `else`가 바깥 if에 붙는지 안쪽 if에 붙는지 두 트리가 생김 → **모호**.

대부분의 언어 규칙: **else는 가장 가까운 짝 없는 then과 짝지어진다.**
모호하지 않은 문법:
```
<stmt>      → <matched> | <unmatched>
<matched>   → if (<logic_expr>) then <matched> else <matched>
            | a non-if statement
<unmatched> → if (<logic_expr>) then <stmt>
            | if (<logic_expr>) then <matched> else <unmatched>
```
핵심 아이디어: then과 else 사이에는 **matched**(else까지 짝이 다 맞은) 문장만 올 수 있다.

@lesson L2-5 | EBNF | L03 p.28–30

## EBNF 확장 3가지 {#ebnf}

BNF를 짧게 쓰기 위한 확장. 표현력은 BNF와 같다.

| 표기 | 의미 | 예 |
|---|---|---|
| `[ ]` | 선택(0 또는 1번) | `<if_stmt> → if (<expr>) <stmt> [else <stmt>]` |
| `{ }` | 0번 이상 반복 | `<ident> → letter {letter | digit}` |
| `( | )` | 여러 대안 중 하나 | `<term> → <term> (+ | -) const` |

BNF → EBNF 변환:
```
BNF:  <expr> → <expr> + <term> | <expr> - <term> | <term>
      <term> → <term> * <factor> | <term> / <factor> | <factor>
EBNF: <expr> → <term> {(+ | -) <term>}
      <term> → <factor> {(* | /) <factor>}
```
변환 요령: `A → A α | β` 꼴(좌순환)은 `A → β {α}` 로 바꾼다.

> 주의: EBNF로 바꾸면 좌순환이 `{}` 반복으로 사라지므로 결합성 정보가 문법에서 안 보인다 → 파서(구현)가 좌결합을 맞춰줘야 한다. 그리고 비단말 수가 줄어서 **재귀 하강 파서의 기반으로 딱 좋다** (Ch.4).

## 최근의 EBNF 변형 {#ebnf-variants}

- RHS 대안들을 각각 다른 줄에 씀, `→` 대신 `:` 사용
- 선택 부분에 아래첨자 `opt`: `ConstructorDeclarator → SimpleName (FormalParameterList_opt)`
- 선택지에 `one of`: `AssignmentOperator → one of = *= /= %= += -= ...`
