# Builds bank.json: OOP midterm past-exam question bank with model answers.
import json, os

Q = []
def q(id, year, no, pts, typ, topics, scope, prompt, answer, tip="", code="", src=""):
    Q.append(dict(id=id, year=year, no=no, pts=pts, type=typ, topics=topics, scope=scope,
                  prompt=prompt.strip(), code=code.strip("\n"), answer=answer.strip(), tip=tip.strip(), src=src))

FILECOPY = """#include <iostream>
#include <fstream>
using namespace std;
int main() {
    ifstream in("src.bin", ios::in | ios::binary | ios::ate);
    if (!in.is_open()) return 1;
    streampos size = in.tellg();          // ate: 끝에서 열었으니 tellg = 파일 크기
    char* memblock = new char[size];
    in.seekg(0, ios::beg);                // 처음으로 되감기
    in.read(memblock, size);
    in.close();

    ofstream out("des.bin", ios::out | ios::binary);
    out.write(memblock, size);
    out.close();
    delete[] memblock;
    return 0;
}"""

# ───────────────────────── 2025 ─────────────────────────
Y=2025
q("2025-1ab",Y,"1(a)(b)",4,"blank",["static"],"likely",
"In C++, static members are used to represent the properties of (a.        ). Unlike typical member variables, static member variables can be accessed even if there is no (b.        ).",
"(a) the class  (b) created object (instance)",
"L04 보충 'Static Members': static members of a class can be used when handling property of the class / it can be accessed even if there is no created object.","","L04 static")
q("2025-1c",Y,"1(c)",2,"blank",["quality"],"in",
"(c.        ) means the ability of the software to consistently perform its required functions without failure under specified conditions for a specified period of time.",
"(c) reliability",
"dependability(믿고 쓸 수 있음)와 헷갈리기 쉬움. '고장 없이 지정된 기간 동안' = reliability.","","L02, Handout1")
q("2025-1de",Y,"1(d)(e)",4,"blank",["se"],"in",
"(d.        ) arose because as computer hardware power grew rapidly, (e.        ) of the software systems increased even faster – beyond what existing development methods could manage. Increasing (e) is the main cause of (d).",
"(d) software crisis  (e) complexity",
"L02: Software Crisis — Cause : complexity","","L02")
q("2025-1fg",Y,"1(f)(g)",4,"blank",["ctor"],"in",
"In C++, if we do not declare any constructor in a class, (f.        ) generates (g.        ).",
"(f) the compiler  (g) a default constructor",
"L04: If we did not declare any constructor in class, the compiler would generate a default constructor.","","L04")
q("2025-1h",Y,"1(h)",2,"blank",["se"],"in",
"One of the main goals of software engineering is to minimize (h.        ) of software development and maintenance.",
"(h) the cost","L02 Goals: minimize the cost of software development and maintenance","","L02")
q("2025-1ijk",Y,"1(i)(j)(k)",6,"blank",["constfn"],"likely",
"In C++, (i.        ) member function does not (j.        ) any data members of the object on which it is called. This restriction is enforced by (k.        ). (i) member function assures its clients of its benign natures (i.e. safety and readability).",
"(i) const  (j) modify  (k) the compiler",
"3년 연속 나온 문장. 통째로 외우기.","","L04 const member functions")
q("2025-1lm",Y,"1(l)(m)",4,"blank",["encap"],"in",
"In the concept of information hiding, (l.        ) of an object can be modified only through (m.        ).",
"(l) internal data  (m) an interface",
"L02: Internal data of an object can be modified only through an interface.","","L02")
q("2025-2",Y,"2",9,"short",["encap"],"in",
"List three main benefits of data encapsulation and explain each benefit in sufficient detail. [(i) <10 words, (ii)(iii) <15 words]",
"""(i) Protection of implementation (safety): clients cannot directly access encapsulated data.
(ii) Readability (understandability): clients need not know how interface functions use encapsulated data.
(iii) Implementation independence: a change in implementation should not affect the interface seen by clients.""",
"Handout 2 원문 그대로. 이름 + 한 줄 설명 세트로 외우기.","","Handout 2")
q("2025-3",Y,"3",5,"short",["design"],"in",
"In the \"Integration of Components\" step, components are slowly integrated into a completed system, using stubs as yet unimplemented parts. What is the meaning of \"slowly integrated\"? (<15 words)",
"Components are added and tested one at a time (incrementally), not all at once.",
"핵심: incrementally / one by one + test each step → 에러 위치를 좁힐 수 있음.","","L03 8. Integration")
q("2025-4",Y,"4",6,"short",["memory"],"likely",
"(i) In C/C++, what is a dangling pointer? (<15 words)  (ii) Why can dangling pointers be a problem and dangerous? (<15 words)",
"""(i) A pointer that points to memory that has already been deallocated (freed).
(ii) Accessing it causes undefined behavior: crashes or corrupting memory reused by other data.""",
"","","L04 Object Creation")
q("2025-5",Y,"5",9,"short",["assert"],"in",
"(i) What does the assert(e) function call do? (<15 words)  (ii) What is the main purpose of using assert()? (<7 words)  (iii) To achieve the purpose, e in assert(e) should be a condition that (<10 words).",
"""(i) If e is true, execution continues; if false, the program stops with an error message.
(ii) To make programs more reliable (detect bugs early).
(iii) must always be true at that point (e.g. a class invariant).""",
"L04: class invariants and assertions — 'can be used to implement programs that are more reliable'.","","L04")
q("2025-6",Y,"6",6,"short",["design"],"in",
"In project 1 (IIKH), what is the main difference between Recipe class and RecipeDB class? (i) Recipe class is supposed to (<10 words)  (ii) RecipeDB class is supposed to (<10 words)",
"""(i) maintain one recipe's data (ingredients, steps) and edit/display/print itself.
(ii) maintain the collection of recipes: browse, search, add, and edit recipes.""",
"단일 객체 vs 컬렉션 관리. Budd Ch3: Recipe Database = maintain/browse/edit/add; Recipe = ingredients + know how to edit/display/print itself.","","L03 IIKH")
q("2025-7",Y,"7",6,"short",["encap"],"in",
"ADT (Abstract Data Type) is called abstract. Why? ADT is called abstract because (<12 words).",
"its data and operations are specified independently of any particular implementation.",
"L02: A set of data variables and associated operations that are precisely specified independent of any particular implementation.","","L02 ADT")
q("2025-8",Y,"8",15,"code",["fileio"],"in",
"Write a C++ program that performs file-copying from source binary file \"src.bin\" to destination file \"des.bin\". Do not use a file-copy function; read the entire data from src.bin and write it to des.bin.",
FILECOPY,
"2024 5번과 거의 동일. ios::binary | ios::ate → tellg로 크기 → seekg(0, ios::beg) → read → write → delete[]. 실제로 컴파일해서 복사 확인함.",
"#include <iostream>\n#include <fstream>\nusing namespace std;\nint main() {\n    // your code\n}","C++ in Summary 13")
q("2025-9",Y,"9",18,"trace",["trace","copy"],"in",
"(1) The code has five errors. Which lines are wrong and how to correct them? Assume lines 16 and 17 are correct. (2) What is the screen output after the correction?",
"""(1)
line 18: b = &a;
line 22: b->w = 9;
line 25: cout << b->area() << endl;
line 26: cout << c->area() << endl;
line 28: delete b; 삭제 (b는 new로 만든 게 아니라 스택 객체 a를 가리킴)

(2) 출력
c1
c1
c2
f3
c2
=======
54
54
56
30""",
"func(a,9)는 값 전달 → 복사생성자 c2가 f3보다 먼저 출력. obj.h=9는 복사본만 바뀌어서 a에 영향 없음. d는 b->w=9 하기 전에 복사돼서 5*6=30. g++로 실행해서 확인한 출력.",
""" 1: #include <iostream>
 2: using namespace std;
 3: class Rect {
 4: public:
 5:     int w,h;
 6:     Rect(int x, int y): w(x), h(y) { cout << "c1\\n"; }
 7:     Rect(const Rect& x) { w=x.w; h=x.h; cout << "c2\\n"; }
 8:     int area() { return w*h; }
 9: };
10:
11: void func(Rect obj, int y) {
12:     cout << "f3\\n";
13:     obj.h = y;
14: }
15: int main() {
16:     Rect a(5,6);
17:     Rect *b, *c;
18:     b = a;
19:     c = new Rect(7,8);
20:     func(a,9);
21:     Rect d(a);
22:     b.w = 9;
23:     cout << "======="<< endl;
24:     cout << a.area() << endl;
25:     cout << b.area() << endl;
26:     cout << c.area() << endl;
27:     cout << d.area() << endl;
28:     delete b;
29:     delete c;
30:     return 0;
31: }""","C++ in Summary 12, L04")

