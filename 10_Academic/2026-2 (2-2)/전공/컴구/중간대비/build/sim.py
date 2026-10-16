# 계산 문제 정답 검산기: 곱셈·나눗셈 하드웨어 단계, IEEE 754, MIPS 인코딩, 제어 신호, ALU control
# python3 sim.py  → 교안 예제 전부 출력 (레슨·문제의 표는 여기서 나온 값을 그대로 씀)
import struct

def b(x, n): return format(x & ((1 << n) - 1), f'0{n}b')

def mult_v1(mcand, mplier, n=4):
    """원래 곱셈기: multiplicand 2n-bit (shift left), multiplier n-bit (shift right), product 2n-bit"""
    M, Q, P = mcand, mplier, 0
    rows = [("init", "", b(Q, n), b(M, 2*n), b(P, 2*n))]
    for i in range(1, n+1):
        lsb = Q & 1
        if lsb: P = (P + M) & ((1 << 2*n) - 1); act = "1a. Prod = Prod + Mcand"
        else: act = "1. LSB=0, no add"
        rows.append((f"{i}", act, b(Q, n), b(M, 2*n), b(P, 2*n)))
        M = (M << 1) & ((1 << 2*n) - 1); Q >>= 1
        rows.append((f"{i}", "2. Mcand << 1, 3. Mplier >> 1", b(Q, n), b(M, 2*n), b(P, 2*n)))
    return P, rows

def mult_v2(mcand, mplier, n=4):
    """개선 곱셈기: product 2n-bit, 처음에 아래 n bit = multiplier. LSB=1이면 위 n bit에 multiplicand 더하고, 매번 product >> 1"""
    P = mplier
    rows = [("init", "", b(mcand, n), b(P, 2*n))]
    for i in range(1, n+1):
        if P & 1:
            hi = (P >> n) + mcand          # n+1 bit 가능 (carry)
            P = (hi << n) | (P & ((1 << n) - 1)); act = "LSB=1: 위 절반 += Mcand"
            rows.append((f"{i}", act, b(mcand, n), b(P, 2*n+1) if P >> 2*n else b(P, 2*n)))
        else:
            rows.append((f"{i}", "LSB=0: 덧셈 없음", b(mcand, n), b(P, 2*n)))
        P >>= 1
        rows.append((f"{i}", "Product >> 1", b(mcand, n), b(P, 2*n)))
    return P, rows

def div_v1(dividend, divisor, n=4):
    """원래(restoring) 나눗셈기: divisor 2n-bit 처음엔 왼쪽 절반, remainder 2n-bit = dividend, quotient n-bit. n+1번 반복"""
    D, R, Q = divisor << n, dividend, 0
    mask = (1 << 2*n) - 1
    rows = [("init", "", b(Q, n), b(D, 2*n), b(R, 2*n))]
    for i in range(1, n+2):
        R = (R - D)
        rows.append((f"{i}", "1. Rem = Rem − Div", b(Q, n), b(D, 2*n), b(R, 2*n) + (" (<0)" if R < 0 else " (≥0)")))
        if R < 0:
            R += D; Q = (Q << 1) & ((1 << n) - 1)
            rows.append((f"{i}", "2b. Rem<0: Rem += Div, Quo << 1 (LSB 0)", b(Q, n), b(D, 2*n), b(R, 2*n)))
        else:
            Q = ((Q << 1) | 1) & ((1 << n) - 1)
            rows.append((f"{i}", "2a. Rem≥0: Quo << 1, LSB = 1", b(Q, n), b(D, 2*n), b(R, 2*n)))
        D >>= 1
        rows.append((f"{i}", "3. Div >> 1", b(Q, n), b(D, 2*n), b(R, 2*n)))
    return Q, R, rows

def ieee(x, double=False):
    if double:
        bits = struct.unpack('>Q', struct.pack('>d', x))[0]; s, e, f = bits >> 63, (bits >> 52) & 0x7ff, bits & ((1 << 52) - 1)
        return s, b(e, 11), b(f, 52), format(bits, '016X')
    bits = struct.unpack('>I', struct.pack('>f', x))[0]; s, e, f = bits >> 31, (bits >> 23) & 0xff, bits & ((1 << 23) - 1)
    return s, b(e, 8), b(f, 23), format(bits, '08X')

REG = {"$zero":0,"$at":1,"$v0":2,"$v1":3,**{f"$a{i}":4+i for i in range(4)},**{f"$t{i}":8+i for i in range(8)},
       **{f"$s{i}":16+i for i in range(8)},"$t8":24,"$t9":25,"$gp":28,"$sp":29,"$fp":30,"$ra":31}
FUNCT = {"add":32,"sub":34,"and":36,"or":37,"slt":42,"sll":0,"srl":2,"nor":39,"jr":8}
OPC = {"lw":35,"sw":43,"beq":4,"bne":5,"addi":8,"slti":10,"andi":12,"ori":13,"lui":15,"j":2,"jal":3}

def enc_r(op, rd, rs, rt, shamt=0):
    w = (0 << 26) | (REG[rs] << 21) | (REG[rt] << 16) | (REG[rd] << 11) | (shamt << 6) | FUNCT[op]
    return w, f"{b(0,6)} {b(REG[rs],5)} {b(REG[rt],5)} {b(REG[rd],5)} {b(shamt,5)} {b(FUNCT[op],6)}", f"0x{w:08X}"

