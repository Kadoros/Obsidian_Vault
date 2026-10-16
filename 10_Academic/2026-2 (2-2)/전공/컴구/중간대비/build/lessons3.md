@unit U3 | Ch.3 컴퓨터 연산 (정수 · 부동소수점) | week4-수업.pdf p.6–21 · week5-수업.pdf
@intro 곱셈·나눗셈은 "회로를 주고 과정을 보여라" 형식. 교수님이 "회로에 작은 변화가 있을 수 있으니 잘 보라"고 했어. 중간엔 product·multiplicand 8 bit, multiplier 4 bit 크기로만 나옴. 부동소수점은 필드 비트 수를 하나라도 틀리면 0점.

@lesson L3-1 | 덧셈 · 뺄셈 · 오버플로 | week4 p.6–13 | 오버플로 판정

## 정수 덧셈과 뺄셈 {#int-add}

- 덧셈은 십진수와 같음: 자리마다 더하고 2 이상이면 carry를 다음 자리로.
- 예: 7 + 6 = `0111 + 0110 = 1101` (13).
- **뺄셈 = 음수 더하기**: 7 − 6 = 7 + (−6). −6은 2의 보수(반전 + 1)로 만든다.

## 오버플로 판정 {#overflow}

결과가 표현 범위(예: 32-bit)를 넘으면 overflow.

| 연산 | 오버플로 조건 |
|---|---|
| 양수 + 음수 | **절대 없음** |
| 양수 + 양수 | 결과의 sign bit가 **1** |
| 음수 + 음수 | 결과의 sign bit가 **0** |
| 양수 − 양수, 음수 − 음수 | 없음 |
| 음수 − 양수 | 결과 sign이 **0** |
| 양수 − 음수 | 결과 sign이 **1** |

원리: 2의 보수에서 첫 비트가 부호. 양수 둘을 더해 음수가 나올 수 없으니 sign이 1이면 오버플로. 현대 CPU는 오버플로를 **exception**으로 처리.

@lesson L3-2 | 곱셈 하드웨어 | week4 p.14–18 · week5 p.5–8, 14–15 | 곱셈 과정 표

## 곱셈의 원리 {#mult-basic}

종이 곱셈과 같다: multiplier의 각 자리를 보고 1이면 multiplicand를 (자리만큼 shift해서) 더하고, 0이면 더하지 않음.
```
   multiplicand     1000
 × multiplier     × 1001
                    1000
                   0000
                  0000
                 1000
   product       1001000      (8 × 9 = 72)
```
n-bit × n-bit → 결과는 최대 **2n bit**.

## 원래 곱셈기 (first version) {#mult-v1}

구성: **Multiplicand 64-bit (Shift left)**, **Multiplier 32-bit (Shift right)**, **64-bit ALU**, **Product 64-bit**, Control test. (중간엔 8-bit / 4-bit / 8-bit로 축소)

알고리즘:
1. **Product = 0**으로 초기화.
2. Multiplier의 **LSB 검사**: 1이면 `Product = Product + Multiplicand` (ALU에 덧셈 신호), 0이면 아무것도 안 함.
3. 결과와 상관없이 **매 반복**: Multiplicand **왼쪽 shift**, Multiplier **오른쪽 shift**.
4. 32번(중간 크기에선 4번) 반복하면 끝. (교수님 설명: multiplier가 0이 되면 종료)

1000 × 1001:

| 반복 | 단계 | Multiplier | Multiplicand | Product |
|---|---|---|---|---|
| 0 | 초기값 | 1001 | 0000 1000 | 0000 0000 |
| 1 | LSB=1 → Prod += Mcand | 1001 | 0000 1000 | 0000 1000 |
| 1 | Mcand <<1, Mplier >>1 | 0100 | 0001 0000 | 0000 1000 |
| 2 | LSB=0 → 덧셈 없음, shift | 0010 | 0010 0000 | 0000 1000 |
| 3 | LSB=0 → 덧셈 없음, shift | 0001 | 0100 0000 | 0000 1000 |
| 4 | LSB=1 → Prod += Mcand | 0001 | 0100 0000 | 0100 1000 |
| 4 | shift | 0000 | 1000 0000 | **0100 1000** (= 72) |

