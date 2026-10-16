@unit U2 | Ch.2 명령어: 컴퓨터의 언어 (MIPS) | W02 p.41 · week3-수업.pdf · week4-수업.pdf p.2–5
@intro 시험의 큰 덩어리. "명령어와 설명을 주고 빈칸이나 MIPS 표현을 채우는" 형식이 예고됐어. 교수님이 0점 처리한다고 경고한 규칙이 많은 단원이니 함정 박스를 꼭 읽어.

@lesson L2-1 | 산술 명령어 · 레지스터 피연산자 | week3 p.3–8 | C → MIPS 변환

## MIPS 명령어 분류 {#mips-classes}

MIPS: Stanford에서 나온 RISC ISA, 임베디드 시장에서 큰 점유율, 현대 ISA의 전형.

- **종류별**: Arithmetic · Memory(Data Transfer) · Logical · Conditional · Branch/Jump · Floating Point · Pseudo
- **형식별**: **R-format · I-format · J-format** · FP format

## 산술 명령어 형식 {#arith-format}

`add a, b, c   # a = b + c`

- **destination 1개 + source 2개**. 모든 산술 명령어가 이 형식.
- **Design Principle 1: Simplicity favors regularity** — 규칙적이면 구현이 단순, 단순하면 저비용·고성능.

슬라이드 예제:
```
a = b + c + d;          f = (g + h) - (i + j);
add a, b, c             add t0, g, h
add a, a, d             add t1, i, j
                        sub f, t0, t1
```
> 함정: 결과는 **사용자가 원한 변수**(여기선 f)에 넣어야 한다. 교수님이 "must be very careful at this term"이라고 강조.

## 레지스터 피연산자 {#registers}

- 산술 명령어는 **레지스터 피연산자만** 사용. 레지스터는 프로세서 안의 특별한 저장 위치.
- MIPS: **32개 × 32-bit 레지스터** (번호 0–31). 32-bit = word size (설계 당시 표준, MIPS64에서도 호환성 때문에 유지).
- 어셈블러 이름: `$t0–$t9` (임시), `$s0–$s7` (saved).
- **Design Principle 2: Smaller is faster** — 레지스터를 작게 만들어 자주 쓰는 데이터를 빨리 처리.

슬라이드 예제 (f, g, h, i, j가 $s0–$s4):
```
add $t0, $s1, $s2     # g + h
add $t1, $s3, $s4     # i + j
sub $s0, $t0, $t1     # f = (g+h) - (i+j)
```
> 함정: 연산 결과는 메모리로 바로 갈 수 없다. 항상 **레지스터에** 저장. (교안 이 슬라이드에 add/sub 오타가 있었고 수업에서 "change this into subtraction"이라고 고침)

@lesson L2-2 | 메모리 피연산자 · 엔디안 · lw/sw | week3 p.10–14 | lw/sw 오프셋

## 메모리 기본 {#memory-basics}

- 메인 메모리는 배열·구조체·동적 데이터 같은 **composite data**용. 레지스터가 적어서 모든 변수를 담을 수 없음.
- 산술 연산 전에 **load**(메모리 → 레지스터), 끝나면 **store**(레지스터 → 메모리).
- **Byte addressed**: 주소 하나 = 8-bit byte 하나.
- **Words are aligned**: word(32-bit)의 주소는 **4의 배수**.
- 배열 원소 주소 = base address + index × 4 (int 배열).

## Big Endian vs Little Endian {#endian}

- **Big endian**: MSB(가장 큰 자리 byte)를 **가장 낮은 주소**에.
- **Little endian**: LSB(가장 작은 자리 byte)를 **가장 낮은 주소**에.

0x12345678을 주소 0–3에:

| 주소 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Big endian | 12 | 34 | 56 | 78 |
| Little endian | 78 | 56 | 34 | 12 |

