from qdsl import Q

# ───────── U3 Ch.3 의미론 ─────────
Q("3-ss-1","static-semantics","short","정적 의미론이 필요한 이유를, CFG(BNF)로 기술하기 어려운 구조 두 부류를 들어 설명하시오.",
  "CFG로는 언어 구문을 전부 기술할 수 없다.\n① 문맥 자유지만 기술이 번거로운 것: 식에서 피연산자의 타입 규칙\n② 문맥 자유가 아닌 것: 변수는 사용 전에 선언되어야 한다\n정적 의미론은 이런 프로그램의 적법한 형식(주로 타입 제약)에 대한 규칙이며, 컴파일 시간에 검사할 수 있다.",
  keys=["CFG로 다 기술 불가","번거로운 것: 피연산자 타입","문맥 자유 아님: 사용 전 선언","적법한 형식/컴파일 시간 검사"])
Q("3-ss-2","static-semantics","mc","'변수는 사용하기 전에 선언되어야 한다'는 규칙에 대한 설명으로 옳은 것은?",
  2, choices=["BNF로 쉽게 기술된다","동적 의미론에 속한다","문맥 자유가 아니라 BNF로 기술할 수 없다","어휘 분석기가 검사한다"])
Q("3-ss-3","static-semantics","ox","정적 의미론은 프로그램의 실행 의미와 직접 관련이 있고 실행 시간에 검사된다.",
  False, explain="정적 의미론은 의미와 간접적으로만 관련되며(적법한 형식), 컴파일 시간에 검사한다.")

Q("3-ag-1","ag-def","short","속성 문법(attribute grammar)을 정의하고 주된 용도 두 가지를 쓰시오.",
  "속성 문법: 문맥 자유 문법에 속성, 의미 함수(속성 계산 함수), 술어 함수를 추가하여 파스 트리 노드에 의미 정보를 담을 수 있게 한 문법.\n용도: 정적 의미론 명세, 컴파일러 설계(정적 의미 검사).",
  keys=["CFG + 속성/의미 함수/술어 함수","정적 의미론 명세","컴파일러 설계(정적 의미 검사)"])
Q("3-ag-2","ag-def","mc","속성 문법에서 '속성들과 리터럴 값에 대한 불리언 식'으로, 거짓이면 규칙 위반을 뜻하는 것은?",
  1, choices=["의미 함수","술어 함수","내장 속성","생성 규칙"])
Q("3-ag-3","ag-def","blank","모든 속성 값이 계산된 파스 트리를 (a) 파스 트리라고 한다.",
  ["완전히 속성화된"], accept=[["완전히속성화된","fullyattributed","완전속성화된","완전히속성화"]])

Q("3-ak-1","ag-attr-kinds","mc","규칙 X0 → X1 … Xn 에서 S(X0) = f(A(X1), …, A(Xn)) 형태로 정의되는 속성은?",
  0, choices=["합성 속성","상속 속성","내장 속성","술어 속성"], explain="자식들의 속성으로 부모(X0)의 속성을 계산 → 정보가 위로 흐름 → 합성.")
Q("3-ak-2","ag-attr-kinds","short","합성 속성, 상속 속성, 내장 속성을 각각 설명하시오.",
  "합성 속성: 자식 노드들의 속성 값으로 부모 노드의 속성을 계산 (정보가 아래→위로).\n상속 속성: 부모(와 형제) 노드의 속성으로 자식 노드의 속성을 계산 (정보가 위→아래).\n내장 속성: 잎 노드에 처음부터 정해져 있는 속성 (예: 심볼 테이블에서 찾은 변수의 타입).",
  keys=["합성: 자식→부모","상속: 부모/형제→자식","내장: 잎의 초기 값"])
Q("3-ak-3","ag-attr-kinds","mc","모든 속성이 합성 속성이라면 파스 트리를 어떤 순서로 장식할 수 있는가?",
  1, choices=["하향식","상향식","왼쪽에서 오른쪽만","순서를 정할 수 없음"])
