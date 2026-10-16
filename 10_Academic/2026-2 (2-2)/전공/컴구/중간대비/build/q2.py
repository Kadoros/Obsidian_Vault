from qdsl import Q
# ───────── U2 명령어 (MIPS) ─────────
REGS = "$s0–$s7 = 16–23, $t0–$t7 = 8–15, $zero = 0, $sp = 29, $ra = 31, $a0–$a3 = 4–7, $v0 = 2"

Q("2-mc-1","mips-classes","mc","MIPS 명령어 '형식(format)' 분류가 아닌 것은?",3,choices=["R-format","I-format","J-format","B-format"])
Q("2-mc-2","mips-classes","ox","MIPS는 RISC ISA의 전형적인 예다.",True)

Q("2-af-1","arith-format","calc","C 코드 `a = b + c + d;`를 MIPS 산술 명령어로 쓰시오 (변수 이름을 그대로 피연산자로 써도 됨).",
  "add a, b, c\nadd a, a, d",keys=["두 줄로 분해","add a, b, c","add a, a, d"])
Q("2-af-2","arith-format","mc","`add a, b, c`의 의미는?",1,choices=["b = a + c","a = b + c","c = a + b","a = a + b + c"])
Q("2-af-3","arith-format","blank","Design Principle 1: (a) favors (b)",["Simplicity","regularity"],accept=[["simplicity","단순성"],["regularity","규칙성"]])
Q("2-af-4","arith-format","ox","MIPS 산술 명령어는 모두 destination 1개와 source 2개의 형식을 따른다.",True)

Q("2-rg-1","registers","calc","`f = (g + h) - (i + j);`를 MIPS로 쓰시오. f, g, h, i, j는 각각 $s0, $s1, $s2, $s3, $s4에 있다.",
  "add $t0, $s1, $s2   # g + h\nadd $t1, $s3, $s4   # i + j\nsub $s0, $t0, $t1   # f = (g+h) - (i+j)",
  keys=["add $t0, $s1, $s2","add $t1, $s3, $s4","sub $s0, $t0, $t1 (결과는 $s0)"],slot=7,pts=6)
Q("2-rg-2","registers","mc","MIPS 레지스터의 개수와 크기는?",2,choices=["16개 × 32 bit","32개 × 64 bit","32개 × 32 bit","64개 × 32 bit"])
Q("2-rg-3","registers","blank","Design Principle 2: (a) is faster",["Smaller"],accept=[["smaller","작을수록","small"]])
Q("2-rg-4","registers","ox","MIPS 산술 명령어는 메모리에 있는 피연산자로 직접 연산할 수 있다.",False,explain="레지스터 피연산자만. 메모리는 lw/sw로.")
Q("2-rg-5","registers","calc","`x = y - (z + 5);`를 MIPS로 쓰시오. x, y, z는 $s0, $s1, $s2.",
  "addi $t0, $s2, 5     # z + 5\nsub  $s0, $s1, $t0   # x = y - (z+5)",keys=["addi로 z+5","sub $s0, $s1, $t0"])

Q("2-mb-1","memory-basics","mc","MIPS 메모리 주소에 대한 설명으로 옳은 것은?",1,choices=["word 단위로 주소가 붙는다","byte 단위로 주소가 붙고 word 주소는 4의 배수","주소는 항상 홀수","레지스터와 같은 주소 공간"])
Q("2-mb-2","memory-basics","calc","int 배열 A의 base address가 0x1000이다. A[5]의 주소는?",
  "0x1000 + 5 × 4 = 0x1000 + 20 = 0x1014",keys=["base + index × 4","0x1014"])
Q("2-mb-3","memory-basics","ox","레지스터가 32개뿐이라 배열·구조체 같은 composite data는 메모리에 둔다.",True)

Q("2-en-1","endian","calc","32-bit 값 0x12345678을 주소 0–3에 저장한다. Big endian과 little endian에서 각 주소의 값을 쓰시오.",
  "Big endian:    0: 12, 1: 34, 2: 56, 3: 78\nLittle endian: 0: 78, 1: 56, 2: 34, 3: 12",keys=["big: MSB(12)가 0번지","little: LSB(78)가 0번지","byte 안 자리 순서 유지"],slot=6,pts=5)
Q("2-en-2","endian","calc","32-bit 값 0x34125678을 주소 0–3에 저장한다. Big endian과 little endian에서 각 주소의 값은?",
  "Big endian:    0: 34, 1: 12, 2: 56, 3: 78\nLittle endian: 0: 78, 1: 56, 2: 12, 3: 34",keys=["big 34 12 56 78","little 78 56 12 34"],slot=6,pts=5)
Q("2-en-3","endian","mc","0xA1B2C3D4를 little endian으로 저장할 때 주소 0의 값은?",3,choices=["A1","1A","4D","D4"],explain="LSB byte = D4. 두 자리 순서는 뒤집지 않음.")
Q("2-en-4","endian","ox","Little endian에서는 0x12345678의 마지막 byte 78을 0번지에 87로 저장한다.",False,explain="byte 안의 두 자리 순서는 바꾸지 않는다 → 78.")
Q("2-en-5","endian","blank","Big endian은 (a)를 가장 낮은 주소에, little endian은 (b)를 가장 낮은 주소에 저장한다.",["MSB","LSB"],accept=[["msb","mostsignificantbyte","최상위바이트"],["lsb","leastsignificantbyte","최하위바이트"]])
Q("2-en-6","endian","calc","0xCAFE0012를 주소 100–103에 big endian과 little endian으로 저장할 때 각 주소의 값은?",
  "Big:    100: CA, 101: FE, 102: 00, 103: 12\nLittle: 100: 12, 101: 00, 102: FE, 103: CA",keys=["big CA FE 00 12","little 12 00 FE CA"])