> 함정: 16진수 두 자리가 **1 byte**. Little endian에서도 byte 안의 두 자리 순서는 뒤집지 않는다 (78을 87로 쓰면 틀림). 교수님이 두 번 강조.

## lw / sw {#lw-sw}

`lw dest, offset(base)`  ·  `sw src, offset(base)`

- 피연산자 3개: 레지스터, **offset(상수, byte 단위)**, base address(레지스터).
- sw는 첫 번째 레지스터가 **source** (메모리에 쓸 값).

슬라이드 예제 1: `g = h + A[8];` (g:$s1, h:$s2, A의 base:$s3)
```
lw  $t0, 32($s3)      # offset = 8 × 4 = 32
add $s1, $s2, $t0
```
슬라이드 예제 2: `A[12] = h + A[8];`
```
lw  $t0, 32($s3)
add $t0, $s2, $t0
sw  $t0, 48($s3)      # 12 × 4 = 48
```

> 함정: **offset은 반드시 상수**. 레지스터를 offset 자리에 쓰면 정답이어도 **0점**, OX 문제면 무조건 False. 인덱스가 변수면 주소를 먼저 계산(`sll`, `add`)한 뒤 `lw $t0, 0($t1)`.

## Registers vs Memory {#reg-vs-mem}

- 레지스터가 메모리보다 훨씬 빠르고 쓰기 쉬움.
- 메모리 데이터로 연산하려면 load/store가 필요 → 실행 명령어 수 증가.
- 컴파일러는 변수를 최대한 레지스터에 두고, 덜 쓰는 변수만 메모리로 **spill**. 레지스터 최적화가 효율의 핵심.

@lesson L2-3 | 상수 · 2의 보수 · 부호 확장 · 16진수 | week3 p.15–23 | 2의 보수·부호확장

## Immediate 피연산자와 $zero {#immediate}

`addi $s3, $s3, 4` — 명령어 안에 상수를 직접 넣음.

- **subtract immediate는 없다** → 음수 상수로 addi: `addi $s2, $s1, -1`.
- **Design Principle 3: Make the common case fast** — 작은 상수가 흔하므로, immediate가 load를 없애 준다.
- **$zero (레지스터 0)** = 항상 상수 0, **덮어쓸 수 없음**.
- 레지스터 복사(move): `add $t2, $s1, $zero`

> 함정: 복사는 **`add` + `$zero`**. `addi`에 `$zero`(레지스터)를 상수 자리처럼 넣으면 0점 (교수님 4주-2). `$zero`는 상수가 아니라 레지스터.

## Unsigned와 2의 보수 {#twos}

- **Unsigned** n-bit: `x = x_{n-1}2^{n-1} + … + x_0 2^0`, 범위 **0 ~ 2ⁿ − 1** (32-bit 최대 4,294,967,295).
- **2's complement** n-bit: `x = −x_{n-1}2^{n-1} + x_{n-2}2^{n-2} + … + x_0 2^0`, 범위 **−2^{n−1} ~ 2^{n−1} − 1**.
  - bit 31 = sign bit (1 음수, 0 음이 아님). 음이 아닌 수는 unsigned와 표현이 같음.
  - `1111…1111` = −1, `1000…0000` = −2,147,483,648, `0111…1111` = 2,147,483,647.

## 부호 반전: Complement and add 1 {#negation}

`x + x̄ = 1111…1111₂ = −1` 이므로 `x̄ + 1 = −x`.

예: +2 = `0000 … 0010` → 반전 `1111 … 1101` → +1 → `1111 … 1110` = −2.

수업 예제: −10 (32-bit)
```
+10 = 0000 0000 0000 0000 0000 0000 0000 1010
반전 = 1111 1111 1111 1111 1111 1111 1111 0101
 +1  = 1111 1111 1111 1111 1111 1111 1111 0110   (= 0xFFFFFFF6)
```

## 부호 확장 (Sign extension) {#sign-ext}