def enc_i(op, rt, rs, imm):
    w = (OPC[op] << 26) | (REG[rs] << 21) | (REG[rt] << 16) | (imm & 0xffff)
    return w, f"{b(OPC[op],6)} {b(REG[rs],5)} {b(REG[rt],5)} {b(imm,16)}", f"0x{w:08X}"

# 제어 신호 (교안 week6 p.31 표)
CTRL = {
 "R":   dict(RegDst=1, ALUSrc=0, MemtoReg=0, RegWrite=1, MemRead=0, MemWrite=0, Branch=0, ALUOp1=1, ALUOp0=0),
 "lw":  dict(RegDst=0, ALUSrc=1, MemtoReg=1, RegWrite=1, MemRead=1, MemWrite=0, Branch=0, ALUOp1=0, ALUOp0=0),
 "sw":  dict(RegDst="X", ALUSrc=1, MemtoReg="X", RegWrite=0, MemRead=0, MemWrite=1, Branch=0, ALUOp1=0, ALUOp0=0),
 "beq": dict(RegDst="X", ALUSrc=0, MemtoReg="X", RegWrite=0, MemRead=0, MemWrite=0, Branch=1, ALUOp1=0, ALUOp0=1),
}

def alu_control(aluop, funct):
    """K-map 결과 (교안 식에는 NOT 표시가 빠져 있음): Op3=0, Op2=ALUOp0+ALUOp1·F1, Op1=¬ALUOp1+¬F2, Op0=ALUOp1·(F3+F0)"""
    a1, a0 = aluop >> 1 & 1, aluop & 1
    F = [(funct >> i) & 1 for i in range(6)]
    op2 = a0 | (a1 & F[1]); op1 = (1 - a1) | (1 - F[2]); op0 = a1 & (F[3] | F[0])
    return f"0{op2}{op1}{op0}"

if __name__ == "__main__":
    def show(rows, head):
        print(" | ".join(head)); [print(" | ".join(r)) for r in rows]; print()
    print("== week4 p.14–17: 1000 × 1001 (원래 곱셈기)"); P, r = mult_v1(0b1000, 0b1001); show(r, ["iter","step","Mplier","Mcand","Product"]); print("=", b(P, 8), P)
    print("== week4 p.17: 1000 × 1001 (개선 곱셈기)"); P, r = mult_v2(0b1000, 0b1001); show(r, ["iter","step","Mcand","Product"]); print("=", b(P, 8), P)
    print("== week5 Ex1: 1010 × 0010 (원래 곱셈기)"); P, r = mult_v1(0b1010, 0b0010); show(r, ["iter","step","Mplier","Mcand","Product"]); print("=", b(P, 8), P)
    print("== week5 Ex2: 1010 × 1100 (개선 곱셈기)"); P, r = mult_v2(0b1010, 0b1100); show(r, ["iter","step","Mcand","Product"]); print("=", b(P, 8), P)
    print("== week5 Ex3: 0001 0100 ÷ 0010 (나눗셈기)"); Q, R, r = div_v1(0b00010100, 0b0010); show(r, ["iter","step","Quot","Divisor","Remainder"]); print("Q =", b(Q, 4), Q, " R =", R)
    print("== week4 p.19: 1001010 ÷ 1000"); print(0b1001010 // 0b1000, 0b1001010 % 0b1000)
    for x in [-0.75, 0.625, -3.75, 0.5, -0.4375, 0.0625, -0.21875]: print("IEEE", x, ieee(x))
    print("IEEE double -0.75", ieee(-0.75, True))
    print("add $t0,$s1,$s2", enc_r("add", "$t0", "$s1", "$s2"))
    print("lw $t0,1200($t1)", enc_i("lw", "$t0", "$t1", 1200)); print("sw $t0,1200($t1)", enc_i("sw", "$t0", "$t1", 1200))
    print("add $t0,$s2,$t0", enc_r("add", "$t0", "$s2", "$t0"))
    print("sub $s0,$t0,$t1", enc_r("sub", "$s0", "$t0", "$t1"))
    print("lw $t0,32($s3)", enc_i("lw", "$t0", "$s3", 32)); print("addi $s3,$s3,-1", enc_i("addi", "$s3", "$s3", -1))
    print("beq $t0,$t1,3", enc_i("beq", "$t1", "$t0", 3))
    print("-10 =", b(-10, 32), format(-10 & 0xffffffff, '08X'))
    for name, ao, fn in [("lw",0,0),("sw",0,0),("beq",1,0),("add",2,0b100000),("sub",2,0b100010),("and",2,0b100100),("or",2,0b100101),("slt",2,0b101010)]:
        print("ALU control", name, alu_control(ao, fn))
    print("CPU time A/B", 600/500, " CPI seq", (2*1+1*2+2*3)/5, (4*1+1*2+1*3)/6, " MIPS", 4e9/(1.0e6), 4e9/(1.1e6), " time", 10e9*1.0/4e9, 8e9*1.1/4e9, " power", 0.85**4)
