from qdsl import Q
# ───────── U3 컴퓨터 연산 ─────────

Q("3-ad-1","int-add","calc","4-bit로 7 + 6과 7 − 6을 계산하시오 (뺄셈은 2의 보수 덧셈으로).",
  "7 + 6: 0111 + 0110 = 1101 (13, unsigned)\n7 − 6 = 7 + (−6): −6 = 1010 → 0111 + 1010 = 1 0001 → carry 버림 → 0001 = 1",keys=["0111+0110","−6 = 1010","결과 0001"])
Q("3-ad-2","int-add","ox","뺄셈은 빼는 수의 2의 보수를 더하는 것으로 처리할 수 있다.",True)

Q("3-of-1","overflow","mc","오버플로가 '절대' 일어나지 않는 경우는?",2,choices=["양수 + 양수","음수 + 음수","양수 + 음수","음수 − 양수"])
Q("3-of-2","overflow","calc","4-bit 2의 보수에서 0110 (6) + 0101 (5)를 계산하고 오버플로 여부를 판정하시오.",
  "0110 + 0101 = 1011 → sign bit 1 (음수). 양수 + 양수가 음수 → overflow.",keys=["1011","양+양인데 sign 1","overflow"],slot=6,pts=5)
Q("3-of-3","overflow","calc","4-bit 2의 보수에서 1100 (−4) + 1011 (−5)을 계산하고 오버플로 여부를 판정하시오.",
  "1100 + 1011 = 1 0111 → 4 bit = 0111 → sign 0 (양수). 음수 + 음수가 양수 → overflow.",keys=["0111","음+음인데 sign 0","overflow"])
Q("3-of-4","overflow","blank","양수 − 음수에서 결과 sign bit가 (a)이면 오버플로, 음수 − 양수에서 결과 sign bit가 (b)이면 오버플로.",["1","0"],accept=[["1"],["0"]])
Q("3-of-5","overflow","ox","4-bit에서 0011 + 1110 (3 + (−2))은 결과에 carry가 나오므로 오버플로다.",False,explain="양수+음수는 오버플로 없음. carry out ≠ overflow.")
Q("3-of-6","overflow","mc","현대 CPU가 정수 오버플로를 처리하는 방식으로 수업에서 말한 것은?",1,choices=["무시한다","exception으로 처리","항상 0으로 만든다","결과를 64 bit로 확장"])

Q("3-mb-1","mult-basic","mc","n-bit × n-bit 곱셈 결과는 최대 몇 bit?",2,choices=["n","n+1","2n","n²"])
Q("3-mb-2","mult-basic","calc","종이 곱셈으로 1000 × 1001을 계산하고 10진수로 확인하시오.",
  "1000 + 0000(shift) + 0000(shift) + 1000(3칸 shift) = 1001000 = 72 (8 × 9)",keys=["부분곱","1001000","72"])

Q("3-m1-1","mult-v1","calc","원래 곱셈기(Multiplicand 8-bit shift left, Multiplier 4-bit shift right, Product 8-bit)로 0110 × 0011을 계산하시오. 각 반복의 Multiplier, Multiplicand, Product를 쓰시오.",
  "0: Mplier 0011, Mcand 0000 0110, Prod 0000 0000\n1: LSB=1 → Prod = 0000 0110; shift → Mplier 0001, Mcand 0000 1100\n2: LSB=1 → Prod = 0001 0010; shift → Mplier 0000, Mcand 0001 1000\n3: LSB=0 → no add; shift → 0000, 0011 0000\n4: LSB=0 → no add; shift → 0000, 0110 0000\nProduct = 0001 0010 (18)",
  keys=["매 반복 LSB 검사","LSB=1일 때만 덧셈","매 반복 두 번 shift","결과 0001 0010 = 18"],slot=11,pts=8)
Q("3-m1-2","mult-v1","calc","원래 곱셈기로 0111 × 0101을 계산하시오 (반복마다 Product 값).",
  "1: LSB=1 → Prod 0000 0111 (Mcand → 0000 1110)\n2: LSB=0 → Prod 0000 0111 (Mcand → 0001 1100)\n3: LSB=1 → Prod 0010 0011 (Mcand → 0011 1000)\n4: LSB=0 → Prod 0010 0011\n= 35",keys=["0000 0111","0010 0011","35"],slot=11,pts=8)