더 많은 비트로 표현할 때 **값을 보존**: **sign bit를 왼쪽으로 복제**.

- MIPS에서 쓰는 곳: `addi`(immediate 확장), `lb`·`lh`(로드한 byte/halfword), **`beq`·`bne`(변위 확장)**.
- 8-bit → 16-bit: +2 = `0000 0010` → `0000 0000 0000 0010`, −2 = `1111 1110` → `1111 1111 1111 1110`.

> 함정: 교안 p.21에는 −2의 확장 결과가 `1111 1111 1000 0010`으로 적혀 있는데 **오타**. 올바른 값은 `1111 1111 1111 1110`.

## 16진수 {#hex}

16진수 한 자리 = 4 bit. 표: 0=0000 … 9=1001, a=1010, b=1011, c=1100, d=1101, e=1110, f=1111.

예: `eca8 6420` → `1110 1100 1010 1000 0110 0100 0010 0000`

@lesson L2-4 | 명령어 인코딩: R-format · I-format | week3 p.22–28 | 명령어 → 이진/16진

## 명령어 표현의 기본 {#encoding-basics}

- 명령어는 **32-bit 이진수(machine code)**로 인코딩. 형식 수를 적게 → **Regularity**.
- **opcode**: 앞 6 bit. 어떤 형식의 명령어인지 알려 줘서 나머지를 해석할 준비를 시킴.
- 레지스터 번호: `$t0–$t7` = 8–15, `$s0–$s7` = 16–23, `$t8–$t9` = 24–25 (그 외: $zero 0, $v0–$v1 2–3, $a0–$a3 4–7, $gp 28, $sp 29, $fp 30, $ra 31).

## R-format {#r-format}

| op | rs | rt | rd | shamt | funct |
|---|---|---|---|---|---|
| 6 bits | 5 | 5 | 5 | 5 | 6 bits |

- **op = 항상 0** (연산 종류는 funct가 결정).
- rs: 첫 번째 source, rt: 두 번째 source, **rd: destination**, shamt: shift amount (지금은 0), funct: function code (opcode 확장).
- funct 값은 시험에서 **주어짐** (외울 필요 없음). 참고: add 32, sub 34, and 36, or 37, slt 42.

예: `add $t0, $s1, $s2`
```
op      rs     rt     rd     shamt  funct
000000  10001  10010  01000  00000  100000
0       17     18     8      0      32
= 0000 0010 0011 0010 0100 0000 0010 0000₂ = 0x02324020
```

> 함정: 어셈블리는 **dest, src, src** 순서, 기계어는 **rs, rt, rd** (source 먼저, destination 나중). 교수님이 3주·6주 두 번 다 강조.

## I-format {#i-format}

| op | rs | rt | constant or address |
|---|---|---|---|
| 6 bits | 5 | 5 | 16 bits |

- immediate 산술과 load/store. **rt = destination(lw, addi) 또는 source(sw)**.
- constant: −2¹⁵ ~ +2¹⁵ − 1. address: rs의 base address에 더해지는 offset.
- 예: addi, lw, sw, beq, bne, slti, andi, ori, lui. opcode 참고: lw 35, sw 43, beq 4, bne 5, addi 8.
- **Design Principle 4: Good design demands good compromises** — 형식이 여러 개면 해석이 복잡하지만 모든 명령어를 32-bit로 통일할 수 있음. 형식은 최대한 비슷하게.

## 인코딩 예제: A[300] = h + A[300] {#encode-example}

`$t1` = A의 base, `$s2` = h.
```
lw  $t0, 1200($t1)     # 300 × 4 = 1200
add $t0, $s2, $t0
sw  $t0, 1200($t1)
```

| 명령어 | op | rs | rt | rd | shamt | funct / address |
|---|---|---|---|---|---|---|
| lw | 35 | 9 | 8 | | | 1200 |
| add | 0 | 18 | 8 | 8 | 0 | 32 |
| sw | 43 | 9 | 8 | | | 1200 |

