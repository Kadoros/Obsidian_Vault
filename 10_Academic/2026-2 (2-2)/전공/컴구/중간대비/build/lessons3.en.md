@unit U3 | Ch.3 Arithmetic for Computers (Integer · Floating Point) | week4-수업.pdf p.6–21 · week5-수업.pdf
@intro Multiplication and division come as "given the circuit, show the process". The professor said "there may be small changes in the circuit, so look carefully". On the midterm the sizes are only product/multiplicand 8 bits and multiplier 4 bits. In floating point, getting even one field's bit count wrong gets zero points.

@lesson L3-1 | Addition · Subtraction · Overflow | week4 p.6–13 | Detecting overflow

## Integer Addition and Subtraction {#int-add}

- Addition works like decimal: add digit by digit, and if a column reaches 2 or more, carry to the next column.
- Example: 7 + 6 = `0111 + 0110 = 1101` (13).
- **Subtraction = adding the negative**: 7 − 6 = 7 + (−6). Make −6 using two's complement (invert + 1).

## Detecting Overflow {#overflow}

Overflow occurs if the result is out of range (e.g., 32 bits).

| Operation | Overflow condition |
|---|---|
| Positive + negative | **None** |
| Positive + positive | Result sign bit is **1** |
| Negative + negative | Result sign bit is **0** |
| Positive − positive, negative − negative | None |
| Negative − positive | Result sign is **0** |
| Positive − negative | Result sign is **1** |

Why: in two's complement the first bit is the sign. Adding two positives cannot give a negative, so a sign bit of 1 means overflow. Modern CPUs handle overflow as an **exception**.

@lesson L3-2 | Multiplication Hardware | week4 p.14–18 · week5 p.5–8, 14–15 | Multiplication step table

## How Multiplication Works {#mult-basic}

Same as long multiplication on paper: look at each digit of the multiplier; if it is 1, add the multiplicand (shifted by that position); if it is 0, add nothing.
```
   multiplicand     1000
 × multiplier     × 1001
                    1000
                   0000
                  0000
                 1000
   product       1001000      (8 × 9 = 72)
```
n-bit × n-bit → the product is up to **2n bits** long.

## The Original Multiplier (first version) {#mult-v1}

Components: **Multiplicand 64-bit (Shift left)**, **Multiplier 32-bit (Shift right)**, **64-bit ALU**, **Product 64-bit**, Control test. (Scaled down to 8-bit / 4-bit / 8-bit on the midterm.)

Algorithm:
1. Initialize **Product = 0**.
2. **Test the LSB** of the Multiplier: if 1, `Product = Product + Multiplicand` (send an add signal to the ALU); if 0, do nothing.
3. **Every iteration**, regardless of the result: shift the Multiplicand **left** and the Multiplier **right**.
4. Done after 32 repetitions (4 at midterm size). (As the professor explained: it ends when the multiplier becomes 0.)

1000 × 1001:

| Iteration | Step | Multiplier | Multiplicand | Product |
|---|---|---|---|---|
| 0 | Initial values | 1001 | 0000 1000 | 0000 0000 |
| 1 | LSB=1 → Prod += Mcand | 1001 | 0000 1000 | 0000 1000 |
| 1 | Mcand <<1, Mplier >>1 | 0100 | 0001 0000 | 0000 1000 |
| 2 | LSB=0 → no add, shift | 0010 | 0010 0000 | 0000 1000 |
| 3 | LSB=0 → no add, shift | 0001 | 0100 0000 | 0000 1000 |
| 4 | LSB=1 → Prod += Mcand | 0001 | 0100 0000 | 0100 1000 |
| 4 | shift | 0000 | 1000 0000 | **0100 1000** (= 72) |

## The Refined Multiplier (refined version) {#mult-v2}

Components: **Multiplicand 32-bit (not shifted)**, **32-bit ALU**, **Product 64-bit (Shift right)**. There is no separate Multiplier register.

Algorithm:
1. Put the **multiplier in the lower half** of Product and 0 in the upper half.
2. **Test the LSB** of Product: if 1, **add the multiplicand to the upper half** of Product.
3. Every iteration: **shift the whole Product right**.
4. Termination: **number of shifts = number of bits in the multiplier** (shift counter).

> Trap: The termination condition counts the bits of the **multiplier**, not the multiplicand (the professor: "be extremely careful it is not the multiplicand").

1000 × 1001:

| Iteration | Step | Product |
|---|---|---|
| 0 | Initial value (lower half = multiplier) | 0000 1001 |
| 1 | LSB=1 → upper half += 1000 | 1000 1001 |
| 1 | >> 1 | 0100 0100 |
| 2 | LSB=0, >> 1 | 0010 0010 |
| 3 | LSB=0, >> 1 | 0001 0001 |
| 4 | LSB=1 → upper half += 1000 | 1001 0001 |
| 4 | >> 1 | **0100 1000** (= 72) |

## Class Examples 1 and 2 (Week 5) {#mult-examples}

**Example 1: 1010 × 0010 (original multiplier)** → 10 × 2 = 20

