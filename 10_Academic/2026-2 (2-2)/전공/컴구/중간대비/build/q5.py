from qdsl import Q
from sim import CTRL
# ───────── 보강 (재시험용 여유 문항) ─────────
Q("5-ex-1","encode-example","calc","C 코드 `A[10] = A[10] + 7;`을 MIPS로 쓰고 각 명령어의 필드를 10진수로 쓰시오. A의 base = $s0 (16). (lw 35, sw 43, addi 8, $t0 = 8)",
  "lw   $t0, 40($s0)     → 35 | 16 | 8 | 40\naddi $t0, $t0, 7      → 8 | 8 | 8 | 7\nsw   $t0, 40($s0)     → 43 | 16 | 8 | 40",keys=["offset 40","lw 35 16 8 40","addi 8 8 8 7","sw 43 16 8 40"],slot=8,pts=6)
Q("5-ft-1","fact-trace","calc","fact(2)를 200번지의 jal로 호출, $sp 초기값 1000. 각 프레임의 $sp와 저장 값(a0, ra), 최종 $v0를 쓰시오.",
  "fact(2): $sp 992, a0 = 2, ra = 204\nfact(1): $sp 984, a0 = 1, ra = L1+8\nfact(0): $sp 976, a0 = 0, ra = L1+8 → $v0 = 1\n복귀하며 $v0 = 1 → 1 → 2, $sp = 1000, jr → 204",keys=["992/984/976","첫 ra 204","$v0 = 2"],slot=10,pts=8)
Q("5-sw-1","dp-sw","short","sw $t0, 12($s1)이 p.3 데이터패스에서 실행될 때 rt($t0)의 값이 가는 경로와 켜지는 신호를 쓰시오. (영어로)",
  "rs ($s1) is read and added to the sign-extended offset 12 in the ALU (ALUSrc = 1, ALUOp = 00) to form the address. rt ($t0) is read as Read data 2 and goes directly to the data memory's Write data input; MemWrite = 1 writes it. RegWrite = 0, MemRead = 0, RegDst and MemtoReg are X.",
  keys=["주소 = $s1 + 12 (ALUSrc 1)","rt 값 = Read data 2 → Write data","MemWrite = 1","RegWrite = 0, RegDst·MemtoReg X"],slot=16,pts=9)
Q("5-oc-1","offset-const","calc","`x = A[i];`(x: $s0, i: $s1, A base: $s2, int 배열)를 offset 규칙을 지켜 MIPS로 쓰고, `lw $s0, $s1($s2)`가 왜 틀렸는지 한 줄로 쓰시오.",
  "sll $t0, $s1, 2\nadd $t0, $t0, $s2\nlw  $s0, 0($t0)\nlw는 I-type이라 offset이 16-bit 상수 필드에 들어가므로 레지스터를 쓸 수 없다.",keys=["sll ×4","add base","lw 0($t0)","offset은 상수(I-type)"],slot=7,pts=6)
Q("5-bd-1","branch-design","mc","beq/bne만 하드웨어로 두고 <, ≥ 분기를 slt 조합으로 만드는 선택은 어느 설계 원칙의 예인가?",3,choices=["Smaller is faster","Simplicity favors regularity","Make the common case fast","Good design demands good compromises"])
Q("5-rt-1","dp-rtype","sig","p.3 데이터패스에서 `slt $t0, $s1, $s2`의 제어 신호 값을 채우시오.",CTRL["R"],explain="slt도 R-type. 연산 종류는 funct(101010)로 ALU control이 정함.")