# ───────────────────────── 2024 ─────────────────────────
Y=2024
q("2024-1ab",Y,"1(a)(b)",3,"blank",["paradigm"],"in",
"(a.        ) is a programming paradigm based on the concept of (b.        ) which can contain data and code... computer programs are designed by making them out of (b) that interact with one another.",
"(a) Object-oriented programming (OOP)  (b) objects","","","L02")
q("2024-1c",Y,"1(c)",2,"blank",["paradigm"],"in",
"(c.        ) makes extensive use of GOTO statements... In (c), a program contains only a single code block.",
"(c) Unstructured programming","L02: Unstructured Programming — only one main program, only global data, use goto.","","L02")
q("2024-1de",Y,"1(d)(e)",3,"blank",["paradigm"],"in",
"Using (d.        ) variables is often unsafe because this makes all modules (e.        ) on one another.",
"(d) global  (e) dependent","매년 나옴. 'dependent on one another'.","","L02")
q("2024-1fg",Y,"1(f)(g)",3,"blank",["ctor"],"in",
"In C++, (f.        ) is a constructor that is automatically generated by (g.        ) if we do not define any constructor for a class.",
"(f) default constructor  (g) the compiler","","","L04")
q("2024-1h",Y,"1(h)",2,"blank",["memory"],"likely",
"A pointer pointing to a memory location that has been deallocated (or freed) is called a (h.        ) pointer.",
"(h) dangling","","","L04")
q("2024-1ij",Y,"1(i)(j)",3,"blank",["static"],"likely",
"We can define class members (i.        ) using (i) keyword... no matter how many (j.        ) of the class are created, there is only one copy of the (i) member. A (i) member is shared by all (j) of the class.",
"(i) static  (j) objects (instances)","","","L04")
q("2024-1klm",Y,"1(k)(l)(m)",4,"blank",["constfn"],"likely",
"In C++, (k.        ) member function does not (l.        ) any data members of the object on which it is called. This restriction is enforced by (m.        ).",
"(k) const  (l) modify  (m) the compiler","","","L04")
q("2024-1nopq",Y,"1(n)~(q)",6,"blank",["couple"],"in",
"(n.        ) and (o.        ) are two key concepts used to measure design quality. (n) refers to the degree of interdependence between modules. (p.        ) (n) means modules are closely connected... (q.        ) (n) means modules are independent... (o) refers to the degree to which elements within a module work together for a single purpose.",
"(n) Coupling  (o) Cohesion  (p) High (tight)  (q) Low (loose)","","","L03")
q("2024-1rst",Y,"1(r)(s)(t)",4,"blank",["se"],"in",
"Fred Brooks stated that over 90% of (r.        ) of a typical system arise in (s.        ) phase, and that any successful piece of software will inevitably be (t.        ).",
"(r) the costs  (s) the maintenance  (t) maintained","L02 원문 그대로.","","L02")
q("2024-2",Y,"2",10,"blank",["encap"],"in",
"It is often desirable to avoid data members in the public area of class. List three advantageous properties: (i) (a.        ): accessing a data member will be done always through a method. (ii) precise (b.        ) over the (c.        ) of data members. (iii) functional (d.        ): you can later (e.        ) the data member with a computation.",
"(a) Consistency  (b) control  (c) accessibility  (d) abstraction  (e) replace",
"L04 'Avoid data members in the public interface': Consistency / Precise control over the accessibility / Functional abstraction.","","L04")
q("2024-3",Y,"3",10,"short",["encap"],"in",
"(a) What is the most serious problem if you make every member private in a class? Why? (<15 words)  (b) ... every member public? Why? (<15 words)",
"""(a) No interface: clients cannot use the object at all, since nothing is accessible.
(b) No encapsulation: clients can directly modify internal data, breaking safety and implementation independence.""",
"private only → 쓸모없는 클래스. public only → 캡슐화 장점 3개 다 잃음.","","L04")
q("2024-4",Y,"4",12,"code",["fileio"],"in",
"Write a program that calculates the size of the file \"in.bin\" (a general binary file) and prints it. Fill in the blanks.",
"""ifstream myfile("in.bin", ios::binary);
begin = myfile.tellg();
myfile.seekg(0, ios::end);
end = myfile.tellg();""",
"cplusplus.com 'File Position Example' 그대로. tellg/seekg는 get 위치, tellp/seekp는 put 위치.",
"""int main() {
    streampos begin, end;
    ________________________;
    begin = ________________;
    myfile.________________;
    end = __________________;
    myfile.close();
    cout << "size: " << (end-begin) << " bytes\\n";
    return 0;
}""","C++ in Summary 13")
q("2024-5",Y,"5",16,"code",["fileio"],"in",
"Write a C++ program that copies the binary file \"src.bin\" to \"des.bin\" without a file-copy function (read the entire data and write it).",
FILECOPY,"2025 8번과 동일.","","C++ in Summary 13")
q("2024-6",Y,"6",22,"trace",["trace","copy","ctor"],"in",
"Two lines contain compile errors (lines 16-18 are correct). (a) Which two lines? (b) Correct them. (c) Screen output after correction?",
"""(a) line 22, line 26
(b) line 22 → b->h = 9;
    line 26 → cout << b->w << " " << b->h << endl;
(c)
c2
c3
f1 called!
d
c3
==========
2 9
2 9
1 6
d
d""",
"func 값 전달 → c3, 함수 끝날 때 obj 소멸 → d. b는 a를 가리켜서 b->h=9가 a.h를 바꿈. c는 그 전에 복사돼서 (2,6) 상태에서 c.w=1 → 1 6. main 끝에 c, a 순서로 소멸 → d d. g++로 확인.",
""" 1: #include <iostream>
 2: using namespace std;
 3: class X {
 4: public:
 5:     int w,h;
 6:     X() { w=0; h=0; cout << "c1\\n"; }
 7:     X(int a,int b) { w=a; h=b; cout << "c2\\n"; }
 8:     X(const X& x) { w=x.w; h=x.h; cout << "c3\\n"; }
 9:     ~X() { cout << "d\\n"; }
10: };
11: void func(X obj, int a, int b) {
12:     cout << "f1 called!\\n";
13:     obj.w = a; obj.h = b;
14: }
15: int main() {
16:     X a(5,6);
17:     X* b;
18:     b = &a;
19:     a.w = 2;
20:     func(a,7,8);
21:     X c(a);
22:     b.h = 9;
23:     c.w = 1;
24:     cout << "=========="<< endl;
25:     cout << a.w <<" "<< a.h << endl;
26:     cout << b.w <<" "<< b.h << endl;
27:     cout << c.w <<" "<< c.h << endl;
28:     return 0;
29: }""","L04")

