@unit U4 | Ch.4 The Processor: Datapath and Control (Simplified Version) | week6-수업.pdf
@intro In Week 6-2 the professor said "today's goal is to completely understand this one slide (p.3, the simplified CPU)". The key is which wires the data flows through for each instruction, and whether each MUX gets 0 or 1. After reading the concepts, use the '수업 따라가기' (Follow the Lecture) tab to see the professor's explanation scene by scene, and the '데이터패스 놀이터' (Datapath Playground) to check the path for each instruction.

@lesson L4-1 | Processor Overview · Instruction Execution Steps | week6 p.2–7 | Only these instructions

## Two Implementations and the Instruction Subset {#proc-intro}

- CPU performance factors: Instruction Count, **CPI and Cycle Time** (this unit covers the implementation, which determines CPI and cycle time).
- Two MIPS implementations: **a simplified version (midterm)** and a more realistic pipelined version (final).
- Instructions covered: memory reference `lw, sw` · arithmetic/logical `add, sub, and, or` · control transfer `beq, j` (p.4 also includes `slt`).

> Exam point: The professor said "on the midterm you must use only these instructions. Using any other instruction gets zero points." In class he said "seven instructions", but the slide list is lw, sw, add, sub, and, or, beq, j. The simplified datapath actually covered R-type, lw, sw and beq.

## Instruction Execution Steps {#exec-steps}

1. **PC → instruction memory**, fetch the instruction.
2. **Register numbers → register file**, read the registers.
3. Depending on the instruction class:
   - Use the **ALU** to calculate: the arithmetic result / the **memory address** for load/store / the **branch target address**
   - Access **data memory** for load/store
   - **PC ← branch target address or PC + 4**

An instruction is 1 word = **32 bits = 4 bytes** → to go to the next line, **PC + 4**.

> Trap: In the Week 6-1 recording the professor said "word = 32 bytes"; that was a slip of the tongue. It is 32 **bits** = 4 bytes.

## CPU Overview and Why MUXes Are Needed {#cpu-overview}

p.5 overview: PC → Instruction memory → Registers → ALU → Data memory, plus the PC+4 adder and the branch adder.

p.6: **"Can't just join wires together: Use multiplexers"** — wires from different sources cannot simply be joined, so a selector is needed in 3 places:
1. **PC input**: PC + 4 or the branch target
2. **Second ALU input**: a register value or the instruction's 16-bit constant (sign-extended)
3. **Register write data**: the ALU result or the value read from data memory

p.7: a **Control** unit is added, which generates the MUX select signals, RegWrite, MemRead/MemWrite, the ALU operation, and Branch.

> The professor explained: for R-format, the ALU result is the value we want; but for lw the ALU result is **only an address**, and what we actually want is the memory value at that address. That is why the write-data MUX is needed.

@lesson L4-2 | Logic Design Basics · Clocking | week6 p.8–15 | Reading MUX 0/1

## Information Encoding and Combinational Elements {#comb-elements}

- Information encoded in binary: low voltage = 0, high voltage = 1. **One wire per bit**; multi-bit data is encoded on multi-wire buses (32 bits = 32 wires).
- **Combinational element**: operates on data. **The output is a function of the input only** (no memory).

| Element | Expression |
|---|---|
| AND gate | Y = A & B |
| **Multiplexer** | **Y = S ? I1 : I0** |
| Adder | Y = A + B |
| ALU | Y = F(A, B), F = the function to perform |

The ALU is an extension of the adder. For R-format, F is determined by the lowest 6 bits of the instruction (**funct**).

## How to Read a Multiplexer {#mux-basic}

- Each input wire is numbered (I0, I1).
- **Select line S = 0 → I0, S = 1 → I1**.
- On the exam, **the figure shows which wire is 0 and which is 1**. The professor wrote the 0s and 1s on the board when explaining.

> Exam point: Decide the signal value by **the number written on the MUX**, not by "top/bottom". If the numbers are swapped, the signal is reversed too (Week 6-2: "be extremely careful on what is actually written on the multiplexer").

