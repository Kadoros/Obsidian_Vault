@unit U2 | Ch.2 Instructions: Language of the Computer (MIPS) | W02 p.41 · week3-수업.pdf · week4-수업.pdf p.2–5
@intro The biggest chunk of the exam. The announced format is "given an instruction and a description, fill in the blank or write the MIPS expression". This unit has many rules the professor warned would get zero points, so be sure to read the Trap boxes.

@lesson L2-1 | Arithmetic Instructions · Register Operands | week3 p.3–8 | C → MIPS translation

## Classes of MIPS Instructions {#mips-classes}

MIPS: a RISC ISA from Stanford, with a large share of the embedded market; typical of many modern ISAs.

- **By type**: Arithmetic · Memory (Data Transfer) · Logical · Conditional · Branch/Jump · Floating Point · Pseudo
- **By format**: **R-format · I-format · J-format** · FP format

## Arithmetic Instruction Format {#arith-format}

`add a, b, c   # a = b + c`

- **One destination + two sources**. All arithmetic instructions have this form.
- **Design Principle 1: Simplicity favors regularity** — regularity makes implementation simpler; simplicity enables higher performance at lower cost.

Slide example:
```
a = b + c + d;          f = (g + h) - (i + j);
add a, b, c             add t0, g, h
add a, a, d             add t1, i, j
                        sub f, t0, t1
```
> Trap: The result must go into **the variable the user asked for** (here, f). The professor stressed "must be very careful at this term".

## Register Operands {#registers}

- Arithmetic instructions use **register operands only**. A register is a special storage location inside the processor.
- MIPS has **32 × 32-bit registers** (numbered 0–31). 32-bit = word size (the standard when MIPS was designed, kept in MIPS64 for compatibility).
- Assembler names: `$t0–$t9` (temporaries), `$s0–$s7` (saved).
- **Design Principle 2: Smaller is faster** — we design very small registers for faster operations on frequently accessed data.

Slide example (f, g, h, i, j in $s0–$s4):
```
add $t0, $s1, $s2     # g + h
add $t1, $s3, $s4     # i + j
sub $s0, $t0, $t1     # f = (g+h) - (i+j)
```
> Trap: An operation's result cannot go directly to memory. It is always stored **in a register**. (This slide had an add/sub typo, which the professor corrected in class: "change this into subtraction".)

@lesson L2-2 | Memory Operands · Endianness · lw/sw | week3 p.10–14 | lw/sw offsets

## Memory Basics {#memory-basics}

- Main memory is used for **composite data** such as arrays, structures and dynamic data. There are too few registers to hold every variable.
- Before an arithmetic operation, **load** (memory → register); afterwards, **store** (register → memory).
- **Byte addressed**: each address identifies one 8-bit byte.
- **Words are aligned**: the address of a word (32-bit) must be a **multiple of 4**.
- Address of an array element = base address + index × 4 (int array).

## Big Endian vs Little Endian {#endian}

- **Big endian**: the MSB (most significant byte) is stored at the **lowest memory address**.
- **Little endian**: the LSB (least significant byte) is stored at the **lowest memory address**.

0x12345678 stored at addresses 0–3:

| Address | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Big endian | 12 | 34 | 56 | 78 |
| Little endian | 78 | 56 | 34 | 12 |

> Trap: Two hex digits are **1 byte**. Even in little endian, do not reverse the two digits inside a byte (writing 78 as 87 is wrong). The professor stressed this twice.

## lw / sw {#lw-sw}

`lw dest, offset(base)`  ·  `sw src, offset(base)`

- Three operands: a register, an **offset (constant, in bytes)**, and a base address (register).
- In sw the first register is the **source** (the value written to memory).

Slide example 1: `g = h + A[8];` (g:$s1, h:$s2, base of A:$s3)
```
lw  $t0, 32($s3)      # offset = 8 × 4 = 32
add $s1, $s2, $t0
```
Slide example 2: `A[12] = h + A[8];`
```
lw  $t0, 32($s3)
add $t0, $s2, $t0
sw  $t0, 48($s3)      # 12 × 4 = 48
```