# ───────────────────────── 2023 ─────────────────────────
Y=2023
q("2023-1ab",Y,"1(a)(b)",4,"blank",["se"],"in",
"(a.        ) is a term used in the early days of computing science for the difficulty of writing correct, useful and efficient programs in the required time. (a) was due to the rapid increases in computer power and the (b.        ) of the problems...",
"(a) Software crisis  (b) complexity","","","L02")
q("2023-1c",Y,"1(c)",2,"blank",["fileio"],"in",
"In C++, the file open mode ios::app means that all output operations are performed at the (c.        ) of the file.",
"(c) end","ios::app = append: 모든 출력이 파일 끝에 덧붙음.","","C++ in Summary 13")
q("2023-1de",Y,"1(d)(e)",4,"blank",["fileio"],"in",
"In C++, the file open mode (d.        ) means that if the file is opened for output operations and the file is already (e.        ), its previous content is deleted and replaced by the new one.",
"(d) ios::trunc  (e) existing (it already existed)","","","C++ in Summary 13")
q("2023-1f",Y,"1(f)",2,"blank",["se"],"in",
"(f.        ) is the process of changing, modifying, and updating software to keep up with customer needs. (f) is done after the product has launched...",
"(f) Software maintenance","","","L02, L03")
q("2023-1ghij",Y,"1(g)~(j)",8,"blank",["couple"],"in",
"Coupling is the degree to which each program module (g.        ) on each one of the other modules. (h.        ) is a measure of how strongly-related and focused the responsibilities of a module are. It is often desirable to (i.        ) coupling and (j.        ) (h).",
"(g) relies (depends)  (h) Cohesion  (i) minimize  (j) maximize","","","L03")
q("2023-1klm",Y,"1(k)(l)(m)",6,"blank",["encap"],"in",
"One of the main benefits of data encapsulation is (k.        ). (k) means (l.        ) in implementation should not affect (m.        ) seen by clients of a class.",
"(k) implementation independence  (l) a change  (m) the interface","","","Handout 2")
q("2023-1nop",Y,"1(n)(o)(p)",6,"blank",["constfn"],"likely",
"(n.        ) member function does not (o.        ) any data members of the object on which it is called. This restriction is enforced by (p.        ).",
"(n) const  (o) modify  (p) the compiler","","","L04")
q("2023-2",Y,"2",20,"short",["memory"],"in",
"Describe the main advantage and disadvantage of static memory allocation (int x[10];) and dynamic memory allocation (int* x = new int[10];) for using an array, and why. (advantage/disadvantage <10 words, why <15 words each)",
"""Static
 advantage: simple and fast; memory is freed automatically.
   why: size is fixed at compile time; allocated on the stack and released at scope exit.
 disadvantage: size cannot change at run time (waste or shortage).
   why: array size must be decided at compile time.
Dynamic
 advantage: size can be decided at run time; memory used efficiently.
   why: memory is allocated with new during execution as needed.
 disadvantage: programmer must free it; risk of memory leak, dangling pointers.
   why: heap memory is not released automatically; needs delete[].""",
"토론 자료 'static vs dynamic memory allocation' 그대로 출제됨. dynamic = 'occurs at run-time'.","","static vs dynamic 토론")
q("2023-3",Y,"3",20,"code",["trace"],"in",
"Fill in empty boxes so that output is: Area Calculation: obj:12, foo:12, bar:30, baz[0]:1",
"""line 5 : public:
line 7 : Rectangle(int x, int y) : width(x), height(y) {}
line 12: Rectangle *foo, *bar, *baz;
line 13: foo = &obj;
line 17: obj.area()
line 18: foo->area()
line 19: bar->area()
line 20: baz[0].area()""",
"baz[0]은 기본생성자(1,1) → 1. 포인터는 ->, 배열 원소는 객체라서 '.'",
""" 3: class Rectangle {
 4:     int width, height;
 5:     [        ]
 6:     Rectangle() { width=1; height=1; }
 7:     Rectangle(int x, int y) [        ] {}
 8:     int area() { return width*height; }
 9: };
10: int main() {
11:     Rectangle obj(3,4);
12:     Rectangle *foo, [        ];
13:     foo = [        ];
14:     bar = new Rectangle (5,6);
15:     baz = new Rectangle[2];
16:     cout << "Area Calculation: ";
17:     cout << "obj:" << obj[        ] << ", ";
18:     cout << "foo:" << foo[        ] << ", ";
19:     cout << "bar:" << bar[        ] << ", ";
20:     cout << "baz[0]:" << baz[0][        ] << "\\n";
21:     delete bar; delete[] baz; return 0;
22: }""","C++ in Summary 12")
q("2023-4",Y,"4",8,"code",["fileio"],"in",
"Fill in the boxes to print the size of \"example.bin\": line 9 myfile.[  ]; line 10 end = [  ];",
"line 9 : myfile.seekg(0, ios::end);\nline 10: end = myfile.tellg();","",
""" 7: ifstream myfile("example.bin", ios::binary);
 8: begin = myfile.tellg();
 9: myfile.[        ];
10: end = [        ];
11: myfile.close();""","C++ in Summary 13")
q("2023-5",Y,"5",20,"trace",["trace","friend","copy"],"likely",
"The code contains one compile error (lines 1-7 correct). (a) Which line? (b) Why wrong? (c) Insert one line at line 12 to fix. (d) Screen output after correction?",
"""(a) line 18 (obj.w*obj.h)
(b) w and h are private; f1 is a non-member function, so it cannot access them.
(c) friend int f1(X obj);
(d)
c3 called
c1 called
c5 called
c5 called
f1 called!
d called
area: 30
d called
d called
d called""",
"X c = a; → 복사생성자(c5). b = c; → 대입연산자라 출력 없음! f1(b) 값 전달 → c5, 리턴 후 obj 소멸 d. main 끝에 c,b,a 소멸 d×3. g++ 확인.",
""" 4: class X {
 5: private:
 6:    int w,h;
 7: public:
 8:    X() { cout << "c1 called\\n"; }
 9:    X(int a,int b) { w=a; h=b; cout << "c3 called\\n"; }
10:    X(const X& x) { w=x.w; h=x.h; cout << "c5 called\\n"; }
11:    ~X() { cout << "d called\\n"; }
12:
13: };
15: int f1(X obj)
16: {
17:     cout << "f1 called!\\n";
18:     return obj.w*obj.h;
19: }
20: int main()
21: {
22:     int z;
23:     X a(5,6), b;
24:     X c = a;
25:     b = c;
26:     z = f1(b);
27:     cout << "area: " << z << "\\n";
28:     return 0;
29: }""","L04")

# ───────────────────────── 2022 ─────────────────────────
Y=2022
q("2022-1a-e",Y,"1(a)~(e)",10,"blank",["encap"],"in",
"The three main benefits of data encapsulation are (a.        ), (b.        ), (c.        ). (c) means (d.        ) in implementation should not affect (e.        ) seen by clients of a class.",
"(a) protection of implementation (safety)  (b) readability (understandability)  (c) implementation independence  (d) a change  (e) the interface","","","Handout 2")
q("2022-1fg",Y,"1(f)(g)",4,"blank",["couple"],"in",
"(f.        ) is the degree to which each program module relies on each one of the other modules. (g.        ) is a measure of how strongly-related and focused the responsibilities of a module are. It is desirable to minimize (f) and maximize (g).",
"(f) Coupling  (g) Cohesion","","","L03")
q("2022-1h",Y,"1(h)",2,"blank",["constfn"],"likely",
"(h.        ) member function does not modify any data members of the object on which it is called.","(h) const","","","L04")
q("2022-1ij",Y,"1(i)(j)",4,"blank",["se"],"in",
"One of the formal definitions of (i.        ) is \"the establishment and use of sound engineering principles in order to (j.        ) obtain software that is reliable and works efficiently\".",
"(i) software engineering  (j) economically","Fritz Bauer 정의. 'economically' 자주 나옴.","","L02")
q("2022-1k",Y,"1(k)",2,"blank",["design"],"in",
"(k.        ) is a simple dummy routine with no behavior or with very limited behavior, and it can be a temporary substitute for yet-to-be-developed code.",
"(k) Stub","","","L03")
q("2022-1lm",Y,"1(l)(m)",4,"blank",["assert"],"in",
"(l.        ) contains a boolean expression that you believe will be true when (l) executes. If not true, the system will throw an error... writing (l) while programming is one of the quickest and most effective ways to detect (m.        ).",
"(l) An assertion (assert)  (m) bugs (errors)","","","L04")
q("2022-1n",Y,"1(n)",2,"blank",["se"],"in",
"Software crisis is the term used to describe the impact of rapid increases in computer power and the (n.        ) of the problems. Software technology could not follow the (n).",
"(n) complexity","","","L02")
q("2022-1op",Y,"1(o)(p)",4,"blank",["paradigm"],"in",
"Using (o.        ) variables can be dangerous because it can make all modules (p.        ) on one another.",
"(o) global  (p) dependent","","","L02")
q("2022-1qr",Y,"1(q)(r)",4,"blank",["paradigm"],"in",
"structured programming ≒ (q.        ) ≒ (r.        ) ≒ functional decomposition",
"(q) top-down approach  (r) divide and conquer","L02 Structured Programming: Top-down approach / Divide and conquer / Functional decomposition. (procedural/modular programming도 맥락상 인정될 수 있음)","","L02")
q("2022-2",Y,"2",8,"blank",["encap"],"in",
"Avoid data members in the public interface. Three advantageous properties: (i) (a.        ), (ii) precise control over the (b.        ) of data members, (iii) functional (c.        ): you can later replace the data member with (d.        ).",
"(a) consistency  (b) accessibility  (c) abstraction  (d) a computation","","","L04")
q("2022-3",Y,"3",8,"short",["encap"],"in",
"(a) Most serious problem if every member is private? Why?  (b) ... if every member is public? Why?",
"""(a) The class has no interface, so clients cannot use any of its functionality.
(b) No encapsulation: clients can directly access/modify internal data, so safety and implementation independence are lost.""","","","L04")
q("2022-4",Y,"4",14,"short",["inline"],"likely",
"(1) What is an inline function? (2) In which situations can we get benefits of using it? List two. (3) Main benefit and why? (4) Possible disadvantage, and especially when?",
"""(1) A function whose call is replaced by its body (code expanded at the call site) by the compiler.
(2) ① the function body is small (e.g. getters/setters)  ② the function is called very frequently (e.g. in a loop).
(3) Faster execution — because function-call overhead (passing arguments, jump, stack frame, return) is removed.
(4) Code size increases (code bloat) — especially when the function is large or called in many places.""",
"강의 슬라이드는 'What is inline function? / Why useful?' 질문만 있음 → 수업 설명으로 채워야 하는 부분.","","L04 inline")
q("2022-5",Y,"5",9,"short",["static"],"likely",
"class File { static int open_files; ... File(...) { ++open_files; } ~File() { --open_files; } }; (1) Meaning of static in line 2 and the difference it makes? (2) Why is static necessary for open_files? (3) What problem occurs without static?",
"""(1) open_files becomes one variable per class, shared by all File objects (exists even with no object). Without static, each object has its own copy.
(2) It must count all File objects — a property of the class, not of one object — so it must be shared.
(3) Each object gets its own open_files, incremented only in its own copy (always 1), so the total number of File objects cannot be counted.""","","","L04 static example")
q("2022-6",Y,"6",9,"trace",["friend","trace"],"likely",
"Code computes the area of a rectangle but has a compile error. (a) Which line? (b) Why wrong? (c) Insert one line at line 3 to fix.",
"""(a) line 11 (c.width * c.height)
(b) width and height are private members; get_area is a non-member function, so it cannot access them.
(c) friend int get_area(Rectangle c);""","",
""" 1: #include <iostream>
 2: class Rectangle {
 3:
 4: public:
 5:   Rectangle(int w, int h) { width=w; height=h; }
 6: private:
 7:   int width;
 8:   int height;
 9: };
10: int get_area(Rectangle c) {
11:       return c.width * c.height;
12: }
13: int main() {
14:       Rectangle rect(5,6);
15:       std::cout << get_area(rect) << "\\n";
16:       return 0;
17: }""","L04 friend")
STACK_DECL = """#include <iostream>
const unsigned int DEFAULT_SIZE = 256;
class TIntStack {
public :
    TIntStack(unsigned int stackSize = DEFAULT_SIZE);
    TIntStack(const TIntStack& that);
    ~TIntStack();
    bool Push(int thisValue); // return true if successful, false if stack is full
    unsigned int getCount() const { return _count; }
private :
    int* _sp;             // memory is dynamically allocated during constructor call
    unsigned int _count;  // number of elements in stack
    unsigned int _size;   // size (capacity) of stack
};"""
q("2022-7",Y,"7",16,"code",["stack","copy"],"likely",
"Write (1) the constructor TIntStack(unsigned int stackSize), (2) a deep-copy copy constructor, (3) the destructor, (4) bool Push(int thisValue).",
"""// (1)
TIntStack::TIntStack(unsigned int stackSize) {
    _size = stackSize;
    _count = 0;
    _sp = new int[_size];
}
// (2) deep copy
TIntStack::TIntStack(const TIntStack& that) {
    _size = that._size;
    _count = that._count;
    _sp = new int[_size];
    for (unsigned int i = 0; i < _count; i++)
        _sp[i] = that._sp[i];
}
// (3)
TIntStack::~TIntStack() {
    delete[] _sp;
}
// (4)
bool TIntStack::Push(int thisValue) {
    if (_count >= _size) return false;
    _sp[_count++] = thisValue;
    return true;
}""","깊은 복사의 핵심: 새 배열 new + 원소 복사. 포인터만 복사(_sp = that._sp)하면 얕은 복사 → 감점. g++로 확인.",STACK_DECL,"L04 TIntStack")

