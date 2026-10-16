from qdsl import Q
import gram, lr

def pdt_answer(g):
    G=gram.parse(g); F=gram.first(G); lines=[]; verdicts=[]
    import itertools
    for n,alts in G.items():
        if len(alts)<2: continue
        sets=[(a,gram.fs(G,F,a)) for a in alts]
        bad=[(x[0],y[0],x[1]&y[1]) for x,y in itertools.combinations(sets,2) if x[1]&y[1]]
        fmt=lambda s: "{"+", ".join(sorted(s))+"}"
        lines.append(f"{n}: " + ", ".join(f"FIRST({a}) = {fmt(s)}" for a,s in sets))
        if bad:
            lines.append("   → " + "; ".join(f"FIRST({a}) ∩ FIRST({b}) = {fmt(c)}" for a,b,c in bad) + " → 실패")
        else:
            lines.append("   → 모든 쌍의 교집합이 공집합 → 통과")
    return "\n".join(lines)

PD = [
 ("A -> aB | bAb | Bb ; B -> cB | d", "a. A → aB | bAb | Bb   (B → cB | d)"),
 ("B -> bA | cB | Ac ; A -> aB | b", "b. B → bA | cB | Ac   (A → aB | b)"),
 ("S -> aSb | bAA ; A -> b | cA", "c. S → aSb | bAA   (A → b | cA)"),
 ("S -> Ab | Bc ; A -> aA | d ; B -> bB | a", "d. S → Ab | Bc   (A → aA | d, B → bB | a)"),
 ("X -> abY | bX | Yc ; Y -> cY | e", "e. X → abY | bX | Yc   (Y → cY | e)"),
 ("A -> aB | aAb ; B -> b", "f. A → aB | aAb   (B → b)"),
]
groups=[[0,1,2],[3,4,5],[1,3,4],[0,5,2]]
for gi,grp in enumerate(groups):
    prompt="다음 문법 규칙들에 대해 집합쌍 공통 테스트(pairwise disjointness test)를 수행하시오.\n"+"\n".join(PD[i][1] for i in grp)
    ans="\n\n".join(PD[i][1].split('.')[0]+". "+pdt_answer(PD[i][0]) for i in grp)
    Q(f"5-pd-{gi+1}","pairwise","calc",prompt,ans,
      keys=["각 RHS의 FIRST 집합 명시","비단말로 시작하는 RHS는 그 비단말의 FIRST 사용","교집합 → 통과/실패 판정"], slot=13, pts=5)
Q("5-pd-5","pairwise","mc","A → aB | bC | aD 의 집합쌍 공통 테스트 결과는?",
  1, choices=["통과","실패 (FIRST(aB) ∩ FIRST(aD) = {a})","실패 (FIRST(bC) ∩ FIRST(aD) = {b})","판단 불가"])
Q("5-pd-6","pairwise","mc","FIRST(α)의 정의는?",
  0, choices=["α로부터 유도되는 문자열의 첫 단말들의 집합 {a | α ⇒* aβ}","α의 첫 번째 기호","α 다음에 올 수 있는 단말들의 집합","α가 유도하는 모든 단말"])
Q("5-pd-7","pairwise","mc","A → Bx | y, B → yz | w 일 때 FIRST(Bx)는?",
  2, choices=["{x}","{B}","{y, w}","{y, w, x}"])
Q("5-pd-8","pairwise","ox","집합쌍 공통 테스트는 RHS가 하나뿐인 비단말에도 적용해야 한다.",False,
  explain="둘 이상의 RHS를 가진 비단말의 각 규칙 쌍에 대해서만 검사.")

Q("5-lf-1","left-factoring","calc","다음 규칙을 좌추출(left factoring)하여 집합쌍 공통 테스트를 통과하게 만드시오.\n<stmt> → if <cond> then <stmt> | if <cond> then <stmt> else <stmt>",
  "<stmt> → if <cond> then <stmt> <rest>\n<rest> → ε | else <stmt>\n(EBNF: <stmt> → if <cond> then <stmt> [else <stmt>])",
  keys=["공통 접두부 추출","새 비단말 → ε | else <stmt>"])
Q("5-lf-2","left-factoring","calc","다음 규칙을 좌추출하시오.\nA → abC | abD | e",
  "A  → abA' | e\nA' → C | D",
  keys=["공통 접두부 ab","A' → C | D","e는 그대로"])
Q("5-lf-3","left-factoring","mc","좌추출이 해결하는 문제는?",1,choices=["좌순환","집합쌍 공통 테스트 실패(공통 접두부)","모호성","결합성"])

# ───────── U6 상향식 ─────────
Q("6-bp-1","bu-problem","mc","상향식 파싱의 '파싱 문제'란?",
  2, choices=["다음 토큰 하나로 적용할 규칙 선택","좌순환 제거","우문장 형태에서 환원하면 이전 우문장 형태가 되는 RHS 부분 문자열(핸들)을 찾는 것","FIRST 집합 계산"])
