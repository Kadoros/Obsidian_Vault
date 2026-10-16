from qdsl import Q
from sim import CTRL
# ───────── U4 프로세서: 데이터패스와 제어 ─────────
FLIP = ("※ 이 문제의 데이터패스는 교안 p.3과 같지만 MUX 입력 번호가 아래처럼 표시돼 있다고 하자.\n"
        "RegDst MUX: 위(rt [20–16]) = 1, 아래(rd [15–11]) = 0\n"
        "ALUSrc MUX: 위(Read data 2) = 1, 아래(sign-extended imm) = 0\n"
        "MemtoReg MUX: 위(Read data) = 0, 아래(ALU result) = 1")

Q("4-pi-1","proc-intro","mc","중간고사 범위의 프로세서 구현은?",0,choices=["단순(single-cycle) 버전","파이프라인 버전","멀티사이클 버전","슈퍼스칼라"])
Q("4-pi-2","proc-intro","ox","중간고사 답안에 수업에서 정한 명령어 집합 밖의 명령어를 쓰면 0점 처리된다고 공지됐다.",True)
Q("4-pi-3","proc-intro","mc","week6 p.2의 'Simple subset of instructions'에 '없는' 것은?",3,choices=["lw","beq","or","addi"])

Q("4-es-1","exec-steps","mc","명령어 실행에서 ALU가 계산하는 것이 '아닌' 것은?",2,choices=["산술 결과","load/store용 메모리 주소","instruction memory에서 읽은 명령어","분기 대상 주소"])
Q("4-es-2","exec-steps","blank","분기하지 않으면 PC ← PC + (a). 명령어 하나는 (b) bit다.",["4","32"],accept=[["4"],["32"]])
Q("4-es-3","exec-steps","ox","명령어 하나(1 word)는 32 byte다.",False,explain="32 bit = 4 byte. 녹음의 '32 bytes'는 말실수.")

Q("4-co-1","cpu-overview","short","week6 p.6 'Can't just join wires together'에서 MUX가 필요한 세 곳과 각 MUX가 고르는 두 입력을 쓰시오. (영어로)",
  "1. PC input: PC + 4 vs. branch target address\n2. ALU second input: register (Read data 2) vs. sign-extended immediate from the instruction\n3. Register write data: ALU result vs. data read from data memory",
  keys=["PC: PC+4 vs branch target","ALU 입력: register vs immediate","쓰기 데이터: ALU vs memory"],slot=16,pts=9)
Q("4-co-2","cpu-overview","mc","lw에서 ALU 결과는 무엇인가?",1,choices=["레지스터에 쓸 최종 값","data memory에 접근할 주소","다음 PC","분기 오프셋"])
Q("4-co-3","cpu-overview","ox","서로 다른 출처의 선은 그냥 하나로 연결(join)하면 된다.",False)

Q("4-ce-1","comb-elements","mc","조합 소자(combinational element)의 특징은?",0,choices=["출력이 현재 입력만의 함수","값을 저장한다","클럭 edge에만 바뀐다","write 신호가 필요하다"])
Q("4-ce-2","comb-elements","mc","다음 중 상태(sequential) 소자는?",3,choices=["AND gate","Multiplexer","ALU","Register"])
Q("4-ce-3","comb-elements","blank","ALU는 Y = F(A, B)이고, R-format에서 F는 명령어의 맨 아래 6 bit인 (a)로 정해진다.",["funct"],accept=[["funct","function","functioncode","펑션코드","funct필드"]])
Q("4-ce-4","comb-elements","ox","32-bit 데이터는 데이터패스에서 선 32개(bus)로 전달된다.",True)

