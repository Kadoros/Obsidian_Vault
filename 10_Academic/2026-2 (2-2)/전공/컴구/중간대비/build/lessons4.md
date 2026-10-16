@unit U4 | Ch.4 프로세서: 데이터패스와 제어 (단순 버전) | week6-수업.pdf
@intro 교수님이 6주-2에서 "오늘 목표는 이 슬라이드 한 장(p.3 단순 CPU)을 완벽히 이해하는 것"이라고 함. 명령어마다 어떤 선으로 데이터가 흐르고, 각 MUX에 0/1 중 뭘 줘야 하는지가 핵심. 개념을 읽은 다음 '수업 따라가기' 탭에서 교수님 설명을 장면별로 보고, '데이터패스 놀이터'에서 명령어별 경로를 확인해.

@lesson L4-1 | 프로세서 개요 · 명령어 실행 단계 | week6 p.2–7 | 7개 명령어만

## 두 가지 구현과 명령어 부분집합 {#proc-intro}

- CPU 성능 요소: Instruction Count, **CPI와 Cycle Time** (이 단원은 CPI·cycle time을 결정하는 구현).
- 두 가지 MIPS 구현: **단순 버전 (중간고사)**, 파이프라인 버전 (기말).
- 다루는 명령어: 메모리 `lw, sw` · 산술/논리 `add, sub, and, or` · 제어 `beq, j` (p.4엔 `slt`도 포함).

> 시험 포인트: 교수님 "중간에서는 이 명령어들만 써야 한다. 다른 명령어를 쓰면 0점." 수업에서는 "seven instructions"라고 말했는데, 슬라이드 목록은 lw, sw, add, sub, and, or, beq, j. 단순 데이터패스에서 실제로 다룬 건 R-type, lw, sw, beq.

## 명령어 실행 단계 {#exec-steps}

1. **PC → instruction memory**, 명령어 fetch.
2. **Register numbers → register file**, 레지스터 읽기.
3. 명령어 종류에 따라:
   - **ALU**로 계산: 산술 결과 / load·store용 **메모리 주소** / **분기 대상 주소**
   - load·store면 **data memory** 접근
   - **PC ← 분기 대상 주소 또는 PC + 4**

명령어는 1 word = **32 bit = 4 byte** → 다음 줄로 가려면 **PC + 4**.

> 함정: 6주-1 녹음에서 "word = 32 bytes"라고 말한 부분이 있는데 말실수. 32 **bits** = 4 bytes.

## CPU 개요와 MUX가 필요한 이유 {#cpu-overview}

p.5 개요도: PC → Instruction memory → Registers → ALU → Data memory, 그리고 PC+4 adder와 branch adder.

p.6: **"Can't just join wires together: Use multiplexers"** — 서로 다른 출처의 선을 그냥 합칠 수 없으니 선택기가 필요한 곳 3군데:
1. **PC 입력**: PC + 4 또는 branch target
2. **ALU 두 번째 입력**: 레지스터 값 또는 명령어의 16-bit 상수(sign-extended)
3. **레지스터 쓰기 데이터**: ALU 결과 또는 data memory에서 읽은 값

p.7: 여기에 **Control** 유닛이 붙어서 MUX 선택 신호, RegWrite, MemRead/MemWrite, ALU operation, Branch를 만든다.

> 교수님 설명: R-format이면 ALU 결과가 원하는 값이지만, lw면 ALU 결과는 **주소일 뿐**이고 실제 원하는 건 그 주소의 메모리 값. 그래서 쓰기 데이터 MUX가 필요.

@lesson L4-2 | 논리 설계 기초 · 클럭 | week6 p.8–15 | MUX 0/1 읽기

## 정보 표현과 조합 회로 {#comb-elements}

- 이진 표현: low voltage = 0, high = 1. **선 하나 = 1 bit**, 여러 bit는 multi-wire bus (32-bit면 선 32개).
- **Combinational element**: 데이터에 연산. **출력이 입력만의 함수** (기억 없음).

