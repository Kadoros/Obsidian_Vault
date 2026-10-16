@unit U1 | Ch.1 컴퓨터 개요와 성능 | week1-orientation.pdf · W02 Performance.pdf
@intro 시험은 영어로 쓰고 영어로 답해. 이 단원은 서술형(용어 정의)과 계산형(CPU time · CPI · Amdahl · MIPS)이 반반. 계산 문제는 교수님이 "수업 예제랑 거의 똑같이 나온다"고 했으니 슬라이드 예제를 손으로 다 풀 수 있어야 해.

@lesson L1-1 | 컴퓨터 구성 요소 · 추상화 · ISA | W02 p.2–16 | 구성요소 서술

## 수업 범위와 시험 방식 {#course-info}

- 교재: Computer Organization and Design (MIPS). 하지만 **수업 자료만으로** 출제.
- **모든 수업·시험이 영어. 답도 영어로 써야 함.**
- 평가: 출석(랜덤 호명) 10%, **중간 45%**, 기말 45%. 중간·기말 모두 closed book, 오프라인.
- 중간 범위: Performance → Instructions → Arithmetic → Processor(단순 버전, single-cycle). 파이프라인은 기말.

> 시험 포인트: 중간은 10/20(화) 17:00–19:00. 못 오면 교수님께 이메일.

## 컴퓨터의 종류와 8가지 아이디어 {#classes-ideas}

| 종류 | 목적 | 특징 |
|---|---|---|
| Supercomputer | 고성능 과학·공학 계산 | 성능 지표 **FLOPS** (> MIPS), ~10^17 |
| Server | 네트워크 기반 고성능 처리 | 용량·성능·신뢰성 |
| Personal computer | 범용 | 비용/성능 trade-off |
| Embedded | 시스템 안에 숨어 있음 | 전력·성능·비용 제약이 가장 엄격 |

**Eight Great Ideas**: Design for Moore's Law · Use abstraction to simplify design · **Make the common case fast** · Hierarchy of memories · Dependability via redundancy · Performance via parallelism · Performance via pipelining · Performance via prediction.

## 프로그램 아래의 계층 · 번역 단계 {#below-program}

- **Application software**: 고급 언어(HLL)로 작성 (브라우저, 앱, Office).
- **System software**: **Compiler** (HLL → 기계어, 예: GCC) + **Operating System** (입출력, 메모리·저장장치 관리, 작업 스케줄링·자원 공유).
- **Hardware**: processor, memory, I/O controllers.

번역: `A+B` (HLL) → `add A, B` (assembly, 사람도 읽음) → 이진 machine language.

OS가 앱에 해 주는 것: loading·process creation, **system call**, resource management(메모리·CPU 스케줄링·I/O), IPC, event handling, error handling. 슬라이드 내용을 외울 필요는 없고 "OS가 앱 흐름에서 무엇을 하는지"만.

## 컴퓨터의 구성 요소 {#components}

- **Input/Output**: 사용자 장치(키보드·마우스), 저장 장치(HDD·Flash), **네트워크 어댑터도 I/O** (LAN·Wi-Fi·Bluetooth).
- **Memory**: Primary(RAM: DRAM/SRAM, 휘발성), Secondary(HDD·SSD), **Cache**(작고 빠름, 보통 SRAM). ROM = 비휘발, 부팅용 펌웨어(BIOS).
- **Processor = Datapath + Control unit**
  - **Datapath**: 실제 데이터 처리(산술·논리·메모리 접근). 구성: ALU, Registers, MUX, Buses.
  - **Control unit**: 메모리에서 가져온 명령어를 해석해 **control signals**를 만들어 datapath를 지휘.
- 장치끼리는 **bus**(address bus, data bus, control bus)로 통신.

> 시험 포인트: "Processor의 두 구성 요소와 역할" → Datapath(데이터를 실제로 처리), Control unit(명령어 해석 → 제어 신호 생성).

## 추상화와 ISA {#isa}

**ISA (Instruction Set Architecture)**: 하드웨어와 저수준 소프트웨어 사이의 **인터페이스**. 프로세서가 명령어를 어떻게 해석·실행하는지, 어떤 레지스터가 있는지, 데이터에 어떻게 접근하는지에 대한 **계약(contract)**.

- 개발자가 하드웨어 내부를 몰라도 소프트웨어를 쓸 수 있게 해 줌 (abstraction = hide lower-level detail).
- **Portability**: 하드웨어가 바뀌어도 소프트웨어를 고칠 필요가 없음. 교수님이 가장 중요하다고 한 성질.
- Register = 프로세서 안에 있는 가장 빠른 메모리.

> 한 줄 답안: ISA is the interface between hardware and low-level software; it defines how instructions are executed, which registers exist, and how data is accessed, so software can run without knowing hardware details (portability).