## 개선된 곱셈기 (refined version) {#mult-v2}

구성: **Multiplicand 32-bit (shift 안 함)**, **32-bit ALU**, **Product 64-bit (Shift right)**. Multiplier 레지스터가 따로 없음.

알고리즘:
1. Product의 **아래 절반에 multiplier**를 넣고 위 절반은 0.
2. Product의 **LSB 검사**: 1이면 Product의 **위 절반에 multiplicand를 더함**.
3. 매 반복: Product 전체를 **오른쪽 shift**.
4. 종료: **shift 횟수 = multiplier 비트 수** (shift counter).

> 함정: 종료 조건의 기준은 **multiplier**의 비트 수. multiplicand 아님 (교수님: "be extremely careful it is not the multiplicand").

1000 × 1001:

| 반복 | 단계 | Product |
|---|---|---|
| 0 | 초기값 (아래 = multiplier) | 0000 1001 |
| 1 | LSB=1 → 위 절반 += 1000 | 1000 1001 |
| 1 | >> 1 | 0100 0100 |
| 2 | LSB=0, >> 1 | 0010 0010 |
| 3 | LSB=0, >> 1 | 0001 0001 |
| 4 | LSB=1 → 위 절반 += 1000 | 1001 0001 |
| 4 | >> 1 | **0100 1000** (= 72) |

## 수업 예제 1·2 (week5) {#mult-examples}

**Example 1: 1010 × 0010 (원래 곱셈기)** → 10 × 2 = 20

| 반복 | LSB | 동작 | Multiplier (shift 후) | Multiplicand (shift 후) | Product |
|---|---|---|---|---|---|
| 0 | | 초기값 | 0010 | 0000 1010 | 0000 0000 |
| 1 | 0 | 덧셈 없음 | 0001 | 0001 0100 | 0000 0000 |
| 2 | 1 | Prod += 0001 0100 | 0000 | 0010 1000 | 0001 0100 |
| 3 | 0 | 덧셈 없음 | 0000 | 0101 0000 | 0001 0100 |
| 4 | 0 | 덧셈 없음 | 0000 | 1010 0000 | **0001 0100** (= 20) |

**Example 2: 1010 × 1100 (개선 곱셈기)** → 10 × 12 = 120

| 반복 | LSB | 동작 | Product (동작 후) | Product (>>1 후) |
|---|---|---|---|---|
| 0 | | 초기값 | 0000 1100 | |
| 1 | 0 | 덧셈 없음 | 0000 1100 | 0000 0110 |
| 2 | 0 | 덧셈 없음 | 0000 0110 | 0000 0011 |
| 3 | 1 | 위 절반 += 1010 | 1010 0011 | 0101 0001 |
| 4 | 1 | 위 절반 += 1010 | 1111 0001 | **0111 1000** (= 120) |

## MIPS 곱셈 명령어 {#mult-instr}

- 64-bit 곱 결과용 레지스터 2개: **HI** (위 32 bit), **LO** (아래 32 bit).
- `mult rs, rt` / `multu rs, rt`: 64-bit 곱을 HI/LO에.
- `mfhi rd` / `mflo rd`: HI/LO를 rd로 옮김. HI를 보면 32 bit 오버플로 여부를 알 수 있음.
- `mul rd, rs, rt`: 곱의 아래 32 bit만 rd에.

@lesson L3-3 | 나눗셈 하드웨어 | week4 p.19–21 · week5 p.9–13, 16 | 나눗셈 과정 표

## 나눗셈의 원리 {#div-basic}

`Dividend = Quotient × Divisor + Remainder`. n-bit 피연산자 → n-bit 몫과 나머지.

- **0으로 나누는지 먼저 검사** (교안: "Always check for 0 divisor!!").
- Long division: divisor ≤ 지금 보고 있는 dividend 비트들이면 몫에 1 쓰고 빼기, 아니면 몫에 0 쓰고 다음 비트를 내림.
- **Restoring division**: 일단 빼 보고, 나머지가 **음수(<0)면 divisor를 다시 더해 원상 복구**.
- Signed division: 절댓값으로 나누고 몫·나머지 부호를 조정. **Dividend와 remainder는 같은 부호.**