> Trap: **The offset must be a constant.** Putting a register in the offset position gets **zero points** even if the logic is right, and in a True/False question it is always False. If the index is a variable, compute the address first (`sll`, `add`), then use `lw $t0, 0($t1)`.

## Registers vs Memory {#reg-vs-mem}

- Registers are much faster than memory and easier to use.
- Operating on memory data requires loads and stores → more instructions executed.
- The compiler must use registers for variables as much as possible and only **spill** to memory for less frequently used variables. Register optimization is important for efficiency.

@lesson L2-3 | Constants · Two's Complement · Sign Extension · Hexadecimal | week3 p.15–23 | Two's complement and sign extension

## Immediate Operands and $zero {#immediate}

`addi $s3, $s3, 4` — the constant is placed directly in the instruction.

- **There is no subtract immediate** → use addi with a negative constant: `addi $s2, $s1, -1`.
- **Design Principle 3: Make the common case fast** — small constants are common, and an immediate operand avoids a load instruction.
- **$zero (register 0)** = always the constant 0, **cannot be overwritten**.
- Copying a register (move): `add $t2, $s1, $zero`

> Trap: A copy is **`add` + `$zero`**. Using `addi` with `$zero` (a register) as if it were the constant gets zero points (the professor, Week 4-2). `$zero` is a register, not a constant.

## Unsigned and Two's Complement {#twos}

- **Unsigned** n-bit: `x = x_{n-1}2^{n-1} + … + x_0 2^0`, range **0 to 2ⁿ − 1** (32-bit max 4,294,967,295).
- **2's complement** n-bit: `x = −x_{n-1}2^{n-1} + x_{n-2}2^{n-2} + … + x_0 2^0`, range **−2^{n−1} to 2^{n−1} − 1**.
  - bit 31 = sign bit (1 = negative, 0 = non-negative). Non-negative numbers have the same representation as unsigned.
  - `1111…1111` = −1, `1000…0000` = −2,147,483,648, `0111…1111` = 2,147,483,647.

## Signed Negation: Complement and Add 1 {#negation}

Since `x + x̄ = 1111…1111₂ = −1`, we get `x̄ + 1 = −x`.

Example: +2 = `0000 … 0010` → invert `1111 … 1101` → +1 → `1111 … 1110` = −2.

Class example: −10 (32-bit)
```
+10 = 0000 0000 0000 0000 0000 0000 0000 1010
inv = 1111 1111 1111 1111 1111 1111 1111 0101
 +1  = 1111 1111 1111 1111 1111 1111 1111 0110   (= 0xFFFFFFF6)
```

## Sign Extension {#sign-ext}

Representing a number using more bits while **preserving its value**: **replicate the sign bit to the left**.

- Used in MIPS by: `addi` (extends the immediate), `lb`·`lh` (extend the loaded byte/halfword), **`beq`·`bne` (extend the displacement)**.
- 8-bit → 16-bit: +2 = `0000 0010` → `0000 0000 0000 0010`, −2 = `1111 1110` → `1111 1111 1111 1110`.

> Trap: Slide p.21 shows the extended −2 as `1111 1111 1000 0010`; that is a **typo**. The correct value is `1111 1111 1111 1110`.

## Hexadecimal {#hex}

One hex digit = 4 bits. Table: 0=0000 … 9=1001, a=1010, b=1011, c=1100, d=1101, e=1110, f=1111.

Example: `eca8 6420` → `1110 1100 1010 1000 0110 0100 0010 0000`

@lesson L2-4 | Instruction Encoding: R-format · I-format | week3 p.22–28 | Instruction → binary/hex

## Representing Instructions {#encoding-basics}

- Instructions are encoded as **32-bit binary numbers (machine code)**. Keep the number of formats small → **regularity**.
- **opcode**: the first 6 bits. It tells which format the instruction has, so the rest can be interpreted.
- Register numbers: `$t0–$t7` = 8–15, `$s0–$s7` = 16–23, `$t8–$t9` = 24–25 (others: $zero 0, $v0–$v1 2–3, $a0–$a3 4–7, $gp 28, $sp 29, $fp 30, $ra 31).