Q("3-m1-3","mult-v1","mc","원래 곱셈기에서 매 반복 Multiplicand와 Multiplier가 하는 shift는?",0,choices=["Multiplicand 왼쪽, Multiplier 오른쪽","둘 다 왼쪽","Multiplicand 오른쪽, Multiplier 왼쪽","LSB가 1일 때만 shift"])
Q("3-m1-4","mult-v1","ox","원래 곱셈기에서 Product 레지스터는 처음에 0으로 초기화한다.",True)
Q("3-m1-5","mult-v1","mc","원래 곱셈기(32-bit)에서 Multiplicand 레지스터와 ALU의 크기는?",3,choices=["32-bit, 32-bit","32-bit, 64-bit","64-bit, 32-bit","64-bit, 64-bit"])
Q("3-m1-6","mult-v1","ox","원래 곱셈기에서 Multiplier의 LSB가 0이면 그 반복에서는 shift도 하지 않는다.",False,explain="LSB와 상관없이 매 반복 shift.")

Q("3-m2-1","mult-v2","calc","개선된 곱셈기(Multiplicand 4-bit, Product 8-bit shift right)로 0011 × 0101을 계산하시오. 각 반복의 Product를 쓰시오.",
  "0: Product = 0000 0101 (아래 절반 = multiplier)\n1: LSB=1 → 위 += 0011 → 0011 0101 → >>1 → 0001 1010\n2: LSB=0 → >>1 → 0000 1101\n3: LSB=1 → 위 += 0011 → 0011 1101 → >>1 → 0001 1110\n4: LSB=0 → >>1 → 0000 1111\n= 15",
  keys=["초기: 아래 절반 = multiplier","LSB=1이면 위 절반에 더함","매 반복 >>1","0000 1111 = 15"],slot=11,pts=8)
Q("3-m2-2","mult-v2","calc","개선된 곱셈기로 1001 × 0110을 계산하시오 (반복마다 Product).",
  "0: 0000 0110\n1: LSB=0 → >>1 → 0000 0011\n2: LSB=1 → 1001 0011 → >>1 → 0100 1001\n3: LSB=1 → 1101 1001 → >>1 → 0110 1100\n4: LSB=0 → >>1 → 0011 0110 = 54",keys=["0100 1001","0110 1100","0011 0110 = 54"],slot=11,pts=8)
Q("3-m2-3","mult-v2","mc","개선된 곱셈기의 종료 조건은?",1,choices=["Product가 0","shift 횟수 = multiplier 비트 수","shift 횟수 = multiplicand 비트 수","Multiplicand가 0"])
Q("3-m2-4","mult-v2","ox","개선된 곱셈기에는 별도의 Multiplier 레지스터가 없고, multiplier는 Product 레지스터의 아래 절반에 들어간다.",True)
Q("3-m2-5","mult-v2","short","개선된 곱셈기가 원래 곱셈기보다 나은 점을 하드웨어 크기 관점에서 쓰시오. (영어로)",
  "The multiplicand register and ALU only need to be 32 bits (not 64), and the multiplier shares the product register's lower half, so no separate multiplier register is needed; only the product shifts right.",
  keys=["Multiplicand·ALU가 32-bit","multiplier가 Product 아래 절반을 공유","Product만 shift right"])
Q("3-m2-6","mult-v2","blank","개선된 곱셈기에서 LSB가 1이면 multiplicand를 Product의 (a) 절반에 더하고, 매 반복 Product를 (b)쪽으로 shift한다.",["위","오른"],accept=[["위","upper","상위","왼쪽"],["오른","오른쪽","right","우"]])

Q("3-me-1","mult-examples","calc","week5 Example 1: 원래 곱셈기로 1010 × 0010의 과정을 보이시오.",
  "0: Mplier 0010, Mcand 0000 1010, Prod 0000 0000\n1: LSB=0 → no add; Mplier 0001, Mcand 0001 0100\n2: LSB=1 → Prod = 0001 0100; Mplier 0000, Mcand 0010 1000\n3: LSB=0; Mcand 0101 0000\n4: LSB=0; Mcand 1010 0000\nProduct = 0001 0100 (20)",keys=["1회차 덧셈 없음","2회차 Prod = 0001 0100","결과 20"],slot=11,pts=8)
Q("3-me-2","mult-examples","calc","week5 Example 2: 개선된 곱셈기로 1010 × 1100의 과정을 보이시오.",
  "0: 0000 1100\n1: LSB=0 → >>1 → 0000 0110\n2: LSB=0 → >>1 → 0000 0011\n3: LSB=1 → 1010 0011 → >>1 → 0101 0001\n4: LSB=1 → 1111 0001 → >>1 → 0111 1000 (120)",keys=["0000 0011","0101 0001","0111 1000 = 120"],slot=11,pts=8)