이진: lw = `100011 01001 01000 0000 0100 1011 0000`, sw는 op만 `101011`.

@lesson L2-5 | 논리 연산 · 조건 분기 · if/while | week3 p.30–40 · week4 p.2 | if·while 컴파일

## Shift 연산 {#shift}

| 연산 | C | Java | MIPS |
|---|---|---|---|
| Shift left | << | << | **sll** |
| Shift right | >> | >>> | **srl** |
| Bitwise AND/OR/NOT | & \| ~ | & \| ~ | and, andi / or, ori / **nor** |

- R-format의 **shamt**에 몇 칸 밀지 들어감.
- **sll i** = 2^i 곱하기 (오른쪽을 0으로 채움). **srl i** = 2^i 나누기, **unsigned만**.

> 함정: srl은 왼쪽을 0으로 채우므로 음수(2의 보수)에 쓰면 부호가 깨진다 (교수님: "you should not just perform this operation on a signed number").

## AND · OR · NOR {#and-or-nor}

- **AND**: 마스킹. 원하는 비트만 남기고 나머지 0.
- **OR**: 원하는 비트를 1로, 나머지 유지.
- **NOT**은 MIPS에 없음 → **NOR 3-operand**: `nor $t0, $t1, $zero` = NOT $t1.

예 ($t1 = 0…0011 1100 0000 0000, $t2 = 0…0000 1101 1100 0000):
- `and $t0,$t1,$t2` → 0…0000 1100 0000 0000
- `or $t0,$t1,$t2` → 0…0011 1101 1100 0000

## 분기 명령어 {#branch-instr}

- `beq rs, rt, L1`: rs == rt면 L1로.
- `bne rs, rt, L1`: rs != rt면 L1로.
- `j L1`: 무조건 L1로 점프.

## if-else 컴파일 {#if-else}

`if (i == j) f = g + h; else f = g - h;` (f, g, h, i, j = $s0–$s4)
```
      bne $s3, $s4, Else    # i != j 이면 else로
      add $s0, $s1, $s2     # f = g + h
      j   Exit
Else: sub $s0, $s1, $s2     # f = g - h
Exit:
```
조건을 **반대로** 검사해서 else로 건너뛰는 게 요령 (i == j면 bne가 안 걸려서 if 블록 실행).

## while 루프 컴파일 {#while-loop}

`while (save[i] == k) i += 1;` (i: $s3, k: $s5, save의 base: $s6)
```
Loop: sll  $t1, $s3, 2      # t1 = i * 4
      add  $t1, $t1, $s6    # t1 = &save[i]
      lw   $t0, 0($t1)      # t0 = save[i]
      bne  $t0, $s5, Exit   # save[i] != k 이면 탈출
      addi $s3, $s3, 1      # i += 1
      j    Loop
Exit:
```
> 함정: 인덱스가 변수(i)라서 `lw $t0, $t1($s6)`처럼 쓰고 싶어도 **안 됨**. 주소를 먼저 계산하고 offset은 0. OX에서 "offset에 레지스터" = False.

## slt / slti / sltu {#slt}

- `slt rd, rs, rt`: rs < rt면 rd = 1, 아니면 0.
- `slti rt, rs, constant`: rs < constant면 rt = 1.
- beq/bne와 조합해서 모든 비교(==, !=, <, <=, >, >=)를 만든다.
```
slt $t0, $s1, $s2       # $s1 < $s2 면 $t0 = 1
bne $t0, $zero, L       # 1 != 0 이면 L로
```
- **Signed vs Unsigned**: slt/slti = signed, sltu/sltiu = unsigned.
  $s0 = 1111…1111, $s1 = 0000…0001일 때 `slt` → −1 < +1 → $t0 = 1, `sltu` → 4,294,967,295 > 1 → $t0 = 0.

## 왜 blt, bge가 없나 {#branch-design}