Q("6-bp-2","bu-problem","calc","E → E + T | T, T → T * F | F, F → (E) | id 에서 id * id + id 의 최우단 유도를 쓰시오.",
  "E ⇒ E + T ⇒ E + F ⇒ E + id ⇒ T + id ⇒ T * F + id ⇒ T * id + id ⇒ F * id + id ⇒ id * id + id",
  keys=["매 단계 가장 오른쪽 비단말 전개","E + T가 최상위","T * F는 왼쪽 E 안에서"])

H1="S → aAb | bBA,  A → ab | aAB,  B → aB | b"
Q("6-hd-1","handle-def","short","핸들(handle), 어구(phrase), 단순 어구(simple phrase)를 정의하시오.",
  "어구: 파스 트리에서 어떤 내부 노드를 루트로 하는 부분 트리의 잎들 (S ⇒* α1Aα2 ⇒+ α1βα2 일 때 β).\n단순 어구: 한 단계 유도로 생긴 어구, 즉 자식이 모두 잎인 내부 노드의 자식들 (S ⇒* α1Aα2 ⇒ α1βα2).\n핸들: 최우단 유도에서 바로 직전에 전개된 부분 (S ⇒*rm αAw ⇒rm αβw 일 때 β). 우문장 형태의 가장 왼쪽 단순 어구.",
  keys=["어구: 부분 트리의 잎","단순 어구: 한 단계(자식이 모두 잎)","핸들 = 가장 왼쪽 단순 어구"])
Q("6-hd-2","handle-def","mc","핸들과 단순 어구의 관계로 옳은 것은?",
  0, choices=["핸들은 가장 왼쪽의 단순 어구","핸들은 가장 긴 어구","핸들은 가장 오른쪽 단순 어구","핸들은 시작 기호의 어구"])
Q("6-hd-3","handle-def","ox","상향식 파싱은 핸들 가지치기(handle pruning)로 볼 수 있다.",True)
Q("6-hd-4","handle-def","ox","우문장 형태 전체(시작 기호 노드가 덮는 문자열)도 어구에 포함된다.",True)

for i,(t,ans) in enumerate([
  ("aaAbb","파스 트리: S(a, A(a, A, B(b)), b)\n어구: aaAbb (S), aAb (A), b (B, 네 번째 기호)\n단순 어구: b\n핸들: b"),
  ("bBab","파스 트리: S(b, B, A(a, b))\n어구: bBab (S), ab (A)\n단순 어구: ab\n핸들: ab"),
  ("aaAaBb","파스 트리: S(a, A(a, A, B(a, B)), b)\n어구: aaAaBb (S), aAaB (A), aB (B)\n단순 어구: aB\n핸들: aB"),
  ("bBaAab","파스 트리: S(b, B, A(a, A, B(a, B(b))))\n어구: bBaAab (S), aAab (A), ab (B), b (B, 마지막 기호)\n단순 어구: b (마지막)\n핸들: b"),
  ("baBab","파스 트리: S(b, B(a, B), A(a, b))\n어구: baBab (S), aB (B), ab (A)\n단순 어구: aB, ab\n핸들: aB (가장 왼쪽 단순 어구)"),
]):
    Q(f"6-hh-{i+1}","handle-howto","calc",f"문법 {H1} 과 우문장 형태 {t} 가 주어졌을 때, 파스 트리를 그리고 어구, 단순 어구, 핸들을 보이시오.",
      ans, keys=["올바른 파스 트리","어구 전부(루트 포함)","단순 어구","핸들"], slot=14, pts=5)
H2="S → aBc | cA,  A → Ab | bB,  B → aB | c"
for i,(t,ans) in enumerate([
  ("cAbb","파스 트리: S(c, A(A(A, b), b))\n어구: cAbb (S), Abb (바깥 A), Ab (안쪽 A)\n단순 어구: Ab\n핸들: Ab"),
  ("cbaBb","파스 트리: S(c, A(A(b, B(a, B)), b))\n어구: cbaBb (S), baBb (바깥 A), baB (안쪽 A), aB (B)\n단순 어구: aB\n핸들: aB"),
  ("aacc","파스 트리: S(a, B(a, B(c)), c)\n어구: aacc (S), ac (B), c (안쪽 B, 세 번째 기호)\n단순 어구: c (세 번째 기호)\n핸들: c (세 번째 기호, 마지막 c 아님)"),
]):
    Q(f"6-hh-{i+6}","handle-howto","calc",f"문법 {H2} 과 우문장 형태 {t} 가 주어졌을 때, 파스 트리를 그리고 어구, 단순 어구, 핸들을 보이시오.",
      ans, keys=["올바른 파스 트리","어구 전부(루트 포함)","단순 어구","핸들"], slot=14, pts=5)