Q("4-mx-1","mux-basic","blank","Multiplexer: Y = S ? (a) : (b)",["I1","I0"],accept=[["i1"],["i0"]])
Q("4-mx-2","mux-basic","mc","MUX의 선택선 S = 0이면?",0,choices=["0번(I0)으로 표시된 입력이 출력","1번 입력이 출력","두 입력의 AND","출력 없음"])
Q("4-mx-3","mux-basic","ox","MUX 신호값은 입력선의 위·아래 위치가 아니라 그림에 표시된 번호(0/1)로 정해진다.",True)
Q("4-mx-4","mux-basic","mc","시험의 MUX 그림에서 원하는 입력선 옆에 '1'이 적혀 있다. 선택 신호는?",1,choices=["0","1","X","위치에 따라 다름"])
Q("4-mx-5","mux-basic","short","MUX의 역할과 데이터패스에 MUX가 필요한 이유를 쓰시오. (영어로)",
  "A multiplexer selects one of several inputs according to a select signal (Y = S ? I1 : I0). The datapath needs MUXes because the same component (e.g., ALU input, register write data, next PC) gets data from different sources for different instructions, and wires cannot simply be joined together.",
  keys=["select signal로 입력 하나 선택","명령어마다 출처가 다름","선을 그냥 합칠 수 없음"],slot=1,pts=3)
Q("4-mx-6","mux-basic","ox","MUX는 조합 소자(combinational element)다.",True)

Q("4-se-1","seq-elements","mc","Edge-triggered register가 값을 갱신하는 시점은 (슬라이드 기준)?",1,choices=["Clk이 1인 동안 계속","Clk이 0 → 1로 바뀔 때","Clk이 1 → 0으로 바뀔 때만","Write가 0일 때"])
Q("4-se-2","seq-elements","ox","Write control이 있는 레지스터는 clock edge이면서 write 입력이 1일 때만 값을 바꾼다.",True)
Q("4-se-3","seq-elements","blank","레지스터 파일의 write control 신호 이름은 (a)이다.",["RegWrite"],accept=[["regwrite"]])
Q("4-se-4","seq-elements","short","Combinational element와 state(sequential) element를 비교하시오. (영어로)",
  "Combinational elements operate on data; their output is a function of the current input only (e.g., AND gate, MUX, adder, ALU). State elements store information; registers update their stored value on a clock edge (edge-triggered), possibly only when a write control is 1.",
  keys=["combinational: output = f(input)","state: store information","clock edge에 갱신","예시"],slot=1,pts=3)

Q("4-cl-1","clocking","mc","Clock period를 결정하는 것은?",2,choices=["가장 짧은 지연","레지스터 개수","가장 긴 조합 회로 지연","명령어 수"])
Q("4-cl-2","clocking","ox","조합 회로는 state element에서 입력을 받아 클럭 edge 사이에 데이터를 변환하고 state element로 출력한다.",True)

Q("4-fe-1","fetch","mc","Instruction fetch에서 PC가 연결되는 두 곳은?",0,choices=["Instruction memory의 read address와 +4 adder","Data memory와 ALU","Register file과 sign-extend","Control과 ALU control"])
Q("4-fe-2","fetch","ox","PC는 32-bit register다.",True)
Q("4-fe-3","fetch","blank","Instruction fetch: PC → (a) memory, 동시에 PC + (b) 계산",["instruction","4"],accept=[["instruction","instructionmemory","명령어"],["4"]])

Q("4-rd-1","r-datapath","mc","R-format 실행 단계로 옳은 것은?",1,choices=["메모리 읽기 → ALU → 레지스터 쓰기","레지스터 2개 읽기 → ALU 연산 → 레지스터 쓰기","레지스터 1개 읽기 → sign extend → 메모리 쓰기","PC + offset → 분기"])
Q("4-rd-2","r-datapath","ox","R-format 명령어는 레지스터에 결과를 쓰므로 RegWrite = 1이다.",True)
Q("4-rd-3","r-datapath","blank","Register file의 Read register 1, Read register 2, Write register 입력은 각각 (a) bit다.",["5"],accept=[["5"]])

