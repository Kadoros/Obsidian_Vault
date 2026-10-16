from qdsl import Q
# ───────── U1 컴퓨터 개요와 성능 ─────────

Q("1-ci-1","course-info","mc","이 수업의 중간·기말 답안 작성 언어는?",1,choices=["한국어만","영어만","한국어·영어 자유","시험지에 따라 다름"],explain="모든 수업·시험이 영어, 답도 영어로 (01주-1).")
Q("1-ci-2","course-info","ox","중간고사 범위에는 파이프라인 구현이 포함된다.",False,explain="중간 = 단순(single-cycle) 버전까지. 파이프라인은 기말.")
Q("1-ci-3","course-info","blank","평가 비율: 출석 (a)%, 중간 (b)%, 기말 45%",["10","45"],accept=[["10"],["45"]])

Q("1-cl-1","classes-ideas","mc","슈퍼컴퓨터의 성능 지표로 슬라이드가 든 것은?",2,choices=["MIPS","CPI","FLOPS","Clock rate"],explain="FLOPS(floating-point operations per second) > MIPS.")
Q("1-cl-2","classes-ideas","mc","전력·성능·비용 제약이 가장 엄격한 컴퓨터 종류는?",3,choices=["Supercomputer","Server","Personal computer","Embedded computer"])
Q("1-cl-3","classes-ideas","mc","Eight Great Ideas에 들어가지 '않는' 것은?",2,choices=["Make the common case fast","Performance via pipelining","Smaller is faster","Hierarchy of memories"],explain="'Smaller is faster'는 MIPS 설계 원칙 2. 8가지 아이디어엔 없음.")

Q("1-bp-1","below-program","mc","System software에 속하는 두 가지는?",1,choices=["Web browser와 Compiler","Compiler와 Operating System","OS와 Processor","Assembler와 Memory"])
Q("1-bp-2","below-program","ox","Assembly language는 사람이 읽을 수 있으면서 기계어와 거의 일대일로 대응하는 언어다.",True)

Q("1-co-1","components","mc","Processor를 구성하는 두 요소는?",0,choices=["Datapath와 Control unit","ALU와 Memory","Register와 Cache","Bus와 I/O"])
Q("1-co-2","components","ox","LAN·Wi-Fi 같은 네트워크 어댑터는 I/O 장치에 포함된다.",True,explain="교수님: 많이 헷갈리는 부분.")
Q("1-co-3","components","short","Processor의 두 구성 요소를 쓰고 각각의 역할을 한 줄로 설명하시오. (영어로)",
  "Datapath: performs the actual data processing (arithmetic, logical, and memory access operations) using ALU, registers, MUXes and buses.\nControl unit: interprets (decodes) instructions fetched from memory and generates control signals that direct the datapath.",
  keys=["Datapath: actual data processing (arithmetic/logical/memory access)","Control unit: interprets instructions","generates control signals for the datapath"])
Q("1-co-4","components","mc","RAM과 ROM에 대한 설명으로 옳은 것은?",2,choices=["RAM은 비휘발성, ROM은 휘발성","둘 다 휘발성","RAM은 휘발성, ROM은 부팅용 펌웨어를 저장하는 비휘발성","캐시는 보통 DRAM으로 만든다"],explain="캐시는 보통 SRAM.")

Q("1-isa-1","isa","short","ISA(Instruction Set Architecture)란 무엇이며 가장 중요한 이점은? (영어로)",
  "ISA is the interface (contract) between hardware and low-level software: it defines how instructions are executed, which registers are available, and how data is accessed and manipulated. It lets developers write software without knowing hardware details; key benefit: portability (hardware can evolve without changing software).",
  keys=["interface between hardware and low-level software","defines instructions/registers/data access (contract)","hides hardware detail (abstraction)","portability"])