| Iteration | LSB | Action | Multiplier (after shift) | Multiplicand (after shift) | Product |
|---|---|---|---|---|---|
| 0 | | Initial values | 0010 | 0000 1010 | 0000 0000 |
| 1 | 0 | No add | 0001 | 0001 0100 | 0000 0000 |
| 2 | 1 | Prod += 0001 0100 | 0000 | 0010 1000 | 0001 0100 |
| 3 | 0 | No add | 0000 | 0101 0000 | 0001 0100 |
| 4 | 0 | No add | 0000 | 1010 0000 | **0001 0100** (= 20) |

**Example 2: 1010 × 1100 (refined multiplier)** → 10 × 12 = 120

| Iteration | LSB | Action | Product (after action) | Product (after >>1) |
|---|---|---|---|---|
| 0 | | Initial value | 0000 1100 | |
| 1 | 0 | No add | 0000 1100 | 0000 0110 |
| 2 | 0 | No add | 0000 0110 | 0000 0011 |
| 3 | 1 | Upper half += 1010 | 1010 0011 | 0101 0001 |
| 4 | 1 | Upper half += 1010 | 1111 0001 | **0111 1000** (= 120) |

## MIPS Multiplication Instructions {#mult-instr}

- Two registers hold the 64-bit product: **HI** (upper 32 bits) and **LO** (lower 32 bits).
- `mult rs, rt` / `multu rs, rt`: 64-bit product into HI/LO.
- `mfhi rd` / `mflo rd`: move HI/LO to rd. Checking HI tells you whether the product overflows 32 bits.
- `mul rd, rs, rt`: only the lower 32 bits of the product go to rd.

@lesson L3-3 | Division Hardware | week4 p.19–21 · week5 p.9–13, 16 | Division step table

## How Division Works {#div-basic}

`Dividend = Quotient × Divisor + Remainder`. n-bit operands yield an n-bit quotient and remainder.

- **Check for a 0 divisor first** (slide: "Always check for 0 divisor!!").
- Long division approach: if divisor ≤ the dividend bits currently being examined, put 1 in the quotient and subtract; otherwise put 0 in the quotient and bring down the next dividend bit.
- **Restoring division**: do the subtract, and if the remainder goes **negative (< 0), add the divisor back** to restore it.
- Signed division: divide using absolute values, then adjust the signs of the quotient and remainder as required. **The dividend and remainder must have the same sign.**

Slide example: 1001010 ÷ 1000 = quotient **1001**, remainder **10** (74 ÷ 8 = 9 remainder 2).

## The Divider (first version) {#div-v1}

Components: **Divisor 64-bit (Shift right, initially in the left half)**, **64-bit ALU**, **Remainder 64-bit (initially the dividend)**, **Quotient 32-bit (Shift left)**.

Algorithm (repeat n+1 times):
1. `Remainder = Remainder − Divisor`
2. Test the result:
   - **≥ 0**: shift Quotient left, new LSB = **1**
   - **< 0**: **restore** with `Remainder = Remainder + Divisor`, shift Quotient left, new LSB = **0**
3. Shift Divisor **right**.