# ───────────────────────── 2019 ─────────────────────────
Y=2019
q("2019-1abc",Y,"1(a)(b)(c)",6,"blank",["couple"],"in",
"(a.        ) is the degree to which each module relies on each one of the other modules. (b.        ) is a measure of how strongly-related the responsibilities of a module are. It is often desirable to minimize (a) because (c.        ).",
"(a) Coupling  (b) Cohesion  (c) a change in one module can affect other modules (making the system hard to maintain/reuse)","","","L03")
q("2019-1d",Y,"1(d)",2,"blank",["memory"],"in",
"Dynamic memory allocation means memory allocation occurs at (d.        ).","(d) run-time (execution time)","C++ in Summary 11: 'dynamic' means '… occurs at run-time (execution-time)'","","C++ in Summary 11")
q("2019-1ef",Y,"1(e)(f)",4,"blank",["fileio"],"in",
"ios::app means all output operations are performed at (e.        ) of the file, (f.        ) the content to the current content of the file.",
"(e) the end  (f) appending","","","C++ in Summary 13")
q("2019-1gh",Y,"1(g)(h)",4,"blank",["fileio"],"in",
"File stream classes: ofstream: write on files / (g.        ): read from files / (h.        ): read and write from/to files.",
"(g) ifstream  (h) fstream","","","C++ in Summary 13")
q("2019-1ij",Y,"1(i)(j)",4,"blank",["se"],"in",
"One of the formal definitions of (i.        ) is \"the establishment and use of sound engineering principles in order to (j.        ) obtain software that is reliable and works efficiently\".",
"(i) software engineering  (j) economically","","","L02")
q("2019-1k",Y,"1(k)",2,"blank",["paradigm"],"in",
"Using (k.        ) variables can be dangerous because it can make all modules dependent on one another.","(k) global","","","L02")
q("2019-1lmn",Y,"1(l)(m)(n)",6,"blank",["encap"],"in",
"(l.        ) is a technique that relies on the separation of interface and implementation. Interface is the outside or service view, describing (m.        ) an object does. Implementation is the inside view, describing (n.        ) an object does.",
"(l) Data abstraction  (m) what  (n) how","L04 첫 슬라이드.","","L04")
q("2019-2",Y,"2",6,"short",["encap"],"in",
"Explain each benefit: (1) protection of implementation (safety): Clients cannot (    ). (2) readability: Clients of interface does not need to (    ). (3) implementation independence: A change in implementation should not (    ).",
"""(1) directly access encapsulated data.
(2) know how the interface functions use the encapsulated information.
(3) affect the interface seen by the clients of a class.""","","","Handout 2")
q("2019-3",Y,"3",8,"short",["se","quality"],"in",
"(1) Definition of maintenance? (2) A program with high maintainability is easy to (read/understand), easy to (a.  ), easy to (b.  ), easy to (c.  ).",
"""(1) Activities after delivery of the initial working version: correcting errors, adapting to changed requirements/hardware, and improving the software.
(2) (a) modify  (b) extend  (c) reuse  (debug/test, port도 인정)""",
"Handout 1 maintainability 하위항목: readability, modifiability, extensibility, reusability, testability, modularity, portability.","","L03 9, Handout 1")
q("2019-4",Y,"4",8,"blank",["ctor"],"in",
"Properties of a constructor: (2) automatically called when (    ). (3) should always have the same (    ) as the class. (4) does not have (    ) type. (5) If you do not make any constructor, the compiler would generate (    ).",
"(2) an object is created  (3) name  (4) return  (5) a default constructor","","","L04")
CPLX_DECL = """class Complex {
private:
    double re, im;
public :
    Complex( double r, double i ) : re(r), im(i) {}
    friend Complex operator-(Complex&, Complex&);
    friend ostream& operator<<(ostream &o, Complex &x);
    // prints "a+bi": re=3.2,im=2.3 → 3.2+2.3i ; im=-2.3 → 3.2-2.3i ; im=0 → 3.2
};"""
CPLX_ANS = """ostream& operator<<(ostream &o, Complex& x) {
    o << x.re;
    if (x.im > 0)      o << "+" << x.im << "i";
    else if (x.im < 0) o << x.im << "i";   // 음수는 '-'가 자동으로 붙음
    return o;
}"""
q("2019-5",Y,"5",29,"code",["opover"],"low",
"Write (1) operator- and (2) operator<< for class Complex.",
"""Complex operator-(Complex& x, Complex& y) {
    return Complex(x.re - y.re, x.im - y.im);
}
"""+CPLX_ANS,"friend라서 private re, im에 접근 가능. return o; 빠뜨리면 감점. g++ 확인.",CPLX_DECL,"Operator Overloading")
q("2019-6",Y,"6",12,"code",["trace"],"in",
"Fill in the boxes so that output is: obj:12, foo:12, bar:30, baz[0]:10",
"line 16: obj.area()\nline 17: foo->area()\nline 18: bar->area()\nline 19: baz[0].area()","",
"""10: Rectangle obj(3,4);
11: Rectangle *foo, *bar, *baz;
12: foo = &obj;
13: bar = new Rectangle (5,6);
14: baz = new Rectangle[2] { {2,5}, {3,6} };
15: cout << "Area Calculation Output\\n";
16: cout << "obj:" << [        ] << ", ";
17: cout << "foo:" << [        ] << ", ";
18: cout << "bar:" << [        ] << ", ";
19: cout << "baz[0]:" << [        ] << "\\n";""","C++ in Summary 12")
q("2019-7",Y,"7",9,"code",["fileio"],"in",
"Fill in the boxes to print the size of example.bin: line 8 begin = [ ]; line 9 myfile.[ ](0,ios::end); line 10 end = [ ];",
"line 8 : begin = myfile.tellg();\nline 9 : myfile.seekg(0, ios::end);\nline 10: end = myfile.tellg();","","","C++ in Summary 13")

