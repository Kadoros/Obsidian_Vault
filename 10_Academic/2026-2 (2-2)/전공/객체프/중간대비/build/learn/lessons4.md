@unit U4 | C++ 데이터 추상화: class | L04 C++ Data Abstraction.pdf + Handout 2 + 보충 자료
@intro 교수님이 "이 수업에서 가장 중요한 부분"이라고 한 단원. 데이터 추상화·캡슐화·정보 은닉, 캡슐화의 이점 3가지, public 데이터를 피하는 이유 3가지, 생성자, 복사 생성자, static, const 멤버 함수, inline, friend, 참조, 인자 전달 방식까지. 10/7 수업은 생성자까지 나갔고 10/14 수업은 녹음 전사가 없어. 그 뒤 내용도 기출 단골이라 같이 정리했어.

@lesson L4-1 | 데이터 추상화 · 캡슐화 · 정보 은닉 | L04 p.2–4 + Handout 2

## 세 용어 {#abs-encap}

| 용어 | 정의 |
|---|---|
| **Data Abstraction** | 불필요한 세부를 감추는, 적절한 기능을 가진 클래스를 만드는 것 |
| **Data Encapsulation** | 구현이 인터페이스로 **감싸여(encapsulated)** 있어서, 구현에 **합법적으로 접근하는 유일한 방법이 인터페이스**인 것 |
| **Information Hiding** | 구현이 사용자로부터 **숨겨져** 있는 것 |

- 세 용어는 **거의 같은 개념**, 강조점만 조금 다름 (추상화 = 핵심만 보여주기, 캡슐화 = 데이터와 함수를 묶어 인터페이스로만 접근, 은닉 = 숨기기)

> 시험 포인트: 교수님이 "취업 면접에서도 나오는 질문, 이 슬라이드가 가장 중요하다"고 함. 모범 답안 = **"Separation of interface and implementation, such that the implementation is hidden from the user and the only way to access it is through the interface."**

## 내부 관점과 외부 관점 {#two-views}

- **데이터 추상화 = 인터페이스와 구현의 분리 (separation of interface and implementation)**
- **Interface**: 바깥, 즉 **서비스 관점(service view)**. 객체가 **무엇을(what)** 하는지 기술
- **Implementation**: 안쪽 관점. **어떻게(how)** 하는지 기술
- **Service view**: 객체가 **어떻게** 일을 수행하는지 몰라도 **제공하는 서비스**로 객체를 특징짓는 능력
- 예) 프로젝터: 버튼(화면 올리기·내리기, 켜기·끄기) = 인터페이스, 안의 회로 = 구현. 사용자는 버튼만 알면 됨

> 시험 포인트: 2019·2016 빈칸 "(Data abstraction) is a technique that relies on the separation of interface and implementation. Interface … describes (what) an object does. Implementation describes (how) it does".

## 데이터 캡슐화의 이점 3가지 (Handout 2) {#encap-benefits}

1. **Protection of implementation (safety)**: 클라이언트는 캡슐화된 데이터에 **직접 접근할 수 없다**
2. **Readability (understandability)**: 인터페이스를 쓰는 클라이언트는 인터페이스 함수들이 캡슐화된 정보를 **어떻게 쓰는지 알 필요가 없다**
3. **Implementation independence**: **구현의 변경이 클라이언트가 보는 인터페이스에 영향을 주지 않는다**. 캡슐화된 구현은 구현자가 인터페이스를 건드리지 않고 **자유롭게 바꿀 수 있게** 해준다 (클라이언트가 인터페이스를 쓰는 방식은 구현과 독립)

> 시험 포인트: **최다 출제**. 2025·2022·2017 "List three main benefits … explain each", 2023 빈칸 "(implementation independence) means (a change) in implementation should not affect (the interface) seen by clients", 2019 "(1) Clients cannot (directly access encapsulated data) (2) Clients of interface does not need to (know how …)". 세 문장을 영어 그대로 외워.