Q("2-lw-1","lw-sw","calc","`g = h + A[8];`을 MIPS로 쓰시오. g는 $s1, h는 $s2, A의 base address는 $s3.",
  "lw  $t0, 32($s3)     # A[8], offset = 8 × 4\nadd $s1, $s2, $t0",keys=["offset 32","lw $t0, 32($s3)","add $s1, $s2, $t0"],slot=7,pts=6)
Q("2-lw-2","lw-sw","calc","`A[12] = h + A[8];`을 MIPS로 쓰시오. h는 $s2, A의 base address는 $s3.",
  "lw  $t0, 32($s3)\nadd $t0, $s2, $t0\nsw  $t0, 48($s3)     # 12 × 4 = 48",keys=["lw offset 32","add","sw $t0, 48($s3)"],slot=7,pts=6)
Q("2-lw-3","lw-sw","mc","`sw $t0, 8($s1)`에서 $t0의 역할은?",0,choices=["메모리에 쓸 값(source)","읽어 온 값을 받을 destination","base address","offset"])
Q("2-lw-4","lw-sw","ox","`lw $t0, $t1($s3)`처럼 offset 자리에 레지스터를 쓸 수 있다.",False,explain="offset은 상수만. 시험 OX에서 무조건 False, 코드에 쓰면 0점.")
Q("2-lw-5","lw-sw","calc","`B[3] = B[1] + B[2];`를 MIPS로 쓰시오. B의 base address는 $s4 (int 배열).",
  "lw  $t0, 4($s4)\nlw  $t1, 8($s4)\nadd $t0, $t0, $t1\nsw  $t0, 12($s4)",keys=["offset 4, 8","add","sw offset 12"],slot=7,pts=6)
Q("2-lw-6","lw-sw","blank","`lw dest, (a)(base)` — 괄호 앞에는 (a)가, 괄호 안에는 (b)가 들어간다.",["offset","base address"],accept=[["offset","상수offset","오프셋","상수"],["baseaddress","base","베이스주소","기준주소","레지스터"]])
Q("2-lw-7","lw-sw","calc","`x = A[i];`를 MIPS로 쓰시오. x는 $s0, i는 $s1, A의 base는 $s2. (offset에 레지스터를 쓰지 말 것)",
  "sll $t1, $s1, 2      # i * 4\nadd $t1, $t1, $s2    # &A[i]\nlw  $s0, 0($t1)",keys=["sll로 ×4","base와 add","lw $s0, 0($t1)"],slot=7,pts=6)

Q("2-rm-1","reg-vs-mem","mc","레지스터 대신 메모리에 변수를 두면 생기는 일은?",2,choices=["CPI가 0이 된다","명령어 수가 줄어든다","load/store가 필요해 실행 명령어 수가 늘어난다","클럭이 빨라진다"])
Q("2-rm-2","reg-vs-mem","blank","자주 쓰지 않는 변수만 메모리로 내보내는 것을 (a)이라고 한다.",["spill"],accept=[["spill","spilling","스필"]])

Q("2-im-1","immediate","calc","레지스터 $s1의 값을 $s2로 복사하는 MIPS 명령어를 쓰시오 (교수님 기준).",
  "add $s2, $s1, $zero",keys=["add 사용","$zero와 더함"],explain="addi에 $zero를 넣으면 0점 (교수님 4주-2).")
Q("2-im-2","immediate","mc","`$s2 = $s1 - 1`을 하는 올바른 MIPS 명령어는?",2,choices=["subi $s2, $s1, 1","sub $s2, $s1, 1","addi $s2, $s1, -1","addi $s2, $s1, $zero"],explain="subtract immediate는 없다.")
Q("2-im-3","immediate","ox","$zero 레지스터에 값을 쓰면 그 값으로 바뀐다.",False)
Q("2-im-4","immediate","blank","Design Principle 3: Make the (a) case fast",["common"],accept=[["common","흔한","일반적인"]])
Q("2-im-5","immediate","ox","교수님 기준으로 `addi $v0, $s0, $zero`는 레지스터 복사로 올바른 코드다.",False,explain="$zero는 레지스터라 immediate 자리에 못 씀 → add $v0, $s0, $zero.")

Q("2-tw-1","twos","mc","32-bit 2의 보수로 표현할 수 있는 범위는?",1,choices=["0 ~ 2³²−1","−2³¹ ~ 2³¹−1","−2³² ~ 2³²","−(2³¹−1) ~ 2³¹"])
Q("2-tw-2","twos","calc","8-bit 2의 보수 `11111010`의 10진수 값은?",
  "−1×2⁷ + 1×2⁶ + 1×2⁵ + 1×2⁴ + 1×2³ + 0 + 1×2¹ + 0 = −128 + 122 = −6\n(또는 반전+1 → 00000110 = 6 → −6)",keys=["sign bit 1 → 음수","−6"],slot=6,pts=5)