Q("3-ak-4","ag-attr-kinds","ox","대부분의 실제 속성 문법은 합성·상속 속성을 모두 사용하므로 하향식과 상향식을 조합한 순서로 계산해야 한다.",True)

Q("3-age-1","ag-example","mc","교안 예제에서 <expr>.expected_type 은 어떤 종류의 속성인가?",
  1, choices=["합성","상속","내장","술어"], explain="부모 <assign>의 <var>.actual_type 에서 물려받음 → 상속.")
Q("3-age-2","ag-example","short","규칙 <expr> → <var>[1] + <var>[2] 에 붙는 의미 규칙과 술어를 쓰시오.",
  "의미 규칙: <expr>.actual_type ← <var>[1].actual_type\n술어: <var>[1].actual_type == <var>[2].actual_type\n      <expr>.expected_type == <expr>.actual_type",
  keys=["actual_type ← <var>[1].actual_type","술어: 두 피연산자 타입 같음","술어: expected == actual"])
Q("3-age-3","ag-example","mc","규칙 <var> → A | B | C 의 의미 규칙 `<var>.actual_type ← lookup(<var>.string)` 에서 lookup이 하는 일은?",
  2, choices=["토큰을 반환","다음 문자를 읽음","심볼 테이블에서 변수 이름을 찾아 그 타입을 반환","예약어인지 검사"])
Q("3-age-4","ag-example","calc","`A = A + B` 에 대해 교안 속성 문법으로 속성이 계산되는 순서를 쓰시오.",
  "1. <var>.actual_type ← lookup(A)  (좌변)\n2. <expr>.expected_type ← <var>.actual_type  (상속)\n3. <var>[1].actual_type ← lookup(A), <var>[2].actual_type ← lookup(B)\n4. 술어: <var>[1].actual_type == <var>[2].actual_type\n5. <expr>.actual_type ← <var>[1].actual_type  (합성)\n6. 술어: <expr>.actual_type == <expr>.expected_type",
  keys=["좌변 lookup → expected_type 상속","우변 두 변수 lookup","타입 비교 술어","actual_type 합성 후 expected와 비교"])

Q("3-sw-1","sem-why","mc","의미론을 형식적으로 기술할 필요가 있는 이유로 교안에 나오지 '않는' 것은?",
  3, choices=["컴파일러 작성자가 구조의 정확한 동작을 알아야 함","정확성 증명이 가능해짐","컴파일러 생성기가 가능해짐","실행 속도가 빨라짐"])
Q("3-sw-2","sem-why","ox","의미론을 기술하는 데에는 널리 받아들여지는 단 하나의 표기법이 있다.",
  False, explain="There is no single widely acceptable notation or formalism.")

Q("3-st-1","sem-three","short","동적 의미론을 기술하는 세 가지 방법을 쓰고 각각을 간략히 설명하시오.",
  "연산 의미론: 이상적인(가상) 기계에서 실행했을 때 기계 상태의 변화로 의미를 기술.\n표기 의미론: 구문 요소를 수학적 객체(재귀 함수)로 사상해 의미를 기술.\n공리 의미론: 형식 논리에 기반해 각 문장에 공리와 추론 규칙(전조건·후조건)을 정의하여 정확성을 증명.",
  keys=["연산: 기계 상태 변화","표기: 수학적 객체/재귀 함수로 사상","공리: 형식 논리, 전/후조건, 정확성 증명"], slot=4, pts=3)
Q("3-st-2","sem-three","mc","'형식 논리에 기반해 전조건과 후조건으로 프로그램의 정확성을 증명'하는 의미론은?",
  2, choices=["연산 의미론","표기 의미론","공리 의미론","정적 의미론"])
Q("3-st-3","sem-three","mc","'재귀 함수 이론'에 기반한 의미론은?",1,choices=["연산 의미론","표기 의미론","공리 의미론","속성 문법"])
Q("3-st-4","sem-three","mc","연산 의미론과 표기 의미론의 차이로 옳은 것은?",
  0, choices=["연산은 상태 변화를 코딩된 알고리즘으로, 표기는 엄밀한 수학 함수로 정의","연산은 수학 함수로, 표기는 알고리즘으로 정의","둘 다 전조건/후조건을 사용","둘은 같은 것"])

