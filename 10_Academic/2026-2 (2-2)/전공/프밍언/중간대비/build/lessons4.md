@unit U4 | Ch.4 어휘 분석 | L04 Lexical and Syntax Analysis.pdf (p.1–31) · 04_code.pptx
@intro 어휘 분석기 = 패턴 매처. front.c가 (sum + 47) / total을 어떻게 토큰으로 자르는지 손으로 따라갈 수 있으면 끝.

@lesson L4-1 | 구문 분석의 두 부분 · 분리하는 이유 | L04 p.3–7

## BNF 기반 구문 분석 {#sa-bnf}

언어 구현 시스템은 구현 방식(컴파일/해석/혼합)과 상관없이 **원시 코드를 분석**해야 하고, 거의 모든 구문 분석은 **BNF**에 기반한다.

BNF로 구문을 기술하는 장점:
- 명확하고 간결한 구문 기술
- 파서를 BNF에 **직접** 기반해서 만들 수 있음
- BNF 기반 파서는 유지보수가 쉬움 (모듈성)

## 어휘 분석기 vs 구문 분석기 {#lex-vs-parser}

구문 분석 부분은 거의 항상 두 부분으로 나뉜다:

| 부분 | 역할 | 수학적 모델 |
|---|---|---|
| **어휘 분석기** (lexical analyzer) | 저수준: 문자 → 어휘항목/토큰 | **유한 오토마타** (정규 문법 기반) |
| **구문 분석기 = 파서** (syntax analyzer, parser) | 고수준: 토큰 → 파스 트리 | **푸시다운 오토마타** (CFG/BNF 기반) |

> 짝 외우기: 어휘 = 정규 문법 = 유한 오토마타 / 구문 = 문맥 자유 문법 = 푸시다운 오토마타.

## 어휘 분석과 구문 분석을 분리하는 이유 {#separate-why}

1. **단순성** (Simplicity): 어휘 분석엔 덜 복잡한 기법으로 충분. 분리하면 파서가 단순해진다(공백·주석 같은 세부를 파서가 신경 안 씀).
2. **효율성** (Efficiency): 어휘 분석이 컴파일 시간의 큰 부분이라, 분리하면 어휘 분석기만 따로 **최적화**할 수 있다.
3. **이식성** (Portability): 어휘 분석기는 입력 파일·버퍼링 등을 다뤄서 플랫폼 의존적일 수 있지만, **파서는 항상 이식 가능**.

> 시험 대비: "분리 이유 3가지" = 단순성·효율성·이식성. 각 한 줄.

@lesson L4-2 | 어휘 분석기 · 상태 다이어그램 | L04 p.8–16

## 어휘 분석기의 역할 {#lexer-role}

- 문자열에 대한 **패턴 매처** (pattern matcher)
- 파서의 **전단부** (front-end)
- 원시 프로그램에서 같이 묶이는 부분 문자열(**어휘항목**)을 찾아내고, 그 어휘항목이 매칭된 패턴의 범주(**토큰**)를 정한다. 예) `sum`은 lexeme, 토큰은 `IDENT`.
- 보통 **파서가 다음 토큰이 필요할 때 호출하는 함수**로 구현된다.
- 부가 역할: 주석·공백 건너뛰기, 사용자 정의 이름을 심볼 테이블에 넣기, 어휘 오류 탐지.

`result = oldsum - value / 100;` →

| 토큰 | 어휘항목 |
|---|---|
| IDENT | result |
| ASSIGN_OP | = |
| IDENT | oldsum |
| SUB_OP | - |
| IDENT | value |
| DIV_OP | / |
| INT_LIT | 100 |
| SEMICOLON | ; |

## 어휘 분석기를 만드는 3가지 방법 {#lexer-build}

1. 토큰을 **형식적으로 기술**(정규식)하고, 이 기술로부터 **표 기반** 어휘 분석기를 만들어주는 **SW 도구**를 사용 (예: lex)
2. 토큰을 기술하는 **상태 다이어그램**을 설계하고, 그 다이어그램을 **구현하는 프로그램**을 작성
3. 상태 다이어그램을 설계하고, 그것의 **표 기반 구현을 손으로** 작성

## 상태 다이어그램 단순화 {#state-diagram}

순진하게 그리면 모든 상태에서 모든 문자에 대한 전이가 있어야 해서 **너무 크다**. 단순화 방법:

- **문자 클래스**: 식별자 인식 중엔 대소문자 모든 글자가 동등 → `LETTER` 클래스 하나로. 정수 리터럴은 모든 숫자가 동등 → `DIGIT` 클래스.
- **예약어와 식별자를 함께 인식**: 예약어마다 다이어그램을 따로 그리지 않고, 식별자처럼 인식한 다음 **테이블 탐색(lookup)** 으로 예약어인지 판별.

