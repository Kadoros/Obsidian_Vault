@unit U1 | Ch.1 Computer Abstractions and Performance | week1-orientation.pdf · W02 Performance.pdf
@intro The exam is written in English and answered in English. This unit is half short-answer (defining terms) and half calculation (CPU time · CPI · Amdahl · MIPS). The professor said the calculation problems will be "almost the same as the class examples", so make sure you can solve every slide example by hand.

@lesson L1-1 | Computer Components · Abstraction · ISA | W02 p.2–16 | Describe the components

## Course Scope and Exam Format {#course-info}

- Textbook: Computer Organization and Design (MIPS). But questions come **only from the lecture materials**.
- **All lectures and exams are in English. You must answer in English too.**
- Grading: attendance (random roll call) 10%, **midterm 45%**, final 45%. Both midterm and final are closed book and offline.
- Midterm scope: Performance → Instructions → Arithmetic → Processor (simplified, single-cycle version). Pipelining is on the final.

> Exam point: The midterm is Tue 10/20, 17:00–19:00. If you cannot attend, email the professor.

## Classes of Computers and the Eight Great Ideas {#classes-ideas}

| Class | Purpose | Characteristics |
|---|---|---|
| Supercomputer | High-end scientific and engineering computation | Measured in **FLOPS** (> MIPS), ~10^17 |
| Server | Network-based, high-performance processing | Capacity, performance, reliability |
| Personal computer | General purpose | Cost/performance trade-off |
| Embedded | Hidden inside a system | Strictest power, performance and cost constraints |

**Eight Great Ideas**: Design for Moore's Law · Use abstraction to simplify design · **Make the common case fast** · Hierarchy of memories · Dependability via redundancy · Performance via parallelism · Performance via pipelining · Performance via prediction.

## Below Your Program · Translation Steps {#below-program}

- **Application software**: written in a high-level language (HLL) (browsers, apps, Office).
- **System software**: **Compiler** (translates HLL into machine code, e.g., GCC) + **Operating System** (handles input/output, manages memory and storage, schedules tasks and shares resources).
- **Hardware**: processor, memory, I/O controllers.

Translation: `A+B` (HLL) → `add A, B` (assembly, still human-readable) → binary machine language.

What the OS does for an application: loading and process creation, **system call**, resource management (memory, CPU scheduling, I/O), IPC, event handling, error handling. You do not need to memorize the slide; just know "what the OS does in the flow of an application".

## Components of a Computer {#components}

- **Input/Output**: user devices (keyboard, mouse), storage devices (HDD, Flash), and **network adapters are also I/O** (LAN, Wi-Fi, Bluetooth).
- **Memory**: Primary (RAM: DRAM/SRAM, volatile), Secondary (HDD, SSD), **Cache** (small and fast, usually SRAM). ROM = non-volatile, holds boot firmware (BIOS).
- **Processor = Datapath + Control unit**
  - **Datapath**: actual data processing (arithmetic, logical, and memory access operations). Components: ALU, Registers, MUX, Buses.
  - **Control unit**: directs the operation of the datapath by interpreting the instructions fetched from memory and generating **control signals**.
- Devices communicate over a **bus** (address bus, data bus, control bus).

> Exam point: "The two components of a processor and their roles" → Datapath (performs the actual data processing), Control unit (interprets instructions → generates control signals).

## Abstraction and ISA {#isa}

**ISA (Instruction Set Architecture)**: the **interface** between hardware and low-level software. A **contract** that specifies how the processor interprets and executes instructions, which registers exist, and how data is accessed.

- Allows developers to write software without needing to understand the detailed inner workings of the hardware (abstraction = hide lower-level detail).
- **Portability**: software does not need to change when the hardware changes. The professor called this the most important property.
- Register = the fastest memory, located inside the processor.

> One-line answer: ISA is the interface between hardware and low-level software; it defines how instructions are executed, which registers exist, and how data is accessed, so software can run without knowing hardware details (portability).

@lesson L1-2 | Defining Performance · Execution Time · Clock | W02 p.17–26 | Performance comparison calculations

## Factors That Affect Performance {#perf-factors}