Q("3-op-1","operational","short","연산 의미론의 특징과 평가를 쓰시오.",
  "프로그램을 (시뮬레이션된 또는 실제) 기계에서 실행했을 때 기계 상태(메모리, 레지스터 등)의 변화로 의미를 정의한다. 수학이 아니라 더 낮은 수준의 언어의 문장으로 기술하며, 고급 언어에 쓰려면 가상 기계가 필요하다.\n평가: 비형식적으로 쓰면(언어 매뉴얼 등) 좋지만, 형식적으로 쓰면 매우 복잡하다(VDL로 PL/I 기술).",
  keys=["기계 상태 변화","저수준 언어로 기술/가상 기계","비형식적: 좋음, 형식적: 매우 복잡"])
Q("3-op-2","operational","calc","C의 `for (expr1; expr2; expr3) { body }` 의 의미를 연산 의미론(저수준 문장)으로 쓰시오.",
  "      expr1;\nloop: if expr2 == 0 goto out\n      body\n      expr3;\n      goto loop\nout:  ...",
  keys=["expr1 먼저 1번","expr2 거짓이면 out으로 탈출","body 후 expr3","goto loop"])
Q("3-op-3","operational","ox","연산 의미론에서 문장의 의미는 수학적 함수가 아니라 더 낮은 수준의 프로그래밍 언어로 기술된다.",True)

Q("3-den-1","denotational","calc","교안의 표기 의미론 Mdec 함수로 Mdec('305')를 단계별로 계산하시오.",
  "Mdec('305') = 10 * Mdec('30') + 5\n            = 10 * (10 * Mdec('3') + 0) + 5\n            = 10 * (10 * 3 + 0) + 5\n            = 10 * 30 + 5 = 305",
  keys=["Mdec(<dec_num> 'd') = 10*Mdec(<dec_num>) + d 적용","재귀적으로 '3'까지","결과 305"])
Q("3-den-2","denotational","blank","표기 의미론에서 구문 요소를 사상하는 함수의 정의역을 (a), 치역을 (b) 이라 한다.",
  ["구문 정의역","의미 정의역"], accept=[["구문정의역","syntacticdomain"],["의미정의역","semanticdomain"]])
Q("3-den-3","denotational","mc","표기 의미론에서 프로그램의 상태(state)란?",
  1, choices=["프로그램 카운터 값","모든 현재 변수의 값들의 집합 {<i1,v1>, …}","스택의 내용","파스 트리"])
Q("3-den-4","denotational","short","표기 의미론에서 while 루프 Ml(while B do L, s)의 정의를 쓰고, 루프가 어떻게 표현되는지 설명하시오.",
  "Ml(while B do L, s) =\n  if Mb(B, s) == undef then error\n  else if Mb(B, s) == false then s\n  else if Msl(L, s) == error then error\n  else Ml(while B do L, Msl(L, s))\n루프는 반복이 아니라 재귀로 표현된다: 몸체를 실행한 새 상태로 Ml을 다시 호출.",
  keys=["B undef → error","B false → s","몸체 error → error","else 재귀 호출 Ml(..., Msl(L,s))"])
Q("3-den-5","denotational","mc","표기 의미론의 평가로 옳은 것은?",
  2, choices=["언어 사용자에게 가장 유용","비형식적으로 쓸 때만 유용","언어를 정밀하게 기술하는 훌륭한 방법이지만 복잡해서 사용자에게는 거의 쓸모없음","정확성 증명이 주 목적"])

Q("3-asr-1","assertions","blank","공리 의미론에서 문장 앞의 단언을 (a), 뒤의 단언을 (b) 이라 하고, 후조건을 보장하는 가장 덜 제한적인 전조건을 (c) 이라 한다.",
  ["전조건","후조건","최약 전조건"], accept=[["전조건","precondition"],["후조건","postcondition"],["최약전조건","weakestprecondition","wp"]])