Q("6-hh-9","handle-howto","mc","E → E + T | T, T → T * F | F, F → (E) | id 에서 우문장 형태 E + T * id 의 핸들은?",
  2, choices=["E + T","T","id","T * id"])
Q("6-hh-10","handle-howto","mc","같은 식 문법에서 우문장 형태 E + F * id 의 핸들은?",
  1, choices=["E + F","F","id","F * id"], explain="트리: E(E, +, T(T(F), *, F(id))). 단순 어구: F(T의 자식), id(F의 자식). 가장 왼쪽 = F.")
Q("6-hh-11","handle-howto","mc","같은 식 문법에서 우문장 형태 T * (E + id) 의 단순 어구를 모두 고른 것은?",
  3, choices=["T","E + id","T * (E + id)","id"], explain="트리: E(T(T, *, F((, E(E, +, T(F(id))), )))). 자식이 모두 잎인 내부 노드는 F → id 하나뿐 → 단순 어구 = 핸들 = id.")

Q("6-sr-1","shift-reduce","short","shift-reduce 알고리즘의 shift와 reduce 행동을 설명하시오.",
  "Shift: 다음 입력 토큰을 파스 스택의 top으로 옮긴다.\nReduce: 스택 top에 있는 핸들을 그에 대응하는 규칙의 LHS로 교체한다.",
  keys=["shift: 입력 토큰을 스택으로","reduce: 스택 top의 핸들 → LHS"])
Q("6-sr-2","shift-reduce","mc","reduce 행동에서 스택 top에서 LHS로 바뀌는 것은?",1,choices=["다음 입력 토큰","핸들","시작 기호","상태 0"])

Q("6-adv-1","lr-advantages","short","LR 파서의 장점 4가지를 쓰시오.",
  "1. 프로그래밍 언어를 기술하는 거의 모든 문법에 대해 동작한다.\n2. 다른 상향식 알고리즘보다 넓은 문법 클래스에서 동작하면서도 다른 상향식 파서만큼 효율적이다.\n3. 구문 오류를 가능한 한 빨리 탐지한다.\n4. LR 문법 클래스는 LL 파서로 파싱 가능한 클래스의 상위 집합이다.",
  keys=["거의 모든 PL 문법","넓은 클래스 + 효율","오류를 가능한 빨리 탐지","LR ⊃ LL"])
Q("6-adv-2","lr-advantages","mc","LR 문법 클래스와 LL 문법 클래스의 관계는?",
  0, choices=["LR이 LL의 상위 집합","LL이 LR의 상위 집합","서로 같다","서로 무관"])
Q("6-adv-3","lr-advantages","mc","LR 파싱 테이블을 만드는 방법으로 교안이 말한 것은?",
  2, choices=["손으로 쉽게 만든다","FIRST 집합만으로 만든다","yacc, bison 같은 도구로 생성한다","재귀 하강 파서에서 변환한다"])
Q("6-adv-4","lr-advantages","short","LR 파싱에 대한 Knuth의 통찰을 설명하시오.",
  "상향식 파서는 현재까지의 파싱 이력 전체를 이용해 파싱 결정을 내릴 수 있다. 가능한 파싱 상황의 수는 유한하고 비교적 작으므로, 이 이력을 파서 상태(state)로 파스 스택에 저장할 수 있다.",
  keys=["파싱 이력 전체 활용","상황 수가 유한·작음","이력을 상태로 스택에 저장"])

Q("6-ls-1","lr-structure","mc","ACTION 테이블의 열은?",1,choices=["비단말","단말","상태","규칙 번호"])
Q("6-ls-2","lr-structure","short","LR 파싱 테이블의 ACTION 테이블과 GOTO 테이블을 각각 설명하시오.",
  "ACTION 테이블: 파서 상태(행)와 다음 입력 토큰(열, 단말)이 주어졌을 때 파서의 행동(shift/reduce/accept/error)을 지정한다.\nGOTO 테이블: reduce 후에 파스 스택 top에 넣을 상태를 지정한다. 행은 상태, 열은 비단말.",
  keys=["ACTION: 상태×단말 → 행동","GOTO: 상태×비단말 → reduce 후 push할 상태"])
Q("6-ls-3","lr-structure","blank","LR 구성(configuration)은 (S0 X1 S1 … Xm Sm, ai … an $) 형태로, 왼쪽은 (a) 내용, 오른쪽은 남은 (b) 이다.",
  ["스택","입력"], accept=[["스택","파스스택","stack"],["입력","입력문자열","input"]])

Q("6-la-1","lr-actions","mc","reduce 후 GOTO 테이블을 찾을 때 사용하는 상태는?",
  2, choices=["reduce 직전 스택 top의 상태","항상 상태 0","핸들을 pop한 뒤 남은 스택 top의 상태","다음 입력 토큰"])