## 유틸리티 부프로그램 {#lexer-utils}

| 함수 | 하는 일 |
|---|---|
| `getChar` | 입력의 다음 문자를 `nextChar`에 넣고, 그 문자의 클래스를 판단해 `charClass`에 넣음 |
| `addChar` | `nextChar`의 문자를 어휘항목을 모으는 곳(`lexeme`)에 추가 |
| `lookup` | `lexeme`(또는 문자)가 예약어/연산자인지 판단해 토큰 코드를 돌려줌 |
| `getNonBlank` | 공백이 아닌 문자가 나올 때까지 `getChar` 호출 |

> 함정: 클래스를 정하는 건 `getChar`, 문자를 이어붙이는 건 `addChar`.

@lesson L4-3 | front.c 따라가기 | L04 p.17–31 · 04_code.pptx

## front.c의 토큰 코드 {#front-codes}

```
#define LETTER 0        #define INT_LIT 10       #define ADD_OP 21
#define DIGIT 1         #define IDENT 11         #define SUB_OP 22
#define UNKNOWN 99      #define ASSIGN_OP 20     #define MULT_OP 23
                                                 #define DIV_OP 24
                                                 #define LEFT_PAREN 25
                                                 #define RIGHT_PAREN 26
EOF = -1
```

`lex()` 의 구조:
```
int lex() {
    lexLen = 0;
    getNonBlank();
    switch (charClass) {
        case LETTER:                 /* 식별자 */
            addChar(); getChar();
            while (charClass == LETTER || charClass == DIGIT) {
                addChar(); getChar();
            }
            nextToken = IDENT; break;
        case DIGIT:                  /* 정수 리터럴 */
            addChar(); getChar();
            while (charClass == DIGIT) { addChar(); getChar(); }
            nextToken = INT_LIT; break;
        case UNKNOWN:                /* 괄호와 연산자 */
            lookup(nextChar); getChar(); break;
        case EOF:
            nextToken = EOF; lexeme = "EOF"; break;
    }
    printf("Next token is: %d, Next lexeme is %s\n", nextToken, lexeme);
    return nextToken;
}
```

## (sum + 47) / total 추적 {#front-trace}

출력:
```
Next token is: 25 Next lexeme is (
Next token is: 11 Next lexeme is sum
Next token is: 21 Next lexeme is +
Next token is: 10 Next lexeme is 47
Next token is: 26 Next lexeme is )
Next token is: 24 Next lexeme is /
Next token is: 11 Next lexeme is total
Next token is: -1 Next lexeme is EOF
```

첫 두 토큰을 변수 단위로 따라가면 (04_code.pptx):
```
[처음 getChar()]  nextChar='('  isalpha F, isdigit F → charClass=UNKNOWN
[lex() #1] lexLen=0, getNonBlank()
           switch(UNKNOWN) → lookup('(') → addChar(): lexeme="(" , nextToken=LEFT_PAREN(25)
           getChar(): nextChar='s' → charClass=LETTER
           printf → "25 (", 
[lex() #2] lexLen=0, getNonBlank()
           switch(LETTER) → addChar(): lexeme="s"; getChar(): nextChar='u' LETTER
           while: addChar() "su"; getChar() 'm' LETTER
                  addChar() "sum"; getChar() ' ' → UNKNOWN → while 종료
           nextToken=IDENT(11) → printf "11 sum"
[lex() #3] getNonBlank(): ' '는 공백 → getChar() → nextChar='+' UNKNOWN
           lookup('+') → ADD_OP(21) ...
```

> 포인트: `lex()`는 항상 **다음 문자를 하나 미리 읽어 둔 상태**(nextChar)로 끝난다. 그래서 식별자 끝을 알 수 있음(공백이나 연산자가 나오면 멈춤). 예약어 판별은 front.c에선 생략됨.

@unit U5 | Ch.4 파싱 문제 · 하향식 파싱 | L04 p.32–62
@intro 하향식 = 최좌단 유도 = 재귀 하강/LL. 시험 13번(집합쌍 공통 테스트)과 7번(하향식 vs 상향식)이 여기서 나와.

@lesson L5-1 | 파싱 문제 · 하향식 vs 상향식 | L04 p.32–42

## 파서의 목표 {#parser-goals}

**파싱**: 토큰 열이 언어의 문법에 맞는지 분석하는 과정.
파서의 두 목표:
1. **모든 구문 오류를 찾는다.** 각각에 적절한 진단 메시지를 내고 빨리 **복구**한다.
2. **파스 트리**(또는 최소한 파스 트리의 흔적)를 만든다.