Q("3-asr-2","assertions","mc","`a = b + 1 {a > 1}` 에 대해 {b > 10}과 {b > 0}의 관계로 옳은 것은?",
  1, choices=["둘 다 전조건이 아니다","둘 다 전조건이지만 최약 전조건은 {b > 0}","최약 전조건은 {b > 10}","{b > 0}만 전조건"])
Q("3-asr-3","assertions","short","공리 의미론으로 프로그램의 정확성을 증명하는 과정을 설명하시오.",
  "프로그램 전체의 후조건(원하는 결과)에서 시작해, 마지막 문장부터 첫 문장까지 거꾸로 전조건(최약 전조건)을 계산한다. 첫 문장의 전조건이 프로그램 명세(입력 조건)와 같으면(또는 명세가 그것을 함의하면) 프로그램은 올바르다.",
  keys=["후조건에서 시작","거꾸로 전조건 계산","첫 문장 전조건 = 명세 → 정확"])

Q("3-wpa-1","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  a = 3 * (b - 2) + 1 {a > 4}",
  "3(b - 2) + 1 > 4\n3b - 6 + 1 > 4\n3b > 9\n최약 전조건: {b > 3}",
  keys=["a를 3(b-2)+1로 치환","전개·정리","{b > 3}"], slot=9, pts=3)
Q("3-wpa-2","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  a = a - 2 * b + 1 {a > 3}",
  "a - 2b + 1 > 3\na - 2b > 2\n최약 전조건: {a > 2b + 2}  (= {a - 2b > 2})",
  keys=["우변의 a도 그대로 둔 채 치환","{a > 2b + 2}"], slot=9, pts=3)
Q("3-wpa-3","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  x = 4 - 2 * x {x > 0}",
  "4 - 2x > 0\n-2x > -4\nx < 2   (음수로 나눠서 부등호 방향이 바뀜)\n최약 전조건: {x < 2}",
  keys=["치환","음수로 나눌 때 부등호 반전","{x < 2}"], slot=9, pts=3)
Q("3-wpa-4","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  y = 2 * (x + 1) - 4 {y >= 0}",
  "2(x + 1) - 4 >= 0\n2x - 2 >= 0\nx >= 1\n최약 전조건: {x >= 1}",
  keys=["치환·괄호 전개","{x >= 1}"], slot=9, pts=3)
Q("3-wpa-5","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  x = 3 * y - 1 {x < 11}",
  "3y - 1 < 11\n3y < 12\n최약 전조건: {y < 4}", keys=["치환","{y < 4}"], slot=9, pts=3)
Q("3-wpa-6","wp-assign","calc","다음 배정문과 후조건에 대해 최약 전조건을 계산하시오.\n  b = a / 3 + 2 {b <= 5}",
  "a/3 + 2 <= 5\na/3 <= 3\n최약 전조건: {a <= 9}", keys=["치환","{a <= 9}"], slot=9, pts=3)
Q("3-wpa-7","wp-assign","mc","`x = x + y - 3 {x > 10}` 의 최약 전조건은?",
  2, choices=["{x > 13}","{y > 13}","{x + y > 13}","{x + y > 7}"])
Q("3-wpa-8","wp-assign","mc","배정 공리 `{Q_x→E} x = E {Q}` 의 의미는?",
  0, choices=["후조건 Q에서 x를 모두 E로 치환한 것이 전조건","전조건에서 E를 x로 치환한 것이 후조건","Q와 E를 AND한 것이 전조건","x = E 가 참이면 Q도 참"])

Q("3-wpt-1","wp-theorem","calc","다음이 참인 정리인지 배정 공리로 판정하시오.\n  {y > 4} x = 2 * y - 3 {x > 5}",
  "wp(x = 2y - 3, x > 5) = (2y - 3 > 5) = {y > 4}\n주어진 전조건 {y > 4}와 같으므로 정리는 증명된다(참).",
  keys=["wp 계산 = {y > 4}","주어진 전조건과 일치 → 참"])