| 소자 | 식 |
|---|---|
| AND gate | Y = A & B |
| **Multiplexer** | **Y = S ? I1 : I0** |
| Adder | Y = A + B |
| ALU | Y = F(A, B), F = 수행할 함수 |

ALU는 adder의 확장판. R-format이면 F는 명령어의 맨 아래 6 bit(**funct**)로 결정됨.

## Multiplexer 읽는 법 {#mux-basic}

- 입력선마다 번호가 붙어 있음 (I0, I1).
- **선택선 S = 0 → I0, S = 1 → I1**.
- 시험에서는 **어떤 선이 0이고 어떤 선이 1인지 그림에 표시돼서** 나옴. 교수님이 판서로 0과 1을 직접 써서 설명.

> 시험 포인트: 신호값은 "위/아래"가 아니라 **MUX에 적힌 숫자**로 정해. 숫자가 뒤집혀 있으면 신호도 반대 (6주-2 "be extremely careful on what is actually written on the multiplexer").

## 순차 소자: 레지스터 {#seq-elements}

- **State (sequential) element**: 정보를 **저장**.
- **Register**: 회로에 데이터를 저장. **clock**으로 언제 값을 갱신할지 결정.
- **Edge-triggered**: Clk이 **0 → 1로 바뀔 때(rising edge)** 갱신.
- **Register with write control**: clock edge이면서 **write control 입력이 1일 때만** 갱신. 나중에 값이 필요할 때 사용. (레지스터 파일의 RegWrite가 이것)

> 함정: 6주-1에서 "0 to 1 or 1 to 0"이라고 말했지만 슬라이드와 6주-2 설명은 **0 → 1**. 시험은 슬라이드 기준.

## Clocking methodology {#clocking}

- 조합 회로는 **클럭 사이클 동안(클럭 edge 사이)** 데이터를 변환.
- 입력은 state element에서 오고, 출력은 state element로 감.
- **가장 긴 지연이 clock period를 결정**.

@lesson L4-3 | 데이터패스 구성 요소 | week6 p.16–24 | 4개의 MUX

## 데이터패스 만들기 · Instruction fetch {#fetch}

- **Datapath**: CPU에서 데이터·주소를 처리하는 요소들 (레지스터, ALU, MUX, 메모리…). 명령어 부분집합에 맞춰 단계적으로 만든다.
- **Instruction fetch**: **PC(32-bit register)**가 instruction memory의 read address로 → 명령어 출력. 동시에 PC가 **Add**에 들어가서 **+4** → 다음 명령어 주소가 다시 PC로.

## R-format 데이터패스 {#r-datapath}

R-format(add, sub, and, or, slt): opcode = 000000, **funct(5:0)**가 연산 결정.
1. 레지스터 피연산자 **2개 읽기** (Read register 1 = rs, Read register 2 = rt, 각 5 bit)
2. 산술/논리 연산 (ALU, ALU operation 4 bit)
3. 결과를 레지스터에 **쓰기** (Write register = rd, Write data, **RegWrite = 1**)

예 `add $t0, $s1, $s2` → op 0 | rs 17 | rt 18 | rd 8 | shamt 0 | funct 32.

## Load/Store 데이터패스 {#ls-datapath}

1. 레지스터 읽기 (rs = base)
2. 16-bit offset으로 주소 계산: ALU 사용, offset은 **sign-extend (16 → 32)**
3. **Load**: 메모리 읽고 레지스터 갱신 (**MemRead = 1, RegWrite = 1**)
4. **Store**: 레지스터 값을 메모리에 쓰기 (**MemWrite = 1**)

Sign extension: 위 16 bit를 상수의 sign bit로 채움 (양수 0, 음수 1).

> 함정: 6주-1 23:18에 lw 설명하면서 "memory write field를 켠다"고 말했는데 말실수. lw는 **MemRead**와 RegWrite, MemWrite는 sw. 바로 뒤(24:50)에 정정함.

## Branch 데이터패스 {#br-datapath}