Q("2-tw-3","twos","mc","32-bit `1111 … 1111` (모두 1)의 2의 보수 값은?",0,choices=["−1","−2,147,483,648","4,294,967,295","0"])
Q("2-tw-4","twos","ox","음이 아닌 수는 unsigned와 2의 보수에서 표현이 같다.",True)
Q("2-tw-5","twos","blank","n-bit unsigned 범위는 0 ~ (a), 2의 보수 범위는 (b) ~ 2^(n−1) − 1",["2^n − 1","−2^(n−1)"],accept=[["2^n1","2n1","2^n−1","2ⁿ1"],["2^n1","2^(n1)","2n1","−2^(n−1)"]])
Q("2-tw-6","twos","calc","8-bit 2의 보수로 표현 가능한 최솟값과 최댓값을 이진수와 10진수로 쓰시오.",
  "최솟값: 1000 0000 = −128\n최댓값: 0111 1111 = +127",keys=["10000000 = −128","01111111 = 127"])

Q("2-ng-1","negation","calc","−10을 32-bit 2의 보수로 쓰시오 (과정 포함).",
  "+10 = 0000 0000 0000 0000 0000 0000 0000 1010\ninvert = 1111 1111 1111 1111 1111 1111 1111 0101\n+1 = 1111 1111 1111 1111 1111 1111 1111 0110 (0xFFFFFFF6)",keys=["+10 이진","비트 반전","+1","…1111 0110"],slot=6,pts=5)
Q("2-ng-2","negation","calc","−5를 32-bit 2의 보수(16진수)로 쓰시오.",
  "+5 = 0…0101 → 반전 1…1010 → +1 = 1…1011 = 0xFFFFFFFB",keys=["반전 + 1","0xFFFFFFFB"])
Q("2-ng-3","negation","blank","Signed negation: (a) and add 1",["Complement"],accept=[["complement","invert","반전","비트반전","보수"]])
Q("2-ng-4","negation","ox","x + x̄ (x의 모든 비트를 반전한 값) = −1 이므로 −x = x̄ + 1 이다.",True)

Q("2-se-1","sign-ext","calc","8-bit 값 +2 (`0000 0010`)와 −2 (`1111 1110`)를 16-bit로 sign extension하시오.",
  "+2: 0000 0000 0000 0010\n−2: 1111 1111 1111 1110",keys=["+2는 위를 0으로","−2는 위를 1로","1111 1111 1111 1110"],slot=6,pts=5,
  explain="교안 p.21의 '1111 1111 1000 0010'은 오타.")
Q("2-se-2","sign-ext","mc","MIPS에서 sign extension이 일어나지 '않는' 경우는?",3,choices=["addi의 immediate","lb로 읽은 byte","beq의 변위(offset)","lbu로 읽은 byte"],explain="lbu·lhu는 zero extension.")
Q("2-se-3","sign-ext","calc","16-bit −3 (`1111 1111 1111 1101`)을 32-bit로 확장하면? 16진수로도 쓰시오.",
  "1111 1111 1111 1111 1111 1111 1111 1101 = 0xFFFFFFFD",keys=["위 16 bit를 1로","0xFFFFFFFD"])
Q("2-se-4","sign-ext","ox","Sign extension은 값을 보존하기 위해 sign bit를 왼쪽으로 복제한다.",True)
Q("2-se-5","sign-ext","ox","교안 p.21의 예 '−2 = 1111 1110 → 1111 1111 1000 0010'은 올바른 sign extension이다.",False,explain="오타. 1111 1111 1111 1110이 맞음.")
Q("2-se-6","sign-ext","calc","8-bit −6 (`1111 1010`)을 16-bit로 sign extension하면?",
  "1111 1111 1111 1010",keys=["위 8 bit를 1로","1111 1111 1111 1010"])

Q("2-hx-1","hex","calc","16진수 `eca8 6420`을 이진수로 바꾸시오.",
  "1110 1100 1010 1000 0110 0100 0010 0000",keys=["자리당 4 bit","1110 1100 1010 1000 0110 0100 0010 0000"])
Q("2-hx-2","hex","mc","이진 `0011 1100`의 16진수는?",1,choices=["0x3A","0x3C","0xC3","0x60"])

Q("2-eb-1","encoding-basics","mc","$t0, $s0, $sp의 레지스터 번호는?",2,choices=["0, 8, 31","8, 17, 30","8, 16, 29","16, 8, 29"])
Q("2-eb-2","encoding-basics","blank","MIPS 명령어는 (a)-bit로 인코딩되고, 맨 앞 (b) bit가 opcode다.",["32","6"],accept=[["32"],["6"]])
Q("2-eb-3","encoding-basics","mc","$t8, $t9의 레지스터 번호는?",3,choices=["16, 17","8, 9","26, 27","24, 25"])

Q("2-rf-1","r-format","calc",f"`add $t0, $s1, $s2`를 R-format 필드(10진수)와 이진수, 16진수로 쓰시오. ({REGS}, add의 funct = 32)",
  "op 0 | rs 17 | rt 18 | rd 8 | shamt 0 | funct 32\n000000 10001 10010 01000 00000 100000\n= 0x02324020",keys=["rs=$s1(17), rt=$s2(18), rd=$t0(8)","순서: rs rt rd","funct 32","0x02324020"],slot=8,pts=6)
Q("2-rf-2","r-format","calc",f"`sub $s0, $t0, $t1`의 기계어를 이진수와 16진수로 쓰시오. ({REGS}, sub의 funct = 34)",
  "op 0 | rs 8 | rt 9 | rd 16 | shamt 0 | funct 34\n000000 01000 01001 10000 00000 100010\n= 0x01098022",keys=["rs=$t0(8)","rt=$t1(9)","rd=$s0(16)","0x01098022"],slot=8,pts=6)