# ───────────────────────── 2017 ─────────────────────────
Y=2017
q("2017-1ab",Y,"1(a)(b)",4,"blank",["se"],"in",
"Fred Brooks stated that over 90% of (a.        ) of a typical system arise in (b.        ) phase.","(a) the costs  (b) the maintenance","","","L02")
q("2017-1c",Y,"1(c)",2,"blank",["quality"],"in",
"(c.        ) means the ability to rely on the software to function properly when needed.","(c) Dependability","L02 Goals of SE: Dependability 정의 그대로.","","L02")
q("2017-1d",Y,"1(d)",2,"blank",["paradigm"],"in",
"Using global variables is dangerous mainly because this makes all modules (d.        ) one another.","(d) dependent on","","","L02")
q("2017-1efgh",Y,"1(e)~(h)",8,"blank",["ctor"],"in",
"Constructor is a special member function that is automatically called when (e.        ) is (f.        ). The name of a constructor is the same as the name of (g.        ). Normally, you should put code in a constructor to (h.        ) member variables.",
"(e) an object  (f) created  (g) the class  (h) initialize","","","L04")
q("2017-2",Y,"2",15,"short",["encap"],"in",
"List three main benefits of data encapsulation and explain each with sufficient details.",
"""(i) Protection of implementation (safety): clients cannot directly access encapsulated data.
(ii) Readability (understandability): clients need not know how interface functions use encapsulated information.
(iii) Implementation independence: a change in implementation should not affect the interface seen by clients.""","","","Handout 2")
q("2017-3",Y,"3",12,"short",["passing"],"likely",
"(a) Why does high overhead occur when passing large objects by value? (b) Why is the overhead very small with call-by-reference?",
"""(a) The whole object is copied into the parameter (copy constructor called, memory allocated, then destructor at return), which costs time and memory.
(b) Only a reference (an alias, implemented like an address) is passed; no copy of the object is made.""","","","L04 Argument passing")
q("2017-4",Y,"4",12,"trace",["trace"],"in",
"The code has four wrong parts (lines 10, 11 correct). Mark each, explain why wrong, and correct it.",
"""line 12: b = a; → b = &a;   (b is a pointer; must store the address of a)
line 15: b.area() → b->area()   (b is a pointer; use ->)
line 16: c.area() → c->area()   (c is a pointer)
line 17: delete b; → remove it   (b points to a stack object not created by new)""","2025 9번의 원형.",
""" 3: class Rectangle {
 4:     int width, height;
 5: public :
 6:     Rectangle(int x,int y) : width(x),height(y){}
 7:     int area() { return width*height; }
 8: };
 9: int main() {
10:     Rectangle a(3,4);
11:     Rectangle *b, *c;
12:     b = a;
13:     c = new Rectangle (5,6);
14:     cout << "area:" << a.area() << "\\n";
15:     cout << "area:" << b.area() << "\\n";
16:     cout << "area:" << c.area() << "\\n";
17:     delete b;
18:     delete c;
19:     return 0;
20: }""","C++ in Summary 12")
q("2017-5",Y,"5",33,"code",["stack","copy"],"likely",
"TIntStack (with void Push, int Pop, operator=). Write (1) copy constructor, (2) destructor, (3) void Push(int). (4) What problems occur if the copy constructor is not provided? What happens, and why is it a problem?",
"""// (1)
TIntStack::TIntStack(const TIntStack& that) {
    _size = that._size;  _count = that._count;
    _sp = new int[_size];
    for (unsigned int i = 0; i < _count; i++) _sp[i] = that._sp[i];
}
// (2)
TIntStack::~TIntStack() { delete[] _sp; }
// (3)
void TIntStack::Push(int thisValue) {
    assert(_count < _size);      // 또는 if (_count >= _size) return;
    _sp[_count++] = thisValue;
}
(4) what happens: the compiler's default copy constructor does a shallow copy — only the pointer _sp is copied, so both stacks share the same array.
why a problem: changing one stack changes the other, and when both are destroyed delete[] is called twice on the same memory (double free / dangling pointer).""","","","L04")
q("2017-6",Y,"6",12,"short",["copy"],"likely",
"(a) Copy constructor is automatically called when (    ). (b) Write an example for each of the three cases where a copy constructor is called.",
"""(a) a new object is created from an existing object of the same type.
(b) case 1: Person r(p);
    case 2: Person p = q;   (initialization in declaration)
    case 3: f(p);            (passing an object by value)""","주의: p = q; (이미 있는 객체에 대입)는 operator=라서 복사생성자 아님.","","L04 Copy Constructor (1)")

# ───────────────────────── 2016 ─────────────────────────
Y=2016
q("2016-1ab",Y,"1(a)(b)",4,"blank",["couple"],"in",
"Coupling means the degree to which the ability to fulfill a certain responsibility (a.        ) the actions of another component. It is desirable to (b.        ) coupling.",
"(a) depends upon  (b) minimize","L03 원문.","","L03")
q("2016-1c",Y,"1(c)",2,"blank",["encap"],"in","(c.        ) is an instance of a class.","(c) An object","","","L02")
q("2016-1d",Y,"1(d)",2,"blank",["paradigm"],"in",
"Using global variables can be dangerous because it can make all modules (d.        ) on one another.","(d) dependent","","","L02")
q("2016-1ef",Y,"1(e)(f)",4,"blank",["se"],"in",
"Goals of software engineering are (i) (e.        ), (ii) (f.        )",
"(e) produce correct, efficient, and reliable software  (f) minimize the cost of software development and maintenance","","","L02")
q("2016-1ghi",Y,"1(g)(h)(i)",6,"blank",["encap"],"in",
"(g.        ) relies on the separation of interface and implementation. Interface describes (h.        ) an object does. Implementation describes (i.        ) an object does.",
"(g) Data abstraction  (h) what  (i) how","","","L04")
q("2016-2a",Y,"2(1)~(3)",13,"short",["se","quality"],"in",
"(1) Definition of maintenance? (2) High maintainability = easy to (read/understand), (a), (b), (c). (3) Why is maintenance so important?",
"""(1) Activities after delivery of the initial working version: fixing bugs, adapting to changed requirements/hardware, improving the software.
(2) (a) modify  (b) extend  (c) reuse
(3) Over 90% of the costs of a typical system arise in maintenance (Brooks), and any successful software will inevitably be changed.""","","","L02, L03")
q("2016-2b",Y,"2(4)~(6)",13,"short",["encap"],"in",
"(4) What is data encapsulation? (5) Why does it make a program more understandable? (6) Why does it make a program safer?",
"""(4) Implementation is encapsulated by the interface, and the only legal way to get to the implementation is through the interface (internal data is hidden).
(5) Clients only need to know the interface (what it does), not how it is implemented.
(6) Clients cannot directly access/modify the internal data, so they cannot accidentally corrupt it.""","","","L04, Handout 2")
q("2016-3",Y,"3",10,"short",["design"],"in",
"For integration, components are slowly integrated into a completed system using stubs. (1) Meaning of 'slowly integrated'? (2) Meaning of 'stubs'?",
"""(1) Components are added and tested one (a few) at a time, incrementally, so errors can be located easily.
(2) Simple dummy routines with no or very limited behavior, used temporarily for yet-unimplemented parts.""","","","L03 8")
q("2016-4",Y,"4",6,"short",["design"],"in",
"Names should be evocative in the context of a problem. What does 'evocative' mean?",
"The name should call to mind (suggest) the meaning/role of the thing in the problem domain.","L03 'The selection of names' 첫 항목.","","L03")
INF_DECL = """class inf_int {
private:
    char* digits;         // string of digits, dynamically allocated
    unsigned int length;  // number of actual digits
    bool thesign;         // false if negative, true otherwise
    // digits stored in reverse order
    // ex) 15311111111111111 : digits -> "11111111111111351", length=17, thesign=true
public:
    inf_int(int n);
    inf_int(const inf_int& x);
    friend bool operator>(const inf_int&, const inf_int&);
};"""
INF_CTOR = """inf_int::inf_int(int n) {
    char buf[100]; int i = 0;
    long long m = n;               // INT_MIN 대비
    thesign = (m >= 0);
    if (m < 0) m = -m;
    do { buf[i++] = '0' + m % 10; m /= 10; } while (m > 0);   // 역순 저장
    buf[i] = '\\0';
    length = i;
    digits = new char[length + 1];
    strcpy(digits, buf);
}"""
INF_COPY = """inf_int::inf_int(const inf_int& x) {
    length = x.length;
    thesign = x.thesign;
    digits = new char[length + 1];   // deep copy
    strcpy(digits, x.digits);
}"""
q("2016-5code",Y,"5(1)~(3)",30,"code",["opover","copy"],"low",
"inf_int: write (1) operator>, (2) copy constructor, (3) constructor inf_int(int n). Don't call other member functions.",
"""bool operator>(const inf_int& x, const inf_int& y) {
    if (x.thesign != y.thesign) return x.thesign;     // 양수 > 음수
    bool absGreater;
    if (x.length != y.length) absGreater = x.length > y.length;
    else {
        int i = x.length - 1;                          // 최상위 자리부터 비교
        while (i >= 0 && x.digits[i] == y.digits[i]) i--;
        if (i < 0) return false;                       // 같음
        absGreater = x.digits[i] > y.digits[i];
    }
    return x.thesign ? absGreater : !absGreater;       // 음수면 절댓값 큰 쪽이 작음
}
"""+INF_COPY+"\n"+INF_CTOR,"Project 2 범위(마감 11/1)라 올해 중간엔 가능성 낮음. g++ 확인.",INF_DECL,"Project 2")
q("2016-5why",Y,"5(4)(5)",10,"short",["copy"],"likely",
"(4) Why do we generally need to write a copy constructor in class inf_int? (5) What happens if we don't?",
"""(4) inf_int holds a pointer to dynamically allocated memory (digits), so a deep copy is needed.
(5) The default copy constructor does a shallow copy: both objects share the same digits array, so changing one changes the other, and the destructors delete[] the same memory twice (crash / dangling pointer).""","","","L04")