- 하드웨어에서 <, > 비교는 =, ≠보다 느림.
- 분기와 합치면 명령어당 일이 많아져 **클럭이 느려짐 → 모든 명령어가 손해**.
- 좋은 절충: **beq, bne** + slt 조합. (`blt`는 assembler의 pseudo-instruction으로 `slt` + `bne`로 바뀜.)

@lesson L2-6 | 프로시저 호출 · 스택 | week3 p.42–51 · week4 p.2–5 | 스택 저장/복원 순서

## 프로시저 호출 단계 · jal / jr {#jal-jr}

1. 인자를 레지스터에 둔다 → 2. 프로시저로 제어 이동 → 3. 저장 공간 확보 → 4. 연산 수행 → 5. 결과를 레지스터에 → 6. 호출한 곳으로 복귀.

- `jal ProcedureLabel` (jump-and-link): **다음 명령어 주소(PC+4)를 $ra에 저장**하고 타깃으로 점프.
- `jr $ra` (jump register): $ra를 PC에 복사 → 복귀. 계산된 점프에도 사용.
- PC: 현재 실행 중인 명령어의 주소를 담은 레지스터.

예: 100번지에서 `jal`, 함수는 388번지 → $ra = 104, PC = 388. 함수 끝의 `jr $ra`로 104로 복귀.

## 레지스터 사용 규약과 스택 {#reg-usage}

| 레지스터 | 번호 | 용도 |
|---|---|---|
| $a0–$a3 | 4–7 | 인자 |
| $v0, $v1 | 2–3 | 결과값 |
| $t0–$t9 | 8–15, 24–25 | 임시 (**보존 안 됨**) |
| $s0–$s7 | 16–23 | saved (**callee가 저장·복원**) |
| $gp / $sp / $fp / $ra | 28 / 29 / 30 / 31 | global ptr / **stack ptr** / frame ptr / **return address** |

- **Stack**: 레지스터를 spill하는 LIFO 구조. **$sp**는 가장 최근에 할당한 주소.
- **스택은 아래로 자란다** (높은 주소 → 낮은 주소): 공간 확보 = `addi $sp, $sp, -N`.
- Procedure frame (activation record): callee가 할당한 지역 데이터.

## Leaf procedure 예제 {#leaf}

다른 함수를 부르지 않는 함수. `int leaf_example(int g, h, i, j) { int f; f = (g+h) - (i+j); return f; }` (인자 $a0–$a3, f는 $s0)
```
leaf_example:
  addi $sp, $sp, -4      # int 하나(4 byte) 공간
  sw   $s0, 0($sp)       # 원래 $s0 저장
  add  $t0, $a0, $a1     # g + h
  add  $t1, $a2, $a3     # i + j
  sub  $s0, $t0, $t1     # f
  add  $v0, $s0, $zero   # 결과를 $v0로 복사
  lw   $s0, 0($sp)       # $s0 복원
  addi $sp, $sp, 4
  jr   $ra
```

## Non-leaf (재귀) 예제: fact {#nonleaf}

다른 함수를 부르는 함수는 호출 전에 **$ra와 이후에 필요한 인자**를 스택에 저장, 호출 후 복원.
```
fact:
  addi $sp, $sp, -8      # 2칸: 인자, 복귀주소
  sw   $ra, 4($sp)
  sw   $a0, 0($sp)
  slti $t0, $a0, 1       # n < 1 ?
  beq  $t0, $zero, L1    # 아니면 L1
  addi $v0, $zero, 1     # return 1
  addi $sp, $sp, 8
  jr   $ra
L1:
  addi $a0, $a0, -1      # n - 1
  jal  fact
  lw   $a0, 0($sp)       # 저장한 그 자리에서 복원
  lw   $ra, 4($sp)
  addi $sp, $sp, 8
  mul  $v0, $a0, $v0     # n * fact(n-1)
  jr   $ra
```
> 함정: **저장한 offset과 복원하는 offset이 같아야** 한다. 인자를 0에, $ra를 4에 넣었으면 복원도 그대로. 반대로 꺼내면 0점 (교수님 4주-1).