| Component | What it affects |
|---|---|
| Algorithm | **Number of operations** executed (e.g., bubble sort n² vs merge sort n log n) |
| Programming language, compiler, architecture | Number of **machine instructions per operation** |
| Processor & memory system | How fast instructions are executed |
| I/O system (including OS) | How fast I/O operations are executed |

**Moore's Law**: IC capacity doubles every 18–24 months. But because of power constraints (the power wall), performance cannot rise forever.

## Response Time vs Throughput {#response-throughput}

- **Response time** (= latency = execution time): how long it takes to do a task/job.
- **Throughput**: total work done per unit time (e.g., tasks/hour).
- In this course we **focus on response time**.

## Comparing Performance: X Is n Times Faster Than Y {#perf-ratio}

`Performance_X = 1 / Execution time_X`

`Performance_X / Performance_Y = Execution time_Y / Execution time_X = n` → "X is n times faster than Y".

Example (slide): the same program takes 7 s on A and 21 s on B → Perf_A/Perf_B = 21/7 = **3**, so A is 3 times faster than B.

> Trap: Do not flip the ratio. The performance ratio is the **inverse** of the time ratio. The professor stressed twice that "many students miss this in their midterm exams".

## Elapsed Time · CPU Time · Clock {#cpu-time-def}

- **Elapsed time**: total response time, including all aspects (I/O waits, OS overhead). Determines system performance, but often not good for comparison purposes.
- **CPU time** = user CPU time + system CPU time.
  - **User CPU time**: time spent actually running the instructions of our program (user mode). **In this course, execution time = user CPU time.**
  - System CPU time: kernel mode (hardware access, I/O, memory management).
- **Clock**: an internal signal that toggles 0→1→0 at a fixed period.
  - **Clock period** (cycle time): duration of one clock cycle, e.g., 250 ps.
  - **Clock rate** (frequency): cycles per second, e.g., 4.0 GHz = 4.0×10⁹ Hz. **The two are reciprocals** (4 GHz ↔ 250 ps).

## The CPU Time Formula and Example {#cpu-time}

`CPU Time = CPU Clock Cycles × Clock Cycle Time = CPU Clock Cycles / Clock Rate`

To improve performance: reduce the number of clock cycles or increase the clock rate. There is often a trade-off between the two.

Slide example: A runs in 10 s at 2 GHz. B should run in 6 s, but needs 1.2 times as many clock cycles as A.
```
Cycles_A = 10 s × 2×10⁹ Hz = 20×10⁹
Cycles_B = 1.2 × 20×10⁹ = 24×10⁹
Clock rate_B = 24×10⁹ / 6 s = 4×10⁹ Hz = 4 GHz
```

> Exam point: In the professor's own words, "the examples that I provided during class will resemble very much your midterm". Practice rearranging the formula to solve for the unknown.

@lesson L1-3 | Instruction Count · CPI · The Performance Equation | W02 p.27–31 | CPI calculations

## IC · CPI · The Three-Factor Formula {#cpi}

- **Instruction Count (IC)**: number of instructions a program executes. Determined by the program, the ISA and the compiler.
- **CPI (Cycles Per Instruction)**: average number of clock cycles per instruction. Determined by the CPU hardware. If instructions have different CPIs, use the average CPI.

`Clock Cycles = IC × CPI`

`CPU Time = IC × CPI × Clock Cycle Time = (IC × CPI) / Clock Rate`

Slide example: A has cycle time 250 ps and CPI 2.0, B has 500 ps and CPI 1.2, same program (IC = I).
```
CPU time_A = I × 2.0 × 250 ps = 500·I ps
CPU time_B = I × 1.2 × 500 ps = 600·I ps
Perf_A / Perf_B = 600I / 500I = 1.2  → A is 1.2 times faster than B
```

> Exam point: If the IC is unknown, call it I; it cancels out in the ratio. This is exactly the method the professor used.

## Weighted Average CPI {#weighted-cpi}

If different instruction classes have different CPIs:

`Clock Cycles = Σ (CPI_i × IC_i)`

`Average CPI = Clock Cycles / IC = Σ CPI_i × (IC_i / IC)` (IC_i / IC = relative frequency)

Slide example (CPI: A=1, B=2, C=3):