Q("2-rf-3","r-format","mc","R-format 필드의 순서로 옳은 것은?",2,choices=["op rd rs rt shamt funct","op rs rd rt shamt funct","op rs rt rd shamt funct","op rt rs rd funct shamt"])
Q("2-rf-4","r-format","ox","R-format 명령어의 opcode는 항상 0이고 연산 종류는 funct가 정한다.",True)
Q("2-rf-5","r-format","blank","어셈블리 `add rd, rs, rt`에서 destination은 맨 (a)에 오지만, 기계어에서 rd는 rs, rt (b)에 온다.",["앞","뒤"],accept=[["앞","처음","첫번째","first"],["뒤","다음","나중","after","뒤에"]])
Q("2-rf-6","r-format","calc",f"기계어 `000000 10001 10010 01000 00000 101010`을 어셈블리로 바꾸시오. (funct 42 = slt, {REGS})",
  "slt $t0, $s1, $s2",keys=["rs=17 → $s1","rt=18 → $s2","rd=8 → $t0","slt"],slot=8,pts=6)
Q("2-rf-7","r-format","calc",f"`and $t0, $t1, $t2`의 기계어를 16진수로 쓰시오. (and의 funct = 36, {REGS})",
  "000000 01001 01010 01000 00000 100100 = 0x012A4024",keys=["rs 9, rt 10, rd 8","funct 100100","0x012A4024"])

Q("2-if-1","i-format","mc","I-format의 필드 구성은?",1,choices=["op(6) rs(5) rt(5) rd(5) shamt(5) funct(6)","op(6) rs(5) rt(5) constant(16)","op(6) address(26)","op(6) rt(5) constant(21)"])
Q("2-if-2","i-format","mc","`lw $t0, 32($s3)`에서 rt 필드에 들어가는 레지스터는?",0,choices=["$t0 (destination)","$s3 (base)","32","rt 필드는 쓰지 않음"])
Q("2-if-3","i-format","calc",f"`lw $t0, 32($s3)`의 기계어를 이진수와 16진수로 쓰시오. (lw opcode = 35, {REGS})",
  "op 35 | rs 19 | rt 8 | 32\n100011 10011 01000 0000 0000 0010 0000 = 0x8E680020",keys=["rs = base $s3(19)","rt = $t0(8)","imm 32","0x8E680020"],slot=8,pts=6)
Q("2-if-4","i-format","blank","Design Principle 4: Good design demands good (a)",["compromises"],accept=[["compromises","compromise","절충","타협"]])
Q("2-if-5","i-format","ox","I-format의 상수 필드는 16 bit라서 −2¹⁵ ~ 2¹⁵ − 1 범위를 표현한다.",True)
Q("2-if-6","i-format","calc",f"`addi $s3, $s3, -1`의 기계어를 16진수로 쓰시오. (addi opcode = 8, {REGS})",
  "001000 10011 10011 1111 1111 1111 1111 = 0x2273FFFF",keys=["rs = rt = 19","−1 = 0xFFFF","0x2273FFFF"])

Q("2-ex-1","encode-example","calc","C 코드 `A[300] = h + A[300];`을 MIPS로 쓰고 각 명령어의 필드를 10진수로 쓰시오. $t1 = A의 base address, $s2 = h. (lw = 35, sw = 43, add funct = 32)",
  "lw  $t0, 1200($t1)    → 35 | 9 | 8 | 1200\nadd $t0, $s2, $t0     → 0 | 18 | 8 | 8 | 0 | 32\nsw  $t0, 1200($t1)    → 43 | 9 | 8 | 1200",
  keys=["offset 300×4 = 1200","lw 35 9 8 1200","add 0 18 8 8 0 32","sw 43 9 8 1200"],slot=8,pts=6)
Q("2-ex-2","encode-example","mc","A[300]의 byte offset은? (int 배열)",2,choices=["300","600","1200","2400"])
Q("2-ex-3","encode-example","calc","`lw $t0, 1200($t1)`의 이진 표현을 쓰시오. ($t0 = 8, $t1 = 9)",
  "100011 01001 01000 0000 0100 1011 0000  (= 0x8D2804B0)",keys=["op 100011","rs 01001","rt 01000","1200 = 0000 0100 1011 0000"])
Q("2-ex-4","encode-example","calc","`sw $t0, 48($s3)`의 16진수 기계어는? (sw = 43, $t0 = 8, $s3 = 19)",
  "101011 10011 01000 0000 0000 0011 0000 = 0xAE680030",keys=["op 43","rs 19","rt 8","0xAE680030"])

Q("2-sh-1","shift","mc","`sll $t2, $s0, 4`의 효과는?",2,choices=["$s0 / 16","$s0 + 4","$s0 × 16","$s0 × 4"])
Q("2-sh-2","shift","ox","srl은 왼쪽을 0으로 채우므로 음수(2의 보수)를 2^i로 나누는 데 그대로 쓸 수 있다.",False)
Q("2-sh-3","shift","blank","R-format에서 shift할 칸 수는 (a) 필드에 들어간다.",["shamt"],accept=[["shamt","shiftamount"]])
Q("2-sh-4","shift","calc","$s0 = 0000 … 0000 1001 (9)일 때 `sll $t2, $s0, 4`의 결과를 이진수와 10진수로 쓰시오.",
  "0000 … 1001 0000 = 144",keys=["왼쪽 4칸, 오른쪽 0 채움","144"])