beq:
1. 레지스터 피연산자 읽기 (rs, rt)
2. ALU로 **빼기** → **Zero 출력** 확인 (같으면 Zero = 1)
3. 분기 대상 주소 계산:
   - 변위(16 bit)를 **sign-extend**
   - **Shift left 2** (word 변위 → byte, ×4)
   - **PC + 4**에 더함 (PC + 4는 fetch에서 이미 계산됨)

> 시험 포인트: 분기 상수는 주소가 아니라 **(PC + 4)부터 몇 줄(명령어) 떨어졌나**. byte가 아니라 줄 수로 주는 이유는 4로 안 나눠지는 값이 들어가면 심각한 오류가 나기 때문.

## 요소 합치기: 4개의 MUX {#composing}

- 단순 데이터패스는 **명령어 하나를 한 클럭 사이클에** 실행.
- 각 요소는 한 번에 한 기능만 → **instruction memory와 data memory를 분리**.
- 출처가 둘인 곳마다 MUX:
  1. ALU 입력: 레지스터 vs 명령어의 immediate → **ALUSrc**
  2. 레지스터 쓰기 데이터: ALU 출력 vs data memory → **MemtoReg**
  3. 다음 PC: PC + 4 vs branch target → **Branch AND Zero** (PCSrc)
  4. 쓰기 레지스터 번호: **Rt vs Rd** → **RegDst**

@lesson L4-4 | 전체 데이터패스 따라가기 (R-type · lw · sw · beq) | week6 p.3, p.26, p.34–37 | 신호값·MUX 숫자

## 명령어 필드가 가는 곳 {#dp-fields}

p.3 그림에서 32-bit 명령어가 쪼개지는 곳:

| 필드 | 비트 | 가는 곳 |
|---|---|---|
| opcode | [31–26] | **Control** |
| rs | [25–21] | Read register 1 (항상 읽음) |
| rt | [20–16] | Read register 2 **그리고** RegDst MUX의 0번 입력 |
| rd | [15–11] | RegDst MUX의 1번 입력 |
| imm | [15–0] | **Sign-extend** (16 → 32) |
| funct | [5–0] | **ALU control** |

## R-type (add $t0, $s1, $s2) {#dp-rtype}

- opcode 000000 → Control이 R-type 신호를 냄.
- rs, rt 읽기 → ALU의 두 입력 모두 **레지스터** → **ALUSrc = 0**.
- 결과를 **rd(세 번째 레지스터)**에 씀 → RegDst MUX에서 [15–11]을 고름 → **RegDst = 1** (p.3에선 1번 입력이 rd).
- 쓰기 데이터는 **ALU 결과** → **MemtoReg = 0**. **RegWrite = 1**.
- 메모리 접근 없음 → MemRead = MemWrite = 0. Branch = 0. ALUOp = 10 (funct가 연산 결정).

## lw ($t0, offset($s1)) {#dp-lw}

- rs = base 읽기, 상수 offset을 sign-extend → ALU 두 번째 입력은 **상수** → **ALUSrc = 1**.
- ALU는 **덧셈**으로 주소 계산 (ALUOp = 00). ALU 결과는 값이 아니라 **주소**.
- Data memory 읽기 → **MemRead = 1**.
- 읽은 값을 레지스터에 → **MemtoReg = 1**, **RegWrite = 1**.
- 쓰는 레지스터는 **rt(두 번째)** → **RegDst = 0**.

## sw ($t0, offset($s1)) {#dp-sw}