Q("3-wpt-2","wp-theorem","calc","다음을 증명하시오. (배정 공리만으로 안 되면 필요한 규칙을 쓰시오)\n  {x > 10} x = x - 4 {x > 3}",
  "wp(x = x - 4, x > 3) = {x - 4 > 3} = {x > 7}\n배정 공리: {x > 7} x = x - 4 {x > 3}\nx > 10 ⇒ x > 7 이므로 결과 규칙에 의해 {x > 10} x = x - 4 {x > 3} 이 성립.",
  keys=["wp = {x > 7}","x > 10 ⇒ x > 7","결과 규칙 적용"])
Q("3-wpt-3","wp-theorem","ox","{x > 3} x = x - 3 {x > 0} 은 배정 공리만으로 증명된다.",True,
  explain="wp(x = x - 3, x > 0) = {x > 3}으로 주어진 전조건과 정확히 같다.")

Q("3-con-1","consequence","mc","결과 규칙 {P} S {Q}, P' ⇒ P, Q ⇒ Q' ⊢ {P'} S {Q'} 이 말하는 것은?",
  1, choices=["전조건은 약하게, 후조건은 강하게 바꿀 수 있다","전조건은 강하게, 후조건은 약하게 바꿀 수 있다","전조건과 후조건을 바꿀 수 있다","S를 다른 문장으로 바꿀 수 있다"])
Q("3-con-2","consequence","calc","결과 규칙을 써서 다음을 증명하시오.\n  {a > 8} a = a - 5 {a > 2}",
  "배정 공리: wp(a = a - 5, a > 2) = {a > 7}, 즉 {a > 7} a = a - 5 {a > 2}\na > 8 ⇒ a > 7 이므로 결과 규칙에 의해\n{a > 8} a = a - 5 {a > 2}",
  keys=["배정 공리로 {a > 7}","a > 8 ⇒ a > 7","결과 규칙 결론"])
Q("3-con-3","consequence","blank","추론 규칙에서 선 위의 것들을 (a), 선 아래의 것을 (b) 이라 볼 수 있다.",
  ["전제","결론"], accept=[["전제","가정","antecedent","전건"],["결론","consequent","후건"]])

Q("3-seq-1","wp-seq","calc","다음 시퀀스와 후조건에 대해 최약 전조건을 계산하시오.\n  a = 3 * b - 2;\n  b = a + 4;\n  {b > 10}",
  "① b = a + 4 {b > 10}: a + 4 > 10 → {a > 6}\n② a = 3b - 2 {a > 6}: 3b - 2 > 6 → 3b > 8 → {b > 8/3}\n최약 전조건: {b > 8/3}  (정수라면 {b >= 3})",
  keys=["마지막 문장부터 거꾸로","① {a > 6}","② {b > 8/3}"], slot=11, pts=5)
Q("3-seq-2","wp-seq","calc","다음 시퀀스와 후조건에 대해 최약 전조건을 계산하시오.\n  x = 2 * y + 1;\n  y = x - 5;\n  {y > 0}",
  "① y = x - 5 {y > 0}: x - 5 > 0 → {x > 5}\n② x = 2y + 1 {x > 5}: 2y + 1 > 5 → {y > 2}\n최약 전조건: {y > 2}",
  keys=["거꾸로 계산","① {x > 5}","② {y > 2}"], slot=11, pts=5)
Q("3-seq-3","wp-seq","calc","다음 시퀀스와 후조건에 대해 최약 전조건을 계산하시오.\n  a = b + 2;\n  b = 2 * a - 1;\n  {b < 9}",
  "① b = 2a - 1 {b < 9}: 2a - 1 < 9 → {a < 5}\n② a = b + 2 {a < 5}: b + 2 < 5 → {b < 3}\n최약 전조건: {b < 3}",
  keys=["거꾸로","① {a < 5}","② {b < 3}"], slot=11, pts=5)
Q("3-seq-4","wp-seq","calc","다음 시퀀스와 후조건에 대해 최약 전조건을 계산하시오.\n  x = x + 1;\n  y = 2 * x;\n  {y > 6}",
  "① y = 2x {y > 6}: 2x > 6 → {x > 3}\n② x = x + 1 {x > 3}: x + 1 > 3 → {x > 2}\n최약 전조건: {x > 2}",
  keys=["거꾸로","① {x > 3}","② {x > 2}"], slot=11, pts=5)