Q("2-ao-1","and-or-nor","calc","$t1 = 0000 0000 0000 0000 0011 1100 0000 0000, $t2 = 0000 0000 0000 0000 0000 1101 1100 0000일 때 `and $t0, $t1, $t2`와 `or $t0, $t1, $t2`의 결과는?",
  "and: 0000 0000 0000 0000 0000 1100 0000 0000\nor:  0000 0000 0000 0000 0011 1101 1100 0000",keys=["and 결과","or 결과"])
Q("2-ao-2","and-or-nor","mc","MIPS에서 $t1의 모든 비트를 반전(NOT)하는 방법은?",1,choices=["not $t0, $t1","nor $t0, $t1, $zero","xor $t0, $t1, $zero","sub $t0, $zero, $t1"])
Q("2-ao-3","and-or-nor","ox","AND는 원하는 비트만 남기고 나머지를 0으로 만드는 마스킹에 쓴다.",True)

Q("2-bi-1","branch-instr","mc","`bne rs, rt, L1`의 동작은?",1,choices=["rs == rt면 L1로","rs != rt면 L1로","항상 L1로","rs < rt면 L1로"])
Q("2-bi-2","branch-instr","ox","`j L1`은 조건 없이 L1로 점프한다.",True)

Q("2-ie-1","if-else","calc","`if (i == j) f = g + h; else f = g - h;`를 MIPS로 쓰시오. f, g, h, i, j = $s0, $s1, $s2, $s3, $s4.",
  "      bne $s3, $s4, Else\n      add $s0, $s1, $s2\n      j   Exit\nElse: sub $s0, $s1, $s2\nExit:",
  keys=["bne로 반대 조건 검사","add $s0, $s1, $s2","j Exit","Else: sub","Exit 레이블"],slot=9,pts=8)
Q("2-ie-2","if-else","calc","`if (a != b) x = x + 1;`을 MIPS로 쓰시오. a, b, x = $s0, $s1, $s2.",
  "      beq  $s0, $s1, Skip\n      addi $s2, $s2, 1\nSkip:",keys=["beq로 반대 조건","addi $s2, $s2, 1","Skip 레이블"],slot=9,pts=8)
Q("2-ie-3","if-else","mc","if-else 컴파일에서 if 블록 끝에 `j Exit`가 필요한 이유는?",0,choices=["else 블록을 건너뛰려고","루프를 반복하려고","레지스터를 저장하려고","함수에서 복귀하려고"])
Q("2-ie-4","if-else","calc","`if (i < j) f = 1; else f = 0;`을 slt를 써서 MIPS로 쓰시오 (분기 없이 가능하면 그렇게). i, j, f = $s3, $s4, $s0.",
  "slt $s0, $s3, $s4",keys=["slt 한 줄로 끝","rs = i, rt = j"])
Q("2-ie-5","if-else","calc","`if (x == 0) y = y - 5; else y = y + 5;`를 MIPS로 쓰시오. x, y = $s0, $s1.",
  "      bne  $s0, $zero, Else\n      addi $s1, $s1, -5\n      j    Exit\nElse: addi $s1, $s1, 5\nExit:",keys=["bne $s0, $zero","addi -5 (subi 없음)","j Exit","Else: addi 5"],slot=9,pts=8)

Q("2-wl-1","while-loop","calc","`while (save[i] == k) i += 1;`을 MIPS로 쓰시오. i = $s3, k = $s5, save의 base = $s6.",
  "Loop: sll  $t1, $s3, 2\n      add  $t1, $t1, $s6\n      lw   $t0, 0($t1)\n      bne  $t0, $s5, Exit\n      addi $s3, $s3, 1\n      j    Loop\nExit:",
  keys=["sll ×4","add base","lw offset 0","bne로 탈출","addi i+1","j Loop"],slot=9,pts=8)
Q("2-wl-2","while-loop","ox","while 루프에서 `lw $t0, $s3($s6)`처럼 인덱스 레지스터를 offset에 바로 쓸 수 있다.",False)
Q("2-wl-3","while-loop","calc","`while (A[i] != 0) i++;`을 MIPS로 쓰시오. i = $s0, A의 base = $s1 (int 배열).",
  "Loop: sll  $t1, $s0, 2\n      add  $t1, $t1, $s1\n      lw   $t0, 0($t1)\n      beq  $t0, $zero, Exit\n      addi $s0, $s0, 1\n      j    Loop\nExit:",keys=["주소 계산","lw 0($t1)","beq $t0, $zero, Exit","j Loop"],slot=9,pts=8)
Q("2-wl-4","while-loop","mc","`sll $t1, $s3, 2`를 쓰는 이유는?",1,choices=["i를 2배 하려고","int 배열 원소가 4 byte라서 index × 4","부호를 확장하려고","루프를 끝내려고"])
Q("2-wl-5","while-loop","calc","`sum = 0; for (i = 0; i < 10; i++) sum += i;`을 MIPS로 쓰시오. sum = $s0, i = $s1.",
  "      add  $s0, $zero, $zero\n      add  $s1, $zero, $zero\nLoop: slti $t0, $s1, 10\n      beq  $t0, $zero, Exit\n      add  $s0, $s0, $s1\n      addi $s1, $s1, 1\n      j    Loop\nExit:",keys=["초기화","slti로 i<10","beq로 탈출","sum += i","i++","j Loop"])