교안 예: 1001010 ÷ 1000 = 몫 **1001**, 나머지 **10** (74 ÷ 8 = 9 … 2).

## 나눗셈기 (first version) {#div-v1}

구성: **Divisor 64-bit (Shift right, 처음엔 왼쪽 절반에)**, **64-bit ALU**, **Remainder 64-bit (처음엔 dividend)**, **Quotient 32-bit (Shift left)**.

알고리즘 (n+1번 반복):
1. `Remainder = Remainder − Divisor`
2. 결과 검사:
   - **≥ 0**: Quotient 왼쪽 shift, 새 LSB = **1**
   - **< 0**: `Remainder = Remainder + Divisor`로 **복구**, Quotient 왼쪽 shift, 새 LSB = **0**
3. Divisor **오른쪽 shift**.

> 함정: 음수인지는 결과의 **첫 비트(sign bit)**로 판단 (2의 보수). 음수면 반드시 다시 더해서(add back) 원래 값으로 되돌린 뒤 다음 자리로.

## 수업 예제 3: 0001 0100 ÷ 0010 {#div-example}

20 ÷ 2 = 10 … 0. 4-bit 나눗셈이라 **5번** 반복. Divisor 초기값 = 0010을 왼쪽 절반에 → `0010 0000`.

| 반복 | Rem − Div | 판정 | Quotient | Divisor (>>1 후) | Remainder |
|---|---|---|---|---|---|
| 0 | | 초기값 | 0000 | 0010 0000 | 0001 0100 |
| 1 | 1111 0100 | < 0 → 복구, 0 | 0000 | 0001 0000 | 0001 0100 |
| 2 | 0000 0100 | ≥ 0 → 1 | 0001 | 0000 1000 | 0000 0100 |
| 3 | 1111 1100 | < 0 → 복구, 0 | 0010 | 0000 0100 | 0000 0100 |
| 4 | 0000 0000 | ≥ 0 → 1 | 0101 | 0000 0010 | 0000 0000 |
| 5 | 1111 1110 | < 0 → 복구, 0 | **1010** | 0000 0001 | **0000 0000** |

결과: Quotient = 1010 (10), Remainder = 0.

## 개선된 나눗셈기 {#div-v2}

교안 week5 p.13: **Divisor 32-bit (shift 안 함)**, **32-bit ALU**, **Remainder 64-bit (Shift right / Shift left / Write)**. 몫이 Remainder 레지스터의 아래 절반에 쌓이고 나머지는 위 절반에 남음 (곱셈 개선판과 같은 아이디어: 레지스터 하나로 합치기).

@lesson L3-4 | IEEE 754 부동소수점 표현 | week5 p.17–26 | 32-bit 표현 쓰기

## IEEE 754 형식 {#ieee-format}

| | S | Exponent | Fraction | Bias |
|---|---|---|---|---|
| Single (float) | 1 | **8 bits** | **23 bits** | **127** |
| Double (double) | 1 | **11 bits** | **52 bits** | **1023** |

`x = (−1)^S × (1 + Fraction) × 2^(Exponent − Bias)`

- **S**: 0 = 음이 아님, 1 = 음수.
- **Normalized significand**: 1.0 ≤ |significand| < 2.0. 앞의 "1."은 항상 있으니 **저장하지 않음 (hidden bit)**.
- **Exponent는 excess(bias) 표현**: 저장값 = 실제 지수 + Bias. 그래서 exponent는 항상 unsigned.

> 함정: 필드 비트 수(1/8/23, 1/11/52)를 하나라도 틀리면 다른 필드까지 밀려서 **전부 0점** (교수님 5주).

## 변환 예제 {#ieee-examples}

**−0.75**: 0.75 = 0.11₂ = **1.1₂ × 2⁻¹** → S = 1, Exponent = −1 + 127 = 126 = `01111110`, Fraction = `1000…0`
```
1 01111110 10000000000000000000000   = 0xBF400000
```
Double: Exponent = −1 + 1023 = 1022 = `01111111110`, Fraction = `1000…0` (52 bit).

**0.625**: 0.101₂ = **1.01₂ × 2⁻¹** → S = 0, E = 126, F = `01000…0` → `0 01111110 01000000000000000000000` = 0x3F200000