Q("4-ls-1","ls-datapath","mc","lw가 켜는 신호 조합은?",2,choices=["MemWrite, RegWrite","MemRead, MemWrite","MemRead, RegWrite","MemWrite만"])
Q("4-ls-2","ls-datapath","mc","sw가 켜는 메모리 신호는?",1,choices=["MemRead","MemWrite","MemtoReg","RegWrite"])
Q("4-ls-3","ls-datapath","ox","load/store의 16-bit offset은 ALU에 들어가기 전에 32-bit로 sign extend된다.",True)
Q("4-ls-4","ls-datapath","ox","lw를 실행할 때는 MemWrite를 1로 켠다.",False,explain="lw는 MemRead. 6주-1 23:18의 말실수에 주의.")

Q("4-bd-1","br-datapath","mc","beq에서 두 레지스터가 같은지는 어떻게 확인하나?",2,choices=["AND 게이트로","두 값을 더해서","ALU로 빼서 Zero 출력 확인","sign extend로"])
Q("4-bd-2","br-datapath","short","beq의 분기 대상 주소를 계산하는 데이터패스 단계를 쓰시오. (영어로)",
  "Sign-extend the 16-bit displacement to 32 bits, shift it left by 2 (word displacement → byte offset, ×4), and add it to PC + 4 (already computed during instruction fetch).",
  keys=["sign-extend","shift left 2 (×4)","PC + 4에 더함"])
Q("4-bd-3","br-datapath","ox","Shift left 2는 offset에 4를 곱하는 것과 같다.",True)
Q("4-bd-4","br-datapath","mc","분기 상수를 byte 주소가 아니라 '줄(명령어) 수'로 주는 이유로 교수님이 든 것은?",0,choices=["4로 안 나눠지는 값이 들어가면 심각한 오류가 나므로","비트를 아끼려고","ALU가 빼기만 해서","jump와 구분하려고"])

Q("4-cp-1","composing","short","단순 데이터패스에서 MUX가 들어가는 네 곳과 각 MUX를 제어하는 신호를 쓰시오. (영어로)",
  "1. ALU input: register vs. immediate → ALUSrc\n2. Register write data: ALU output vs. data memory → MemtoReg\n3. Next PC: PC + 4 vs. branch target → Branch AND Zero (PCSrc)\n4. Write register number: rt vs. rd → RegDst",
  keys=["ALUSrc","MemtoReg","PCSrc = Branch AND Zero","RegDst"],slot=16,pts=9)
Q("4-cp-2","composing","mc","단순 데이터패스가 instruction memory와 data memory를 분리하는 이유는?",1,choices=["메모리가 싸서","한 클럭 사이클에 명령어 하나를 실행하고 각 요소는 한 번에 한 기능만 하므로","캐시 때문에","파이프라인 때문에"])
Q("4-cp-3","composing","mc","쓰기 레지스터 번호를 rt와 rd 중에서 고르는 MUX의 신호는?",3,choices=["ALUSrc","MemtoReg","Branch","RegDst"])
Q("4-cp-4","composing","ox","단순(single-cycle) 데이터패스는 모든 명령어를 한 클럭 사이클에 실행한다.",True)
Q("4-cp-5","composing","mc","레지스터 쓰기 데이터를 ALU 결과와 메모리 값 중에서 고르는 신호는?",2,choices=["RegDst","ALUSrc","MemtoReg","MemRead"])

Q("4-df-1","dp-fields","mc","p.3 데이터패스에서 Instruction [31–26]이 들어가는 곳은?",0,choices=["Control","ALU control","Sign-extend","Read register 1"])
Q("4-df-2","dp-fields","mc","Instruction [5–0]이 들어가는 곳은?",1,choices=["Control","ALU control","Data memory","Shift left 2"])
Q("4-df-3","dp-fields","blank","rs [25–21] → Read register (a), rt [20–16] → Read register 2와 RegDst MUX의 (b)번 입력",["1","0"],accept=[["1"],["0"]])
Q("4-df-4","dp-fields","mc","Instruction [15–0]이 들어가는 곳은?",2,choices=["Control","RegDst MUX","Sign-extend","PC"])