## R-format {#r-format}

| op | rs | rt | rd | shamt | funct |
|---|---|---|---|---|---|
| 6 bits | 5 | 5 | 5 | 5 | 6 bits |

- **op = always 0** (the funct field selects the operation).
- rs: first source register, rt: second source register, **rd: destination register**, shamt: shift amount (0 for now), funct: function code (extends the opcode).
- funct values are **given** in the exam (no need to memorize). For reference: add 32, sub 34, and 36, or 37, slt 42.

Example: `add $t0, $s1, $s2`
```
op      rs     rt     rd     shamt  funct
000000  10001  10010  01000  00000  100000
0       17     18     8      0      32
= 0000 0010 0011 0010 0100 0000 0010 0000₂ = 0x02324020
```

> Trap: Assembly order is **dest, src, src**, but machine code order is **rs, rt, rd** (sources first, destination last). The professor stressed this in both Week 3 and Week 6.

## I-format {#i-format}

| op | rs | rt | constant or address |
|---|---|---|---|
| 6 bits | 5 | 5 | 16 bits |

- Immediate arithmetic and load/store. **rt = destination (lw, addi) or source (sw)**.
- constant: −2¹⁵ to +2¹⁵ − 1. address: an offset added to the base address in rs.
- Examples: addi, lw, sw, beq, bne, slti, andi, ori, lui. Opcodes for reference: lw 35, sw 43, beq 4, bne 5, addi 8.
- **Design Principle 4: Good design demands good compromises** — different formats complicate decoding, but allow all instructions to be 32 bits uniformly. Keep formats as similar as possible.

## Encoding Example: A[300] = h + A[300] {#encode-example}

`$t1` = base of A, `$s2` = h.
```
lw  $t0, 1200($t1)     # 300 × 4 = 1200
add $t0, $s2, $t0
sw  $t0, 1200($t1)
```

| Instruction | op | rs | rt | rd | shamt | funct / address |
|---|---|---|---|---|---|---|
| lw | 35 | 9 | 8 | | | 1200 |
| add | 0 | 18 | 8 | 8 | 0 | 32 |
| sw | 43 | 9 | 8 | | | 1200 |

Binary: lw = `100011 01001 01000 0000 0100 1011 0000`; sw differs only in op, `101011`.

@lesson L2-5 | Logical Operations · Conditional Branches · if/while | week3 p.30–40 · week4 p.2 | Compiling if and while

## Shift Operations {#shift}

| Operation | C | Java | MIPS |
|---|---|---|---|
| Shift left | << | << | **sll** |
| Shift right | >> | >>> | **srl** |
| Bitwise AND/OR/NOT | & \| ~ | & \| ~ | and, andi / or, ori / **nor** |

- The number of positions to shift goes in the R-format **shamt** field.
- **sll by i** = multiply by 2^i (fills the right with 0s). **srl by i** = divide by 2^i, **unsigned only**.