- 주소 계산은 lw와 같음 → **ALUSrc = 1**, ALUOp = 00.
- rt의 값(Read data 2)이 data memory의 **Write data**로 → **MemWrite = 1**.
- 레지스터에 쓰지 않음 → **RegWrite = 0**, 그래서 RegDst와 MemtoReg는 **X (don't care)**.

## beq (rs, rt, offset) {#dp-beq}

- opcode → Control이 **Branch = 1**.
- 두 레지스터를 **빼서** 비교 → ALU 입력 둘 다 레지스터 → **ALUSrc = 0**, ALUOp = 01 (빼기).
- 같으면 ALU **Zero = 1** → **AND(Branch, Zero) = 1** → PC MUX가 **branch target(1번)** 선택. 다르면 0 → **PC + 4(0번)**.
- 분기 대상: offset sign-extend → shift left 2 → (PC + 4)에 더함.
- 레지스터 쓰기 없음 → RegWrite = 0, RegDst = X, MemtoReg = X. 메모리 접근 없음.

## MUX 숫자 함정 (p.3 MemtoReg) {#mux-trap}

p.3 그림의 MUX 3개는 **0이 위**인데, 맨 오른쪽 **MemtoReg MUX는 1이 위**(Read data), **0이 아래**(ALU result).

- 교수님 설명: "ALU 결과를 고르려면 0, data memory 값을 고르려면 1" → 그림 숫자와 일치. 위/아래가 아니라 **숫자**를 봐야 함.
- 교수님: "if I flip the numbers on your multiplexer … you will have to generate a total opposite signal". 시험 그림에서 숫자가 바뀌면 답도 바뀜.

> 시험 포인트: MUX 문제를 풀 땐 ① 원하는 입력선 찾기 ② 그 선에 적힌 숫자 = 신호값. 표를 외워서 쓰지 말 것.

## 분기 오프셋 계산 (판서 예제) {#branch-calc}

**Offset = (Target − (PC + 4)) / 4**, **Target = (PC + 4) + Offset × 4**

6주-2 판서: PC = 108 → PC + 4 = 112, 목표 = 124
```
(124 − 112) / 4 = 3          → beq rs, rt, 3
3 (16-bit) → sign-extend → 0000 … 0011 (32-bit)
shift left 2 → 12
112 + 12 = 124  ✓
```
6주-1 판서: 100번지의 beq, 목표 180 → (180 − 104) / 4 = 76 / 4 = **19**.

- 목표가 위쪽(이전 코드)이면 **음수 오프셋** → sign extension으로 위 비트가 1로 채워짐.

@lesson L4-5 | ALU control | week6 p.27–30 | ALUOp 표 읽기

## ALU의 쓰임과 ALU control 코드 {#alu-uses}

- Load/Store: F = **add** (주소 계산)
- Branch: F = **subtract** (같은지 비교)
- R-type: F는 **funct 필드**에 따라

| ALU control | Function |
|---|---|
| 0000 | AND |
| 0001 | OR |
| 0010 | add |
| 0110 | subtract |
| 0111 | set-on-less-than |
| 1100 | NOR |

> 시험 포인트: 교수님 "이 표는 외울 필요 없다. 시험에 주어진다. 대신 **읽고 회로에 적용**할 줄 알아야 한다." (6주-2 37:31, 어느 표를 가리켰는지는 녹음상 추정)

## ALUOp와 funct로 ALU control 만들기 {#aluop}

2-bit **ALUOp**는 opcode에서 (Main control이) 만들고, ALU control 유닛이 **ALUOp + funct(6 bit)**로 4-bit ALU control을 만든다 (조합 논리).

| opcode | ALUOp | Operation | funct | ALU function | ALU control |
|---|---|---|---|---|---|
| lw | 00 | load word | XXXXXX | add | 0010 |
| sw | 00 | store word | XXXXXX | add | 0010 |
| beq | 01 | branch equal | XXXXXX | subtract | 0110 |
| R-type | 10 | add | 100000 | add | 0010 |
| | | subtract | 100010 | subtract | 0110 |
| | | AND | 100100 | AND | 0000 |
| | | OR | 100101 | OR | 0001 |
| | | set-on-less-than | 101010 | set-on-less-than | 0111 |

- lw/sw/beq는 I-type이라 **funct가 없음** → ALUOp만 보고 결정 (00 → 더하기, 01 → 빼기).
- ALUOp = 10이면 ALU control이 **funct를 기다렸다가** 결정 (add = 32 = 100000).

> 함정: R-type funct들은 전부 `10`으로 시작(100000, 100010, …)해서 R-type ALUOp `10`과 앞 두 비트가 같다. 교수님이 "헷갈리지 말라"고 짚은 부분 (6주-2 42:08).

## K-map으로 구한 ALU control 논리 {#kmap}

ALU control 표를 진리표로 놓고 K-map으로 간단히 하면:
```
Op3 = 0
Op2 = ALUOp0 + ALUOp1·F1
Op1 = ¬ALUOp1 + ¬F2
Op0 = ALUOp1·(F3 + F0)
```
> 함정: 교안 p.30에는 NOT 표시가 빠져서 `Op1 = ALUOp1 + F2`로 적혀 있음 (Op3 줄의 `APUOp0`도 오타). 그대로 쓰면 lw(ALUOp 00)에서 Op1 = 0이 나와 표(0010)와 안 맞는다. 위 식은 표의 8행 전부와 일치하는지 검산한 것.

@lesson L4-6 | Main control unit · 제어 신호 표 | week6 p.31–33 | 제어 신호 표

## 명령어 형식과 제어의 관계 {#main-control}

| | [31:26] | [25:21] | [20:16] | [15:11] | [10:6] | [5:0] |
|---|---|---|---|---|---|---|
| R-type | 0 | rs | rt | rd | shamt | funct |
| Load/Store | 35 or 43 | rs | rt | address (15:0) | | |
| Branch | 4 | rs | rt | address (15:0) | | |

- **opcode** → Control 입력
- **rs: 항상 읽음** (Always read)
- **rt: 읽음, 단 load에서는 쓰기 대상** (read, except for load)
- **rd: R-type에서 쓰기 대상** (write for R-type)… load는 rt에 씀 → RegDst MUX
- **address: sign-extend 후 더함**

## 제어 신호 표 {#control-table}

| 신호 | R-format | lw | sw | beq |
|---|---|---|---|---|
| RegDst | 1 | 0 | X | X |
| ALUSrc | 0 | 1 | 1 | 0 |
| MemtoReg | 0 | 1 | X | X |
| RegWrite | 1 | 1 | 0 | 0 |
| MemRead | 0 | 1 | 0 | 0 |
| MemWrite | 0 | 0 | 1 | 0 |
| Branch | 0 | 0 | 0 | 1 |
| ALUOp1 | 1 | 0 | 0 | 0 |
| ALUOp0 | 0 | 0 | 0 | 1 |

입력(opcode Op5–Op0): R-format 000000, lw 100011 (35), sw 101011 (43), beq 000100 (4).

외우지 말고 **이유로** 맞히기:
- **X가 나오는 곳 = 레지스터에 안 쓰는 명령어(sw, beq)의 RegDst·MemtoReg**. 쓰지 않으니 어떤 레지스터·어떤 데이터든 상관없음.
- ALUSrc = 1 ⇔ 상수(offset)를 쓰는 lw, sw.
- RegWrite = 1 ⇔ 결과를 레지스터에 쓰는 R-type, lw.

## 제어 유닛 회로 (p.33) {#control-logic}

Opcode 비트 6개(Op5–Op0)를 AND 게이트 4개가 각각 **R-format / lw / sw / beq**로 디코딩하고, OR 게이트로 출력 신호를 만든다. 예: ALUSrc = lw OR sw, RegWrite = R-format OR lw. RegDst = R-format, MemtoReg = lw, MemRead = lw, MemWrite = sw, Branch = beq, ALUOp1 = R-format, ALUOp0 = beq.

## lw/sw offset은 상수 (교수님 반복 강조) {#offset-const}

- lw/sw는 **I-type**이라 offset은 반드시 **상수**.
- 시험에서 offset을 레지스터 값으로 준 문장 → **False**.
- 레지스터에 든 offset을 쓰려면: 먼저 base + offset을 계산해서 레지스터에 넣고, `lw $t0, 0($t1)`처럼 **상수 0**을 offset으로.

> 시험 포인트: 3주·4주·6주에 걸쳐 같은 경고. "you can never just provide your offset which is contained inside the register directly into an I-type instruction".