@lesson L1-2 | 성능 정의 · 실행 시간 · 클럭 | W02 p.17–26 | 성능 비교 계산

## 성능을 좌우하는 요소 {#perf-factors}

| 요소 | 영향 |
|---|---|
| Algorithm | 실행할 **연산 수** (예: bubble sort n² vs merge sort n log n) |
| Programming language, compiler, architecture | 연산당 **기계 명령어 수** |
| Processor & memory system | 명령어가 얼마나 빨리 실행되나 |
| I/O system (OS 포함) | I/O 연산이 얼마나 빨리 실행되나 |

**Moore's Law**: IC capacity가 18–24개월마다 두 배. 하지만 전력 제약(power wall) 때문에 성능이 무한히 오르진 않음.

## Response time vs Throughput {#response-throughput}

- **Response time** (= latency = execution time): 한 작업을 끝내는 데 걸리는 시간.
- **Throughput**: 단위 시간당 처리하는 작업량 (tasks/hour).
- 수업에서는 **response time 기준으로 통일**.

## 성능 비교: X is n times faster than Y {#perf-ratio}

`Performance_X = 1 / Execution time_X`

`Performance_X / Performance_Y = Execution time_Y / Execution time_X = n` → "X is n times faster than Y".

예제(슬라이드): 같은 프로그램이 A에서 7s, B에서 21s → Perf_A/Perf_B = 21/7 = **3**, A가 B보다 3배 빠름.

> 함정: 비율을 뒤집지 마. 성능 비 = 시간 비의 **역수**. 교수님이 "많은 학생이 시험에서 이걸 틀린다"고 두 번 강조함.

## Elapsed time · CPU time · Clock {#cpu-time-def}

- **Elapsed time**: 전체 응답 시간 (I/O 대기, OS 오버헤드 포함). 시스템 성능을 보여 주지만 비교용으로는 부정확.
- **CPU time** = user CPU time + system CPU time.
  - **User CPU time**: 우리 프로그램의 명령어를 실제로 실행한 시간 (user mode). **수업에서 execution time = user CPU time.**
  - System CPU time: kernel mode (하드웨어 접근, I/O, 메모리 관리).
- **Clock**: 0→1→0으로 일정 주기로 바뀌는 내부 신호.
  - **Clock period** (cycle time): 한 사이클 길이, 예) 250 ps.
  - **Clock rate** (frequency): 초당 사이클 수, 예) 4.0 GHz = 4.0×10⁹ Hz. **둘은 역수 관계** (4 GHz ↔ 250 ps).

## CPU Time 공식과 예제 {#cpu-time}

`CPU Time = CPU Clock Cycles × Clock Cycle Time = CPU Clock Cycles / Clock Rate`

성능을 올리려면: clock cycle 수를 줄이거나, clock rate를 올림. 둘은 trade-off.

슬라이드 예제: A는 2 GHz에서 10 s. B는 6 s가 목표, 대신 clock cycle이 A의 1.2배.
```
Cycles_A = 10 s × 2×10⁹ Hz = 20×10⁹
Cycles_B = 1.2 × 20×10⁹ = 24×10⁹
Clock rate_B = 24×10⁹ / 6 s = 4×10⁹ Hz = 4 GHz
```

> 시험 포인트: 교수님 말 그대로 "the examples that I provided during class will resemble very much your midterm". 식을 변형해서 모르는 값을 구하는 연습.

@lesson L1-3 | Instruction Count · CPI · 성능 식 | W02 p.27–31 | CPI 계산

## IC · CPI · 세 요소 공식 {#cpi}

- **Instruction Count (IC)**: 프로그램이 실행하는 명령어 수. program, ISA, compiler가 결정.
- **CPI (Cycles Per Instruction)**: 명령어당 평균 클럭 사이클. CPU 하드웨어가 결정. 명령어마다 다르면 평균 CPI.

`Clock Cycles = IC × CPI`

`CPU Time = IC × CPI × Clock Cycle Time = (IC × CPI) / Clock Rate`

슬라이드 예제: A는 cycle 250 ps·CPI 2.0, B는 500 ps·CPI 1.2, 같은 프로그램(IC = I).
```
CPU time_A = I × 2.0 × 250 ps = 500·I ps
CPU time_B = I × 1.2 × 500 ps = 600·I ps
Perf_A / Perf_B = 600I / 500I = 1.2  → A is 1.2 times faster than B
```

> 시험 포인트: 모르는 IC는 변수 I로 두면 비율에서 약분된다. 교수님이 풀이에서 그대로 쓴 방법.

## 가중 평균 CPI {#weighted-cpi}

명령어 클래스마다 CPI가 다르면:

`Clock Cycles = Σ (CPI_i × IC_i)`