@lesson L4-2 | 클래스의 행동과 상태 · 메서드 · 메시지 전달 | L04 p.5–8

## 행동과 상태 · 메서드의 세 부분 {#method}

- **Class**: C++에서 데이터 추상화의 기본 단위
- **Behavior (method, member function)**: 요청에 응답해서 인스턴스가 수행할 수 있는 행동
- **State (variable)**: 행동을 성공적으로 완수하려고 객체가 유지해야 하는 데이터. 인스턴스 변수(data member, data field)에 저장
- **메서드의 세 부분**
  - **Name**: 메시지와 매칭되어 언제 실행할지 결정
  - **Signature**: **반환 타입과 인자 타입의 조합**. 이름이 같아도 시그니처가 다르면 구별됨
  - **Body**: 메서드가 호출되면 실행되는 코드

## 메시지 전달 (Message Passing) {#message-passing}

**메시지와 함수 호출의 차이**
- 메시지는 항상 **어떤 객체(receiver)** 에게 주어진다
- 응답으로 하는 행동은 **수신자가 결정** → 수신자가 다르면 같은 메시지에도 다른 행동을 할 수 있다

**메시지 전달 문법의 세 부분**: `aGame.displayCard(aCard, 42, 27);`
- **message receiver**: `aGame`
- **message selector**: `displayCard`
- **arguments** (선택): `aCard, 42, 27`

@lesson L4-3 | public 데이터 피하기 · getter/setter · 불변식과 assert | L04 p.9–12

## public 영역에 데이터 멤버를 두지 마라 {#avoid-public}

문법적으로는 문제없지만 OOP 관점에서 좋지 않다. 이유 3가지:
1. **Consistency**: 멤버 변수에 접근할 때 **항상 인터페이스(함수)로** 한다는 일관된 정책
2. **Precise control over the accessibility of data members**: no access, **read-only, read-write, write-only**를 정확히 제어
3. **Functional abstraction**: 나중에 데이터 멤버를 **계산(computation)으로 바꿀 수 있다** (예: 접근 횟수 세기 같은 로직 추가)

```
class AccessLevels {
public:
  int  getReadOnly() const     { return readOnly; }
  void setReadWrite(int value) { readWrite = value; }
  int  getReadWrite() const    { return readWrite; }
  void setWriteOnly(int value) { writeOnly = value; }
private:
  int noAccess;   // 접근 불가
  int readOnly;
  int readWrite;
  int writeOnly;
};
```

> 시험 포인트: 2024·2022 빈칸 "(i) (Consistency) (ii) precise (control) over the (accessibility) of data members (iii) functional (abstraction): you can later (replace) the data member with (a computation)". 2024·2022 서술 "every member private이면? → no interface, clients cannot use the object / every member public이면? → no encapsulation, clients can directly access and corrupt data".

## Accessor(getter)와 Mutator(setter) {#getter-setter}

- **Accessor (getter)**: 내부 데이터 값을 **그냥 반환**하는 메서드. 쓰는 이유: 데이터를 **read-only**로, 데이터에 접근할 수 있다는 걸 **더 잘 문서화**(인터페이스만 봐도 알 수 있음), 나중에 접근 방식을 바꾸기 쉬움 (예: 접근 횟수 세기)
- **Mutator (setter)**: 객체의 변수를 **바꾸는** 메서드. getter보다 **덜 흔함** (쓰기는 위험하므로 가능하면 최소화)

## 클래스 불변식과 assert {#assert}

- **Class invariant**: 객체 안에서 **항상 참이어야 하는 조건**. 모든 멤버 함수 코드가 이 조건을 검사하도록 조건을 추가
- C/C++의 **assert 매크로** `assert(e)` (`#include <assert.h>` 또는 `<cassert>`)
  - **e가 참이면 그냥 계속**
  - **e가 거짓이면 프로그램이 assertion 실패 에러 메시지와 함께 멈춤**