Q("3-me-3","mult-examples","mc","Example 2의 3회차에서 위 절반에 1010을 더하기 직전 Product가 0000 0011이다. 더한 직후 값은?",2,choices=["0000 1101","1010 0000","1010 0011","0101 0001"])

Q("3-mi-1","mult-instr","mc","64-bit 곱 결과의 위 32 bit가 저장되는 레지스터는?",0,choices=["HI","LO","$v0","$ra"])
Q("3-mi-2","mult-instr","ox","`mul rd, rs, rt`는 64-bit 곱의 아래 32 bit만 rd에 넣는다.",True)

Q("3-db-1","div-basic","blank","Dividend = (a) × Divisor + (b)",["Quotient","Remainder"],accept=[["quotient","몫"],["remainder","나머지"]])
Q("3-db-2","div-basic","mc","Restoring division에서 빼기 결과가 음수일 때 하는 일은?",1,choices=["몫에 1을 넣는다","divisor를 다시 더해 원래 값으로 복구하고 몫에 0","나눗셈을 중단한다","divisor를 2배 한다"])
Q("3-db-3","div-basic","ox","Signed division에서 나머지(remainder)는 dividend와 같은 부호를 가진다.",True)
Q("3-db-4","div-basic","calc","1001010 ÷ 1000의 몫과 나머지를 이진수와 10진수로 쓰시오.",
  "몫 1001 (9), 나머지 10 (2) — 74 = 9 × 8 + 2",keys=["몫 1001","나머지 10","74 = 9×8 + 2"])

Q("3-d1-1","div-v1","calc","나눗셈기(Divisor 8-bit shift right, 처음엔 왼쪽 절반 / Remainder 8-bit / Quotient 4-bit shift left)로 0000 0111 ÷ 0010을 계산하시오. 각 반복의 판정과 Quotient, Remainder를 쓰시오.",
  "Divisor 초기 0010 0000, Rem 0000 0111\n1: Rem−Div < 0 → 복구, Q 0000, Div → 0001 0000\n2: < 0 → 복구, Q 0000, Div → 0000 1000\n3: 0000 0111 − 0000 1000 < 0 → 복구, Q 0000, Div → 0000 0100\n4: 0000 0111 − 0000 0100 = 0000 0011 ≥ 0 → Q 0001, Div → 0000 0010\n5: 0000 0011 − 0000 0010 = 0000 0001 ≥ 0 → Q 0011\nQuotient = 0011 (3), Remainder = 0000 0001 (1)",
  keys=["Divisor 초기 0010 0000","n+1 = 5회","음수면 add back + 0","Q = 0011 (3)","R = 1"],slot=12,pts=7)
Q("3-d1-2","div-v1","calc","같은 나눗셈기로 0000 1101 ÷ 0011을 계산하시오 (몫·나머지와 ≥0이 된 반복).",
  "Divisor 0011 0000에서 시작.\n1, 2회: 음수 → 복구\n3회: 0000 1101 − 0000 1100 = 0000 0001 ≥ 0 → Q 0001\n4회: 0000 0001 − 0000 0110 < 0 → Q 0010\n5회: 0000 0001 − 0000 0011 < 0 → Q 0100\nQ = 0100 (4), R = 1",keys=["3회차만 ≥ 0","Q = 0100 = 4","R = 1"],slot=12,pts=7)
Q("3-d1-3","div-v1","mc","4-bit 나눗셈기는 몇 번 반복하나?",2,choices=["3","4","5","8"],explain="n + 1 = 5 (32-bit면 33번).")
Q("3-d1-4","div-v1","ox","나눗셈기에서 Divisor는 처음에 Divisor 레지스터의 왼쪽(위) 절반에 놓인다.",True)
Q("3-d1-5","div-v1","mc","Rem − Div가 음수인지 판단하는 방법은?",0,choices=["결과의 첫 비트(sign bit)가 1인지","결과가 짝수인지","Quotient의 LSB","Divisor의 MSB"])
Q("3-d1-6","div-v1","blank","Rem ≥ 0이면 Quotient를 왼쪽 shift하고 새 LSB에 (a), Rem < 0이면 Divisor를 (b) 복구하고 LSB에 0.",["1","더해"],accept=[["1"],["더해","더해서","다시더해","addback","add","plusback","더함"]])