# ───────────────────────── 2015 ─────────────────────────
Y=2015
q("2015-1a",Y,"1(a)",2,"blank",["ctor"],"in",
"In C++, if we do not (a.        ) in a class, the compiler would generate a default constructor.","(a) declare any constructor","","","L04")
q("2015-1bc",Y,"1(b)(c)",4,"blank",["se"],"in",
"Software engineering: ...sound engineering principles in order to (b.        ) obtain software... One of the main goals is to minimize (c.        ) of software development and maintenance.",
"(b) economically  (c) the cost","","","L02")
q("2015-1de",Y,"1(d)(e)",4,"blank",["encap"],"in",
"In the concept of information hiding, (d.        ) of an object can be modified only through (e.        ).","(d) internal data  (e) an interface","2025 1(l)(m)과 동일.","","L02")
q("2015-1f",Y,"1(f)",2,"blank",["design"],"in",
"Good SW design recognizes the inevitability of (f.        ) and plans an accommodation for them from the very beginning.","(f) changes","L03 9. Maintenance and Evolution","","L03")
q("2015-1g",Y,"1(g)",2,"blank",["couple"],"in",
"Coupling is the degree to which the ability to fulfill a certain responsibility (g.        ) upon the actions of another component.","(g) depends","","","L03")
q("2015-1h",Y,"1(h)",2,"blank",["friend"],"likely",
"friend function of a class has the right to access (h.        ) of the class while a typical function does not.","(h) the non-public (private) members","","","L04 friend")
q("2015-1i",Y,"1(i)",2,"blank",["copy"],"likely",
"(i.        ) is called when a new object is created and copied from an existing object with the same type.","(i) Copy constructor","","","L04")
q("2015-2",Y,"2",18,"short",["encap"],"in",
"List three main benefits of data encapsulation and explain each.",
"""(i) Protection of implementation (safety): clients cannot directly access encapsulated data.
(ii) Readability (understandability): clients need not know how interface functions use encapsulated information.
(iii) Implementation independence: a change in implementation should not affect the interface seen by clients.""","","","Handout 2")
q("2015-3",Y,"3",12,"short",["assert"],"in",
"For assert(e): (1) If e is true, (    ). (2) If e is false, (    ). (3) Goal of using assert(e)?",
"""(1) the program just continues.
(2) the program is stopped with an error message indicating the failure of the assertion.
(3) To check that conditions (class invariants) always hold, making programs more reliable.""","L04 원문.","","L04")
q("2015-4",Y,"4",12,"short",["static"],"likely",
"class File { static int open_files; int var; ... }. (1) Meaning of static in line 2? (2) Lifetime of open_files: creation/deletion time? (3) Lifetime of var?",
"""(1) open_files is one variable per class, shared by all File objects.
(2) Created when the program starts (before main, independent of objects); deleted when the program ends.
(3) Created when a File object is created; deleted when that object is destroyed.""","","","L04")
q("2015-5",Y,"5",40,"code",["opover","copy"],"low",
"inf_int: write (1) operator==, (2) copy constructor, (3) constructor inf_int(int n).",
"""bool operator==(const inf_int& x, const inf_int& y) {
    return x.thesign == y.thesign && x.length == y.length
        && strcmp(x.digits, y.digits) == 0;
}
"""+INF_COPY+"\n"+INF_CTOR,"","","Project 2")

# ───────────────────────── 2014 ─────────────────────────
Y=2014
q("2014-1a",Y,"1(a)",2,"blank",["se"],"in","Fred Brooks states that over 90% of the costs of a typical system arise in the (a.        ) phase.","(a) maintenance","","","L02")
q("2014-1b",Y,"1(b)",2,"blank",["ctor"],"in","If we did not declare any constructor in class, the compiler would generate (b.        ).","(b) a default constructor","","","L04")
q("2014-1c",Y,"1(c)",2,"blank",["design"],"in","(c.        ) is a simple dummy routine with no behavior or very limited behavior, used when components are slowly integrated into completed system.","(c) Stub","","","L03")
q("2014-1d",Y,"1(d)",2,"blank",["constfn"],"likely","const member function does not (d.        ) any data members of the object on which it is called.","(d) modify","","","L04")
q("2014-1ef",Y,"1(e)(f)",4,"blank",["encap"],"in","One of the main benefits of data encapsulation is (e.        ) which means a change in (f.        ) should not affect interface seen by clients.","(e) implementation independence  (f) implementation","","","Handout 2")
q("2014-1g",Y,"1(g)",2,"blank",["couple"],"in","(g.        ) is the degree to which the tasks assigned to a component seem to form a meaningful unit.","(g) Cohesion","","","L03")
q("2014-1h",Y,"1(h)",2,"blank",["couple"],"in","Coupling is the degree to which the ability to fulfill a certain responsibility (h.        ) upon the actions of another component.","(h) depends","","","L03")
q("2014-1i",Y,"1(i)",2,"blank",["friend"],"likely","friend function of a class has the right to access (i.        ) members of the class.","(i) non-public (private)","","","L04")
q("2014-1j",Y,"1(j)",2,"blank",["se"],"in","One of the main goals of software engineering is to minimize (j.        ) of software development and maintenance.","(j) the cost","","","L02")
q("2014-2",Y,"2",18,"short",["inline"],"likely",
"(1) What is inline function? (2) In what situations can we benefit? List two. (3) What benefit and why?",
"""(1) A function whose body the compiler inserts at each call site instead of performing a normal function call.
(2) ① small functions (a few lines, e.g. getters)  ② functions called very frequently (e.g. inside loops)
(3) Faster execution, because function-call overhead (argument passing, jump, stack frame, return) is eliminated.""","","","L04")
q("2014-3",Y,"3",12,"short",["copy"],"likely",
"(1) What is shallow copy? (2) You don't need to write a copy constructor if shallow copies are OK. Why?",
"""(1) Copying data members value by value (memberwise); for pointer members only the address is copied, so both objects point to the same memory.
(2) The compiler automatically generates a default copy constructor that performs a shallow copy.""","L04: Compiler automatically generates default copy construct, default operator assignment and default destructor if we don't provide them.","","L04")
q("2014-4",Y,"4",18,"code",["stack","copy"],"likely",
"TIntStack: write the copy constructor TIntStack::TIntStack(const TIntStack& that).",
"""TIntStack::TIntStack(const TIntStack& that) {
    _size = that._size;
    _count = that._count;
    _sp = new int[_size];
    for (unsigned int i = 0; i < _count; i++)
        _sp[i] = that._sp[i];
}""","",STACK_DECL,"L04")
q("2014-5",Y,"5",32,"code",["opover"],"low",
"Complex: write (1) friend Complex operator+(Complex&, Complex&) and (2) ostream& operator<<(ostream&, const Complex&) printing a+bi format.",
"""Complex operator+(Complex& x, Complex& y) {
    return Complex(x.re + y.re, x.im + y.im);
}
"""+CPLX_ANS.replace("Complex& x","const Complex& x"),"","","Operator Overloading")