Q("3-seq-5","wp-seq","calc","다음 시퀀스와 후조건에 대해 최약 전조건을 계산하시오.\n  c = a + b;\n  a = c - 2 * b;\n  {a > 1}",
  "① a = c - 2b {a > 1}: c - 2b > 1 → {c - 2b > 1}\n② c = a + b {c - 2b > 1}: (a + b) - 2b > 1 → a - b > 1\n최약 전조건: {a - b > 1}  (= {a > b + 1})",
  keys=["두 변수가 남아도 그대로 치환","① {c - 2b > 1}","② {a - b > 1}"], slot=11, pts=5)
Q("3-seq-6","wp-seq","mc","시퀀스 S1; S2 의 최약 전조건을 구하는 올바른 순서는?",
  1, choices=["S1의 wp를 먼저 구한 뒤 S2에 넣는다","S2의 wp를 먼저 구하고, 그것을 S1의 후조건으로 써서 S1의 wp를 구한다","S1과 S2의 wp를 각각 구해 AND한다","순서는 상관없다"])

Q("3-sel-1","wp-select","calc","다음 선택문과 후조건에 대해 최약 전조건을 계산하시오.\n  if (a > b)\n      b = a - 1\n  else\n      b = a + 2;\n  {b > 3}",
  "then: b = a - 1 {b > 3} → a - 1 > 3 → {a > 4}\nelse: b = a + 2 {b > 3} → a + 2 > 3 → {a > 1}\na > 4 ⇒ a > 1 이므로 (교재 방식) 최약 전조건: {a > 4}\n(정밀하게는 {(a > b and a > 4) or (a <= b and a > 1)})",
  keys=["then 쪽 {a > 4}","else 쪽 {a > 1}","합침: {a > 4} (또는 정밀형)"], slot=12, pts=5)
Q("3-sel-2","wp-select","calc","다음 선택문과 후조건에 대해 최약 전조건을 계산하시오.\n  if (x < y)\n      x = x - 2\n  else\n      x = 2 * x;\n  {x > 4}",
  "then: x - 2 > 4 → {x > 6}\nelse: 2x > 4 → {x > 2}\nx > 6 ⇒ x > 2 이므로 최약 전조건: {x > 6}\n(정밀하게는 {(x < y and x > 6) or (x >= y and x > 2)})",
  keys=["then {x > 6}","else {x > 2}","결론 {x > 6}"], slot=12, pts=5)
Q("3-sel-3","wp-select","calc","다음 선택문과 후조건에 대해 최약 전조건을 계산하시오.\n  if (a == b)\n      b = 3 * a - 3\n  else\n      b = a + 1;\n  {b > 3}",
  "then: 3a - 3 > 3 → {a > 2}\nelse: a + 1 > 3 → {a > 2}\n두 분기의 전조건이 같으므로 최약 전조건: {a > 2}",
  keys=["then {a > 2}","else {a > 2}","결론 {a > 2}"], slot=12, pts=5)
Q("3-sel-4","wp-select","calc","다음 선택문과 후조건에 대해 최약 전조건을 계산하시오.\n  if (y > 0)\n      x = y + 1\n  else\n      x = 1 - y;\n  {x > 2}",
  "then: y + 1 > 2 → {y > 1}\nelse: 1 - y > 2 → -y > 1 → {y < -1}\n두 전조건은 서로를 함의하지 않는다. 조건과 결합하면:\n  then 분기는 y > 0 이므로 y > 1 이면 됨, else 분기는 y <= 0 이므로 y < -1 이면 됨\n최약 전조건: {y > 1 or y < -1}",
  keys=["then {y > 1}","else {y < -1} (부등호 반전)","B와 결합해 {y > 1 or y < -1}"], slot=12, pts=5)