Q("3-dx-1","div-example","calc","week5 Example 3: 0001 0100 ÷ 0010을 나눗셈기로 계산하시오.",
  "Div 0010 0000, Rem 0001 0100\n1: 1111 0100 <0 → 복구, Q 0000, Div 0001 0000\n2: 0000 0100 ≥0 → Q 0001, Div 0000 1000\n3: 1111 1100 <0 → 복구, Q 0010, Div 0000 0100\n4: 0000 0000 ≥0 → Q 0101, Div 0000 0010\n5: 1111 1110 <0 → 복구, Q 1010\nQuotient 1010 (10), Remainder 0",keys=["2회 ≥0","4회 ≥0","Q = 1010 = 10","R = 0"],slot=12,pts=7)
Q("3-dx-2","div-example","mc","Example 3의 1회차에서 0001 0100 − 0010 0000의 결과는?",1,choices=["0000 0100","1111 0100","0001 0100","1110 1100"])

Q("3-d2-1","div-v2","mc","개선된 나눗셈기의 특징은?",0,choices=["Divisor·ALU를 32-bit로 줄이고 몫을 Remainder 레지스터에 함께 넣는다","Divisor를 64-bit로 늘린다","Quotient 레지스터를 두 개 쓴다","곱셈기와 같은 회로를 쓴다"])
Q("3-d2-2","div-v2","ox","0으로 나누는지(divisor = 0) 먼저 검사해야 한다.",True)

Q("3-if-1","ieee-format","mc","IEEE 754 single precision의 sign, exponent, fraction 비트 수는?",1,choices=["1, 11, 52","1, 8, 23","1, 7, 24","2, 8, 22"])
Q("3-if-2","ieee-format","mc","Double precision의 bias는?",3,choices=["127","128","1024","1023"])
Q("3-if-3","ieee-format","blank","x = (−1)^S × ((a) + Fraction) × 2^(Exponent − (b))",["1","Bias"],accept=[["1"],["bias","127","바이어스"]])
Q("3-if-4","ieee-format","ox","정규화된 수의 맨 앞 '1.'은 항상 1이라 저장하지 않는다 (hidden bit).",True)
Q("3-if-5","ieee-format","short","IEEE 754에서 exponent를 bias(excess) 표현으로 저장하는 이유와 single에서 bias 값을 쓰시오. (영어로)",
  "Exponent is stored as actual exponent + bias so that the stored exponent is always unsigned (easy to compare/sort). Single precision bias = 127 (double = 1023).",keys=["stored = actual + bias","exponent가 unsigned","single bias 127"])
Q("3-if-6","ieee-format","calc","Single precision에서 exponent 필드가 1000 0010이면 실제 지수는?",
  "130 − 127 = 3",keys=["130","−127","3"])

Q("3-ie-1","ieee-examples","calc","−0.75를 IEEE 754 single precision으로 표현하시오 (S, Exponent, Fraction, 16진수).",
  "0.75 = 0.11₂ = 1.1₂ × 2⁻¹\nS = 1, Exponent = −1 + 127 = 126 = 0111 1110, Fraction = 1000…0\n1 01111110 10000000000000000000000 = 0xBF400000",keys=["1.1 × 2⁻¹","S = 1","E = 126 = 01111110","F = 100…0","0xBF400000"],slot=13,pts=6)
Q("3-ie-2","ieee-examples","calc","0.625를 IEEE 754 single precision으로 표현하시오.",
  "0.625 = 0.101₂ = 1.01₂ × 2⁻¹\nS = 0, E = 126 = 0111 1110, F = 0100…0\n0 01111110 01000000000000000000000 = 0x3F200000",keys=["1.01 × 2⁻¹","E = 126","F = 0100…","0x3F200000"],slot=13,pts=6)
Q("3-ie-3","ieee-examples","calc","−3.75를 IEEE 754 single precision으로 표현하시오.",
  "3.75 = 11.11₂ = 1.111₂ × 2¹\nS = 1, E = 1 + 127 = 128 = 1000 0000, F = 1110…0\n1 10000000 11100000000000000000000 = 0xC0700000",keys=["1.111 × 2¹","E = 128 = 10000000","F = 111000…","0xC0700000"],slot=13,pts=6)
Q("3-ie-4","ieee-examples","calc","−12.5를 IEEE 754 single precision으로 표현하시오.",
  "12.5 = 1100.1₂ = 1.1001₂ × 2³\nS = 1, E = 3 + 127 = 130 = 1000 0010, F = 1001 0…0\n1 10000010 10010000000000000000000 = 0xC1480000",keys=["1.1001 × 2³","E = 130","F = 1001…","0xC1480000"],slot=13,pts=6)
Q("3-ie-5","ieee-examples","calc","−0.75를 IEEE 754 double precision으로 표현하시오 (exponent·fraction 비트 수 주의).",
  "S = 1, Exponent = −1 + 1023 = 1022 = 011 1111 1110 (11 bit), Fraction = 1000…0 (52 bit)\n= 0xBFE8000000000000",keys=["E = 1022 (11 bit)","F 52 bit","0xBFE8000000000000"])