Q("4-rt-1","dp-rtype","sig","p.3 데이터패스에서 R-type 명령어(add $t0, $s1, $s2)의 제어 신호 값을 채우시오.",CTRL["R"],slot=14,pts=8)
Q("4-rt-2","dp-rtype","mc","R-type에서 RegDst = 1인 이유는?",1,choices=["rt에 써야 해서","rd(세 번째 레지스터)에 써야 하고 p.3에서 rd가 1번 입력이라서","메모리에서 읽어서","분기라서"])
Q("4-rt-3","dp-rtype","mc","R-type에서 ALUSrc 값과 이유는?",0,choices=["0, 두 번째 피연산자도 레지스터라서","1, 상수를 쓰니까","X, 상관없어서","1, 메모리 주소라서"])
Q("4-rt-4","dp-rtype","short","p.3 데이터패스에서 `add $t0, $s1, $s2`가 실행될 때 데이터가 흐르는 경로를 순서대로 쓰시오. (영어로)",
  "PC → instruction memory; opcode → Control. rs ($s1) → Read register 1, rt ($s2) → Read register 2; both read data go to the ALU (ALUSrc = 0), ALU control uses funct (add). The ALU result bypasses data memory through the MemtoReg MUX (0) back to Write data; rd ($t0) is selected by RegDst = 1 and written with RegWrite = 1. PC ← PC + 4.",
  keys=["두 레지스터 읽기","ALUSrc = 0","funct → ALU control","MemtoReg = 0 (data memory 우회)","RegDst = 1, RegWrite = 1","PC + 4"],slot=16,pts=9)
Q("4-rt-5","dp-rtype","ox","R-type 실행 중에는 data memory를 사용하지 않는다.",True)
Q("4-rt-6","dp-rtype","sig",FLIP + "\n\n이 그림에서 R-type 명령어의 제어 신호를 채우시오.",
  dict(CTRL["R"], RegDst=0, ALUSrc=1, MemtoReg=1),slot=14,pts=8,
  explain="RegDst: rd가 0번 → 0. ALUSrc: 레지스터가 1번 → 1. MemtoReg: ALU result가 1번 → 1. 나머지는 그대로.")

Q("4-lw-1","dp-lw","sig","p.3 데이터패스에서 lw 명령어의 제어 신호 값을 채우시오.",CTRL["lw"],slot=14,pts=8)
Q("4-lw-2","dp-lw","mc","lw에서 MemtoReg = 1인 이유는?",2,choices=["ALU 결과를 써야 해서","분기 때문에","data memory에서 읽은 값을 레지스터에 써야 하고 p.3에서 Read data가 1번 입력이라서","메모리에 써야 해서"])
Q("4-lw-3","dp-lw","mc","lw가 결과를 쓰는 레지스터 필드와 RegDst 값은?",0,choices=["rt, 0","rd, 1","rs, 0","rt, 1"])
Q("4-lw-4","dp-lw","short","lw에서 ALU가 하는 일과 그 결과가 어디로 가는지 쓰시오. (영어로)",
  "The ALU adds the base address (rs) and the sign-extended 16-bit offset (ALUSrc = 1, ALUOp = 00 → add). The result is not the wanted value but the memory address; it goes to the data memory address input, and the data read (MemRead = 1) is written to rt via MemtoReg = 1.",
  keys=["base + sign-extended offset","ALU 결과 = 주소","data memory로","읽은 값을 rt에"])
Q("4-lw-5","dp-lw","sig",FLIP + "\n\n이 그림에서 lw의 제어 신호를 채우시오.",dict(CTRL["lw"], RegDst=1, ALUSrc=0, MemtoReg=0),slot=14,pts=8,
  explain="rt가 1번 → RegDst 1, imm이 0번 → ALUSrc 0, Read data가 0번 → MemtoReg 0.")
Q("4-lw-6","dp-lw","ox","lw에서 ALU의 결과는 사용자가 원하는 최종 값이다.",False)