- **목적: 더 신뢰할 수 있는(reliable) 프로그램** → 버그를 빨리 찾고 고치기
- 교수님: "가능한 한 assert를 많이 넣어라"
- 함정: `assert(x = 3)` 은 대입이라 항상 참 (3은 0이 아니니까). 비교는 `assert(x == 3)`

> 시험 포인트: 2025 서술 "(i) What does assert(e) do? (ii) main purpose? (iii)…", 2022 빈칸 "(An assertion) contains a boolean expression that you believe will be true when it executes… writing (assertions) helps find (bugs)".

@lesson L4-4 | PlayingCard 예제 · 가시성 · 생성자 · 기본 생성자 | L04 p.13–16

## PlayingCard 클래스와 가시성 {#visibility}

```
class PlayingCard {
public:
  enum Suits {Spade, Diamond, Club, Heart};
  enum Colors {Red, Black};
  PlayingCard ();
  PlayingCard (Suits is, int ir)                 // constructor
    { suitValue = is; rankValue = ir; faceUp = true; }
  ~PlayingCard () {}                             // destructor
  Suits suit () const { return suitValue; }      // getter
  int rank () const;                             // getter
  void setFaceUp (bool up) { faceUp = up; }      // setter
  Colors color ();
private:
  Suits suitValue;
  int rankValue;
  bool faceUp;
};
```
- color는 데이터로 저장하지 않음 → suit에서 **계산** (Diamond·Heart면 Red)
- **Visibility modifier**: 인터페이스와 구현 관점을 구분
  - **public**: 외부(인터페이스, 서비스) 관점. 누구나(모든 클라이언트) 보고 조작
  - **private**: 내부(구현) 관점. **클래스 안에서만** 접근 (그 클래스의 멤버 함수만)
  - **protected**: 상속에서 다룸 (상속이 없으면 private과 같음)
- 설계 순서: 필요한 **인터페이스(public)** 를 먼저 정하고 → 그걸 구현하는 데 필요한 함수·변수를 **private**에

## 생성자 (Constructor) {#constructor}

- 새로 만든 객체의 **데이터 멤버를 초기화**하는 메서드
- 객체가 **생성될 때 자동으로(implicitly) 호출** (100%)
- **반환 타입·반환 값이 없다**
- **클래스와 이름이 같다**
- 여러 개 가능 (매개변수가 다르면)
- 초기화 자체가 자동인 건 아님 → 생성자 안에 초기화 코드를 써야 함. 안 하면 쓰레기 값 → 위험

**멤버 초기화자 (member initializer)**
```
PlayingCard (Suits is, int ir) : suitValue(is), rankValue(ir) { faceUp = true; }
```

> 시험 포인트: 2019 빈칸 "(2) automatically called when (an object is created) (3) should always have the same (name) as the class (4) does not have (return) type", 2017 "automatically called when (an object) is (created)… the name is the same as (the class)… used to (initialize) data members".

## 기본 생성자와 소멸자 {#default-ctor}

- 클래스에 **생성자를 하나도 선언하지 않으면 컴파일러가 기본 생성자(default constructor)를 만든다**
  - 모양: `TIntStack::TIntStack() { /* Empty */ }` (매개변수 없고 몸체가 빔)
  - **생성자를 하나라도 만들면** 기본 생성자는 **자동 생성되지 않는다**
- **소멸자 (destructor)**: 객체가 메모리에서 삭제될 때 자동 호출. `~클래스이름()`, 하나뿐. 안 만들면 컴파일러가 빈 소멸자를 만듦

> 시험 포인트: 2025·2024 빈칸 "if we do not declare any constructor in a class, (the compiler) generates (a default constructor)".

@lesson L4-5 | 복사 생성자 · 얕은/깊은 복사 | L04 p.17–18

## 복사 생성자가 호출되는 때 {#copy-when}