## 하향식 vs 상향식 {#topdown-bottomup}

| | 하향식 (Top-down) | 상향식 (Bottom-up) |
|---|---|---|
| 트리 생성 | **루트**부터 잎 방향으로 | **잎**부터 루트 방향으로 |
| 유도 순서 | **최좌단 유도** 순서 | **최우단 유도의 역순** |
| 순회 | 전위 순회(preorder)로 추적/생성 | |
| 결정할 것 | 문장 형태 `xAα`에서 **다음 토큰 하나만 보고** 올바른 A-규칙 선택 | 우문장 형태에서 **어떤 부분 문자열(핸들)을 LHS로 환원**할지 |
| 대표 알고리즘 | **재귀 하강**(코드 구현), **LL** 파서(표 기반) | **LR** 계열 (shift-reduce) |

> 시험 포인트: 24 중간 7번. "하향식: 루트부터, 최좌단 유도 순서, 재귀하강/LL / 상향식: 잎부터, 최우단 유도의 역순, LR(shift-reduce)" 이 정도면 만점.

표기 관례 (Ch.4 전체에서 사용):
- 단말: 알파벳 앞쪽 소문자 `a, b, …`
- 비단말: 알파벳 앞쪽 대문자 `A, B, …`
- 단말 또는 비단말: 뒤쪽 대문자 `W, X, Y, Z`
- 단말 문자열: 뒤쪽 소문자 `w, x, y, z`
- 혼합 문자열: 그리스 소문자 `α, β, γ, δ`

예) 하향식: 문장 형태 `xAα`, 규칙 `A → bB | cBb | a`. 다음 토큰이 `c`면 `A → cBb` 선택.
예) 상향식: `S → aAc`, `A → aA | b`. 입력 `aabc`에서 `b`를 A로 환원 → `aaAc` → `aA`를 A로 → `aAc` → S. 이건 `S ⇒ aAc ⇒ aaAc ⇒ aabc` (최우단 유도)를 거꾸로 한 것.

## 파싱의 복잡도 {#parse-complexity}

- **모든** 모호하지 않은 문법에 작동하는 파서는 복잡하고 비효율적: **O(n³)**.
- 그래서 컴파일러는 모호하지 않은 문법의 **부분 집합**에서만 동작하지만 **선형 시간 O(n)** 에 끝나는 파서를 쓴다.

@lesson L5-2 | 재귀 하강 파서 | L04 p.43–55

## 재귀 하강 파서의 구조 {#rd-structure}

- 부프로그램들의 모음. 재귀적이고, **하향식** 순서로 파스 트리를 만든다.
- 재귀는 프로그래밍 언어의 **중첩 구조**를 반영한 것.
- **문법의 비단말 하나당 부프로그램 하나.** 그 부프로그램은 그 비단말이 생성할 수 있는 문장을 파싱.
- **EBNF가 재귀 하강 파서의 기반으로 이상적**: EBNF는 비단말 수를 최소화하므로.

```
<expr>   → <term> {(+ | -) <term>}
<term>   → <factor> {(* | /) <factor>}
<factor> → id | int_constant | ( <expr> )
```

## 코딩 규칙 {#rd-coding}

어휘 분석기 `lex`가 다음 토큰 코드를 `nextToken`에 넣는다고 가정.

RHS가 하나일 때:
- RHS의 **단말**: 다음 입력 토큰과 비교 → 같으면 계속(lex 호출), 다르면 오류
- RHS의 **비단말**: 그 비단말의 파싱 부프로그램을 호출

```
void expr() {
    printf("Enter <expr>\n");
    term();
    while (nextToken == ADD_OP || nextToken == SUB_OP) {
        lex();
        term();
    }
    printf("Exit <expr>\n");
}
```
**관례**: 모든 파싱 루틴은 끝날 때 **다음 토큰을 nextToken에 남겨둔다.**

RHS가 여러 개인 비단말(예: `<factor>`): 다음 토큰(**lookahead**)을 각 RHS가 생성할 수 있는 **첫 토큰**과 비교해서 고른다. 맞는 게 없으면 구문 오류.
```
void factor() {
    printf("Enter <factor>\n");
    if (nextToken == IDENT || nextToken == INT_LIT)
        lex();
    else if (nextToken == LEFT_PAREN) {
        lex();
        expr();
        if (nextToken == RIGHT_PAREN) lex();
        else error();
    }
    else error();
    printf("Exit <factor>\n");
}
```

## (sum + 47) / total 추적 {#rd-trace}