`Average CPI = Clock Cycles / IC = Σ CPI_i × (IC_i / IC)` (IC_i / IC = relative frequency)

슬라이드 예제 (CPI: A=1, B=2, C=3):

| | A | B | C | 총 IC | Cycles | 평균 CPI |
|---|---|---|---|---|---|---|
| Sequence 1 | 2 | 1 | 2 | 5 | 2+2+6 = 10 | **2.0** |
| Sequence 2 | 4 | 1 | 1 | 6 | 4+2+3 = 9 | **1.5** |

Sequence 2가 명령어는 더 많지만 사이클은 더 적어서 빠르다.

## 성능 요약표 {#perf-summary}

`CPU Time = (Instructions / Program) × (Clock cycles / Instruction) × (Seconds / Clock cycle)`

| | IC | CPI | Clock rate |
|---|---|---|---|
| Algorithm/Program | ✔ | ✔ | |
| Programming language | ✔ | ✔ | |
| Compiler | ✔ | ✔ | |
| ISA | ✔ | ✔ | |
| Hardware organization | | ✔ | ✔ |
| Technology | | | ✔ |

> 함정: Hardware organization은 CPI와 clock rate에 영향, IC에는 영향 없음. Technology는 clock rate만.

@lesson L1-4 | 전력 · Amdahl · MIPS 함정 · RISC vs CISC | W02 p.32–41 | Amdahl·MIPS 계산

## Power wall {#power}

CMOS: `Power ∝ 1/2 × Capacitive load × Voltage² × Frequency`

예: 새 CPU가 capacitive load 85%, voltage 15%↓, frequency 15%↓ → P_new/P_old = 0.85 × 0.85² × 0.85 = 0.85⁴ ≈ **0.52**.

**Power wall**: 전압을 더 낮출 수 없고, 열을 더 뺄 수 없음 → 단일 프로세서 성능 향상이 막힘 → **multicore** (explicit parallel programming, load balancing 필요). 교수님: 식은 외울 필요 없고 "전력 제약이 있다"는 것만.

## Amdahl's Law {#amdahl}

> Pitfall: 컴퓨터의 한 부분을 개선하면 전체 성능도 그만큼 좋아질 거라고 기대하는 것.

`T_improved = T_affected / improvement factor + T_unaffected`

슬라이드 예제: 100 s 중 곱셈이 80 s. 전체를 5배 빠르게(20 s) 하려면?
```
20 = 80/n + 20  →  80/n = 0  → 불가능
```
곱셈을 무한히 빠르게 해도 나머지 20 s가 병목이라 최대 5배에 그친다. → **Make the common case fast**와 연결.

## MIPS는 성능 지표로 부적절 {#mips-metric}

`MIPS = IC / (Execution time × 10⁶) = Clock rate / (CPI × 10⁶)`

MIPS는 (1) 컴퓨터마다 ISA가 다른 것, (2) 명령어 복잡도 차이를 반영 못 함. IC가 약분돼서 사라짐.

슬라이드 예제 (둘 다 4 GHz):

| | IC | CPI | MIPS | CPU time |
|---|---|---|---|---|
| A | 10 billion | 1.0 | 4000 | 10×10⁹×1.0 / 4×10⁹ = 2.5 s |
| B | 8 billion | 1.1 | ≈3636 | 8×10⁹×1.1 / 4×10⁹ = 2.2 s |

MIPS로는 A가 높지만, **실제로는 B가 빠름** (Perf_A/Perf_B = 2.2/2.5 = 0.88). 그래서 CPU time을 쓴다.

## 기타: SPEC · 유휴 전력 {#spec-idle}

- **SPEC** (Standard Performance Evaluation Corp.): CPU·I/O·Web 등의 표준 벤치마크 세트. SPEC CPU는 I/O가 거의 없는 프로그램의 elapsed time, SPEC Power는 부하 수준별 전력.
- **Fallacy: low power at idle** — i7은 10% 부하에서도 121 W(최대의 47%). 데이터센터는 대부분 10–50% 부하 → 전력이 부하에 비례하도록 설계해야.

## RISC vs CISC {#risc-cisc}

| | RISC | CISC |
|---|---|---|
| 예 | **MIPS**, ARM, PowerPC | **x86, x86-64** (Intel, AMD) |
| 전략 | 단순하고 작은 명령어 집합 | 크고 복잡한 명령어로 프로그램당 명령어 수 최소화 |
| 장점 | 빠른 실행, 전력 효율, 확장성(병렬화 쉬움) | 프로그램 크기 감소, 옛 명령어와 호환 |
| 단점 | 복잡한 작업에 명령어가 더 많이 필요 → 프로그램 커짐 | 느린 실행, 전력 소모 큼 |

MIPS = Microprocessor without Interlocked Pipeline Stages. (성능 지표 MIPS와 이름만 같음!)