Q("4-sw-1","dp-sw","sig","p.3 데이터패스에서 sw 명령어의 제어 신호 값을 채우시오.",CTRL["sw"],slot=14,pts=8)
Q("4-sw-2","dp-sw","mc","sw에서 RegDst와 MemtoReg가 X인 이유는?",1,choices=["메모리를 읽지 않아서","레지스터에 쓰지 않으므로(RegWrite = 0) 어떤 값이든 상관없어서","ALU를 안 써서","분기라서"])
Q("4-sw-3","dp-sw","mc","sw에서 data memory의 Write data로 들어가는 값은?",2,choices=["ALU result","sign-extended offset","rt의 값 (Read data 2)","PC + 4"])
Q("4-sw-4","dp-sw","ox","sw는 ALUSrc = 1, ALUOp = 00이다.",True)

Q("4-bq-1","dp-beq","sig","p.3 데이터패스에서 beq 명령어의 제어 신호 값을 채우시오.",CTRL["beq"],slot=14,pts=8)
Q("4-bq-2","dp-beq","mc","beq에서 PC가 분기 대상으로 바뀌는 조건은?",3,choices=["Branch = 1","Zero = 1","Branch = 0이고 Zero = 1","Branch = 1이고 Zero = 1"])
Q("4-bq-3","dp-beq","short","beq rs, rt, offset이 실행될 때 rs = rt인 경우와 아닌 경우의 PC 결정 과정을 쓰시오. (영어로)",
  "Control sets Branch = 1 and ALUOp = 01 so the ALU subtracts rs − rt (ALUSrc = 0). If rs = rt the result is 0 and Zero = 1, so Branch AND Zero = 1 and the PC MUX selects the branch target (PC + 4) + (sign-extended offset << 2). Otherwise Zero = 0, the AND output is 0, and the PC MUX selects PC + 4.",
  keys=["Branch = 1","ALU 빼기 (ALUOp 01, ALUSrc 0)","같으면 Zero = 1 → AND = 1 → 분기 대상","다르면 PC + 4","대상 = PC+4 + offset×4"],slot=16,pts=9)
Q("4-bq-4","dp-beq","ox","beq는 레지스터에 쓰지 않으므로 RegWrite = 0이다.",True)
Q("4-bq-5","dp-beq","mc","beq의 ALUOp는?",1,choices=["00","01","10","11"])
Q("4-bq-6","dp-beq","sig",FLIP + "\n\n이 그림에서 beq의 제어 신호를 채우시오.",dict(CTRL["beq"], ALUSrc=1),slot=14,pts=8,
  explain="레지스터(Read data 2)가 1번 → ALUSrc 1. RegDst·MemtoReg는 여전히 X.")

Q("4-mt-1","mux-trap","mc","교안 p.3의 MemtoReg MUX에서 위쪽 입력의 번호는?",1,choices=["0 (ALU result)","1 (Read data)","0 (Read data)","표시 없음"])
Q("4-mt-2","mux-trap","ox","MUX 그림의 숫자가 뒤집혀 있으면 같은 명령어라도 선택 신호 값이 반대가 된다.",True)
Q("4-mt-3","mux-trap","mc",FLIP + "\n\n이 그림에서 sw의 ALUSrc 값은?",0,choices=["0","1","X","그림과 무관하게 1"],explain="imm이 0번으로 표시됨.")
Q("4-mt-4","mux-trap","short","교수님이 'be extremely careful on what is actually written on the multiplexer'라고 한 이유를 설명하시오. (영어로)",
  "A MUX control value selects the input labeled with that number (0 or 1), not the top or bottom input. If the labels are flipped in the figure, the required control signal for the same instruction is the opposite (e.g., RegDst for R-type would become 0), so you must read the numbers on each MUX.",keys=["신호값 = 입력선에 적힌 번호","위/아래 아님","번호가 바뀌면 신호 반대"])
Q("4-mt-5","mux-trap","mc",FLIP + "\n\n이 그림에서 add의 MemtoReg 값은?",1,choices=["0","1","X","2"])