**새 객체가 같은 타입의 기존 객체로부터 만들어질 때** 호출된다.
```
Person q("Mickey");   // 일반 생성자로 q를 만듦
Person r(p);          // 복사 생성자로 r을 만듦
Person p = q;         // 선언에서 초기화 → 복사 생성자
f(p);                 // 값 매개변수 초기화 → 복사 생성자
p = q;                // 대입 연산자! 생성자도 복사 생성자도 아님 → p.operator=(q)
```
- 선언: `Person(const Person& p) { … }`
- 대입 연산자: `Person& operator=(const Person& p) { … }`

> 시험 포인트: 2017 "(a) Copy constructor is automatically called when (a new object is created from an existing object of the same type). (b) 세 경우의 예" → `Person r(p);` / `Person p = q;` / `f(p);`. 그리고 `p = q;`는 아니라는 것.

## 얕은 복사와 깊은 복사 {#shallow-deep}

- 복사 생성자를 안 만들면 컴파일러가 **기본 복사 생성자, 기본 대입 연산자, 기본 소멸자**를 만든다 → **얕은 복사(shallow copy)**: 멤버 값을 그대로 복사 (**포인터면 주소만 복사**)
- 얕은 복사로 괜찮으면 복사 생성자를 쓰지 마라
- 동적 할당한 메모리를 가리키는 포인터 멤버가 있으면 **깊은 복사(deep copy)** 가 필요: **새 메모리를 new로 할당하고 내용을 복사**
- 얕은 복사의 문제: 두 객체가 **같은 배열을 공유** → 한쪽을 바꾸면 다른 쪽도 바뀜, 둘 다 소멸될 때 **delete[]가 같은 메모리에 두 번** (double free, dangling pointer)

## 복사 생성자가 필요하면 소멸자와 operator=도 {#rule-of-three}

- **복사 생성자가 필요하면 소멸자와 operator=도 필요하다** (Why? 셋 다 같은 이유, 즉 동적 할당 자원을 소유하기 때문: 복사 때 깊은 복사, 소멸 때 delete[], 대입 때 기존 메모리 해제 후 깊은 복사)
- 예) Project 2의 `inf_int`: 자릿수를 동적 할당한 포인터로 가짐 → 깊은 복사를 하는 복사 생성자 필요. 안 쓰면 얕은 복사로 배열 공유, delete[] 두 번

> 시험 포인트: 2016 "Why do we generally need to write a copy constructor in class inf_int? What happens if we don't?", 2017 TIntStack "(4) What problems occur if the copy constructor is not provided?".

@lesson L4-6 | 객체 생성과 메모리 문제 | L04 p.19

## 객체 생성과 해제 {#object-creation}

```
PlayingCard aCard(diamond, 3);                            // 정적 (지역 객체)
PlayingCard* aCardPtr = new PlayingCard(diamond, 3);      // 동적
PlayingCard* CardsPtr = new PlayingCard[100];             // 동적 배열 (기본 생성자 100번)
delete aCardPtr;      // 해제
delete [] CardsPtr;   // 배열 해제
```
- 지역 객체는 **만든 역순**으로 소멸, `delete[]`는 배열 원소를 **뒤에서부터** 소멸

## 메모리 누수 · 댕글링 포인터 · GC {#leak-dangling}

- **Memory leak**: 동적 할당한 메모리를 **해제하지 않아서** 다시 쓸 수 없게 되는 것 (가리키는 포인터를 잃어버림)
- **Dangling pointer**: **이미 해제된 메모리를 가리키는 포인터**. 접근하면 정의되지 않은 동작(undefined behavior) → 충돌, 다른 데이터가 쓰는 메모리를 망가뜨림
- **Garbage collection**: 안 쓰는 메모리를 자동으로 회수 (Java). C++에는 없음

> 시험 포인트: 2025 서술 "(i) What is a dangling pointer? (ii) Why dangerous?", 2024 빈칸 "A pointer pointing to a memory location that has been deallocated is called a (dangling) pointer".

@lesson L4-7 | static · const 멤버 함수 · inline · 정의와 구현 분리 | L04 p.20–25 + 보충 자료

## static 멤버 {#static-member}