Q("1-isa-2","isa","ox","ISA 덕분에 하드웨어가 바뀌어도 소프트웨어를 고치지 않고 실행할 수 있다(portability).",True)
Q("1-isa-3","isa","mc","컴퓨터 시스템에서 가장 빠른 메모리로 프로세서 안에 있는 것은?",1,choices=["Cache","Register","DRAM","SSD"])

Q("1-pf-1","perf-factors","mc","'연산당 실행되는 기계 명령어 수'를 결정하는 요소가 '아닌' 것은?",3,choices=["Programming language","Compiler","Architecture(ISA)","Algorithm의 연산 수"],explain="알고리즘은 연산 수를 결정. 연산당 명령어 수는 언어·컴파일러·아키텍처.")
Q("1-pf-2","perf-factors","ox","Moore's Law에 따르면 IC capacity가 18–24개월마다 두 배가 되므로 단일 프로세서 성능도 제한 없이 계속 오른다.",False,explain="전력 제약(power wall) 때문에 막힘.")
Q("1-pf-3","perf-factors","mc","같은 정렬 작업에서 bubble sort(n²) 대신 merge sort(n log n)를 쓰면 주로 줄어드는 것은?",0,choices=["실행되는 연산의 수","CPI","Clock rate","Clock period"])

Q("1-rt-1","response-throughput","mc","Throughput의 정의는?",1,choices=["한 작업이 끝나는 데 걸리는 시간","단위 시간당 처리하는 작업량","클럭 한 사이클의 길이","명령어당 사이클 수"])
Q("1-rt-2","response-throughput","blank","Response time은 (a) 또는 execution time이라고도 부른다.",["latency"],accept=[["latency","레이턴시","지연시간"]])
Q("1-rt-3","response-throughput","short","Response time과 throughput을 각각 정의하시오. (영어로)",
  "Response time (latency, execution time): how long it takes to complete one task/job.\nThroughput: total work done per unit time (e.g., tasks or transactions per hour).",
  keys=["response time = time to do one task","throughput = work per unit time"])

Q("1-pr-1","perf-ratio","calc","같은 프로그램이 시스템 A에서 12 s, B에서 30 s 걸린다. A는 B보다 몇 배 빠른가? 과정을 쓰시오.",
  "Perf_A / Perf_B = Time_B / Time_A = 30 / 12 = 2.5\nA is 2.5 times faster than B.",keys=["성능 비 = 시간의 역비","30/12","2.5"],slot=3,pts=6)
Q("1-pr-2","perf-ratio","mc","Performance_X / Performance_Y = n 일 때 같은 값은?",2,choices=["Time_X / Time_Y","Time_X × Time_Y","Time_Y / Time_X","1 / (Time_X + Time_Y)"])
Q("1-pr-3","perf-ratio","ox","X의 실행 시간이 Y의 실행 시간의 2배이면, X가 Y보다 2배 빠르다.",False,explain="실행 시간이 길면 느림. Y가 2배 빠름.")
Q("1-pr-4","perf-ratio","calc","컴퓨터 P는 어떤 프로그램을 8 s에, Q는 같은 프로그램을 10 s에 실행한다. 'P is n times faster than Q'의 n은?",
  "n = Time_Q / Time_P = 10 / 8 = 1.25",keys=["Time_Q / Time_P","1.25"],slot=3,pts=6)
Q("1-pr-5","perf-ratio","blank","Performance_X = 1 / (a)",["Execution time_X"],accept=[["executiontimex","executiontime","실행시간","responsetime","cputime"]])
Q("1-pr-6","perf-ratio","calc","시스템 A가 B보다 4배 빠르다. B의 실행 시간이 20 s일 때 A의 실행 시간은?",
  "Time_B / Time_A = 4 → Time_A = 20 / 4 = 5 s",keys=["Time_B/Time_A = 4","5 s"])