> Trap: srl fills the left with 0s, so using it on a negative (two's complement) number destroys the sign (the professor: "you should not just perform this operation on a signed number").

## AND · OR · NOR {#and-or-nor}

- **AND**: masking. Keeps the selected bits and clears the rest to 0.
- **OR**: sets the selected bits to 1 and leaves the rest unchanged.
- MIPS has no **NOT** → use **3-operand NOR**: `nor $t0, $t1, $zero` = NOT $t1.

Example ($t1 = 0…0011 1100 0000 0000, $t2 = 0…0000 1101 1100 0000):
- `and $t0,$t1,$t2` → 0…0000 1100 0000 0000
- `or $t0,$t1,$t2` → 0…0011 1101 1100 0000

## Branch Instructions {#branch-instr}

- `beq rs, rt, L1`: if rs == rt, branch to L1.
- `bne rs, rt, L1`: if rs != rt, branch to L1.
- `j L1`: unconditional jump to L1.

## Compiling if-else {#if-else}

`if (i == j) f = g + h; else f = g - h;` (f, g, h, i, j = $s0–$s4)
```
      bne $s3, $s4, Else    # if i != j, go to Else
      add $s0, $s1, $s2     # f = g + h
      j   Exit
Else: sub $s0, $s1, $s2     # f = g - h
Exit:
```
The trick is to test the **opposite** condition and skip to Else (if i == j, bne is not taken, so the if-block runs).

## Compiling a while Loop {#while-loop}

`while (save[i] == k) i += 1;` (i: $s3, k: $s5, base of save: $s6)
```
Loop: sll  $t1, $s3, 2      # t1 = i * 4
      add  $t1, $t1, $s6    # t1 = &save[i]
      lw   $t0, 0($t1)      # t0 = save[i]
      bne  $t0, $s5, Exit   # exit if save[i] != k
      addi $s3, $s3, 1      # i += 1
      j    Loop
Exit:
```
> Trap: Because the index i is a variable, you might want to write `lw $t0, $t1($s6)`, but that is **not allowed**. Compute the address first and use offset 0. In True/False, "a register as the offset" = False.

## slt / slti / sltu {#slt}

- `slt rd, rs, rt`: if rs < rt then rd = 1, else 0.
- `slti rt, rs, constant`: if rs < constant then rt = 1.
- Combined with beq/bne, they build every comparison (==, !=, <, <=, >, >=).
```
slt $t0, $s1, $s2       # $t0 = 1 if $s1 < $s2
bne $t0, $zero, L       # branch to L if 1 != 0
```
- **Signed vs Unsigned**: slt/slti = signed, sltu/sltiu = unsigned.
  With $s0 = 1111…1111 and $s1 = 0000…0001: `slt` → −1 < +1 → $t0 = 1; `sltu` → 4,294,967,295 > 1 → $t0 = 0.

## Why There Is No blt or bge {#branch-design}

- In hardware, < and > comparisons are slower than = and ≠.
- Combining them with a branch means more work per instruction → **slower clock → every instruction is penalized**.
- A good compromise: **beq, bne** + slt. (`blt` is an assembler pseudo-instruction that becomes `slt` + `bne`.)

@lesson L2-6 | Procedure Calls · The Stack | week3 p.42–51 · week4 p.2–5 | Stack save/restore order

## Procedure Call Steps · jal / jr {#jal-jr}

1. Place parameters in registers → 2. Transfer control to the procedure → 3. Acquire storage → 4. Perform the operations → 5. Place the result in a register → 6. Return to the place of the call.

- `jal ProcedureLabel` (jump-and-link): **stores the address of the next instruction (PC+4) in $ra** and jumps to the target.
- `jr $ra` (jump register): copies $ra into the PC → return. Also used for computed jumps.
- PC: the register holding the address of the instruction currently being executed.

Example: `jal` at address 100, function at address 388 → $ra = 104, PC = 388. The `jr $ra` at the end of the function returns to 104.

## Register Usage Conventions and the Stack {#reg-usage}

| Register | Number | Use |
|---|---|---|
| $a0–$a3 | 4–7 | Arguments |
| $v0, $v1 | 2–3 | Result values |
| $t0–$t9 | 8–15, 24–25 | Temporaries (**not preserved**) |
| $s0–$s7 | 16–23 | Saved (**callee saves and restores**) |
| $gp / $sp / $fp / $ra | 28 / 29 / 30 / 31 | global ptr / **stack ptr** / frame ptr / **return address** |

- **Stack**: a data structure for spilling registers, organized as a last-in-first-out (LIFO) queue. **$sp** holds the most recently allocated address in the stack.
- **The stack grows "down"** (from high memory address to low memory address): allocate space with `addi $sp, $sp, -N`.
- Procedure frame (activation record): local data allocated by the callee.

## Leaf Procedure Example {#leaf}

A procedure that does not call other procedures. `int leaf_example(int g, h, i, j) { int f; f = (g+h) - (i+j); return f; }` (arguments in $a0–$a3, f in $s0)
```
leaf_example:
  addi $sp, $sp, -4      # space for one int (4 bytes)
  sw   $s0, 0($sp)       # save original $s0
  add  $t0, $a0, $a1     # g + h
  add  $t1, $a2, $a3     # i + j
  sub  $s0, $t0, $t1     # f
  add  $v0, $s0, $zero   # copy result to $v0
  lw   $s0, 0($sp)       # restore $s0
  addi $sp, $sp, 4
  jr   $ra
```

## Non-leaf (Recursive) Example: fact {#nonleaf}

A procedure that calls another procedure must save **$ra and any arguments needed afterwards** on the stack before the call, and restore them after the call.
```
fact:
  addi $sp, $sp, -8      # 2 slots: argument, return address
  sw   $ra, 4($sp)
  sw   $a0, 0($sp)
  slti $t0, $a0, 1       # n < 1 ?
  beq  $t0, $zero, L1    # if not, go to L1
  addi $v0, $zero, 1     # return 1
  addi $sp, $sp, 8
  jr   $ra
L1:
  addi $a0, $a0, -1      # n - 1
  jal  fact
  lw   $a0, 0($sp)       # restore from the same slot it was saved in
  lw   $ra, 4($sp)
  addi $sp, $sp, 8
  mul  $v0, $a0, $v0     # n * fact(n-1)
  jr   $ra
```
> Trap: **The offset you save to and the offset you restore from must match.** If you saved the argument at 0 and $ra at 4, restore them the same way. Restoring them in the opposite order gets zero points (the professor, Week 4-1).

> Trap: The C code on the Week 3 slide has a typo, `return f`. It is corrected to `return 1` on the Week 5 slide.

## Tracing the Stack for fact(3) {#fact-trace}

Caller: `jal fact` at address 100 → $ra = 104, $a0 = 3. Initial $sp = 500.

| Step | $sp | Saved at 0($sp) | Saved at 4($sp) |
|---|---|---|---|
| Enter fact(3) | 492 | a0 = 3 | ra = 104 |
| Enter fact(2) | 484 | a0 = 2 | ra = L1+8 |
| Enter fact(1) | 476 | a0 = 1 | ra = L1+8 |
| Enter fact(0) | 468 | a0 = 0 | ra = L1+8 |

fact(0): slti → 0 < 1, so $t0 = 1 → beq not taken → $v0 = 1, $sp = 476, jr → L1+8.
On the way back, each `lw` restores a0 to 1, 2, 3 and $v0 goes 1 → 1 → 2 → 6. The last jr returns to **104**.

> Trap: In `slti $t0, $a0, 1`, when a0 = 1, 1 < 1 is false → $t0 = 0 (recursion continues). This is the spot where the professor said "be extremely careful".

## Stack Size by Argument Type (as taught by the professor) {#stack-size}

- One int argument + $ra → 4 + 4 = **8 bytes**.
- **As the professor explained**: each char argument takes 1 byte. E.g., two char arguments + $ra → 4 + 1 + 1 = **6 bytes**; three chars → 4 + 3 = 7.
- If the value being saved is an int, you still move by 4 even when handling a char array (in strcpy the saved value is int i).

> Caution: Real MIPS compilers usually round up to a multiple of 4 for alignment, but this is how it was explained in class. On the exam, follow the class rule.

## Byte Operations · strcpy {#byte-ops}

- `lb rt, offset(rs)` / `lh`: sign-extend to 32 bits. `lbu` / `lhu`: zero-extend.
- `sb` / `sh`: store just the rightmost byte/halfword.

`void strcpy(char x[], char y[])` (addresses of x, y in $a0, $a1; i in $s0)
```
strcpy:
  addi $sp, $sp, -4
  sw   $s0, 0($sp)
  add  $s0, $zero, $zero   # i = 0
L1: add  $t1, $s0, $a1     # &y[i]  (char, so no ×4)
  lbu  $t2, 0($t1)
  add  $t3, $s0, $a0       # &x[i]
  sb   $t2, 0($t3)
  beq  $t2, $zero, L2      # stop at '\0'
  addi $s0, $s0, 1
  j    L1
L2: lw   $s0, 0($sp)
  addi $sp, $sp, 4
  jr   $ra
```
> Trap: Elements of a char array are 1 byte, so **do not multiply by 4 with sll**. This is the difference from an int array.

@lesson L2-7 | Addressing · 32-bit Constants · Translating and Linking | week3 p.49–67 | Branch address calculation

## 32-bit Constants: lui + ori {#lui-ori}

Most constants fit in a 16-bit immediate. When a 32-bit constant is occasionally needed:

- `lui rt, constant`: copies the 16-bit constant into the **upper 16 bits** of rt and clears the lower 16 bits to 0.
- Fill the lower 16 bits with **ori** (do not use addi, because of sign extension).
```
lui $s0, 61          # 0000 0000 0111 1101 0000 0000 0000 0000
ori $s0, $s0, 2304   # 0000 0000 0111 1101 0000 1001 0000 0000
```

## Branch Addressing (PC-relative) {#branch-addr}

| op | rs | rt | constant or address (16) |
|---|---|---|---|

- beq/bne are I-format. Most branch targets are near the branch (loops, ifs).
- **Target address = (PC + 4) + offset × 4**
- The offset is the **difference in number of instructions (words)**, signed → range **±2¹⁵ words** (= ±2¹⁷ bytes).
- If the target is too far, the assembler rewrites the branch by inverting the condition and using j:
```
beq $s0, $s1, L1      →      bne $s0, $s1, L2
                             j   L1
                         L2: …
```

> Exam point: In Week 6 the professor explained it again on the board: offset = (target − (PC + 4)) / 4. E.g., PC 108, target 124 → (124 − 112)/4 = **3**. (The Week 4-2 preview was rough; the Week 6 explanation is the exact rule.)

## Jump Addressing (J-format) {#jump-addr}

| op (6) | address (26) |
|---|---|

- j, jal: the target can be anywhere in the text segment → encode the absolute address.
- (Pseudo) direct jump addressing: **Target = address × 4** (upper 4 bits come from the PC). Range 2²⁶ words = 2²⁸ bytes.
- `jr`: the full 32-bit address is in a register → R-format.

Slide example (Loop at address 80000):
```
80000 Loop: sll  $t1,$s3,2     0  0 19  9 2  0
80004       add  $t1,$t1,$s6   0  9 22  9 0 32
80008       lw   $t0,0($t1)   35  9  8   0
80012       bne  $t0,$s5,Exit  5  8 21   2      → (80012+4) + 2×4 = 80024 = Exit
80016       addi $s3,$s3,1     8 19 19   1
80020       j    Loop          2   20000        → 20000 × 4 = 80000 = Loop
80024 Exit:
```

## Addressing Mode Summary {#addr-modes}

1. Immediate (addi), 2. Register (add, jr), 3. Base/displacement (**lw, sw**), 4. PC-relative (**beq, bne**), 5. Pseudo-direct (**j, jal**).

## Pseudo-instructions · Translation · Linking {#translate}

- **Pseudo-instruction**: "figments of the assembler's imagination" that the assembler turns into real instructions. `move $t0,$t1` → `add $t0,$zero,$t1`, `blt $t0,$t1,L` → `slt $at,$t0,$t1` + `bne $at,$zero,L`.
- Object module: header, text segment, static data, relocation info, symbol table, debug info.
- **Linker**: merges segments → resolves label addresses → patches location-dependent and external references → executable.
- **Loader**: reads the header → creates the virtual address space → copies text and data → puts arguments on the stack → initializes registers ($sp, $fp, $gp) → jumps to the startup routine.
- **Dynamic linking**: link/load a library procedure only when it is called. Requires relocatable code; avoids image bloat; automatically picks up new library versions.
- **Memory layout**: Text (code) → Static data (globals, $gp) → Dynamic data (heap, malloc) → Stack (automatic storage).

## Fallacies and Design Principles Summary {#fallacies}

- Fallacy: powerful instructions = higher performance (complex instructions are hard to implement and may slow down even the simple ones).
- Fallacy: use assembly code for high performance (modern compilers do better).
- x86 never changes its instruction set, it only keeps adding (backward compatibility).
- **The four design principles**: 1. Simplicity favors regularity, 2. Smaller is faster, 3. Make the common case fast, 4. Good design demands good compromises.