Q("2-sl-1","slt","calc","$s0 = 1111 … 1111, $s1 = 0000 … 0001일 때 `slt $t0, $s0, $s1`과 `sltu $t0, $s0, $s1`의 결과는?",
  "slt (signed): −1 < +1 → $t0 = 1\nsltu (unsigned): 4,294,967,295 > 1 → $t0 = 0",keys=["slt → 1","sltu → 0","signed/unsigned 해석"])
Q("2-sl-2","slt","mc","`slti $t0, $a0, 1`에서 $a0 = 1이면 $t0는?",0,choices=["0","1","−1","변하지 않음"],explain="1 < 1은 거짓.")
Q("2-sl-3","slt","calc","`if ($s1 < $s2) goto L;`을 MIPS 두 줄로 쓰시오.",
  "slt $t0, $s1, $s2\nbne $t0, $zero, L",keys=["slt","bne $t0, $zero"])
Q("2-sl-4","slt","ox","`blt`는 MIPS의 진짜 명령어가 아니라 slt + bne로 바뀌는 pseudo-instruction이다.",True)

Q("2-bd-1","branch-design","short","MIPS가 blt, bge 같은 명령어 대신 beq, bne + slt를 쓰는 이유는? (영어로)",
  "Hardware for <, ≥ is slower than for =, ≠. Combining comparison with branching would do more work per instruction and require a slower clock, penalizing all instructions. beq/bne (with slt) is a good design compromise.",
  keys=["<,> 비교 하드웨어가 느림","명령어당 일 증가 → 클럭 느려짐","모든 명령어 손해","beq/bne = 좋은 절충"],slot=2,pts=3)
Q("2-bd-2","branch-design","ox","blt를 하드웨어 명령어로 넣으면 그 명령어만 느려지고 다른 명령어는 영향이 없다.",False)

Q("2-jj-1","jal-jr","mc","100번지의 `jal Proc`(Proc는 388번지)를 실행한 직후 $ra와 PC는?",2,choices=["$ra = 100, PC = 388","$ra = 388, PC = 104","$ra = 104, PC = 388","$ra = 104, PC = 104"])
Q("2-jj-2","jal-jr","blank","프로시저에서 복귀하는 명령어는 (a) $ra 이다.",["jr"],accept=[["jr","jumpregister"]])
Q("2-jj-3","jal-jr","ox","jal은 다음 명령어의 주소(PC + 4)를 $ra에 저장한다.",True)

Q("2-ru-1","reg-usage","mc","callee가 사용하려면 저장·복원해야 하는 레지스터는?",1,choices=["$t0–$t9","$s0–$s7","$a0–$a3","$zero"])
Q("2-ru-2","reg-usage","mc","MIPS 스택에서 4 byte 공간을 확보하는 명령어는?",0,choices=["addi $sp, $sp, -4","addi $sp, $sp, 4","subi $sp, 4","lw $sp, 4($sp)"])
Q("2-ru-3","reg-usage","blank","$a0–$a3는 (a), $v0–$v1은 (b)용 레지스터다.",["인자","결과값"],accept=[["인자","argument","arguments","인수","매개변수"],["결과값","결과","result","results","returnvalue","반환값"]])
Q("2-ru-4","reg-usage","ox","스택은 높은 주소에서 낮은 주소 방향으로 자란다.",True)

Q("2-lf-1","leaf","calc","`int leaf_example(int g, h, i, j) { int f; f = (g + h) - (i + j); return f; }`를 MIPS로 쓰시오. 인자는 $a0–$a3, f는 $s0, 결과는 $v0.",
  "leaf_example:\n  addi $sp, $sp, -4\n  sw   $s0, 0($sp)\n  add  $t0, $a0, $a1\n  add  $t1, $a2, $a3\n  sub  $s0, $t0, $t1\n  add  $v0, $s0, $zero\n  lw   $s0, 0($sp)\n  addi $sp, $sp, 4\n  jr   $ra",
  keys=["$sp −4, sw $s0","g+h, i+j","sub $s0","add $v0, $s0, $zero","lw $s0 복원","$sp +4","jr $ra"],slot=10,pts=8)
Q("2-lf-2","leaf","mc","leaf_example에서 $s0을 스택에 저장하는 이유는?",2,choices=["$s0이 인자라서","$s0이 $ra라서","$s0은 saved 레지스터라 callee가 원래 값을 보존해야 해서","스택 포인터라서"])
Q("2-lf-3","leaf","ox","Leaf procedure는 다른 프로시저를 호출하지 않는 프로시저다.",True)
Q("2-lf-4","leaf","calc","`int sum3(int a, int b, int c) { return a + b + c; }`를 MIPS로 쓰시오 (saved 레지스터 사용 안 함). 인자 $a0–$a2, 결과 $v0.",
  "sum3:\n  add $t0, $a0, $a1\n  add $v0, $t0, $a2\n  jr  $ra",keys=["임시 레지스터만 사용 → 스택 불필요","add 두 번","jr $ra"])
Q("2-lf-5","leaf","calc","leaf_example에서 f를 $s0, $s1 두 saved 레지스터에 나눠 쓴다면 프롤로그(스택 저장)는 어떻게 바뀌나?",
  "addi $sp, $sp, -8\nsw   $s1, 4($sp)\nsw   $s0, 0($sp)\n(에필로그는 같은 offset에서 lw 후 addi $sp, $sp, 8)",keys=["−8 확보","각각 다른 offset에 sw","복원 offset 일치"])