Q("1-ctd-1","cpu-time-def","mc","수업에서 'execution time'이라고 하면 무엇을 뜻하나?",2,choices=["Elapsed time","System CPU time","User CPU time","I/O time"])
Q("1-ctd-2","cpu-time-def","blank","CPU time = (a) CPU time + (b) CPU time",["user","system"],accept=[["user","유저","사용자"],["system","kernel","시스템"]])
Q("1-ctd-3","cpu-time-def","calc","Clock rate가 2.5 GHz일 때 clock period는?",
  "Clock period = 1 / 2.5×10⁹ Hz = 0.4×10⁻⁹ s = 0.4 ns = 400 ps",keys=["역수","400 ps (0.4 ns)"])
Q("1-ctd-4","cpu-time-def","ox","Elapsed time은 I/O·OS 오버헤드까지 포함하므로 CPU 성능만 비교하기에는 부정확하다.",True)
Q("1-ctd-5","cpu-time-def","mc","Clock period가 250 ps면 clock rate는?",1,choices=["2 GHz","4 GHz","250 MHz","25 GHz"])

Q("1-ct-1","cpu-time","calc","Computer A는 2 GHz에서 프로그램을 10 s에 실행한다. 6 s에 실행하는 Computer B를 설계하려는데, B는 clock rate를 올리는 대가로 A보다 1.2배 많은 clock cycle이 필요하다. B의 clock rate는?",
  "Clock cycles_A = CPU time_A × Clock rate_A = 10 s × 2×10⁹ Hz = 20×10⁹\nClock cycles_B = 1.2 × 20×10⁹ = 24×10⁹\nClock rate_B = Clock cycles_B / CPU time_B = 24×10⁹ / 6 s = 4×10⁹ Hz = 4 GHz",
  keys=["Cycles_A = 20×10⁹","Cycles_B = 1.2 × Cycles_A = 24×10⁹","Rate_B = 24×10⁹ / 6","4 GHz"],slot=3,pts=6)
Q("1-ct-2","cpu-time","calc","Computer A는 3 GHz에서 15 s 걸린다. Computer B로 같은 프로그램을 10 s에 돌리고 싶은데, B는 A보다 1.5배의 clock cycle이 필요하다. B의 clock rate는?",
  "Cycles_A = 15 × 3×10⁹ = 45×10⁹\nCycles_B = 1.5 × 45×10⁹ = 67.5×10⁹\nRate_B = 67.5×10⁹ / 10 = 6.75 GHz",keys=["45×10⁹","67.5×10⁹","6.75 GHz"],slot=3,pts=6)
Q("1-ct-3","cpu-time","mc","CPU Time과 같지 '않은' 식은?",3,choices=["CPU clock cycles × Clock cycle time","CPU clock cycles / Clock rate","IC × CPI / Clock rate","Clock rate / CPU clock cycles"])
Q("1-ct-4","cpu-time","ox","Clock rate를 높이면 CPU clock cycle 수가 늘어나는 trade-off가 흔히 있다.",True)
Q("1-ct-5","cpu-time","calc","어떤 프로그램이 4×10⁹ clock cycle을 쓰고 clock rate가 2 GHz다. CPU time은?",
  "CPU time = cycles / rate = 4×10⁹ / 2×10⁹ = 2 s",keys=["cycles / rate","2 s"])
Q("1-ct-6","cpu-time","blank","성능을 높이려면 clock cycle 수를 (a)거나 clock rate를 (b)야 한다.",["줄이","높여"],accept=[["줄이","줄","감소","decrease","reduce","줄여"],["높이","높여","올려","증가","increase"]])

Q("1-cpi-1","cpi","calc","Computer A: cycle time 250 ps, CPI 2.0. Computer B: cycle time 500 ps, CPI 1.2. 같은 ISA·같은 프로그램일 때 어느 쪽이 몇 배 빠른가?",
  "Let IC = I.\nCPU time_A = I × 2.0 × 250 ps = 500·I ps\nCPU time_B = I × 1.2 × 500 ps = 600·I ps\nPerf_A / Perf_B = 600I / 500I = 1.2 → A is 1.2 times faster than B",
  keys=["IC를 I로 둠","A = 500I ps","B = 600I ps","A가 1.2배 빠름"],slot=4,pts=6)