# ───────────────────────── 2013 ─────────────────────────
Y=2013
q("2013-1ab",Y,"1(a)(b)",4,"blank",["encap"],"in","One of the main benefits of data encapsulation is (a.        ) which means a change in implementation should not affect (b.        ) seen by clients of a class.","(a) implementation independence  (b) the interface","","","Handout 2")
q("2013-1c",Y,"1(c)",4,"blank",["design"],"in","(c.        ) is a simple dummy routine with no or very limited behavior, a temporary substitute for yet-to-be-developed code.","(c) Stub","","","L03")
q("2013-1d",Y,"1(d)",4,"blank",["se"],"in","(d.        ) is the modification of a software product after delivery to correct faults, to improve performance or other attributes.","(d) Maintenance","","","L03")
q("2013-1e",Y,"1(e)",4,"blank",["copy"],"likely","Don't write a copy constructor if (e.        ) are OK.","(e) shallow copies","","","L04")
q("2013-1f",Y,"1(f)",4,"blank",["copy"],"likely","If you need copy constructor, you also need (f.        ) and operator= function.","(f) a destructor","","","L04")
q("2013-2",Y,"2",14,"short",["passing"],"likely",
"Possible advantage and disadvantage of call-by-value (pass-by-value).",
"""(1) advantage: safer — the function works on a copy, so the caller's original argument cannot be modified.
(2) disadvantage: copying overhead — for large objects, copying (copy constructor/destructor calls, memory) costs time and space.""","L04: pass-by-value is safer / Avoid passing large objects by value.","","L04")
q("2013-3",Y,"3",14,"short",["couple"],"in",
"(1) What is coupling? (2) Why is it desirable to minimize coupling?",
"""(1) The degree to which the ability to fulfill a responsibility depends upon the actions of another component.
(2) With low coupling, components are independent: a change in one component has little effect on others, so the system is easier to understand, modify, test and reuse.""","","","L03")
q("2013-4",Y,"4",14,"short",["static"],"likely",
"(1) Meaning of static member variable open_files? (2) Meaning of static member function existing()?",
"""(1) One variable per class shared by all File objects; it exists even if no object has been created.
(2) A function of the class, callable without any object (File::existing()); it cannot access non-static members.""","","","L04")
q("2013-5",Y,"5",34,"code",["opover","copy"],"low",
"inf_int: write (1) operator==, (2) constructor inf_int(const char* str) (e.g. \"-12345\").",
"""bool operator==(const inf_int& x, const inf_int& y) {
    return x.thesign == y.thesign && x.length == y.length
        && strcmp(x.digits, y.digits) == 0;
}
inf_int::inf_int(const char* str) {
    thesign = true;
    if (str[0] == '-') { thesign = false; str++; }
    length = strlen(str);
    digits = new char[length + 1];
    for (unsigned int i = 0; i < length; i++)
        digits[i] = str[length - 1 - i];   // 역순 저장
    digits[length] = '\\0';
}""","","","Project 2")

# ───────────────────────── 2012 ─────────────────────────
Y=2012
q("2012-1abc",Y,"1(a)(b)(c)",12,"blank",["encap","se"],"in",
"Implementation independence means (a.        ) in implementation should not affect (b.        ) seen by clients. Software engineering: ...in order to (c.        ) obtain software that is reliable...",
"(a) a change  (b) the interface  (c) economically","","","Handout 2, L02")
q("2012-1d",Y,"1(d)",4,"blank",["inherit"],"out","Abstract class is a class that contains at least one (d.        ).","(d) pure virtual function","상속 파트 — 올해 중간 범위 밖일 가능성 큼.","","")
q("2012-2a",Y,"2(1)",6,"short",["passing"],"likely","It is often desirable to avoid passing large objects by value. Why?",
"The whole object is copied (copy constructor, memory allocation, destructor), which wastes time and memory.","","","L04")
q("2012-2b",Y,"2(2)",6,"short",["quality"],"in","What is dependability?","The ability to rely on the software to function properly when needed.","","","L02")
q("2012-3a",Y,"3(1)",5,"short",["encap"],"in","Main difference between 'class' and 'object' in C++.",
"A class is a type (blueprint) defining attributes and behaviors; an object is an instance of a class created in memory with its own state.","","","L02")
q("2012-3b",Y,"3(2)(3)",10,"short",["constfn"],"likely","(2) Difference between const member function and a general member function? (3) Main benefits of const member function?",
"""(2) A const member function cannot modify any data members of the object (read-only), enforced by the compiler; a general member function can.
(3) It assures clients of its benign nature: safety (no accidental modification) and readability.""","","","L04")
q("2012-4",Y,"4",12,"short",["copy"],"likely","(1) If you need to write a copy constructor, you also need a destructor. Why? (2) If shallow copies are OK, you don't need a copy constructor. Why?",
"""(1) A copy constructor is needed when the class owns dynamically allocated memory; that memory must be released by a destructor (otherwise a memory leak).
(2) The compiler-generated default copy constructor already does a shallow (memberwise) copy.""","","","L04")
q("2012-5",Y,"5",15,"short",["assert"],"in","assert(x): (1) What should be put into x? (2) What does it do? (3) Why useful?",
"""(1) A condition (boolean expression) that must always be true at that point, e.g. a class invariant.
(2) If x is true, continue; if false, stop the program with an error message showing the failed assertion.
(3) It detects bugs early and makes programs more reliable.""","","","L04")
q("2012-6",Y,"6",30,"code",["opover","copy"],"low","inf_int: write (1) default constructor (value 0), (2) copy constructor, (3) inf_int(int n).",
"""inf_int::inf_int() {
    digits = new char[2];
    digits[0] = '0'; digits[1] = '\\0';
    length = 1; thesign = true;
}
"""+INF_COPY+"\n"+INF_CTOR,"","","Project 2")

# ───────────────────────── 2011 ─────────────────────────
Y=2011
q("2011-1ac",Y,"1(a)(c)",6,"blank",["se"],"in",
"Software crisis... rapid increases in computer power and the (a.        ) of the problems. / Fred Brooks: over 90% of costs arise in the (c.        ) phase.",
"(a) complexity  (c) maintenance","","","L02")
q("2011-1bd",Y,"1(b)(d)",6,"blank",["inherit"],"out","(b.        ) is a function whose behavior can be overridden within an inheriting class. / Dynamic binding means that binding occurs at (d.        ).","(b) virtual function  (d) run time","범위 밖일 가능성 큼.","","")
q("2011-2",Y,"2",12,"short",["quality"],"in","(1) What is portability? (2) What is dependability?",
"""(1) The ability to run (reuse) the software on a different platform (HW, OS) with little or no modification.
(2) The ability to rely on the software to function properly when needed.""","","","Handout 1, L02")
q("2011-3",Y,"3",14,"short",["encap"],"in","(1) What is data encapsulation? (2) Two important benefits and why.",
"""(1) Hiding the implementation behind the interface: the only legal way to access the implementation (internal data) is through the interface.
(2) ① Safety: clients cannot directly access/corrupt internal data.  ② Implementation independence: the implementation can change without affecting clients that use the interface.""","","","L04, Handout 2")
q("2011-4",Y,"4",12,"short",["inherit"],"out","(1) Meaning of 'protected'? (2) Why use protected only where really necessary?",
"""(1) Members accessible within the class and its derived classes, but not by other clients.
(2) It weakens encapsulation: derived classes depend on the implementation, so changes break them.""","상속 파트.","","")
q("2011-5",Y,"5",15,"short",["inline"],"likely","(1) What is inline function? (2) Two situations where it helps. (3) What benefit and why?",
"""(1) A function whose body is expanded at the call site by the compiler instead of a normal call.
(2) ① small function body  ② frequently called (e.g. in loops)
(3) Faster execution — function-call overhead is removed.""","","","L04")
q("2011-6code",Y,"6(1)(2)",20,"code",["opover"],"low","Complex: write (1) member Complex Complex::operator+(const Complex& x), (2) friend operator<<.",
"""Complex Complex::operator+(const Complex& x) {
    return Complex(re + x.re, im + x.im);
}
"""+CPLX_ANS.replace("Complex& x","const Complex& x"),"","","Operator Overloading")
q("2011-6theory",Y,"6(3)(4)(5)",15,"short",["friend","copy","passing"],"likely",
"(3) Why should operator<< be a friend of Complex? (4) Do we need a copy constructor for Complex? Why? (5) Benefits of parameter type const Complex& (two).",
"""(3) Its left operand is an ostream, so it cannot be a member of Complex, yet it must access the private re and im.
(4) No. Complex has no pointer/dynamic memory, so the default shallow copy is enough.
(5) ① No copy of the object is made (efficient).  ② The argument cannot be modified (safe); temporaries/const objects can be passed.""","","","L04")