Q("2-nl-1","nonleaf","calc","재귀 `int fact(int n) { if (n < 1) return 1; else return n * fact(n - 1); }`를 MIPS로 쓰시오. 인자 $a0, 결과 $v0.",
  "fact:\n  addi $sp, $sp, -8\n  sw   $ra, 4($sp)\n  sw   $a0, 0($sp)\n  slti $t0, $a0, 1\n  beq  $t0, $zero, L1\n  addi $v0, $zero, 1\n  addi $sp, $sp, 8\n  jr   $ra\nL1:\n  addi $a0, $a0, -1\n  jal  fact\n  lw   $a0, 0($sp)\n  lw   $ra, 4($sp)\n  addi $sp, $sp, 8\n  mul  $v0, $a0, $v0\n  jr   $ra",
  keys=["$sp −8, $ra·$a0 저장","slti + beq","base case $v0 = 1","n−1, jal fact","같은 offset에서 복원","mul","jr $ra"],slot=10,pts=8)
Q("2-nl-2","nonleaf","mc","Non-leaf procedure가 호출 전에 스택에 반드시 저장해야 하는 것은?",3,choices=["$zero","$t 레지스터 전부","$sp","$ra와 호출 뒤에 필요한 인자·임시값"])
Q("2-nl-3","nonleaf","ox","fact에서 $a0를 0($sp)에, $ra를 4($sp)에 저장했다면 복원할 때 $a0를 4($sp)에서 읽어도 된다.",False,explain="반대로 복원하면 0점 (교수님 4주-1).")
Q("2-nl-4","nonleaf","short","Non-leaf procedure에서 $ra를 스택에 저장해야 하는 이유를 쓰시오. (영어로)",
  "Because the procedure itself calls another procedure with jal, which overwrites $ra with a new return address. Without saving it on the stack, the original return address to the caller would be lost.",keys=["jal이 $ra를 덮어씀","원래 복귀 주소를 잃음"])
Q("2-nl-5","nonleaf","blank","fact에서 n < 1 검사는 `slti $t0, $a0, 1` 다음 `(a) $t0, $zero, L1`으로 한다.",["beq"],accept=[["beq"]])

Q("2-ft-1","fact-trace","calc","100번지에서 `jal fact`로 fact(3)을 호출한다. $sp 초기값은 500. 재귀가 가장 깊어졌을 때까지 각 단계의 $sp와 스택에 저장된 (a0, ra)를 쓰시오.",
  "fact(3): $sp 492, 0($sp) = 3, 4($sp) = 104\nfact(2): $sp 484, 0($sp) = 2, 4($sp) = L1+8\nfact(1): $sp 476, 0($sp) = 1, 4($sp) = L1+8\nfact(0): $sp 468, 0($sp) = 0, 4($sp) = L1+8\n(fact(0)에서 slti → $t0 = 1 → $v0 = 1 반환)",
  keys=["492/484/476/468","첫 ra = 104","이후 ra = L1+8","a0 = 3,2,1,0"],slot=10,pts=8)
Q("2-ft-2","fact-trace","mc","fact(1) 실행 중 `slti $t0, $a0, 1`의 결과와 그 다음 동작은?",1,choices=["$t0 = 1, base case로 1 반환","$t0 = 0, beq가 L1로 분기해 fact(0) 호출","$t0 = 1, L1로 분기","$t0 = 0, 바로 jr $ra"])
Q("2-ft-3","fact-trace","calc","fact(3)이 모두 끝나면 $v0와 $sp, 마지막 jr이 가는 주소는?",
  "$v0 = 6 (1 → 1×1 → 2×1 → 3×2), $sp = 500 (원래대로), jr $ra → 104",keys=["$v0 = 6","$sp = 500","104로 복귀"])
Q("2-ft-4","fact-trace","ox","fact(3) 호출 시 스택은 총 4개의 frame(각 8 byte)이 쌓였다가 모두 해제된다.",True,explain="fact(3), (2), (1), (0) — 500 → 468.")

Q("2-ss-1","stack-size","mc","교수님 기준으로, char 인자 2개를 받는 재귀 함수가 $ra와 인자를 저장할 스택 크기는?",1,choices=["4 byte","6 byte","8 byte","12 byte"],explain="$ra 4 + char 1 + char 1 = 6.")
Q("2-ss-2","stack-size","mc","int 인자 1개를 받는 재귀 함수가 $ra와 인자를 저장할 스택 크기는?",2,choices=["4","6","8","16"])
Q("2-ss-3","stack-size","ox","strcpy처럼 char 배열을 다뤄도 스택에 저장하는 값이 int(i)라면 $sp는 4만큼 움직인다.",True)

Q("2-by-1","byte-ops","calc","`void strcpy(char x[], char y[]) { int i = 0; while ((x[i] = y[i]) != '\\0') i += 1; }`를 MIPS로 쓰시오. x, y는 $a0, $a1, i는 $s0.",
  "strcpy:\n  addi $sp, $sp, -4\n  sw   $s0, 0($sp)\n  add  $s0, $zero, $zero\nL1: add  $t1, $s0, $a1\n  lbu  $t2, 0($t1)\n  add  $t3, $s0, $a0\n  sb   $t2, 0($t3)\n  beq  $t2, $zero, L2\n  addi $s0, $s0, 1\n  j    L1\nL2: lw   $s0, 0($sp)\n  addi $sp, $sp, 4\n  jr   $ra",
  keys=["$s0 저장","i = 0","주소 = i + base (×4 없음)","lbu / sb","beq로 '\\0' 검사","i++, j L1","복원, jr"],slot=10,pts=8)