Q("1-cpi-2","cpi","calc","Computer A: clock 2 GHz, CPI 1.5. Computer B: clock 3 GHz, CPI 2.4. 같은 프로그램에서 어느 쪽이 몇 배 빠른가?",
  "CPU time_A = I × 1.5 / 2×10⁹ = 0.75·I ns\nCPU time_B = I × 2.4 / 3×10⁹ = 0.8·I ns\nPerf_A / Perf_B = 0.8 / 0.75 ≈ 1.067 → A is about 1.07 times faster",keys=["IC×CPI/rate","A 0.75I ns, B 0.8I ns","A가 약 1.07배 빠름"],slot=4,pts=6)
Q("1-cpi-3","cpi","mc","CPI를 주로 결정하는 것은?",1,choices=["Program만","CPU hardware (organization)","Technology만","Clock rate"],explain="슬라이드: CPI는 CPU hardware가 결정. 요약표에선 program·language·compiler·ISA·organization 모두 영향.")
Q("1-cpi-4","cpi","blank","Clock Cycles = (a) × (b)",["Instruction Count","CPI"],accept=[["instructioncount","ic","명령어수"],["cpi","cyclesperinstruction"]])
Q("1-cpi-5","cpi","calc","IC = 2×10⁹, CPI = 1.5, clock rate = 3 GHz인 프로그램의 CPU time은?",
  "CPU time = IC × CPI / rate = 2×10⁹ × 1.5 / 3×10⁹ = 1 s",keys=["IC×CPI/rate","1 s"])
Q("1-cpi-6","cpi","ox","두 컴퓨터를 같은 프로그램으로 비교할 때 IC를 몰라도 성능 비는 구할 수 있다.",True,explain="같은 IC는 비율에서 약분 (교수님 풀이 방식).")

Q("1-wc-1","weighted-cpi","calc","클래스 A, B, C의 CPI가 1, 2, 3이다. Sequence 1은 A 2개, B 1개, C 2개, Sequence 2는 A 4개, B 1개, C 1개를 실행한다. 각 sequence의 평균 CPI와 더 빠른 쪽은?",
  "Seq 1: IC = 5, cycles = 2×1 + 1×2 + 2×3 = 10 → CPI = 10/5 = 2.0\nSeq 2: IC = 6, cycles = 4×1 + 1×2 + 1×3 = 9 → CPI = 9/6 = 1.5\nSeq 2 uses fewer cycles (9 < 10), so it is faster (same clock).",
  keys=["seq1 10 cycles / 5","CPI 2.0","seq2 9 cycles / 6","CPI 1.5","seq2가 빠름(사이클 적음)"],slot=4,pts=6)
Q("1-wc-2","weighted-cpi","calc","CPI가 A=1, B=3, C=4인 클래스로, 프로그램이 A 50%, B 30%, C 20%로 구성된다. 평균 CPI는?",
  "CPI = 1×0.5 + 3×0.3 + 4×0.2 = 0.5 + 0.9 + 0.8 = 2.2",keys=["relative frequency 가중","2.2"],slot=4,pts=6)
Q("1-wc-3","weighted-cpi","ox","명령어 수가 더 많은 코드 sequence는 항상 더 느리다.",False,explain="예제에서 Seq 2가 명령어는 6개로 많지만 사이클 9로 더 빠름.")
Q("1-wc-4","weighted-cpi","blank","가중 평균 CPI = Σ CPI_i × (IC_i / IC)에서 IC_i / IC를 (a)라고 한다.",["relative frequency"],accept=[["relativefrequency","상대빈도","상대도수"]])
Q("1-wc-5","weighted-cpi","calc","CPI: A=2, B=4. 프로그램 X는 A 300개·B 100개, 프로그램 Y는 A 100개·B 200개. 각각의 총 cycle과 평균 CPI는?",
  "X: cycles = 300×2 + 100×4 = 1000, IC = 400, CPI = 2.5\nY: cycles = 100×2 + 200×4 = 1000, IC = 300, CPI ≈ 3.33",keys=["X 1000 cycles, CPI 2.5","Y 1000 cycles, CPI 3.33"])