> Trap: Whether the result is negative is decided by its **first bit (sign bit)** (two's complement). If it is negative, you must add the divisor back to restore the original value before moving on to the next bit.

## Class Example 3: 0001 0100 ÷ 0010 {#div-example}

20 ÷ 2 = 10 remainder 0. A 4-bit division, so **5** iterations. Initial Divisor = 0010 in the left half → `0010 0000`.

| Iteration | Rem − Div | Decision | Quotient | Divisor (after >>1) | Remainder |
|---|---|---|---|---|---|
| 0 | | Initial values | 0000 | 0010 0000 | 0001 0100 |
| 1 | 1111 0100 | < 0 → restore, 0 | 0000 | 0001 0000 | 0001 0100 |
| 2 | 0000 0100 | ≥ 0 → 1 | 0001 | 0000 1000 | 0000 0100 |
| 3 | 1111 1100 | < 0 → restore, 0 | 0010 | 0000 0100 | 0000 0100 |
| 4 | 0000 0000 | ≥ 0 → 1 | 0101 | 0000 0010 | 0000 0000 |
| 5 | 1111 1110 | < 0 → restore, 0 | **1010** | 0000 0001 | **0000 0000** |

Result: Quotient = 1010 (10), Remainder = 0.

## The Refined Divider {#div-v2}

Slide week5 p.13: **Divisor 32-bit (not shifted)**, **32-bit ALU**, **Remainder 64-bit (Shift right / Shift left / Write)**. The quotient accumulates in the lower half of the Remainder register and the remainder stays in the upper half (same idea as the refined multiplier: merge into one register).

@lesson L3-4 | IEEE 754 Floating-Point Representation | week5 p.17–26 | Writing the 32-bit representation

## The IEEE 754 Format {#ieee-format}

| | S | Exponent | Fraction | Bias |
|---|---|---|---|---|
| Single (float) | 1 | **8 bits** | **23 bits** | **127** |
| Double (double) | 1 | **11 bits** | **52 bits** | **1023** |

`x = (−1)^S × (1 + Fraction) × 2^(Exponent − Bias)`

- **S**: 0 = non-negative, 1 = negative.
- **Normalized significand**: 1.0 ≤ |significand| < 2.0. The leading "1." is always there, so it is **not stored (hidden bit)**.
- **The exponent uses excess (biased) representation**: stored value = actual exponent + Bias. So the stored exponent is always unsigned.

> Trap: If you get any field width wrong (1/8/23, 1/11/52), the other fields shift too and the **whole answer gets zero points** (the professor, Week 5).

## Conversion Examples {#ieee-examples}

**−0.75**: 0.75 = 0.11₂ = **1.1₂ × 2⁻¹** → S = 1, Exponent = −1 + 127 = 126 = `01111110`, Fraction = `1000…0`
```
1 01111110 10000000000000000000000   = 0xBF400000
```
Double: Exponent = −1 + 1023 = 1022 = `01111111110`, Fraction = `1000…0` (52 bits).

**0.625**: 0.101₂ = **1.01₂ × 2⁻¹** → S = 0, E = 126, F = `01000…0` → `0 01111110 01000000000000000000000` = 0x3F200000

**−3.75**: 11.11₂ = **1.111₂ × 2¹** → S = 1, E = 1 + 127 = 128 = `10000000`, F = `111000…0` → `1 10000000 11100000000000000000000` = 0xC0700000

Steps: ① determine the sign ② convert to a binary fraction ③ normalize to 1.xxx × 2^e ④ e + bias ⑤ put the bits after the binary point into the fraction (rest 0).

## Range · Special Values · Precision {#ieee-range}

In single precision, exponents `00000000` and `11111111` are **reserved**:

| Exponent | Fraction | Meaning |
|---|---|---|
| 0 | 0 | **0** |
| 0 | ≠ 0 | **Denormal** (hidden bit = 0, `(0 + F) × 2^(−bias)`) |
| 255 | 0 | **±∞** |
| 255 | ≠ 0 | **NaN** (undefined result such as 0.0/0.0) |

- Single smallest (normalized): exponent 1 → 1 − 127 = −126, ±1.0 × 2⁻¹²⁶ ≈ ±1.2 × 10⁻³⁸
- Single largest: exponent 254 → +127, ≈ ±2.0 × 2¹²⁷ ≈ ±3.4 × 10³⁸
- Double: −1022 to +1023, ≈ ±2.2 × 10⁻³⁰⁸ to ±1.8 × 10³⁰⁸
- Precision: single ≈ 2⁻²³ → about **6 decimal digits**; double ≈ 2⁻⁵² → about **16 digits**.
- Denormals represent values smaller than the normalized numbers, allowing **gradual underflow**.

@lesson L3-5 | Floating-Point Addition · Multiplication · FP Instructions | week5 p.27–31 | FP operation steps

## FP Addition in 4 Steps {#fp-add}

1. **Align**: shift the number with the smaller exponent to match the larger exponent.
2. **Add significands**.
3. **Normalize** the result and check for over/underflow.
4. **Round**, and renormalize if necessary.

Decimal example: 9.999×10¹ + 1.610×10⁻¹ → 9.999×10¹ + 0.016×10¹ → 10.015×10¹ → 1.0015×10² → **1.002×10²**

Binary example: 0.5 + (−0.4375) = 1.000₂×2⁻¹ + (−1.110₂×2⁻²)
```
1. 1.000×2⁻¹ + (−0.111×2⁻¹)
2. 0.001×2⁻¹
3. 1.000×2⁻⁴  (no over/underflow)
4. 1.000×2⁻⁴ = 0.0625
```

## FP Multiplication in 5 Steps {#fp-mul}

1. **Add exponents** (for biased exponents, subtract the bias once from the sum).
2. **Multiply significands**.
3. **Normalize**, check for over/underflow.
4. **Round**, renormalize if necessary.
5. **Determine the sign** (from the operands' signs).

Binary example: 0.5 × (−0.4375) = 1.000₂×2⁻¹ × (−1.110₂×2⁻²)
```
1. exponent: −1 + −2 = −3   (biased: (−1+127) + (−2+127) − 127 = −3 + 127)
2. 1.000 × 1.110 = 1.110  → 1.110×2⁻³
3. already normalized, no over/underflow
4. rounding leaves it unchanged
5. +ve × −ve → −ve :  −1.110×2⁻³ = −0.21875
```
> Trap: Adding two biased exponents counts the bias twice, so you must **subtract 127 once**.

## FP Hardware and Instructions {#fp-instr}

- Usually dedicated FP hardware (multi-cycle): addition, subtraction, multiplication, division, reciprocal, square root, FP ↔ integer conversion.
- **Separate FP registers**: 32 single-precision `$f0–$f31`; doubles use pairs `$f0/$f1`, `$f2/$f3`, …
- FP instructions operate only on FP registers (integer operations are not applied to FP data) → more registers with minimal impact on code size.