Q("2-by-2","byte-ops","mc","char 배열 x[i]의 주소 계산이 int 배열과 다른 점은?",0,choices=["원소가 1 byte라서 index에 4를 곱하지 않는다","index에 8을 곱한다","base address가 필요 없다","offset에 레지스터를 쓸 수 있다"])
Q("2-by-3","byte-ops","mc","1 byte를 읽어 32-bit로 zero extend하는 명령어는?",2,choices=["lw","lb","lbu","sb"])

Q("2-lu-1","lui-ori","calc","32-bit 상수 0x007D0900을 $s0에 넣는 MIPS 코드를 쓰시오 (0x007D = 125, 0x0900 = 2304).",
  "lui $s0, 125         # 0x007D → upper 16 bits\nori $s0, $s0, 2304   # 0x0900 → lower 16 bits",keys=["lui로 위 16 bit","ori로 아래 16 bit"])
Q("2-lu-2","lui-ori","ox","아래 16 bit를 채울 때 addi 대신 ori를 쓰는 이유는 addi가 immediate를 sign extend하기 때문이다.",True)

Q("2-ba-1","branch-addr","blank","Branch target address = (PC + (a)) + offset × (b)",["4","4"],accept=[["4"],["4"]])
Q("2-ba-2","branch-addr","calc","beq가 108번지에 있고 분기 대상이 124번지다. beq의 offset 필드 값은?",
  "offset = (124 − (108 + 4)) / 4 = 12 / 4 = 3",keys=["PC + 4 = 112","(124 − 112)/4","3"],slot=15,pts=6)
Q("2-ba-3","branch-addr","calc","beq가 1000번지에 있고 offset 필드가 −3이다. 분기 대상 주소는?",
  "(1000 + 4) + (−3) × 4 = 1004 − 12 = 992",keys=["PC+4 = 1004","−3 × 4 = −12","992"],slot=15,pts=6)
Q("2-ba-4","branch-addr","mc","PC-relative branch가 도달할 수 있는 범위는?",1,choices=["±2¹⁵ bytes","±2¹⁵ words(명령어)","±2²⁶ words","전체 메모리"])
Q("2-ba-5","branch-addr","calc","분기 대상이 너무 멀어 16-bit offset으로 표현할 수 없을 때 assembler는 `beq $s0, $s1, L1`을 어떻게 바꾸나?",
  "    bne $s0, $s1, L2\n    j   L1\nL2: …",keys=["조건 반전 bne","j L1","L2 레이블"])
Q("2-ba-6","branch-addr","ox","beq의 offset 필드에는 분기 대상의 byte 주소 차이가 그대로 들어간다.",False,explain="명령어(word) 개수 차이. ×4는 하드웨어(shift left 2)가 함.")

Q("2-ja-1","jump-addr","mc","J-format에서 address 필드는 몇 bit인가?",2,choices=["16","5","26","32"])
Q("2-ja-2","jump-addr","calc","Loop가 80000번지, `j Loop`의 address 필드 값은?",
  "80000 / 4 = 20000",keys=["Target = address × 4","20000"])
Q("2-ja-3","jump-addr","calc","80012번지의 `bne $t0, $s5, Exit`에서 offset 필드가 2일 때 Exit의 주소는?",
  "(80012 + 4) + 2 × 4 = 80024",keys=["PC+4 = 80016","+8","80024"])
Q("2-ja-4","jump-addr","mc","jr은 어느 형식인가?",0,choices=["R-format","I-format","J-format","FP format"])

Q("2-am-1","addr-modes","mc","lw, sw가 쓰는 addressing mode는?",2,choices=["PC-relative","Pseudo-direct","Base (displacement)","Immediate"])
Q("2-am-2","addr-modes","mc","beq, bne가 쓰는 addressing mode는?",0,choices=["PC-relative","Register","Base","Pseudo-direct"])

Q("2-tr-1","translate","mc","Linker가 하는 일이 '아닌' 것은?",3,choices=["segment 병합","레이블 주소 결정","위치 의존·외부 참조 수정","가상 주소 공간 생성 후 프로그램을 메모리에 복사"],explain="마지막은 loader.")
Q("2-tr-2","translate","calc","pseudo-instruction `move $t0, $t1`과 `blt $t0, $t1, L`을 실제 MIPS 명령어로 바꾸시오.",
  "move $t0, $t1 → add $t0, $zero, $t1\nblt $t0, $t1, L → slt $at, $t0, $t1\n                  bne $at, $zero, L",keys=["add $t0, $zero, $t1","slt $at","bne $at, $zero, L"])
Q("2-tr-3","translate","ox","Dynamic linking은 라이브러리 프로시저가 호출될 때만 링크·로드한다.",True)

Q("2-fa-1","fallacies","ox","강력한(복잡한) 명령어를 쓰면 항상 성능이 높아진다.",False)
Q("2-fa-2","fallacies","mc","MIPS 설계 원칙 4개에 들어가지 '않는' 것은?",2,choices=["Simplicity favors regularity","Smaller is faster","Hierarchy of memories","Good design demands good compromises"])
