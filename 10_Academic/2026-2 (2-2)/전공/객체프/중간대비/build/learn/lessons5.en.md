@unit U5 | Operator Overloading (Project 2 reference) | Operator Overloading (Proj2 참고).pdf + Project2/src/complex.cpp
@intro Material for Project 2 (inf_int). The project deadline (11/1) is after the exam, so a coding question is unlikely, but the difference between the member-function method and the friend (non-member) method may come up as a concept question.

@lesson L5-1 | Operator Functions: Member Method vs Non-Member (friend) Method | Operator Overloading p.1–3

## Operator Functions and the Two Methods {#opover-basic}

- **Operator function**: **redefines an operator** (`+ - * / [] << >>` …) **as a function**
- **Member function method**
  - Uses `this` to implicitly get one argument → the **left operand** of a binary operator
  - The **leftmost object must be of the same class** as the operator
  - `c = a + b;` → `c = a.operator+(b);`
- **Non-member function method**
  - Needs **parameters for both operands**
  - The left object can be of a **different class** (e.g. `cout << obj`)
  - Must be a **friend** to access private/protected data
  - `c = a + b;` → `c = operator+(a, b);`

> Exam point: "In the member method, what provides the left operand? (this)", "What must a non-member operator function be to access private data? (a friend)".

## Complex Example {#opover-complex}

**Non-member (friend) method**
```
class Complex {
private:
  double re, im;
public:
  Complex(double r, double i) : re(r), im(i) {}
  friend Complex operator+(Complex&, Complex&);
  friend Complex operator-(Complex&, Complex&);
  friend Complex operator*(Complex&, Complex&);
  void Display() { ... }
};
Complex operator+(Complex& i, Complex& other) {
  return Complex(i.re + other.re, i.im + other.im);
}
Complex operator*(Complex& i, Complex& other) {
  return Complex(i.re*other.re - i.im*other.im, i.re*other.im + i.im*other.re);
}
```
**Member method**
```
class Complex {
  ...
  Complex operator+(Complex& other);
};
Complex Complex::operator+(Complex& other) {
  return Complex(re + other.re, im + other.im);
}
```
- a = 1.2+3.4i, b = 5.6+7.8i → a+b = 6.8+11.2i, a−b = −4.4−4.4i, a×b = −19.8+28.4i (both methods give the same results)
- Project 2's `inf_int` uses the same approach to build an infinite-precision integer calculator supporting `+ - * ( )`. Because `inf_int` allocates its digits dynamically, it needs a **copy constructor, destructor and operator=** (L4-5)