Q("1-ps-1","perf-summary","mc","Clock rate에 영향을 주는 것만 고른 것은?",2,choices=["Algorithm, Compiler","Programming language, ISA","Hardware organization, Technology","Compiler, Technology"])
Q("1-ps-2","perf-summary","ox","Compiler는 instruction count와 CPI 모두에 영향을 준다.",True)
Q("1-ps-3","perf-summary","blank","CPU Time = (Instructions / Program) × ((a) / Instruction) × (Seconds / (b))",["Clock cycles","Clock cycle"],accept=[["clockcycles","cycles","clockcycle"],["clockcycle","cycle","clockcycles"]])

Q("1-pw-1","power","calc","새 CPU가 capacitive load는 옛 CPU의 85%, voltage와 frequency는 각각 15% 낮다. 전력 비 P_new / P_old는?",
  "P ∝ C × V² × F\nP_new/P_old = 0.85 × 0.85² × 0.85 = 0.85⁴ ≈ 0.52",keys=["P ∝ C·V²·F","0.85⁴","≈ 0.52"],slot=5,pts=5)
Q("1-pw-2","power","mc","Power wall의 원인으로 옳은 것은?",0,choices=["전압을 더 낮출 수 없고 열을 더 제거할 수 없음","트랜지스터 수가 줄어듦","클럭이 너무 느림","메모리가 부족함"])
Q("1-pw-3","power","ox","Power wall 때문에 업계는 multicore로 방향을 바꿨고, 이는 programmer의 명시적 병렬 프로그래밍을 요구한다.",True)

Q("1-am-1","amdahl","calc","100 s 프로그램 중 곱셈이 80 s다. 전체를 5배 빠르게 하려면 곱셈을 몇 배 빨리 해야 하나?",
  "T_improved = 80/n + 20, 목표 20 s (100/5)\n20 = 80/n + 20 → 80/n = 0 → 불가능. 곱셈을 무한히 빠르게 해도 최대 5배.",
  keys=["T = 80/n + 20","목표 20 s","불가능 (n → ∞)"],slot=5,pts=5)
Q("1-am-2","amdahl","calc","100 s 프로그램 중 곱셈이 80 s다. 전체를 4배 빠르게 하려면 곱셈을 몇 배 빨리 해야 하나?",
  "목표 100/4 = 25 s\n25 = 80/n + 20 → 80/n = 5 → n = 16",keys=["목표 25 s","80/n = 5","16배"],slot=5,pts=5)
Q("1-am-3","amdahl","blank","T_improved = T_affected / (a) + T_(b)",["improvement factor","unaffected"],accept=[["improvementfactor","개선배수","speedup","개선율"],["unaffected","영향받지않는부분"]])
Q("1-am-4","amdahl","ox","Amdahl's Law의 pitfall: 한 부분을 n배 개선하면 전체 성능도 n배 좋아진다고 기대하는 것.",True)
Q("1-am-5","amdahl","calc","실행 시간 50 s 중 메모리 접근이 30 s다. 메모리 접근을 3배 빠르게 하면 새 실행 시간과 speedup은?",
  "T = 30/3 + 20 = 30 s\nSpeedup = 50 / 30 ≈ 1.67",keys=["30/3 + 20","30 s","약 1.67배"])
Q("1-am-6","amdahl","mc","Amdahl's Law가 주는 설계 교훈과 가장 가까운 것은?",1,choices=["Smaller is faster","Make the common case fast","Simplicity favors regularity","Hierarchy of memories"])