- **static**: 모든 인스턴스가 **같은 값을 공유**. **클래스당 하나 (one per class)**
- static 멤버는 **클래스의 속성(property of the class)** 을 다룰 때 쓴다
- **static 멤버 변수**: 클래스당 하나, **객체가 하나도 없어도 접근 가능**
- **static 멤버 함수**: 객체 없이 `클래스이름::함수()`로 호출 가능, **non-static 멤버 변수·함수에는 접근할 수 없다**
- 클래스 밖에서 정의·초기화: `int File::open_files = 0;`
- `static const int Spade = 1;` (const = 다시 대입하지 않음)
```
class File {
  static int open_files;
public:
  File(const String& filename, const String& modes);
  File(const File&);
  ~File();
  static int existing() { return open_files; }   // 존재하는 File 객체 수
};
int File::open_files = 0;
File::File(const String& filename, const String& modes) { ++open_files; }
File::~File() { --open_files; }
```

> 시험 포인트: 2025 빈칸 "static members are used to represent the properties of (the class)… can be accessed even if there is no (created object)", 2024 "no matter how many (objects) are created, only one copy", 2022 서술 File 예제 "(3) What problem occurs without static?" → 객체마다 자기 open_files를 가져서 각자 1이 되고, 전체 File 객체 수를 셀 수 없다.

## const 멤버 함수 {#const-fn}

- **호출된 객체의 데이터 멤버를 바꾸지 않는** 멤버 함수 (읽기 전용 함수)
- 이 제한은 **컴파일러가 강제(enforced by the compiler)** 한다
- 이점: 클라이언트에게 **해가 없다는 것(benign nature)을 보장** → 안전성, 가독성
- 예: `int PlayingCard::rank () const { return rankValue; }`

> 시험 포인트: 2025·2024·2023·2022 **4년 연속** 빈칸 "(const) member function does not (modify) any data members of the object on which it is called. This restriction is enforced by (the compiler)".

## inline 함수 {#inline}

(슬라이드는 질문만 있고 수업에서 설명하는 부분)
- **inline 함수**: 컴파일러가 **함수 호출을 함수 몸체로 바꿔 넣는(호출 위치에 코드를 펼치는)** 함수. 클래스 정의 안에서 몸체를 쓴 멤버 함수는 암묵적으로 inline
- 이득을 보는 상황: ① 몸체가 **작을 때** (getter/setter) ② **아주 자주 호출**될 때 (루프 안)
- 주 이점: **실행이 빠르다** — 함수 호출 오버헤드(인자 전달, 점프, 스택 프레임, 반환)가 없어지니까
- 단점: **코드 크기 증가 (code bloat)**, 특히 함수가 크거나 여러 곳에서 호출될 때

> 시험 포인트: 2022 서술 4문항 (정의, 이득 상황 2개, 주 이점과 이유, 단점).

## 메서드 순서 · 정의와 구현 분리 {#separate-def}

**메서드 나열 지침**: 중요한 것 먼저, 생성자 먼저, **public을 private보다 먼저**, 긴 목록은 그룹으로, 찾기 쉽게 알파벳 순

**클래스 밖 정의**
```
PlayingCard::Colors PlayingCard::color ( ) {
  if ((suit == Diamond) || (suit == Heart)) return Red;
  return Black;
}
```
- `클래스이름::` 을 붙인다. 반환 타입도 클래스 안의 타입이면 `PlayingCard::Colors`처럼
- 생성자·소멸자는 반환 타입 없이 `TIntStack::TIntStack(...)`

@lesson L4-8 | friend · 참조 | L04 p.26–31 + ref.cpp

## friend {#friend}

- 클래스의 **friend 함수는 그 클래스의 non-public 멤버에 접근할 권리**가 있다
- ClassTwo의 모든 멤버 함수를 ClassOne의 friend로: ClassOne 정의 안에 `friend class ClassTwo;`
```
class Count {
  friend void setX(Count&, int);   // friend 선언 (public/private 어디든 가능)
public:
  Count() : x(0) { }
private:
  int x;
};
void setX(Count &c, int val) { c.x = val; }   // 비멤버지만 private x에 접근 OK
```
- **멤버 함수**는 같은 클래스의 다른 객체의 private에도 접근 가능. 막히는 건 **비멤버 함수**뿐 → 고치려면 friend 선언 한 줄