## Sequential Elements: Registers {#seq-elements}

- **State (sequential) element**: **stores** information.
- **Register**: stores data in a circuit. Uses a **clock** signal to determine when to update the stored value.
- **Edge-triggered**: updates when Clk changes **from 0 to 1 (rising edge)**.
- **Register with write control**: only updates on a clock edge **when the write control input is 1**. Used when the stored value is required later. (The register file's RegWrite is this.)

> Trap: In Week 6-1 the professor said "0 to 1 or 1 to 0", but the slide and the Week 6-2 explanation say **0 → 1**. The exam follows the slide.

## Clocking Methodology {#clocking}

- Combinational logic transforms data during clock cycles (**between clock edges**).
- Input comes from state elements; output goes to a state element.
- **The longest delay determines the clock period**.

@lesson L4-3 | Datapath Elements | week6 p.16–24 | The four MUXes

## Building a Datapath · Instruction Fetch {#fetch}

- **Datapath**: the elements that process data and addresses in the CPU (registers, ALUs, MUXes, memories, …). We build it incrementally for a simple subset of instructions.
- **Instruction fetch**: the **PC (a 32-bit register)** feeds the read address of the instruction memory → the instruction comes out. At the same time the PC goes into an **Add** unit, **+4** → the next instruction address goes back into the PC.

## The R-format Datapath {#r-datapath}

R-format (add, sub, and, or, slt): opcode = 000000, **funct (5:0)** selects the operation.
1. **Read two** register operands (Read register 1 = rs, Read register 2 = rt, 5 bits each)
2. Perform the arithmetic/logical operation (ALU, ALU operation 4 bits)
3. **Write** the result to a register (Write register = rd, Write data, **RegWrite = 1**)

Example `add $t0, $s1, $s2` → op 0 | rs 17 | rt 18 | rd 8 | shamt 0 | funct 32.

## The Load/Store Datapath {#ls-datapath}

1. Read the register operand (rs = base)
2. Calculate the address using the 16-bit offset: use the ALU, but **sign-extend the offset (16 → 32)**
3. **Load**: read memory and update the register (**MemRead = 1, RegWrite = 1**)
4. **Store**: write the register value to memory (**MemWrite = 1**)

Sign extension: fill the upper 16 bits with the constant's sign bit (0 for positive, 1 for negative).

> Trap: At 23:18 in Week 6-1, while explaining lw, the professor said "turn on the memory write field"; that was a slip. lw uses **MemRead** and RegWrite; MemWrite is for sw. He corrected it right after (24:50).

## The Branch Datapath {#br-datapath}

beq:
1. Read the register operands (rs, rt)
2. **Subtract** with the ALU → check the **Zero output** (Zero = 1 if equal)
3. Calculate the target address:
   - **Sign-extend** the displacement (16 bits)
   - **Shift left 2** (word displacement → bytes, ×4)
   - Add to **PC + 4** (PC + 4 was already calculated during instruction fetch)

> Exam point: The branch constant is not an address but **how many lines (instructions) away from (PC + 4)** the target is. It is given in lines rather than bytes because a value not divisible by 4 would cause a serious error.

## Composing the Elements: The Four MUXes {#composing}

- The simplified datapath executes **one instruction in one clock cycle**.
- Each element can do only one function at a time → **separate instruction memory and data memory**.
- A MUX wherever there are two sources:
  1. ALU input: register vs. the instruction's immediate → **ALUSrc**
  2. Register write data: ALU output vs. data memory → **MemtoReg**
  3. Next PC: PC + 4 vs. branch target → **Branch AND Zero** (PCSrc)
  4. Write register number: **Rt vs Rd** → **RegDst**

@lesson L4-4 | Tracing the Full Datapath (R-type · lw · sw · beq) | week6 p.3, p.26, p.34–37 | Signal values and MUX numbers

## Where the Instruction Fields Go {#dp-fields}

Where the 32-bit instruction is split in the p.3 figure:

| Field | Bits | Goes to |
|---|---|---|
| opcode | [31–26] | **Control** |
| rs | [25–21] | Read register 1 (always read) |
| rt | [20–16] | Read register 2 **and** input 0 of the RegDst MUX |
| rd | [15–11] | Input 1 of the RegDst MUX |
| imm | [15–0] | **Sign-extend** (16 → 32) |
| funct | [5–0] | **ALU control** |

## R-type (add $t0, $s1, $s2) {#dp-rtype}

- opcode 000000 → Control outputs the R-type signals.
- Read rs and rt → both ALU inputs are **registers** → **ALUSrc = 0**.
- Write the result to **rd (the third register)** → the RegDst MUX selects [15–11] → **RegDst = 1** (on p.3, input 1 is rd).
- The write data is the **ALU result** → **MemtoReg = 0**. **RegWrite = 1**.
- No memory access → MemRead = MemWrite = 0. Branch = 0. ALUOp = 10 (funct determines the operation).

## lw ($t0, offset($s1)) {#dp-lw}

- Read rs = base, sign-extend the constant offset → the second ALU input is the **constant** → **ALUSrc = 1**.
- The ALU **adds** to compute the address (ALUOp = 00). The ALU result is an **address**, not a value.
- Read data memory → **MemRead = 1**.
- Write the loaded value to a register → **MemtoReg = 1**, **RegWrite = 1**.
- The register written is **rt (the second one)** → **RegDst = 0**.

## sw ($t0, offset($s1)) {#dp-sw}

- Address calculation is the same as lw → **ALUSrc = 1**, ALUOp = 00.
- The value of rt (Read data 2) goes to the data memory's **Write data** → **MemWrite = 1**.
- No register is written → **RegWrite = 0**, so RegDst and MemtoReg are **X (don't care)**.

## beq (rs, rt, offset) {#dp-beq}

- opcode → Control sets **Branch = 1**.
- Compare the two registers by **subtracting** → both ALU inputs are registers → **ALUSrc = 0**, ALUOp = 01 (subtract).
- If equal, ALU **Zero = 1** → **AND(Branch, Zero) = 1** → the PC MUX selects the **branch target (input 1)**. Otherwise 0 → **PC + 4 (input 0)**.
- Branch target: sign-extend the offset → shift left 2 → add to (PC + 4).
- No register write → RegWrite = 0, RegDst = X, MemtoReg = X. No memory access.

## The MUX Number Trap (p.3 MemtoReg) {#mux-trap}

In the p.3 figure, three of the MUXes have **0 on top**, but the rightmost **MemtoReg MUX has 1 on top** (Read data) and **0 on the bottom** (ALU result).

- The professor explained: "0 to select the ALU result, 1 to select the data memory value" → matches the numbers in the figure. Look at the **numbers**, not top/bottom.
- The professor: "if I flip the numbers on your multiplexer … you will have to generate a total opposite signal". If the exam figure swaps the numbers, the answer changes too.

> Exam point: For a MUX question: ① find the input wire you want ② the number written on that wire = the signal value. Do not just write down a memorized table.

## Branch Offset Calculation (board example) {#branch-calc}

**Offset = (Target − (PC + 4)) / 4**, **Target = (PC + 4) + Offset × 4**

Week 6-2 board: PC = 108 → PC + 4 = 112, target = 124
```
(124 − 112) / 4 = 3          → beq rs, rt, 3
3 (16-bit) → sign-extend → 0000 … 0011 (32-bit)
shift left 2 → 12
112 + 12 = 124  ✓
```
Week 6-1 board: beq at address 100, target 180 → (180 − 104) / 4 = 76 / 4 = **19**.

- If the target is above (earlier code), the offset is **negative** → sign extension fills the upper bits with 1s.

@lesson L4-5 | ALU Control | week6 p.27–30 | Reading the ALUOp table

## Uses of the ALU and the ALU Control Codes {#alu-uses}

- Load/Store: F = **add** (address calculation)
- Branch: F = **subtract** (equality test)
- R-type: F depends on the **funct field**

| ALU control | Function |
|---|---|
| 0000 | AND |
| 0001 | OR |
| 0010 | add |
| 0110 | subtract |
| 0111 | set-on-less-than |
| 1100 | NOR |

> Exam point: The professor said "you do not need to memorize this table. It will be given on the exam. But you must be able to **read it and apply it to the circuit**." (Week 6-2 37:31; which table he pointed to is inferred from the recording.)

## Generating ALU Control from ALUOp and funct {#aluop}

The 2-bit **ALUOp** is derived from the opcode (by the Main control), and the ALU control unit uses **ALUOp + funct (6 bits)** to produce the 4-bit ALU control (combinational logic).

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

- lw/sw/beq are I-type, so they **have no funct** → decided by ALUOp alone (00 → add, 01 → subtract).
- When ALUOp = 10, the ALU control **waits for funct** to decide (add = 32 = 100000).

> Trap: All R-type funct codes start with `10` (100000, 100010, …), the same first two bits as the R-type ALUOp `10`. The professor pointed this out: "don't get confused" (Week 6-2 42:08).

## ALU Control Logic from the K-map {#kmap}

Treating the ALU control table as a truth table and simplifying with a K-map gives:
```
Op3 = 0
Op2 = ALUOp0 + ALUOp1·F1
Op1 = ¬ALUOp1 + ¬F2
Op0 = ALUOp1·(F3 + F0)
```
> Trap: Slide p.30 is missing the NOT bars, so it reads `Op1 = ALUOp1 + F2` (and `APUOp0` in the Op3 line is also a typo). Used as written, lw (ALUOp 00) gives Op1 = 0, which does not match the table (0010). The equations above were checked against all 8 rows of the table.

@lesson L4-6 | The Main Control Unit · Control Signal Table | week6 p.31–33 | Control signal table

## Instruction Formats and Control {#main-control}

| | [31:26] | [25:21] | [20:16] | [15:11] | [10:6] | [5:0] |
|---|---|---|---|---|---|---|
| R-type | 0 | rs | rt | rd | shamt | funct |
| Load/Store | 35 or 43 | rs | rt | address (15:0) | | |
| Branch | 4 | rs | rt | address (15:0) | | |

- **opcode** → input to Control
- **rs: always read**
- **rt: read, except for load** (where it is the write destination)
- **rd: write for R-type**… load writes to rt → RegDst MUX
- **address: sign-extend and add**

## The Control Signal Table {#control-table}

| Signal | R-format | lw | sw | beq |
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

Inputs (opcode Op5–Op0): R-format 000000, lw 100011 (35), sw 101011 (43), beq 000100 (4).

Don't memorize; derive each value **from the reason**:
- **X appears in RegDst and MemtoReg of instructions that do not write a register (sw, beq)**. Since nothing is written, which register or which data does not matter.
- ALUSrc = 1 ⇔ lw, sw, which use a constant (offset).
- RegWrite = 1 ⇔ R-type, lw, which write their result to a register.

## The Control Unit Circuit (p.33) {#control-logic}

Four AND gates each decode the 6 opcode bits (Op5–Op0) into **R-format / lw / sw / beq**, and OR gates form the output signals. E.g., ALUSrc = lw OR sw, RegWrite = R-format OR lw. RegDst = R-format, MemtoReg = lw, MemRead = lw, MemWrite = sw, Branch = beq, ALUOp1 = R-format, ALUOp0 = beq.

## The lw/sw Offset Is a Constant (repeated by the professor) {#offset-const}

- lw/sw are **I-type**, so the offset must be a **constant**.
- On the exam, a statement that gives the offset as a register value → **False**.
- To use an offset held in a register: first compute base + offset into a register, then use **constant 0** as the offset, as in `lw $t0, 0($t1)`.

> Exam point: The same warning in Weeks 3, 4 and 6: "you can never just provide your offset which is contained inside the register directly into an I-type instruction".