Q("3-sel-5","wp-select","mc","선택문 추론 규칙의 전제로 옳은 것은?",
  0, choices=["{B and P} S1 {Q}, {(not B) and P} S2 {Q}","{P} S1 {Q}, {P} S2 {Q}","{B} S1 {Q}, {not B} S2 {P}","{P and Q} S1 {B}"])
Q("3-sel-6","wp-select","calc","`if x > 0 then y = y - 1 else y = y + 1 {y > 0}` 의 최약 전조건을 교재 방식으로 구하고, 결과 규칙이 어디에 쓰이는지 설명하시오.",
  "then: y - 1 > 0 → {y > 1}\nelse: y + 1 > 0 → {y > -1}\ny > 1 ⇒ y > -1 이므로 결과 규칙으로 else 쪽 전조건을 {y > 1}로 강화할 수 있다.\n따라서 전체 전조건 {y > 1}",
  keys=["then {y > 1}","else {y > -1}","결과 규칙으로 강화 → {y > 1}"])

Q("3-lr-1","loop-rule","short","루프 불변자 I가 {P} while B do S end {Q}를 증명하기 위해 만족해야 하는 조건 4가지를 쓰시오.",
  "1. P ⇒ I : 루프 시작 전에 I가 참\n2. {I and B} S {I} : 몸체 실행이 I를 바꾸지 않음\n3. (I and (not B)) ⇒ Q : 루프 종료 시 Q가 함의됨\n4. 루프가 종료함",
  keys=["P ⇒ I","{I and B} S {I}","(I and not B) ⇒ Q","종료"])
Q("3-lr-2","loop-rule","mc","루프 종료까지 증명한 정확성을 무엇이라 하는가?",
  1, choices=["부분 정확성","전체 정확성","약한 정확성","귀납 정확성"])
Q("3-lr-3","loop-rule","blank","{I and B} S {I} 이면 {I} while B do S {(a)} 이다.",
  ["I and (not B)"], accept=[["iand(notb)","iandnotb","i∧¬b","iand~b","i&&!b","i그리고notb"]])

Q("3-inv-1","invariant","calc","`while y <> x do y = y + 1 end {y = x}` 의 루프 불변자를 반복 횟수별 wp로 구하시오.",
  "0회: {y = x}\n1회: wp(y = y + 1, y = x) = {y + 1 = x} = {y = x - 1}\n2회: {y = x - 2}\n…\n패턴: {y <= x} → 불변자 I = {y <= x}\n확인: (y <= x) and (y = x) ⇒ y = x",
  keys=["0,1,2회 wp 나열","I = {y <= x}","I and not B ⇒ Q 확인"])
Q("3-inv-2","invariant","mc","루프 불변자에 대한 설명으로 옳은 것은?",
  2, choices=["후조건보다 항상 강하다","루프 몸체의 첫 문장이다","루프 후조건의 약화된 버전이면서 루프의 전조건이기도 하다","루프가 끝날 때만 참이다"])
Q("3-inv-3","invariant","ox","불변자는 루프 시작 전에 만족될 만큼 약해야 하고, 종료 조건과 합쳐졌을 때 후조건을 강제할 만큼 강해야 한다.",True)
Q("3-inv-4","invariant","calc","`while x <> 0 do x = x - 1 end {x = 0}` 의 루프 불변자를 구하고, 조건 3 (I and not B ⇒ Q)을 확인하시오.",
  "0회: {x = 0}, 1회: {x = 1}, 2회: {x = 2} … → I = {x >= 0}\n확인: (x >= 0) and (x = 0) ⇒ x = 0 ✓",
  keys=["I = {x >= 0}","I and (x = 0) ⇒ x = 0"])