> 시험 포인트: 2023·2022 "code contains one compile error… (a) Which line? (b) Why wrong? (c) Insert one line to fix" → 비멤버 함수가 private에 접근 → `friend 반환형 함수이름(인자);`를 클래스 안에 추가.

## 참조 (Reference) {#reference}

- **참조 = 객체의 별명 (alias for an object)**
- 주로 **참조에 의한 전달 (pass-by-reference)**: 큰 인자를 값으로 전달하는 실행 시간 비용을 피함
- 매개변수, 반환 값, 변수 모두 참조로 정의 가능
```
double square (double &x) { return x *= x; }
double foo = 10.0;
square(foo);   cout << foo;   // 100 (원본이 바뀜)
```
- 함수가 참조를 반환 → lvalue: `v[3] = 100;` (= `v.operator[](3) = 100;`)

**ref.cpp**
```
int x=5;  int* y;  int& z=x;
y=&x;  int w=*y;  x=9;
z=*y*x;  x++;  z=x&*y;
cout << x << " " << *y << " " << z << " " << w << endl;   // 82 82 82 5
```
(z는 x의 별명, y는 x를 가리킴 → x=9 → z=9*9=81 → x++ = 82 → z = 82 & 82 = 82, w는 처음 값 5)

## 참조 vs 포인터 {#ref-vs-pointer}

- 참조는 **const 포인터와 비슷하게 구현**된다
- 차이: **참조는 반드시 실제 객체를 가리켜야** 하지만, 포인터는 객체가 아닌 것도 가리킬 수 있다 (예: 0, NULL)
- 일반적으로 **참조가 더 안전하고, 덜 모호하고, 더 제한적**
```
void printDouble(const double& rd) { cout << rd; }          // 검사 필요 없음
void printDouble(const double *pd) { if (pd) cout << *pd; } // NULL 검사 필요
```

@lesson L4-9 | 인자 전달 방식 · 메모리 안전 · 지역 참조 반환 | L04 p.32–37

## 인자 전달 모드 (클라이언트 관점) {#pass-modes}

```
1. void X::f(T arg)                // pass by value
2. void X::f(const T arg)          // pass by value
3. void X::f(T& arg)               // pass by reference
4. void X::f(const T& arg)         // pass by reference
5. void X::f(T* argp)              // pass by pointer
6. void X::f(const T* argp)        // pass by pointer
7. void X::f(T* const argp)        // pointer is constant
8. void X::f(const T* const argp)
```
- **읽기 전용 매개변수에 const 없는 참조 전달을 절대 쓰지 마라**
- `T&` vs `T`: ① **복사를 피함** (복사 생성자 호출 없음 → 큰 객체에 효율적) ② 함수가 **원본을 바꿀 수 있음**
- `const T&` vs `T&`: 복사는 피하면서 **원본을 못 바꾸게** 보장 (안전)

> 시험 포인트: 2022 기말 서술 "(1) Two purposes of '&' in (b) vs (a)? (2) Purpose of const in (c) vs (b)?".

## 올바른 모드 고르기 {#pass-guide}

- **큰 객체를 값으로 넘기지 마라** — 왜? 객체 전체가 매개변수로 **복사**되므로 (복사 생성자 호출, 메모리 할당과 복사, 끝나면 소멸자) 오버헤드가 큼. 참조는 **주소만** 넘기므로 오버헤드가 아주 작다
- 기본 타입이나 작은 객체는 **값으로** (더 안전)
- 가능한 곳마다 **const** 를 인자와 함수에 → 더 견고한 프로그램
- 객체를 넘길 때 포인터를 넘기지 마라 `void f(T* object);` — 포인터는 NULL일 수 있지만 null 참조는 없다, 참조 전달은 객체의 소유권을 넘기지 않는다

