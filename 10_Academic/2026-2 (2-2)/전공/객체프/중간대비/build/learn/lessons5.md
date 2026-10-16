@unit U5 | 연산자 오버로딩 (Project 2 참고) | Operator Overloading (Proj2 참고).pdf + Project2/src/complex.cpp
@intro Project 2(inf_int)용 자료. 프로젝트 마감(11/1)이 시험 뒤라 코딩 문제로 나올 가능성은 낮지만, 멤버 함수 방식과 friend(비멤버) 방식의 차이는 개념 문제로 나올 수 있어.

@lesson L5-1 | 연산자 함수: 멤버 방식 vs 비멤버(friend) 방식 | Operator Overloading p.1–3

## 연산자 함수와 두 가지 방식 {#opover-basic}

- **연산자 함수 (operator function)**: 연산자(`+ - * / [] << >>` …)를 **함수로 다시 정의**
- **멤버 함수 방식**
  - `this`로 인자 하나를 암묵적으로 받음 → 이항 연산자의 **왼쪽 피연산자**
  - **가장 왼쪽 객체가 연산자와 같은 클래스**여야 함
  - `c = a + b;` → `c = a.operator+(b);`
- **비멤버 함수 방식**
  - **두 피연산자 모두 매개변수**로 받음
  - 왼쪽 객체가 **다른 클래스**여도 됨 (예: `cout << obj`)
  - private/protected 데이터에 접근하려면 **friend**여야 함
  - `c = a + b;` → `c = operator+(a, b);`

> 시험 포인트: "멤버 방식에서 왼쪽 피연산자는 무엇으로 받나 (this)", "비멤버 방식이 private에 접근하려면 (friend)".

## Complex 예제 {#opover-complex}

**비멤버(friend) 방식**
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
**멤버 방식**
```
class Complex {
  ...
  Complex operator+(Complex& other);
};
Complex Complex::operator+(Complex& other) {
  return Complex(re + other.re, im + other.im);
}
```
- a = 1.2+3.4i, b = 5.6+7.8i → a+b = 6.8+11.2i, a−b = −4.4−4.4i, a×b = −19.8+28.4i (두 방식 결과 같음)
- Project 2의 `inf_int`도 같은 방식으로 `+ - * ( )`를 지원하는 무한 정수 계산기를 만든다. `inf_int`는 자릿수를 동적 할당하므로 **복사 생성자·소멸자·operator=** 가 필요 (L4-5)