Q("3-lp-1","loop-proof","calc","다음 프로그램이 올바름을 증명하시오.\n{n >= 0}\ncount = n;\nfact = 1;\nwhile count <> 0 do\n    fact = fact * count;\n    count = count - 1;\nend\n{fact = n!}",
  "불변자 I = (fact = (count+1) * (count+2) * … * n) and (count >= 0)  (count = n이면 빈 곱 = 1)\n1. P ⇒ I: 루프 직전 count = n, fact = 1 = 빈 곱, count = n >= 0 → I 성립\n2. {I and B} S {I}: count ≠ 0 에서 fact = fact * count → fact = count * (count+1) * … * n,\n   count = count - 1 → fact = (count+1) * … * n 다시 성립, count >= 0 유지\n3. (I and not B) ⇒ Q: count = 0 이면 fact = 1 * 2 * … * n = n!\n4. 종료: count는 n >= 0에서 매번 1씩 감소하므로 0에 도달해 종료",
  keys=["적절한 불변자 제시","P ⇒ I","{I and B} S {I}","I and not B ⇒ Q","종료"], slot=19, pts=10)
Q("3-lp-2","loop-proof","calc","다음 프로그램이 올바름을 증명하시오.\n{n >= 0}\nk = n;\np = 0;\nwhile k <> 0 do\n    p = p + 2;\n    k = k - 1;\nend\n{p = 2 * n}",
  "불변자 I = (p = 2 * (n - k)) and (k >= 0)\n1. P ⇒ I: 루프 직전 k = n, p = 0 = 2(n - n), k = n >= 0 ✓\n2. {I and B} S {I}: p = 2(n - k), k ≠ 0(k >= 1)일 때 p = p + 2 → p = 2(n - k) + 2 = 2(n - (k - 1)), k = k - 1 → p = 2(n - k) 다시 성립, k >= 0 유지 ✓\n3. (I and not B) ⇒ Q: k = 0 이면 p = 2(n - 0) = 2n ✓\n4. 종료: k는 n >= 0에서 매번 1씩 감소 → 0에 도달",
  keys=["I = (p = 2(n-k)) and k >= 0","P ⇒ I","몸체가 I 유지","k = 0 → p = 2n","종료"], slot=19, pts=10)
Q("3-lp-3","loop-proof","calc","다음 프로그램이 올바름을 증명하시오.\n{n >= 0}\ni = 0;\ns = 0;\nwhile i <> n do\n    i = i + 1;\n    s = s + i;\nend\n{s = 1 + 2 + … + n}",
  "불변자 I = (s = 1 + 2 + … + i) and (i <= n)   (i = 0이면 빈 합 = 0)\n1. P ⇒ I: 루프 직전 i = 0, s = 0 = 빈 합, 0 <= n ✓\n2. {I and B} S {I}: i ≠ n 이고 i <= n 이므로 i < n. i = i + 1 후 i <= n, s = s + i → s = 1 + … + (i-1) + i ✓\n3. (I and not B) ⇒ Q: i = n 이면 s = 1 + 2 + … + n ✓\n4. 종료: i는 0에서 매번 1씩 증가하고 i <= n 이므로 n에 도달해 종료",
  keys=["I = (s = 1+…+i) and i <= n","P ⇒ I","몸체 유지","i = n → Q","종료"], slot=19, pts=10)
Q("3-lp-4","loop-proof","mc","24 중간 19번 같은 루프 정확성 증명 답안에 반드시 들어가야 하는 것이 '아닌' 것은?",
  3, choices=["루프 불변자","P ⇒ I 확인","(I and not B) ⇒ Q 확인","표기 의미론 함수 Ml의 정의"])

Q("3-ae-1","axiomatic-eval","short","공리 의미론의 장단점을 쓰시오.",
  "장점: 정확성 증명에 좋은 도구이고, 프로그램에 대해 추론하는 훌륭한 틀이다.\n단점: 언어의 모든 문장에 대한 공리·추론 규칙을 만드는 것이 어렵고, 언어 사용자와 컴파일러 작성자에게는 그다지 유용하지 않다.",
  keys=["장점: 정확성 증명·추론 틀","단점: 모든 문장의 공리 만들기 어려움","사용자·컴파일러 작성자에겐 덜 유용"])
Q("3-ae-2","axiomatic-eval","mc","공리 의미론의 원래 목적은?",0,choices=["형식적 프로그램 검증","컴파일러 생성","언어 매뉴얼 작성","가상 기계 설계"])
