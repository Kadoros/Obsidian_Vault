@unit U4 | C++ Data Abstraction: class | L04 C++ Data Abstraction.pdf + Handout 2 + 보충 자료
@intro The professor called this unit "the most important part of this course". Data abstraction, encapsulation and information hiding, the three benefits of encapsulation, the three reasons to avoid public data, constructors, copy constructors, static, const member functions, inline, friend, references, and argument passing modes. The 10/7 class got as far as constructors, and there is no transcript of the 10/14 class. The material after that is also a past-exam regular, so it is covered here too.

@lesson L4-1 | Data Abstraction · Encapsulation · Information Hiding | L04 p.2–4 + Handout 2

## The Three Terms {#abs-encap}

| Term | Definition |
|---|---|
| **Data Abstraction** | creating classes with appropriate functionality, which hide the unnecessary details |
| **Data Encapsulation** | the implementation is **encapsulated** by the interface and **the only way to get to the implementation legally is through the interface** |
| **Information Hiding** | the implementation is **hidden** from the user |

- The three terms are **almost the same concept** with slightly different emphasis (abstraction = show only the essentials, encapsulation = bundle data and functions and allow access only through the interface, hiding = hide it)

> Exam point: the professor said "this question also comes up in job interviews; this slide is the most important". Model answer = **"Separation of interface and implementation, such that the implementation is hidden from the user and the only way to access it is through the interface."**

## Internal and External Views {#two-views}

- **Data abstraction = separation of interface and implementation**
- **Interface**: the outside, or **service view**; describes **what** an object does
- **Implementation**: the inside view; describes **how** it does it
- **Service view**: the ability to characterize an object by **the service it provides**, without knowing **how** it performs its task
- e.g. a projector: the buttons (screen up/down, on/off) = interface, the circuitry inside = implementation. The user only needs to know the buttons

> Exam point: 2019·2016 blanks "(Data abstraction) is a technique that relies on the separation of interface and implementation. Interface … describes (what) an object does. Implementation describes (how) it does".

## Three Benefits of Data Encapsulation (Handout 2) {#encap-benefits}

1. **Protection of implementation (safety)**: clients **cannot directly access** encapsulated data
2. **Readability (understandability)**: clients of the interface **do not need to know how** the functions that describe the interface use the encapsulated information
3. **Implementation independence**: **a change in implementation should not affect the interface seen by the clients** of a class. An encapsulated implementation gives the implementor **freedom to change it** without affecting the interface (how the clients use the interface is independent of the implementation)

> Exam point: **the most frequently asked**. 2025·2022·2017 "List three main benefits … explain each", 2023 blank "(implementation independence) means (a change) in implementation should not affect (the interface) seen by clients", 2019 "(1) Clients cannot (directly access encapsulated data) (2) Clients of interface does not need to (know how …)". Memorize the three sentences in English as they are.

@lesson L4-2 | Behavior and State of a Class · Methods · Message Passing | L04 p.5–8

## Behavior and State · The Three Parts of a Method {#method}

- **Class**: the fundamental unit of data abstraction in C++
- **Behavior (method, member function)**: the actions that an instance can perform in response to a request
- **State (variable)**: the data that an object must maintain in order to successfully complete its behavior. Stored in instance variables (data members, data fields)
- **The three parts of a method**
  - **Name**: will be matched to a message to determine when the method should be executed
  - **Signature**: **the combination of return type and argument types**. Methods with the same name can be distinguished by different signatures
  - **Body**: the code that will be executed when the method is invoked

## Message Passing {#message-passing}

**Differences between a message and a function call**
- A message is always given to **some object, called the receiver**
- The action performed in response is **determined by the receiver** → different receivers can do different actions in response to the same message

**Three parts of message passing syntax**: `aGame.displayCard(aCard, 42, 27);`
- **message receiver**: `aGame`
- **message selector**: `displayCard`
- **arguments** (optional): `aCard, 42, 27`

@lesson L4-3 | Avoiding Public Data · Getters/Setters · Invariants and assert | L04 p.9–12

## Avoid Data Members in the Public Interface {#avoid-public}