> 함정: 교안 week3 슬라이드의 C 코드는 `return f`로 오타. week5 슬라이드에서 `return 1`로 고쳐짐.

## fact(3) 스택 추적 {#fact-trace}

호출한 곳: 100번지 `jal fact` → $ra = 104, $a0 = 3. $sp 초기값 500.

| 단계 | $sp | 0($sp)에 저장 | 4($sp)에 저장 |
|---|---|---|---|
| fact(3) 진입 | 492 | a0 = 3 | ra = 104 |
| fact(2) 진입 | 484 | a0 = 2 | ra = L1+8 |
| fact(1) 진입 | 476 | a0 = 1 | ra = L1+8 |
| fact(0) 진입 | 468 | a0 = 0 | ra = L1+8 |

fact(0): slti → 0 < 1 이므로 $t0 = 1 → beq 안 걸림 → $v0 = 1, $sp = 476, jr → L1+8.
되돌아오며 `lw`로 a0을 1, 2, 3으로 복원하고 $v0 = 1 → 1 → 2 → 6. 마지막 jr은 **104**로.

> 함정: `slti $t0, $a0, 1`에서 a0 = 1이면 1 < 1이 거짓 → $t0 = 0 (재귀 계속). 교수님이 "be extremely careful"이라고 짚은 곳.

## 인자 타입별 스택 크기 (교수님 기준) {#stack-size}

- int 인자 1개 + $ra → 4 + 4 = **8 byte**.
- **교수님 설명**: char 인자는 1 byte씩. 예) char 인자 2개 + $ra → 4 + 1 + 1 = **6 byte**, char 3개면 4 + 3 = 7.
- 저장하는 값이 int면 char 배열을 다뤄도 4씩 움직인다 (strcpy에서 저장하는 건 int i).

> 주의: 실제 MIPS 컴파일러는 정렬 때문에 보통 4의 배수로 잡지만, 수업에서는 위처럼 설명했어. 시험에선 수업 기준으로.

## Byte 연산 · strcpy {#byte-ops}

- `lb rt, offset(rs)` / `lh`: sign extend해서 32-bit로. `lbu` / `lhu`: zero extend.
- `sb` / `sh`: 가장 오른쪽 byte/halfword만 저장.

`void strcpy(char x[], char y[])` (x, y 주소는 $a0, $a1, i는 $s0)
```
strcpy:
  addi $sp, $sp, -4
  sw   $s0, 0($sp)
  add  $s0, $zero, $zero   # i = 0
L1: add  $t1, $s0, $a1     # &y[i]  (char라서 ×4 없음)
  lbu  $t2, 0($t1)
  add  $t3, $s0, $a0       # &x[i]
  sb   $t2, 0($t3)
  beq  $t2, $zero, L2      # '\0' 이면 끝
  addi $s0, $s0, 1
  j    L1
L2: lw   $s0, 0($sp)
  addi $sp, $sp, 4
  jr   $ra
```
> 함정: char 배열은 원소가 1 byte라서 **sll로 ×4 하지 않는다**. int 배열과 다른 점.

@lesson L2-7 | 주소 지정 · 32-bit 상수 · 번역과 링크 | week3 p.49–67 | 분기 주소 계산

## 32-bit 상수: lui + ori {#lui-ori}

대부분 상수는 16-bit immediate로 충분. 가끔 32-bit 상수가 필요하면:

- `lui rt, constant`: 16-bit 상수를 rt의 **위 16 bit**에, 아래 16 bit는 0.
- 아래 16 bit는 **ori**로 채움 (addi 쓰지 말 것: 부호 확장 때문).
```
lui $s0, 61          # 0000 0000 0111 1101 0000 0000 0000 0000
ori $s0, $s0, 2304   # 0000 0000 0111 1101 0000 1001 0000 0000
```