Q("4-bc-1","branch-calc","calc","현재 PC = 108인 beq가 124번지로 분기하려 한다. offset 필드 값과 데이터패스가 대상 주소를 다시 계산하는 과정을 쓰시오.",
  "PC + 4 = 112\noffset = (124 − 112) / 4 = 3\nDatapath: 3 → sign-extend → shift left 2 = 12 → 112 + 12 = 124",keys=["PC+4 = 112","offset 3","<<2 = 12","112 + 12 = 124"],slot=15,pts=6)
Q("4-bc-2","branch-calc","calc","100번지의 beq가 180번지로 분기한다. beq에 쓸 상수는?",
  "(180 − 104) / 4 = 76 / 4 = 19",keys=["next line 104","76","19"],slot=15,pts=6)
Q("4-bc-3","branch-calc","calc","200번지의 beq가 180번지로 분기한다 (위쪽, 루프 시작). offset 값과 16-bit 이진 표현은?",
  "offset = (180 − 204) / 4 = −24 / 4 = −6\n16-bit: 1111 1111 1111 1010",keys=["PC+4 = 204","−6","1111 1111 1111 1010"],slot=15,pts=6)
Q("4-bc-4","branch-calc","mc","offset 필드가 5이고 beq가 400번지에 있으면 분기 대상은?",2,choices=["405","420","424","404"])
Q("4-bc-5","branch-calc","ox","분기 대상이 현재 코드보다 위(이전 주소)에 있으면 offset은 음수가 되고, sign extension으로 위 비트가 1로 채워진다.",True)

Q("4-au-1","alu-uses","mc","ALU control 0110이 뜻하는 연산은?",1,choices=["add","subtract","AND","set-on-less-than"])
Q("4-au-2","alu-uses","blank","Load/Store: F = (a), Branch: F = (b), R-type: F는 funct에 따라",["add","subtract"],accept=[["add","덧셈","더하기"],["subtract","sub","뺄셈","빼기"]])
Q("4-au-3","alu-uses","ox","교수님은 ALU control 표를 시험에서 외워 쓰게 할 것이라고 했다.",False,explain="'This table will be given to you' — 표를 읽고 적용할 줄 알면 됨.")

Q("4-ao-1","aluop","mc","lw/sw의 ALUOp와 ALU control은?",0,choices=["00, 0010","01, 0110","10, funct에 따라","00, 0110"])
Q("4-ao-2","aluop","mc","R-type sub(funct 100010)의 ALU control은?",2,choices=["0010","0000","0110","0111"])
Q("4-ao-3","aluop","calc","ALUOp와 funct가 다음과 같을 때 ALU control을 쓰시오: (1) ALUOp 10, funct 100101 (2) ALUOp 01, funct XXXXXX (3) ALUOp 10, funct 101010",
  "(1) OR → 0001\n(2) beq → subtract → 0110\n(3) slt → 0111",keys=["0001","0110","0111"])
Q("4-ao-4","aluop","ox","lw, sw, beq는 I-type이라 funct 필드가 없어서 ALU control이 ALUOp만으로 결정된다.",True)
Q("4-ao-5","aluop","mc","R-type funct들(100000, 100010, 100100, 100101, 101010)의 공통점으로 교수님이 짚은 것은?",1,choices=["모두 짝수","앞 두 비트가 모두 10으로 R-type ALUOp(10)와 같아 보임","마지막 비트가 0","모두 add로 동작"])
Q("4-ao-6","aluop","blank","ALU control 입력은 Main control의 2-bit (a)와 명령어의 6-bit (b)이다.",["ALUOp","funct"],accept=[["aluop"],["funct","function","functioncode"]])

Q("4-km-1","kmap","calc","ALU control 표를 만족하는 Operation 비트 식을 쓰고, lw(ALUOp = 00)에서 Op1을 계산하시오.",
  "Op3 = 0, Op2 = ALUOp0 + ALUOp1·F1, Op1 = ¬ALUOp1 + ¬F2, Op0 = ALUOp1·(F3 + F0)\nlw: ALUOp1 = 0 → Op1 = ¬0 + … = 1 → 0010 (add) ✓",keys=["Op1 = ¬ALUOp1 + ¬F2","lw에서 Op1 = 1"])