Q("1-mi-1","mips-metric","calc","A와 B는 둘 다 4 GHz. IC는 A 10 billion, B 8 billion, CPI는 A 1.0, B 1.1. 각각의 MIPS와 CPU time을 구하고 어느 쪽이 실제로 빠른지 쓰시오.",
  "MIPS = Clock rate / (CPI × 10⁶)\nMIPS_A = 4×10⁹ / (1.0×10⁶) = 4000, MIPS_B = 4×10⁹ / (1.1×10⁶) ≈ 3636\nCPU time_A = 10×10⁹ × 1.0 / 4×10⁹ = 2.5 s\nCPU time_B = 8×10⁹ × 1.1 / 4×10⁹ = 2.2 s\nMIPS says A, but B is actually faster (Perf_A/Perf_B = 2.2/2.5 = 0.88).",
  keys=["MIPS_A 4000","MIPS_B ≈ 3636","time A 2.5 s","time B 2.2 s","B가 실제로 빠름"],slot=5,pts=5)
Q("1-mi-2","mips-metric","short","MIPS가 성능 지표로 부적절한 이유를 쓰시오. (영어로)",
  "MIPS = IC / (Execution time × 10⁶) = Clock rate / (CPI × 10⁶), so the instruction count cancels out. It does not account for differences in ISAs between computers or differences in instruction complexity, and CPI varies between programs on the same CPU.",
  keys=["instruction count가 빠짐(약분)","ISA 차이 반영 못 함","명령어 복잡도 차이 반영 못 함","CPI가 프로그램마다 다름"],slot=2,pts=3)
Q("1-mi-3","mips-metric","ox","MIPS 값이 높은 컴퓨터가 항상 같은 프로그램을 더 빨리 실행한다.",False)
Q("1-mi-4","mips-metric","blank","MIPS = Clock rate / ((a) × 10⁶)",["CPI"],accept=[["cpi"]])
Q("1-mi-5","mips-metric","calc","3 GHz, CPI 1.5인 컴퓨터의 MIPS rating은?",
  "MIPS = 3×10⁹ / (1.5 × 10⁶) = 2000",keys=["rate/(CPI×10⁶)","2000"])

Q("1-sp-1","spec-idle","mc","SPEC CPU 벤치마크에 대한 설명으로 옳은 것은?",0,choices=["I/O가 거의 없는 프로그램들의 elapsed time으로 CPU 성능을 본다","서버 전력만 측정한다","MIPS 값을 비교한다","CPI만 측정한다"])
Q("1-sp-2","spec-idle","ox","슬라이드의 i7은 10% 부하에서도 최대 전력의 약 절반(47%)을 쓴다 → 저부하에서도 전력이 많이 든다.",True)

Q("1-rc-1","risc-cisc","short","RISC와 CISC를 비교하시오 (예시 아키텍처, 장점, 단점). (영어로)",
  "RISC (e.g., MIPS, ARM, PowerPC): small, simple instruction set → faster execution, power-efficient, scalable (easier parallelism); but needs more instructions for complex tasks (larger programs).\nCISC (e.g., x86, x86-64): large, complex instructions to minimize instructions per program → smaller program size, backward compatibility; but slower execution and higher power consumption.",
  keys=["RISC 예: MIPS/ARM","CISC 예: x86","RISC 장점: 빠름·전력 효율·확장성","RISC 단점: 명령어 수 많음","CISC 장점: 프로그램 작음·호환성","CISC 단점: 느림·전력 큼"],slot=2,pts=3)
Q("1-rc-2","risc-cisc","mc","x86-64는 어느 쪽인가?",1,choices=["RISC","CISC","VLIW","둘 다 아님"])
Q("1-rc-3","risc-cisc","ox","RISC의 단점은 복잡한 작업에 더 많은 명령어가 필요해 프로그램 크기가 커질 수 있다는 것이다.",True)
Q("1-rc-4","risc-cisc","mc","MIPS architecture의 'MIPS'가 뜻하는 것은?",2,choices=["Millions of Instructions Per Second","Multiple Instruction Pipeline System","Microprocessor without Interlocked Pipeline Stages","Memory Instruction Processing Set"])