## Branch addressing (PC-relative) {#branch-addr}

| op | rs | rt | constant or address (16) |
|---|---|---|---|

- beq/bne는 I-format. 대부분 분기 대상은 가까움(루프, if).
- **Target address = (PC + 4) + offset × 4**
- offset은 **명령어(word) 개수 차이**, 부호 있음 → **±2¹⁵ words** (= ±2¹⁷ bytes) 범위.
- 너무 멀면 assembler가 조건을 뒤집고 j로 우회하게 다시 씀:
```
beq $s0, $s1, L1      →      bne $s0, $s1, L2
                             j   L1
                         L2: …
```

> 시험 포인트: 6주에 교수님이 판서로 다시 설명: offset = (target − (PC + 4)) / 4. 예) PC 108, target 124 → (124 − 112)/4 = **3**. (4주-2 미리보기 설명은 대략적이었고 6주 설명이 정확한 규칙.)

## Jump addressing (J-format) {#jump-addr}

| op (6) | address (26) |
|---|---|

- j, jal: 대상이 text segment 어디든 될 수 있음 → 절대 주소를 인코딩.
- (Pseudo) direct jump: **Target = address × 4** (위 4 bit는 PC에서). 2²⁶ words = 2²⁸ bytes 범위.
- `jr`: 32-bit 전체 주소가 레지스터에 → R-format.

슬라이드 예제 (Loop가 80000번지):
```
80000 Loop: sll  $t1,$s3,2     0  0 19  9 2  0
80004       add  $t1,$t1,$s6   0  9 22  9 0 32
80008       lw   $t0,0($t1)   35  9  8   0
80012       bne  $t0,$s5,Exit  5  8 21   2      → (80012+4) + 2×4 = 80024 = Exit
80016       addi $s3,$s3,1     8 19 19   1
80020       j    Loop          2   20000        → 20000 × 4 = 80000 = Loop
80024 Exit:
```

## Addressing modes 요약 {#addr-modes}

1. Immediate (addi), 2. Register (add, jr), 3. Base/displacement (**lw, sw**), 4. PC-relative (**beq, bne**), 5. Pseudo-direct (**j, jal**).

## Pseudo-instruction · 번역 · 링크 {#translate}

- **Pseudo-instruction**: 어셈블러가 진짜 명령어로 바꿔 주는 가짜 명령어. `move $t0,$t1` → `add $t0,$zero,$t1`, `blt $t0,$t1,L` → `slt $at,$t0,$t1` + `bne $at,$zero,L`.
- 오브젝트 모듈: header, text segment, static data, relocation info, symbol table, debug info.
- **Linker**: 세그먼트 병합 → 레이블 주소 결정 → 위치 의존·외부 참조 수정 → executable.
- **Loader**: header 읽기 → 가상 주소 공간 생성 → text·data 복사 → 스택에 인자 → 레지스터 초기화($sp, $fp, $gp) → startup routine으로 점프.
- **Dynamic linking**: 호출될 때만 라이브러리를 링크/로드. relocatable 코드 필요, 이미지 비대 방지, 새 버전 자동 반영.
- **Memory layout**: Text(코드) → Static data(전역, $gp) → Dynamic data(heap, malloc) → Stack(자동 저장).

## Fallacies와 설계 원칙 정리 {#fallacies}

- Fallacy: 강력한 명령어 = 높은 성능 (복잡한 명령어는 구현이 어려워 단순한 것까지 느려짐).
- Fallacy: 고성능을 위해 어셈블리로 작성 (현대 컴파일러가 더 잘함).
- x86은 명령어 집합을 바꾸지 않고 계속 추가 (backward compatibility).
- **설계 원칙 4개**: 1. Simplicity favors regularity, 2. Smaller is faster, 3. Make the common case fast, 4. Good design demands good compromises.