Syntactically fine, but bad from an OOP point of view. Three reasons:
1. **Consistency**: a consistent policy of **always accessing member variables through the interface (functions)**
2. **Precise control over the accessibility of data members**: precisely control no access, **read-only, read-write, write-only**
3. **Functional abstraction**: you can later **replace the data member with a computation** (e.g. add logic such as counting the number of accesses)

```
class AccessLevels {
public:
  int  getReadOnly() const     { return readOnly; }
  void setReadWrite(int value) { readWrite = value; }
  int  getReadWrite() const    { return readWrite; }
  void setWriteOnly(int value) { writeOnly = value; }
private:
  int noAccess;   // no access to this int
  int readOnly;
  int readWrite;
  int writeOnly;
};
```

> Exam point: 2024·2022 blanks "(i) (Consistency) (ii) precise (control) over the (accessibility) of data members (iii) functional (abstraction): you can later (replace) the data member with (a computation)". 2024·2022 essay "what if every member is private? → no interface, clients cannot use the object / what if every member is public? → no encapsulation, clients can directly access and corrupt data".

## Accessor (getter) and Mutator (setter) {#getter-setter}

- **Accessor (getter)**: a method that **simply returns** an internal data value. Why use: makes the data field **read-only**, provides **better documentation** that the data field is accessible (visible from the interface alone), makes it easier to later change the access behavior (e.g. count # of accesses)
- **Mutator (setter)**: a method used to **change** a variable of an object. **Less common** than accessors (writing is risky, so keep it to a minimum where possible)

## Class Invariants and assert {#assert}

- **Class invariant**: a condition that **must always be true inside an object**. Add the condition so that every member function's code checks it
- The C/C++ **assert macro** `assert(e)` (`#include <assert.h>` or `<cassert>`)
  - **If e is true, just continue**
  - **If e is false, the program is stopped with an error message indicating the failure of the assertion**
- **Purpose: more reliable programs** → find and fix bugs early
- The professor: "put in as many asserts as possible"
- Trap: `assert(x = 3)` is an assignment, so it is always true (3 is non-zero). Comparison is `assert(x == 3)`

> Exam point: 2025 essay "(i) What does assert(e) do? (ii) main purpose? (iii)…", 2022 blank "(An assertion) contains a boolean expression that you believe will be true when it executes… writing (assertions) helps find (bugs)".

@lesson L4-4 | PlayingCard Example · Visibility · Constructors · Default Constructor | L04 p.13–16

## The PlayingCard Class and Visibility {#visibility}

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
- color is not stored as data → it is **computed** from the suit (Red if Diamond or Heart)
- **Visibility modifier**: differentiates the interface and implementation views of a class
  - **public**: external (interface, service) view. Can be seen and manipulated by anybody (all clients)
  - **private**: internal (implementation) view. Accessible **only within the class** (only that class's member functions)
  - **protected**: discussed with inheritance (same as private when there is no inheritance)
- Design order: first decide the needed **interface (public)** → then put the functions and variables needed to implement it in **private**

## Constructor {#constructor}

- A method that **initializes the data members** of a newly created object
- **Implicitly invoked when an object is created** (always)
- **No return type/value**
- **Has the same name as the class**
- There can be several (with different parameters)
- Initialization itself is not automatic → you must write initialization code in the constructor. Otherwise garbage values → dangerous

**Member initializer**
```
PlayingCard (Suits is, int ir) : suitValue(is), rankValue(ir) { faceUp = true; }
```

> Exam point: 2019 blanks "(2) automatically called when (an object is created) (3) should always have the same (name) as the class (4) does not have (return) type", 2017 "automatically called when (an object) is (created)… the name is the same as (the class)… used to (initialize) data members".

## Default Constructor and Destructor {#default-ctor}

- **If we do not declare any constructor in a class, the compiler generates a default constructor**
  - It looks like: `TIntStack::TIntStack() { /* Empty */ }` (no parameters, empty body)
  - **If you write even one constructor**, the default constructor is **not generated automatically**
- **Destructor**: called automatically when the object is deleted from memory. `~ClassName()`, only one. If you don't write it, the compiler generates an empty destructor

> Exam point: 2025·2024 blank "if we do not declare any constructor in a class, (the compiler) generates (a default constructor)".

@lesson L4-5 | Copy Constructor · Shallow/Deep Copy | L04 p.17–18

## When the Copy Constructor Is Called {#copy-when}

Called **whenever a new object is created from an existing object of the same type**.
```
Person q("Mickey");   // q is built with a typical constructor
Person r(p);          // copy constructor is used to build r
Person p = q;         // initialization in a declaration → copy constructor
f(p);                 // initializing a value parameter → copy constructor
p = q;                // assignment operator! no constructor or copy constructor → p.operator=(q)
```
- Declaration: `Person(const Person& p) { … }`
- Assignment operator: `Person& operator=(const Person& p) { … }`

> Exam point: 2017 "(a) Copy constructor is automatically called when (a new object is created from an existing object of the same type). (b) examples of the three cases" → `Person r(p);` / `Person p = q;` / `f(p);`. And know that `p = q;` is not one of them.

## Shallow Copy and Deep Copy {#shallow-deep}

- If you don't provide them, the compiler automatically generates a **default copy constructor, default assignment operator, and default destructor** → **shallow copy**: member values are copied as they are (**for a pointer, only the address is copied**)
- Don't write a copy constructor if shallow copies are OK
- If a pointer member points to dynamically allocated memory, a **deep copy** is needed: **allocate new memory with new and copy the contents**
- Problems with shallow copy: the two objects **share the same array** → changing one changes the other; when both are destroyed, **delete[] runs twice on the same memory** (double free, dangling pointer)

## If You Need a Copy Constructor, You Also Need a Destructor and operator= {#rule-of-three}

- **If you need a copy constructor, you also need a destructor and operator=** (Why? All three exist for the same reason — the object owns dynamically allocated resources: deep copy when copying, delete[] when destroying, free the old memory then deep copy when assigning)
- e.g. `inf_int` in Project 2: holds its digits through a dynamically allocated pointer → needs a copy constructor that does a deep copy. Without it, the shallow copy shares the array and delete[] runs twice

> Exam point: 2016 "Why do we generally need to write a copy constructor in class inf_int? What happens if we don't?", 2017 TIntStack "(4) What problems occur if the copy constructor is not provided?".

@lesson L4-6 | Object Creation and Memory Problems | L04 p.19

## Object Creation and Deallocation {#object-creation}

```
PlayingCard aCard(diamond, 3);                            // static (local object)
PlayingCard* aCardPtr = new PlayingCard(diamond, 3);      // dynamic
PlayingCard* CardsPtr = new PlayingCard[100];             // dynamic array (default constructor 100 times)
delete aCardPtr;      // deallocation
delete [] CardsPtr;   // array deallocation
```
- Local objects are destroyed **in reverse order of creation**; `delete[]` destroys array elements **from the last one backwards**

## Memory Leak · Dangling Pointer · GC {#leak-dangling}

- **Memory leak**: dynamically allocated memory that is **never deallocated** and can no longer be used (the pointer to it has been lost)
- **Dangling pointer**: **a pointer pointing to memory that has already been deallocated**. Accessing it is undefined behavior → crashes, corrupts memory used by other data
- **Garbage collection**: automatically reclaims unused memory (Java). C++ has none

> Exam point: 2025 essay "(i) What is a dangling pointer? (ii) Why dangerous?", 2024 blank "A pointer pointing to a memory location that has been deallocated is called a (dangling) pointer".

@lesson L4-7 | static · const Member Functions · inline · Separating Definition and Implementation | L04 p.20–25 + 보충 자료

## static Members {#static-member}

- **static**: all instances **share the same value**. **One per class**
- static members are used to represent **the properties of the class**
- **static member variable**: one per class, **accessible even if no object exists**
- **static member function**: can be called without an object as `ClassName::function()`; **cannot access non-static class data and functions**
- Defined and initialized outside the class: `int File::open_files = 0;`
- `static const int Spade = 1;` (const = it will not be reassigned)
```
class File {
  static int open_files;
public:
  File(const String& filename, const String& modes);
  File(const File&);
  ~File();
  static int existing() { return open_files; }   // number of existing File objects
};
int File::open_files = 0;
File::File(const String& filename, const String& modes) { ++open_files; }
File::~File() { --open_files; }
```

> Exam point: 2025 blank "static members are used to represent the properties of (the class)… can be accessed even if there is no (created object)", 2024 "no matter how many (objects) are created, only one copy", 2022 essay on the File example "(3) What problem occurs without static?" → each object has its own open_files, each becomes 1, and the total number of File objects cannot be counted.

## const Member Functions {#const-fn}

- A member function that **does not modify any data members of the object on which it is called** (read-only function)
- This restriction is **enforced by the compiler**
- Benefit: assures its clients of its **benign nature** → safety, readability
- e.g. `int PlayingCard::rank () const { return rankValue; }`

> Exam point: blank **four years in a row** (2025·2024·2023·2022) "(const) member function does not (modify) any data members of the object on which it is called. This restriction is enforced by (the compiler)".

## inline Functions {#inline}

(The slide only has the questions; this part was explained in class)
- **inline function**: a function whose **calls the compiler replaces with the function body (expands the code at the call site)**. A member function whose body is written inside the class definition is implicitly inline
- When it pays off: ① the body is **small** (getter/setter) ② it is **called very often** (inside a loop)
- Main benefit: **faster execution** — because the function call overhead (passing arguments, jumping, stack frame, returning) disappears
- Drawback: **larger code size (code bloat)**, especially when the function is large or called from many places

> Exam point: 2022 essay with 4 parts (definition, two situations where it helps, main benefit and why, drawback).

## Order of Methods · Separating Definition and Implementation {#separate-def}

**Guidelines for listing methods**: important topics first, constructors first, **public before private**, break long lists into groups, alphabetical order to make searching easier

**Definition outside the class**
```
PlayingCard::Colors PlayingCard::color ( ) {
  if ((suit == Diamond) || (suit == Heart)) return Red;
  return Black;
}
```
- Prefix with `ClassName::`. If the return type is a type declared inside the class, write it like `PlayingCard::Colors`
- Constructors and destructors have no return type: `TIntStack::TIntStack(...)`

@lesson L4-8 | friend · References | L04 p.26–31 + ref.cpp

## friend {#friend}

- **A friend function of a class has the right to access the non-public members** of the class
- To make all member functions of ClassTwo friends of ClassOne: put `friend class ClassTwo;` in the definition of ClassOne
```
class Count {
  friend void setX(Count&, int);   // friend declaration (may go in public or private)
public:
  Count() : x(0) { }
private:
  int x;
};
void setX(Count &c, int val) { c.x = val; }   // non-member, but may access private x
```
- **A member function** can access the private members of other objects of the same class too. Only **non-member functions** are blocked → the fix is one friend declaration line

> Exam point: 2023·2022 "code contains one compile error… (a) Which line? (b) Why wrong? (c) Insert one line to fix" → a non-member function accesses a private member → add `friend ReturnType functionName(args);` inside the class.

## References {#reference}

- **reference = alias for an object**
- Mainly used for **pass-by-reference**: avoids the run-time cost of passing large arguments by value
- Parameters, return values, and variables can all be defined as references
```
double square (double &x) { return x *= x; }
double foo = 10.0;
square(foo);   cout << foo;   // 100 (the original is changed)
```
- A function returning a reference → an lvalue: `v[3] = 100;` (= `v.operator[](3) = 100;`)

**ref.cpp**
```
int x=5;  int* y;  int& z=x;
y=&x;  int w=*y;  x=9;
z=*y*x;  x++;  z=x&*y;
cout << x << " " << *y << " " << z << " " << w << endl;   // 82 82 82 5
```
(z is an alias of x, y points to x → x=9 → z=9*9=81 → x++ = 82 → z = 82 & 82 = 82; w keeps the initial value 5)

## Reference vs Pointer {#ref-vs-pointer}

- References are **implemented similarly to const pointers**
- Difference: **a reference must refer to an actual object**, but a pointer can refer to things that aren't objects (e.g. 0, NULL)
- In general, **references are safer, less ambiguous, and more restricted** than pointers
```
void printDouble(const double& rd) { cout << rd; }          // no need to test
void printDouble(const double *pd) { if (pd) cout << *pd; } // NULL check needed
```

@lesson L4-9 | Argument Passing Modes · Memory Safety · Returning Local References | L04 p.32–37

## Argument Passing Modes (The Client's View) {#pass-modes}

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
- **Do not ever use pass by reference (without const qualifier) mode for read-only parameters**
- `T&` vs `T`: ① **avoids copying** (no copy constructor call → efficient for large objects) ② the function **can modify the original**
- `const T&` vs `T&`: avoids copying while guaranteeing **the original cannot be modified** (safe)

> Exam point: 2022 final essay "(1) Two purposes of '&' in (b) vs (a)? (2) Purpose of const in (c) vs (b)?".

## Selecting the Correct Mode {#pass-guide}

- **Avoid passing large objects by value** — why? The whole object is **copied** into the parameter (copy constructor call, memory allocation and copying, destructor at the end), so the overhead is high. A reference passes **only the address**, so the overhead is very small
- For primitive types or small objects, pass **by value** (safer)
- Use **const** for arguments and functions wherever possible → a more robust program
- Don't pass pointers when you mean to pass objects `void f(T* object);` — a pointer can be NULL but there is no null reference; passing a reference does not transfer ownership of the object

> Exam point: 2017 essay "(a) Why does high overhead occur when passing large objects by value? (b) Why is the overhead very small with call-by-reference?".

## Memory-Safe Classes · The Client's Responsibilities {#memory-safe}

**Writing memory safe classes**
- Avoid making copies of objects (expensive); avoid creating new objects and reuse existing ones
- Use const reference parameters and const member functions
- Use pointers instead of references as data members, delay storage allocation in the default constructor, use reference counting wherever possible
- Resist tricks in the initial stage: **safety first** (no memory leaks), optimization later

**Client's responsibilities** (summary): understand the purpose of the class, understand what the implementor expects (the contract), pay attention to member functions especially const ones, understand the arguments, understand your responsibility for returned pointers/references, don't rely on undocumented details, prefer functions that take const pointers/references

## Never Return a Reference to a Local Object {#return-local}

```
int  f () { int i = 2; return i; }    // OK (value is copied)
int* g () { int j = 2; return &j; }   // warning: address of local variable returned
int& h () { int k = 2; return k; }    // warning: reference to local variable returned
```
- When the function returns, its local variables are gone → that address/reference is **dangling** → undefined behavior

@lesson L4-10 | Copy-On-Write · TIntStack | L04 p.38–40 + 기출

## Copy-On-Write (TString) {#cow}

- Object creation and destruction is expensive. If the copy constructor of a large object is called often, a lot of time goes into copying and deleting dynamic memory
- **Copy-on-write**: allocate new memory **only when writing**. Until then the original and the new object **share** the data
- Maintain a **reference count (use_count)**
- e.g. three TStrings s, k, m share one "ADD ONE TO COBOL" (use_count=3) → the moment `s.to_lower();` writes to s, only s gets new memory ("add one to cobol", use_count=1); k and m keep sharing (use_count=2)

## TIntStack (Deep Copy Implementation) {#tintstack}

An integer stack built on a dynamic array. Past exams asked you to write the constructor, copy constructor, destructor and Push yourself (2022, 2017).
```
class TIntStack {
public:
  TIntStack(unsigned int stackSize = DEFAULT_SIZE);
  TIntStack(const TIntStack& that);
  ~TIntStack();
  bool Push(int thisValue);           // false if full
private:
  int* _sp;              // dynamically allocated in the constructor
  unsigned int _count;   // number of elements
  unsigned int _size;    // capacity
};
TIntStack::TIntStack(unsigned int stackSize) { _size = stackSize; _count = 0; _sp = new int[_size]; }
TIntStack::TIntStack(const TIntStack& that) {          // deep copy
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
- Definitions outside the class: **no return type** (constructors/destructor), prefix with `TIntStack::`, access the other object with `.` as in `that._size`
- Writing only `_sp = that._sp;` is a shallow copy → points deducted
- Stack = **LIFO** (last in, first out): push 1, 3, 4 in that order and pop gives 4, 3, 1