> 시험 포인트: 2017 서술 "(a) Why does high overhead occur when passing large objects by value? (b) Why is the overhead very small with call-by-reference?".

## 메모리 안전한 클래스 · 클라이언트의 책임 {#memory-safe}

**Writing memory safe classes**
- 객체 복사를 피해라 (비쌈), 새 객체 생성을 피하고 재사용
- const 참조 매개변수, const 멤버 함수를 써라
- 데이터 멤버로는 참조 대신 포인터를, 기본 생성자에서 저장소 할당을 미루기, 가능하면 참조 계수(reference counting)
- 초기에 트릭 쓰지 말기: **안전 먼저**(메모리 누수 없게), 최적화는 나중에

**Client's responsibilities** (요약): 클래스의 목적을 이해, 구현자가 기대하는 것(계약)을 이해, 멤버 함수 특히 const 멤버 함수에 주의, 인자를 이해, 반환된 포인터·참조에 대한 책임 이해, 문서에 없는 세부에 의존하지 말기, const 포인터·참조를 받는 함수를 선호

## 지역 객체의 참조를 반환하지 마라 {#return-local}

```
int  f () { int i = 2; return i; }    // OK (값 복사)
int* g () { int j = 2; return &j; }   // 경고: 지역 변수 주소 반환
int& h () { int k = 2; return k; }    // 경고: 지역 변수 참조 반환
```
- 함수가 반환되면 지역 변수는 사라진다 → 그 주소·참조는 **댕글링** → 정의되지 않은 동작

@lesson L4-10 | Copy-On-Write · TIntStack | L04 p.38–40 + 기출

## Copy-On-Write (TString) {#cow}

- 객체 생성·소멸은 비싸다. 큰 객체의 복사 생성자가 자주 불리면 동적 메모리 복사·삭제에 많은 시간
- **Copy-on-write**: **쓸 때만** 새 메모리를 할당. 그 전엔 원본과 새 객체가 데이터를 **공유**
- **참조 계수(use_count)** 를 유지
- 예) s, k, m 세 TString이 "ADD ONE TO COBOL" 하나를 공유 (use_count=3) → `s.to_lower();` 로 s에 쓰는 순간 s만 새 메모리 ("add one to cobol", use_count=1), k와 m은 계속 공유 (use_count=2)

## TIntStack (깊은 복사 구현) {#tintstack}

동적 배열로 만든 정수 스택. 기출에서 생성자·복사 생성자·소멸자·Push를 직접 쓰게 함 (2022, 2017).
```
class TIntStack {
public:
  TIntStack(unsigned int stackSize = DEFAULT_SIZE);
  TIntStack(const TIntStack& that);
  ~TIntStack();
  bool Push(int thisValue);           // 꽉 찼으면 false
private:
  int* _sp;              // 생성자에서 동적 할당
  unsigned int _count;   // 원소 수
  unsigned int _size;    // 용량
};
TIntStack::TIntStack(unsigned int stackSize) { _size = stackSize; _count = 0; _sp = new int[_size]; }
TIntStack::TIntStack(const TIntStack& that) {          // 깊은 복사
  _size = that._size; _count = that._count;
  _sp = new int[_size];
  for (unsigned int i = 0; i < _count; i++) _sp[i] = that._sp[i];
}
TIntStack::~TIntStack() { delete[] _sp; }
bool TIntStack::Push(int thisValue) {
  if (_count >= _size) return false;
  _sp[_count++] = thisValue;
  return true;
}
```
- 클래스 밖 정의: **반환 타입 없이**(생성자·소멸자), `TIntStack::` 붙이고, 다른 객체는 `that._size`처럼 `.`
- `_sp = that._sp;` 만 하면 얕은 복사 → 감점
- 스택 = **LIFO** (last in, first out): 1, 3, 4 순서로 push하면 pop은 4, 3, 1