Q("6-la-2","lr-actions","mc","규칙 T → T * F 로 reduce 할 때 스택에서 pop하는 항목 수(기호+상태)는?",
  3, choices=["1","2","3","6"])
Q("6-la-3","lr-actions","short","LR 파서의 Shift와 Reduce 행동을 스택 관점에서 정확히 설명하시오.",
  "Shift(Sn): 다음 입력 기호와 상태 n을 스택에 push하고 입력에서 그 기호를 제거한다.\nReduce(Rn): 규칙 n의 RHS(핸들)를 상태 기호와 함께 스택에서 제거(RHS 길이×2개 pop)하고, LHS를 push한 뒤, 새 LHS 바로 아래 상태와 LHS로 GOTO 테이블을 찾아 그 상태를 push한다. 입력은 변하지 않는다.",
  keys=["Shift: 기호+상태 push, 입력 소비","Reduce: RHS×2 pop","LHS push 후 GOTO[아래 상태, LHS] push","입력 불변"])

def trace_table(s):
    rows=lr.run(s)
    w1=max(len(r[0]) for r in rows); w2=max(len(r[1]) for r in rows)
    return "\n".join(f"{r[0]:<{w1}}  | {r[1]:<{w2}}  | {r[2]}" for r in rows)
TB="(교안 p.78의 파싱 테이블 사용)\n1. E → E + T   2. E → T   3. T → T * F\n4. T → F       5. F → (E)  6. F → id"
for i,s in enumerate(["( id + id ) * id","id * id + id","id + id + id","( id ) * id + id"]):
    disp=s.replace("( ","(").replace(" )",")")
    Q(f"6-lt-{i+1}","lr-trace","calc",f"다음 문법과 LR 파싱 테이블을 사용하여 문자열 {disp} 에 대해 파서 스택 내용, 입력 문자열, 행동을 포함한 파싱 과정 전체를 보이시오.\n"+TB,
      trace_table(s), keys=["매 줄 ACTION[상태, 토큰] 조회","Reduce 시 RHS×2 pop 후 GOTO","스택·입력·행동 3열","accept까지"], slot=15, pts=10)

# step MCs from traces
import random
rnd=random.Random(7)
step_src=[("id * id + id",[3,6,10]),("( id + id ) * id",[3,8,10,13]),("id + id * id",[7,9,12])]
k=0
for s,idxs in step_src:
    rows=lr.run(s)
    for j in idxs:
        st,inp,act=rows[j]
        k+=1
        correct=act.split(",")[0] if act.startswith("Reduce") else act
        if act.startswith("Reduce"):
            correct=act
        pool=["Shift 5","Shift 6","Shift 7","Shift 4","Shift 11","Reduce 1 (E→E+T), goto[0,E]=1","Reduce 2 (E→T), goto[0,E]=1","Reduce 3 (T→T*F), goto[0,T]=2","Reduce 4 (T→F), goto[0,T]=2","Reduce 6 (F→id), goto[0,F]=3","accept"]
        wrong=[p for p in pool if p.split(",")[0].split(" (")[0]!=correct.split(",")[0].split(" (")[0]]
        rnd.shuffle(wrong)
        ch=[correct]+wrong[:3]; rnd.shuffle(ch)
        Q(f"6-step-{k}","lr-routine","mc",f"LR 파싱(교안 테이블) 중 현재 구성이 다음과 같다.\n스택: {st}\n입력: {inp}\n다음 행동은?",
          ch.index(correct), choices=ch, explain=f"스택 맨 오른쪽 상태와 다음 토큰 '{inp.split()[0]}' 로 ACTION 칸을 보면 {act}")
Q("6-rt-1","lr-routine","mc","교안 테이블에서 상태 2(스택 top이 T2)일 때 다음 토큰이 * 이면 Shift 7, + 이면 R2인 이유는?",
  0, choices=["*가 +보다 우선순위가 높아 T * F를 먼저 완성해야 하므로","*가 좌결합이므로","+가 오른쪽 결합이므로","상태 2가 accept 상태이므로"])
Q("6-rt-2","lr-routine","mc","Reduce 5 (F → (E)) 를 수행할 때 pop하는 기호는?",
  2, choices=["E 하나","( 와 E","(, E, ) 세 개 (상태 포함 6칸)","F 하나"])

Q("6-tb-1","lr-table","mc","교안 LR 테이블에서 ACTION[0, id]는?",0,choices=["S5","S4","R6","accept"])
Q("6-tb-2","lr-table","mc","교안 LR 테이블에서 GOTO[6, T]는?",2,choices=["2","3","9","10"])
Q("6-tb-3","lr-table","mc","교안 LR 테이블에서 ACTION[8, )]는?",3,choices=["R2","S6","R5","S11"])