# ───────────────────────── 2010 ─────────────────────────
Y=2010
q("2010-1ab",Y,"1(a)(b)",4,"blank",["se"],"in","(a.        ) is defined as modification of a software product after delivery... (a) is considered to be the most (b.        ) part of the software life cycle.","(a) Maintenance  (b) expensive (costly)","","","L02")
q("2010-1c",Y,"1(c)",2,"blank",["quality"],"in","(c.        ) is the software feature to be able to reuse existing code when moving software from one environment (platform) to another.","(c) Portability","","","Handout 1")
q("2010-1d",Y,"1(d)",2,"blank",["paradigm"],"in","(d.        ) involves splitting complex program tasks into smaller pieces with clear flow-control and interfaces between components.","(d) Structured (modular) programming","","","L02")
q("2010-1ef",Y,"1(e)(f)",4,"blank",["encap"],"in","The advantage of using data encapsulation comes when (e.        ) of the class changes but (f.        ) remains the same.","(e) the implementation  (f) the interface","","","Handout 2")
q("2010-1gh",Y,"1(g)(h)",4,"blank",["assert"],"in","(g.        ) contains a boolean expression that you believe will be true... writing (g) while programming is one of the quickest and most effective ways to detect (h.        ).","(g) An assertion  (h) bugs","2022 1(l)(m)과 동일.","","L04")
q("2010-1i",Y,"1(i)",2,"blank",["design"],"in","A good software design recognizes the inevitability of (i.        ) and plans an accommodation for them from the very beginning.","(i) changes","","","L03")
q("2010-1jkl",Y,"1(j)(k)(l)",8,"short",["copy"],"likely","If you need to write a copy constructor, you also need to write (j.        ) and (k.        ). Why? (l)",
"""(j) a destructor  (k) operator= (assignment operator)
(l) A copy constructor is needed when the class owns dynamically allocated memory (deep copy). The destructor must free that memory, and operator= must also deep-copy, since the default one does a shallow copy (sharing memory, double delete, leak).""","","","L04")
q("2010-2",Y,"2",10,"short",["paradigm"],"in","(1) Why is overusing global variables not desirable? (2) Main advantage of OOP compared to structured programming?",
"""(1) Any module can change a global variable, so all modules become dependent on one another: side effects are hard to track, and code is hard to debug, modify and reuse.
(2) OOP combines data and operations into objects (encapsulation), so large software is easier to maintain, extend and reuse.""","","","L02")
q("2010-4a",Y,"4(1)(2)",4,"short",["couple"],"in","Explain (1) Cohesion (2) Coupling.",
"""(1) The degree to which the tasks assigned to a component form a meaningful unit (maximize).
(2) The degree to which a component's ability to fulfill a responsibility depends on other components (minimize).""","","","L03")
q("2010-4b",Y,"4(3)(4)",4,"short",["copy"],"likely","Explain (3) shallow copy (4) deep copy.",
"""(3) Copying member values only; pointers are copied so both objects share the same memory.
(4) Allocating new memory and copying the pointed-to data, so each object has its own copy.""","","","L04")
q("2010-5",Y,"5",10,"short",["passing"],"likely","(1) Why is it inefficient to pass large objects by value? (2) One beneficial effect of pass-by-value and why.",
"""(1) The whole object is copied (copy constructor, memory, destructor) on every call.
(2) Safety: the function works on a copy, so the caller's original data cannot be modified accidentally.""","","","L04")
q("2010-6",Y,"6",28,"code",["opover","copy"],"low","inf_int: (1) copy constructor, (2) friend bool operator<, (3) maximum number it can represent and justification.",
"""// (1) 2016 해설의 copy constructor와 동일 (digit 이름만 다름)
// (2)
bool operator<(const inf_int& l, const inf_int& r) {
    return r > l;   // 시험에선 operator> 로직을 직접 써야 함 (다른 멤버 호출 금지)
}
(3) length is unsigned int, so up to 2^32 − 1 (4294967295) digits: max ≈ 10^4294967295 − 1 (all digits 9). In practice limited by available memory.""","","","Project 2")
q("2010-7",Y,"7",7,"short",["friend"],"likely","Why should the use of friend function/class be minimized?",
"Friends can access private members, which breaks encapsulation and increases coupling: a change in the implementation can break friend code.","","","L04")
q("2010-8",Y,"8",9,"short",["quality"],"in","List at least six properties of good software.",
"correctness, efficiency, maintainability (readability, modifiability, extensibility, reusability), reliability (robustness), usability, portability  (+ security, completeness, consistency...)","Handout 1 목록.","","Handout 1")

# ───────────────────────── 2009 ─────────────────────────
Y=2009
q("2009-1-12",Y,"1(1)(2)",4,"blank",["se","paradigm"],"in","(1) One goal of SE is to minimize the (c        ) of software development and maintenance. (2) OOP increases (programmer productivity), (    ), (    ), and (    ).",
"(1) cost  (2) quality, understandability, scalability (extensibility, reusability), lifetime (maintainability) of software","L02 'Why Object Oriented?' 목록.","","L02")
q("2009-1-345",Y,"1(3)(4)(5)",4,"blank",["couple","constfn","friend"],"likely","(3) (    ) is the degree to which each module relies on others. (    ) measures how strongly-related a module's responsibilities are. Maximize (    ) and minimize (    ). (4) (    ) member function does not modify any data members. (5) (    ) function of a class has the right to access the non-public members.",
"(3) Coupling, Cohesion, cohesion, coupling  (4) const  (5) friend","","","L03, L04")
q("2009-1-67",Y,"1(6)(7)",2,"blank",["inherit"],"out","(6) An abstract class should contain at least one (    ). (7) (    ) can check whether two classes have inheritance relationship.","(6) pure virtual function  (7) dynamic_cast","","","")
q("2009-2",Y,"2",6,"short",["encap"],"in","(1) What is encapsulation? (2) Two important benefits and why.",
"""(1) Concealing the implementation (internal data) of a class so it can be accessed only through its interface.
(2) ① Safety — clients cannot corrupt internal data directly. ② Implementation independence — implementation can change without affecting clients.""","","","L02, Handout 2")
q("2009-3",Y,"3",6,"short",["passing"],"likely","(a) void X::f(T arg) (b) void X::f(T* argp) (c) void X::f(const T* argp). (1) Two purposes of using * in (b) vs (a)? (2) Purpose of const in (c) vs (b)?",
"""(1) purpose1: avoid copying a large object (only an address is passed → efficient).
    purpose2: allow the function to modify the caller's object.
(2) Prevent the function from modifying the pointed-to object (read-only) while keeping the efficiency.""","2022 기말 4번과 같은 유형 (T& 버전).","","L04 Argument Passing")
q("2009-4",Y,"4",6,"trace",["inherit"],"out","What is the output? (B with virtual get_val and non-virtual gv2; D1 overrides get_val; D2 declares virtual gv2; called via B* array)",
"0 : -1\n1 : -2\n2 : 2\n3 : -4","gv2는 B에서 non-virtual이라 B*로 부르면 B::gv2. D2(4)는 B() 기본생성자 → z=-2 → -4. g++ 확인.","","")
q("2009-5",Y,"5",2,"short",["se"],"in","What is software crisis?",
"The difficulty of writing correct, understandable, verifiable programs on time and budget, caused by rapid increases in computer power and the complexity of problems that software technology could not follow.","","","L02")

# ───────────────────────── 2022 기말 (중간 범위 문항만) ─────────────────────────
Y=2022
q("2022F-2",Y,"기말 2",18,"trace",["trace","passing"],"likely",
"(1) Meaning of '*' in line 2? (2) '&' in line 3? (3) '&' in line 4? (4) first and second '*' in '*y*x' in line 7? (5) Output of line 9?",
"""(1) pointer type declaration (y is a pointer to int)
(2) reference type declaration (z is an alias of x)
(3) address-of operator
(4) first: the value-of (dereference) operator / second: multiplication
(5) 82 82 82 5""","L04 ref.cpp와 거의 같은 코드! x=9 → z=*y*x=81 (z가 x라서 x=81) → x++ → 82. w는 5에서 고정.",
"""1: int x=5;
2: int* y;
3: int& z=x;
4: y=&x;
5: int w=*y;
6: x=9;
7: z=*y*x;
8: x++;
9: cout << x << " " << *y << " " << z << " " << w << endl;""","L04 ref.cpp, C++ in Summary 10")
q("2022F-4",Y,"기말 4",12,"short",["passing"],"likely",
"(a) void X::f(T arg) (b) void X::f(T& argp) (c) void X::f(const T& argp). (1) Two purposes of '&' in (b) vs (a)? (2) Purpose of const in (c) vs (b)?",
"""(1) purpose 1: avoid copying the argument (no copy constructor call) → efficient for large objects.
    purpose 2: the function can modify the caller's original object.
(2) The function cannot modify the argument (read-only) while still avoiding the copy → safe and efficient.""","L04: Do not ever use pass by reference (without const) for read-only parameters.","","L04")

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank.json")
ids = [x["id"] for x in Q]; assert len(ids)==len(set(ids)), "dup id"
# 영어판 (bank_en.json: tip·answer 번역) → *_en
import sys as _sys; _sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../../_shared"))
from en_lessons import attach_q_en
print("english:", attach_q_en(Q, [os.path.join(os.path.dirname(os.path.abspath(__file__)), "bank_en.json")]))
json.dump({"version":1,"questions":Q}, open(out,"w"), ensure_ascii=False, indent=0)
print(len(Q), "questions;", sum(1 for x in Q if x["scope"]!="out"), "in-scope-ish")