```
Next token is: 25 Next lexeme is (
Enter <expr>
Enter <term>
Enter <factor>
Next token is: 11 Next lexeme is sum
Enter <expr>
Enter <term>
Enter <factor>
Next token is: 21 Next lexeme is +
Exit <factor>
Exit <term>
Next token is: 10 Next lexeme is 47
Enter <term>
Enter <factor>
Next token is: 26 Next lexeme is )
Exit <factor>
Exit <term>
Exit <expr>
Next token is: 24 Next lexeme is /
Exit <factor>
Next token is: 11 Next lexeme is total
Enter <factor>
Next token is: -1 Next lexeme is EOF
Exit <factor>
Exit <term>
Exit <expr>
```
읽는 법: `(`를 본 factor가 `lex()` 후 `expr()`을 재귀 호출 → 괄호 안을 다 파싱 → `)` 확인 후 `lex()` → `/`가 남아 있으니 term의 while이 한 번 더 돌아 factor 호출(total).

> 재귀 하강 파서는 **LL 파서**의 한 종류다 (Summary).

@lesson L5-3 | LL 문법: 좌순환 · 집합쌍 공통 · 좌추출 | L04 p.56–62

## LL 파싱 {#ll-parsing}

- **L**eft-to-right 스캔 + **L**eftmost derivation. lookahead 토큰으로 생성 규칙 선택.
- **LL 문법**: 왼→오로 읽으며 최좌단 유도를 구성하는 방식으로 파싱 가능한 CFG.
- LL(1) 파싱 테이블 예:
```
S → aAB     A → bA | ε     B → c

         a          b         c
S    S → aAB      error     error
A    error        A → bA    A → ε
B    error        error     B → c
```

하향식 파싱을 막는 문법의 두 가지 특성: **① 좌순환 ② 집합쌍 공통 테스트 실패**

## 좌순환 문제와 제거 {#left-recursion}

**좌순환이 있으면(직접이든 간접이든) 하향식 파서의 기반이 될 수 없다.**
이유: `A → A + B` 에서 A()가 아무 토큰도 소비하지 않고 바로 A()를 또 호출 → 무한 재귀.

**직접 좌순환 제거**:
```
A → Aα1 | … | Aαm | β1 | β2 | … | βn     (β들은 A로 시작하지 않음)
⇓
A  → β1A' | β2A' | … | βnA'
A' → α1A' | α2A' | … | αmA' | ε
```
예)
```
E → E + T | T            ⇒   E  → T E'
                             E' → + T E' | ε
T → T * F | F            ⇒   T  → F T'
                             T' → * F T' | ε
F → (E) | id             ⇒   그대로
```
요령: **좌순환 대안의 꼬리(α)는 A'로, 좌순환이 아닌 대안(β)은 뒤에 A'를 붙여서 A로.**

## 집합쌍 공통 테스트 (Pairwise Disjointness Test) {#pairwise}

하향식 파싱을 막는 다른 특성 = 다음 토큰 하나로 올바른 RHS를 고를 수 없는 것.

**FIRST(α) = { a | α ⇒* aβ }** : α에서 유도되는 문자열의 첫 단말들의 집합. (α ⇒* ε 이면 ε도 포함)

**테스트**: 둘 이상의 RHS를 가진 각 비단말 A에 대해, 모든 규칙 쌍 `A → αi`, `A → αj` 에 대해
**FIRST(αi) ∩ FIRST(αj) = ∅** 이어야 통과.

예)
```
A → a | bB | cAb
  FIRST(a) = {a}, FIRST(bB) = {b}, FIRST(cAb) = {c}  → 모두 서로소 → 통과
A → a | aB
  FIRST(a) = {a}, FIRST(aB) = {a}  → 공통 a → 실패
```
RHS가 **비단말로 시작**하면 그 비단말의 FIRST를 구해서 넣어야 한다:
```
A → aB | Bb ,  B → aC | d
  FIRST(aB) = {a},  FIRST(Bb) = FIRST(B) = {a, d}  → 공통 a → 실패
```

> 시험 포인트: 24 중간 13번(5점). 답안 형식 = **각 RHS의 FIRST 집합을 모두 쓰고 → 교집합 → 통과/실패 판정**. 결론만 쓰면 감점.

## 좌추출 (Left factoring) {#left-factoring}

집합쌍 공통 테스트 실패를 해결할 수 있는 경우가 있다: 공통 접두부를 뽑아낸다.
```
<variable> → identifier | identifier [<expression>]
⇓
<variable> → identifier <new>
<new>      → ε | [<expression>]
또는 (EBNF)
<variable> → identifier [[<expression>]]     (바깥 [ ]는 EBNF 메타기호)
```
일반형: `A → αβ1 | αβ2` ⇒ `A → αA'`, `A' → β1 | β2`