Q("4-km-2","kmap","ox","교안 p.30의 식 'Op1 = ALUOp1 + F2'를 그대로 쓰면 lw에서도 ALU control 0010이 나온다.",False,explain="NOT 표시가 빠진 식. 그대로면 Op1 = 0 → 0000(AND)이 되어 표와 안 맞음.")

Q("4-mc-1","main-control","mc","week6 p.31에서 'Always read'인 필드는?",0,choices=["rs","rt","rd","funct"])
Q("4-mc-2","main-control","mc","'write for R-type and load'와 관련된 필드 설명으로 옳은 것은?",2,choices=["R-type과 load 모두 rd에 씀","R-type과 load 모두 rt에 씀","R-type은 rd, load는 rt에 씀 (그래서 RegDst MUX)","둘 다 쓰지 않음"])
Q("4-mc-3","main-control","blank","lw의 opcode는 (a), sw는 (b), beq는 (c) (10진수)",["35","43","4"],accept=[["35"],["43"],["4"]])

Q("4-ct-1","control-table","mc","sw의 RegWrite, MemRead, MemWrite는?",3,choices=["1, 0, 0","0, 1, 0","1, 1, 0","0, 0, 1"])
Q("4-ct-2","control-table","mc","제어 신호 표에서 X(don't care)가 나오는 명령어와 신호는?",1,choices=["R-type의 ALUSrc","sw·beq의 RegDst와 MemtoReg","lw의 RegDst","모든 명령어의 Branch"])
Q("4-ct-3","control-table","ox","ALUSrc = 1인 명령어는 lw와 sw다.",True)
Q("4-ct-4","control-table","short","제어 신호 표에서 sw와 beq의 RegDst, MemtoReg가 X인 이유를 쓰시오. (영어로)",
  "Neither sw nor beq writes a register (RegWrite = 0), so it does not matter which register number is selected (RegDst) or which data is selected for write-back (MemtoReg).",keys=["RegWrite = 0","레지스터에 쓰지 않음","어떤 값이든 결과에 영향 없음"])
Q("4-ct-5","control-table","calc","opcode Op5–Op0 = 100011이 들어왔다. 어떤 명령어이며 RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp0는?",
  "100011 = 35 = lw\nRegDst 0, ALUSrc 1, MemtoReg 1, RegWrite 1, MemRead 1, MemWrite 0, Branch 0, ALUOp1 0, ALUOp0 0",keys=["lw","0 1 1 1 1 0 0 0 0"])
Q("4-ct-6","control-table","mc","Branch = 1인 명령어는?",2,choices=["R-type","lw","beq","sw"])

Q("4-cg-1","control-logic","mc","p.33 제어 회로에서 ALUSrc를 만드는 OR 게이트의 입력은?",0,choices=["lw, sw","R-format, lw","sw, beq","R-format, beq"])
Q("4-cg-2","control-logic","mc","p.33 제어 회로에서 RegWrite는?",1,choices=["lw OR sw","R-format OR lw","beq","sw"])

Q("4-oc-1","offset-const","ox","`lw $t0, $t2($t1)` (offset이 레지스터 값)은 올바른 MIPS 명령어다.",False)
Q("4-oc-2","offset-const","calc","$t1 = base, $t2 = byte offset일 때 그 주소의 word를 $t0에 load하는 올바른 MIPS 코드를 쓰시오.",
  "add $t3, $t1, $t2\nlw  $t0, 0($t3)",keys=["주소를 먼저 add","offset은 상수 0"],slot=7,pts=6)
Q("4-oc-3","offset-const","mc","lw/sw의 offset이 반드시 상수여야 하는 이유는?",1,choices=["R-type이라서","I-type이라 offset이 명령어의 16-bit immediate 필드에 들어가서","ALU가 하나라서","레지스터가 32개라서"])
Q("4-oc-4","offset-const","ox","lbu도 I-type이므로 offset 자리에 레지스터를 쓸 수 없다.",True)