**−3.75**: 11.11₂ = **1.111₂ × 2¹** → S = 1, E = 1 + 127 = 128 = `10000000`, F = `111000…0` → `1 10000000 11100000000000000000000` = 0xC0700000

순서: ① 부호 결정 ② 이진 소수로 변환 ③ 1.xxx × 2^e로 정규화 ④ e + bias ⑤ 소수점 뒤 비트를 fraction에 (나머지 0).

## 범위 · 특수값 · 정밀도 {#ieee-range}

Single에서 exponent `00000000`과 `11111111`은 **예약**:

| Exponent | Fraction | 의미 |
|---|---|---|
| 0 | 0 | **0** |
| 0 | ≠ 0 | **Denormal** (hidden bit = 0, `(0 + F) × 2^(−bias)`) |
| 255 | 0 | **±∞** |
| 255 | ≠ 0 | **NaN** (0.0/0.0 같은 정의 안 된 결과) |

- Single 최소(정규): exponent 1 → 1 − 127 = −126, ±1.0 × 2⁻¹²⁶ ≈ ±1.2 × 10⁻³⁸
- Single 최대: exponent 254 → +127, ≈ ±2.0 × 2¹²⁷ ≈ ±3.4 × 10³⁸
- Double: −1022 ~ +1023, ≈ ±2.2 × 10⁻³⁰⁸ ~ ±1.8 × 10³⁰⁸
- 정밀도: single ≈ 2⁻²³ → 약 **6자리** 십진 정밀도, double ≈ 2⁻⁵² → 약 **16자리**.
- Denormal은 정규화 수보다 작은 값을 표현해 **gradual underflow** 허용.

@lesson L3-5 | 부동소수점 덧셈 · 곱셈 · FP 명령어 | week5 p.27–31 | FP 연산 단계

## FP 덧셈 4단계 {#fp-add}

1. **Align**: 지수가 작은 쪽을 shift해서 큰 지수에 맞춤.
2. **Add significands**.
3. **Normalize** 하고 over/underflow 검사.
4. **Round**, 필요하면 다시 normalize.

십진 예: 9.999×10¹ + 1.610×10⁻¹ → 9.999×10¹ + 0.016×10¹ → 10.015×10¹ → 1.0015×10² → **1.002×10²**

이진 예: 0.5 + (−0.4375) = 1.000₂×2⁻¹ + (−1.110₂×2⁻²)
```
1. 1.000×2⁻¹ + (−0.111×2⁻¹)
2. 0.001×2⁻¹
3. 1.000×2⁻⁴  (over/underflow 없음)
4. 1.000×2⁻⁴ = 0.0625
```

## FP 곱셈 5단계 {#fp-mul}

1. **Add exponents** (biased면 합에서 bias를 한 번 빼기).
2. **Multiply significands**.
3. **Normalize**, over/underflow 검사.
4. **Round**, 필요하면 renormalize.
5. **부호 결정** (피연산자 부호로).

이진 예: 0.5 × (−0.4375) = 1.000₂×2⁻¹ × (−1.110₂×2⁻²)
```
1. 지수: −1 + −2 = −3   (biased: (−1+127) + (−2+127) − 127 = −3 + 127)
2. 1.000 × 1.110 = 1.110  → 1.110×2⁻³
3. 정규화 그대로, over/underflow 없음
4. 반올림 그대로
5. +ve × −ve → −ve :  −1.110×2⁻³ = −0.21875
```
> 함정: biased 지수끼리 더하면 bias가 두 번 들어가니까 **127을 한 번 빼야** 한다.

## FP 하드웨어와 명령어 {#fp-instr}

- 보통 FP 전용 하드웨어(여러 사이클): 덧셈·뺄셈·곱셈·나눗셈·역수·제곱근, FP ↔ 정수 변환.
- **별도의 FP 레지스터**: single 32개 `$f0–$f31`, double은 짝으로 `$f0/$f1`, `$f2/$f3`…
- FP 명령어는 FP 레지스터에서만 동작 (정수 연산을 FP 데이터에 하지 않음) → 코드 크기 영향 적게 레지스터를 늘림.