Q("3-ie-6","ieee-examples","calc","single precision `0 01111111 10000000000000000000000`의 10진수 값은?",
  "E = 127 → 2⁰, significand 1.1₂ = 1.5 → 1.5",keys=["E−127 = 0","1.1₂","1.5"])
Q("3-ie-7","ieee-examples","calc","−2.25를 IEEE 754 single precision 16진수로 쓰시오.",
  "2.25 = 10.01₂ = 1.001₂ × 2¹ → S 1, E 128, F 0010…0 → 1 10000000 00100000000000000000000 = 0xC0100000",keys=["1.001 × 2¹","E 128","0xC0100000"])

Q("3-ir-1","ieee-range","mc","Single precision에서 exponent = 255, fraction ≠ 0이 뜻하는 것은?",3,choices=["0","±∞","Denormal","NaN"])
Q("3-ir-2","ieee-range","mc","Single precision의 대략적인 십진 정밀도는?",0,choices=["6자리","16자리","23자리","3자리"])
Q("3-ir-3","ieee-range","ox","Exponent = 0이고 fraction ≠ 0이면 denormal number이며 hidden bit는 0이다.",True)
Q("3-ir-4","ieee-range","calc","Single precision에서 가장 작은 정규화 양수와 가장 큰 수의 exponent 필드 값과 실제 지수는?",
  "최소: exponent 0000 0001 → 1 − 127 = −126 (1.0 × 2⁻¹²⁶)\n최대: exponent 1111 1110 → 254 − 127 = +127 (≈ 2.0 × 2¹²⁷)",keys=["00000001 → −126","11111110 → +127","00000000·11111111은 예약"])

Q("3-fa-1","fp-add","calc","4자리 이진 FP로 0.5 + (−0.4375)를 4단계로 계산하시오.",
  "1.000×2⁻¹ + (−1.110×2⁻²)\n1. Align: −1.110×2⁻² → −0.111×2⁻¹\n2. Add: 1.000 − 0.111 = 0.001 × 2⁻¹\n3. Normalize: 1.000×2⁻⁴ (no over/underflow)\n4. Round: 1.000×2⁻⁴ = 0.0625",keys=["작은 지수를 큰 쪽에 맞춤","0.001 × 2⁻¹","1.000 × 2⁻⁴","0.0625"],slot=13,pts=6)
Q("3-fa-2","fp-add","mc","FP 덧셈의 첫 단계는?",0,choices=["지수가 작은 쪽 significand를 shift해 지수를 맞춘다","significand를 곱한다","지수를 더한다","부호를 정한다"])
Q("3-fa-3","fp-add","calc","4자리 십진 FP로 9.999×10¹ + 1.610×10⁻¹을 계산하시오.",
  "1. 1.610×10⁻¹ → 0.016×10¹\n2. 9.999 + 0.016 = 10.015 ×10¹\n3. 1.0015×10²\n4. round → 1.002×10²",keys=["align 0.016×10¹","10.015","1.0015×10²","1.002×10²"])

Q("3-fm-1","fp-mul","calc","4자리 이진 FP로 0.5 × (−0.4375)를 5단계로 계산하시오 (biased exponent도 쓰시오).",
  "1.000×2⁻¹ × −1.110×2⁻²\n1. Exponent: −1 + −2 = −3 (biased: 126 + 125 − 127 = 124 = −3 + 127)\n2. 1.000 × 1.110 = 1.110 → 1.110×2⁻³\n3. Normalized, no over/underflow\n4. Round: no change\n5. Sign: + × − = − → −1.110×2⁻³ = −0.21875",keys=["지수 −3","bias 한 번 빼기","1.110 × 2⁻³","부호 −","−0.21875"],slot=13,pts=6)
Q("3-fm-2","fp-mul","ox","biased exponent 두 개를 더하면 bias가 두 번 들어가므로 bias를 한 번 빼야 한다.",True)
Q("3-fm-3","fp-mul","mc","FP 곱셈에서 결과의 부호는 언제 정하나 (슬라이드 순서)?",3,choices=["1단계","2단계","3단계","5단계 (마지막)"])

Q("3-fi-1","fp-instr","mc","MIPS single precision FP 레지스터는?",1,choices=["$t0–$t9","$f0–$f31","$s0–$s7","HI/LO"])
Q("3-fi-2","fp-instr","ox","Double precision은 FP 레지스터 두 개($f0/$f1)를 짝지어 쓴다.",True)