| | A | B | C | Total IC | Cycles | Avg. CPI |
|---|---|---|---|---|---|---|
| Sequence 1 | 2 | 1 | 2 | 5 | 2+2+6 = 10 | **2.0** |
| Sequence 2 | 4 | 1 | 1 | 6 | 4+2+3 = 9 | **1.5** |

Sequence 2 executes more instructions but fewer cycles, so it is faster.

## Performance Summary Table {#perf-summary}

`CPU Time = (Instructions / Program) × (Clock cycles / Instruction) × (Seconds / Clock cycle)`

| | IC | CPI | Clock rate |
|---|---|---|---|
| Algorithm/Program | ✔ | ✔ | |
| Programming language | ✔ | ✔ | |
| Compiler | ✔ | ✔ | |
| ISA | ✔ | ✔ | |
| Hardware organization | | ✔ | ✔ |
| Technology | | | ✔ |

> Trap: Hardware organization affects CPI and clock rate, but not IC. Technology affects only the clock rate.

@lesson L1-4 | Power · Amdahl · The MIPS Pitfall · RISC vs CISC | W02 p.32–41 | Amdahl and MIPS calculations

## The Power Wall {#power}

CMOS: `Power ∝ 1/2 × Capacitive load × Voltage² × Frequency`

Example: a new CPU has 85% of the capacitive load, 15% lower voltage and 15% lower frequency → P_new/P_old = 0.85 × 0.85² × 0.85 = 0.85⁴ ≈ **0.52**.

**Power wall**: we cannot reduce the voltage further and cannot remove more heat → single-processor performance improvement stalls → **multicore** (requires explicit parallel programming and load balancing). The professor said you do not need to memorize the formula; just know that "power is constrained".

## Amdahl's Law {#amdahl}

> Pitfall: Expecting the improvement of one aspect of a computer to increase overall performance by a proportional amount.

`T_improved = T_affected / improvement factor + T_unaffected`

Slide example: of 100 s, multiplication takes 80 s. How much must multiplication improve to make the whole program 5 times faster (20 s)?
```
20 = 80/n + 20  →  80/n = 0  → impossible
```
Even with infinitely fast multiplication, the remaining 20 s is the bottleneck, so the speedup is capped at 5×. → Connects to **Make the common case fast**.

## MIPS Is a Poor Performance Metric {#mips-metric}

`MIPS = IC / (Execution time × 10⁶) = Clock rate / (CPI × 10⁶)`

MIPS does not account for (1) differences in ISA between computers or (2) differences in instruction complexity. The IC cancels out and disappears.

Slide example (both 4 GHz):

| | IC | CPI | MIPS | CPU time |
|---|---|---|---|---|
| A | 10 billion | 1.0 | 4000 | 10×10⁹×1.0 / 4×10⁹ = 2.5 s |
| B | 8 billion | 1.1 | ≈3636 | 8×10⁹×1.1 / 4×10⁹ = 2.2 s |

A has the higher MIPS, but **B is actually faster** (Perf_A/Perf_B = 2.2/2.5 = 0.88). That is why we use CPU time.

## Other: SPEC · Power at Idle {#spec-idle}

- **SPEC** (Standard Performance Evaluation Corp.): standard benchmark suites for CPU, I/O, Web, etc. SPEC CPU measures the elapsed time of programs with negligible I/O; SPEC Power measures power at different load levels.
- **Fallacy: low power at idle** — an i7 draws 121 W (47% of peak) even at 10% load. Data centers mostly run at 10–50% load → processors should be designed so that power is proportional to load.

## RISC vs CISC {#risc-cisc}

| | RISC | CISC |
|---|---|---|
| Examples | **MIPS**, ARM, PowerPC | **x86, x86-64** (Intel, AMD) |
| Strategy | Simple, small instruction set | Large, complex instructions that minimize instructions per program |
| Advantages | Fast execution, power efficiency, scalability (easy to parallelize) | Smaller programs, compatibility with old instructions |
| Disadvantages | Complex tasks need more instructions → larger programs | Slower execution, higher power consumption |

MIPS = Microprocessor without Interlocked Pipeline Stages. (Same name as the MIPS performance metric, nothing else in common!)
