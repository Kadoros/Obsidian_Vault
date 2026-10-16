# 레슨 점검 문제 (즉시 채점: mc / ox / blank). blank의 accept는 소문자·공백 무시 비교
from cdsl import C

# ── U1 ──
C("c-cri-1","crisis","blank","(a) arose because computer hardware power grew rapidly and the (b) of software systems increased even faster than software technology could follow.",
  ["software crisis","complexity"], accept=[["software crisis","소프트웨어 위기"],["complexity","복잡도"]])
C("c-cri-2","crisis","mc","소프트웨어 위기의 '원인'으로 교안이 꼽은 것은?",2,
  choices=["프로그래머 부족","하드웨어 가격","복잡도 (complexity)","유지보수 비용"])
C("c-cri-3","crisis","ox","소프트웨어 위기의 증상에는 예산 초과(over-budget), 일정 초과(over-time), 요구사항 불충족이 있다.",True)
C("c-lc-1","lifecycle","blank","Fred Brooks: over 90% of (a) of a typical system arise in the (b) phase, and any successful piece of software will inevitably be (c).",
  ["the costs","maintenance","maintained"], accept=[["the costs","costs","cost","the cost","비용"],["maintenance","the maintenance","유지보수"],["maintained","유지보수된다"]])
C("c-lc-2","lifecycle","mc","소프트웨어 생명주기 순서로 옳은 것은?",1,
  choices=["Design → Requirement → Test → Implementation → Maintenance","Requirement Analysis → Design → Implementation → Test → Maintenance","Implementation → Design → Test → Requirement → Maintenance","Requirement → Implementation → Design → Maintenance → Test"])
C("c-lc-3","lifecycle","ox","Test 단계에는 unit test와 integration test가 있다.",True)
C("c-sed-1","se-def","blank","Fritz Bauer: software engineering is the establishment and use of sound engineering principles in order to (a) obtain software that is (b) and works efficiently.",
  ["economically","reliable"], accept=[["economically","경제적으로"],["reliable","신뢰할 수 있는"]])
C("c-sed-2","se-def","mc","SE의 목표 중 '필요할 때 SW가 제대로 작동한다고 믿을 수 있는 능력'은?",1,
  choices=["Maintainability","Dependability","Efficiency","Usability"])
C("c-sed-3","se-def","blank","Goals of software engineering: (i) produce a correct, efficient, and reliable software (ii) minimize (a) of software development and maintenance.",
  ["the cost"], accept=[["the cost","cost","costs","the costs","비용"]])
C("c-sed-4","se-def","ox","IEEE 정의에 따르면 SE는 SW의 개발·운영·유지보수에 체계적이고 규율 있고 정량화 가능한 접근을 적용하는 것이다.",True)
C("c-qual-1","quality","mc","Handout 1에서 maintainability에 포함되지 '않는' 것은?",3,
  choices=["readability","modifiability","extensibility","security"])
C("c-qual-2","quality","blank","A program with high maintainability is easy to read, easy to (a), easy to (b), and easy to reuse.",
  ["modify","extend"], accept=[["modify","change","수정"],["extend","확장","debug","test"]])
C("c-qual-3","quality","ox","correctness는 사용자 요구사항·명세를 오류 없이 만족하는 것이다.",True)
C("c-rob-1","robust","blank","(a) means the ability of the software to consistently perform its required functions without failure under specified conditions for a specified period.",
  ["reliability"], accept=[["reliability","신뢰성"]])
C("c-rob-2","robust","mc","재해나 잘못된 입력 같은 예외 상황에서도 올바른 기능을 유지하는 성질은?",2,
  choices=["usability","portability","robustness","conciseness"])
C("c-sp-1","sw-props","mc","'divide and conquer'에 해당하는 SW 성질은?",0,
  choices=["Modularity","Localization","Uniformity","Confirmability"])
C("c-sp-2","sw-props","mc","'be able to prove that the software works properly'에 해당하는 SW 성질은?",3,
  choices=["Completeness","Abstraction","Encapsulation","Confirmability"])
C("c-sp-3","sw-props","ox","Localization은 비슷한 것들을 한곳에 모으는 것(collect similar things together)이다.",True)
C("c-uns-1","unstructured","blank","(a) programming makes extensive use of GOTO statements, and the program contains only a single code block with only (b) data.",
  ["unstructured","global"], accept=[["unstructured","비구조적"],["global","전역"]])
C("c-uns-2","unstructured","ox","스파게티 코드는 goto가 여기저기 점프해서 흐름을 따라가기 어렵고 수정하기 어려운 코드다.",True)
C("c-pro-1","procedural","blank","structured programming ≒ (a) approach ≒ (b) ≒ functional decomposition",
  ["top-down","divide and conquer"], accept=[["top-down","top down","하향식"],["divide and conquer","분할 정복"]])
C("c-pro-2","procedural","mc","모듈 프로그래밍에서 '보이는 것'과 '숨겨지는 것'은?",0,
  choices=["interface는 visible, implementation은 hidden","implementation은 visible, interface는 hidden","둘 다 visible","둘 다 hidden"])
C("c-pro-3","procedural","ox","절차적 프로그래밍에서 프로그램은 프로시저 호출의 나열이다.",True)
C("c-gv-1","global-vars","blank","Using (a) variables is often unsafe because this makes all modules (b) on one another.",
  ["global","dependent"], accept=[["global","전역"],["dependent","dependant","의존"]])
C("c-gv-2","global-vars","mc","전역 변수 문제의 해결책으로 교안이 제시한 것은?",1,
  choices=["전역 변수를 const로","데이터를 모듈 안에 지역화 (modularized data)","goto 사용","전역 변수 이름을 길게"])
C("c-gv-3","global-vars","ox","전역 변수를 쓰면 어떤 모듈도 독립적으로 개발·이해할 수 없게 된다.",True)
C("c-ow-1","oop-why","mc","절차적/모듈 프로그래밍의 문제로 교안에 나온 것은?",2,
  choices=["데이터와 연산이 한 객체에 묶여 있음","상속이 너무 많음","데이터와 연산이 분리(decoupled)되어 있어 큰 시스템에서 디버그·확장·유지보수가 어려움","컴파일이 느림"])
C("c-ow-2","oop-why","blank","(a) is a programming paradigm based on the concept of (b), which can contain data and code.",
  ["object-oriented programming","objects"], accept=[["object-oriented programming","oop","object oriented programming","객체지향 프로그래밍"],["objects","object","객체"]])
C("c-ow-3","oop-why","ox","OOP에서 'object + object = program'이고, 절차적 프로그래밍에서는 'data + function = program'이다.",True)
C("c-adt-1","adt","mc","ADT가 'abstract'라고 불리는 이유는?",1,
  choices=["추상 클래스를 써서","데이터와 연산이 특정 구현과 독립적으로 명세되어서","데이터가 없어서","상속을 쓰기 때문에"])
C("c-adt-2","adt","blank","ADT = data + (a) (no (b))",
  ["operations","implementation"], accept=[["operations","operation","연산"],["implementation","구현"]])
C("c-adt-3","adt","ox","C++에서는 class로 ADT를 정의한다.",True)
C("c-co-1","class-object","blank","(a) is an instance of a class. Class defines attributes (member (b)) and behaviors (member functions).",
  ["an object","variables"], accept=[["an object","object","객체"],["variables","variable","data","변수"]])
C("c-co-2","class-object","ox","같은 클래스로 만든 객체들은 같은 메모리 공간을 공유하므로 사실상 하나의 객체이다.",False,
  explain="각 객체는 다른 메모리 공간·주소를 받는 서로 다른 객체. 공유하는 건 클래스의 메서드.")
C("c-co-3","class-object","mc","객체의 내부 데이터에 접근할 수 있는 것은?",3,
  choices=["모든 함수","main 함수","전역 함수","그 클래스의 메서드"])
C("c-ei-1","encap-intro","blank","In the concept of information hiding, (a) of an object can be modified only through (b).",
  ["internal data","an interface"], accept=[["internal data","data","내부 데이터"],["an interface","interface","interfaces","인터페이스"]])
C("c-ei-2","encap-intro","ox","캡슐화는 메시지를 보내는 객체들로부터 클래스의 기능적 세부를 감춘다.",True)
C("c-ip-1","inherit-poly","mc","C++에서 다형성(polymorphism)을 지원하는 기능이 '아닌' 것은?",3,
  choices=["virtual function","operator overloading","template","static member"])
C("c-ip-2","inherit-poly","ox","상속의 목표는 객체(클래스)의 재사용이다.",True)

# ── U2 ──
C("c-io-1","cpp-io","mc","cout << Hello; 가 출력하는 것은?",1,
  choices=["문자열 Hello","변수 Hello의 값","컴파일 오류가 항상 남","아무것도 안 함"])
C("c-io-2","cpp-io","blank","cout은 (a) 스트림 객체(standard output), cin은 (b) 스트림 객체(standard input)이다.",
  ["screen","keyboard"], accept=[["screen","화면","monitor"],["keyboard","키보드"]])
C("c-io-3","cpp-io","ox","C++ 프로그램 안에서 C 코드(printf 등)를 써도 된다.",True)
C("c-bas-1","cpp-basics","mc","for (A; B; C) { body } 의 실행 순서는?",0,
  choices=["A → B → body → C → B → body → C …","A → body → B → C …","B → A → body → C …","A → C → B → body …"])
C("c-bas-2","cpp-basics","ox","C++ string은 C 문자열(char*)과 달리 메모리를 자동으로 관리한다.",True)
C("c-bas-3","cpp-basics","mc","함수의 지역 변수(매개변수 포함)는 언제 생성·삭제되나?",2,
  choices=["프로그램 시작·끝","컴파일 때","함수 호출 때 생성, 반환 때 삭제","new·delete 때"])
C("c-ptr-1","pointer","mc","int *x; 에서 *의 의미는?",2,
  choices=["곱셈","가리키는 값 (dereference)","포인터 타입 선언","주소 연산자"])
C("c-ptr-2","pointer","mc","x = &y; 에서 &의 의미는?",1,
  choices=["비트 AND","주소 연산자 (address-of)","참조 타입 선언","논리 AND"])
C("c-ptr-3","pointer","mc","int& y = x; 에서 &의 의미는?",3,
  choices=["비트 AND","주소 연산자","포인터 선언","참조 타입 선언"])
C("c-ptr-4","pointer","blank","int *xPtr, x; x = 5; xPtr = &x; *xPtr = 10; cout << x; 의 출력은 (a) 이다.",
  ["10"], accept=[["10"]])
C("c-nd-1","new-delete","blank","Dynamic memory allocation means memory allocation occurs at (a). C의 malloc/free는 C++의 (b)/(c)에 대응한다.",
  ["run-time","new","delete"], accept=[["run-time","run time","runtime","execution time","실행 시간"],["new"],["delete"]])
C("c-nd-2","new-delete","mc","int* p = new int[10]; 으로 할당한 메모리를 해제하는 올바른 문장은?",1,
  choices=["delete p;","delete[] p;","free(p);","p = NULL;"])
C("c-nd-3","new-delete","ox","C++은 Java처럼 garbage collection이 있어서 delete를 안 해도 된다.",False)
C("c-sd-1","static-dynamic","mc","정적 할당 배열 int x[10]; 의 단점은?",0,
  choices=["크기가 컴파일 시간에 고정되어 실행 중 바꿀 수 없음","직접 해제해야 함","댕글링 포인터 위험","느림"])
C("c-sd-2","static-dynamic","mc","동적 할당 배열 new int[n]의 단점은?",2,
  choices=["크기를 실행 중 정할 수 없음","컴파일 오류가 남","프로그래머가 delete[]로 직접 해제해야 해서 메모리 누수·댕글링 위험","스택에 할당됨"])
C("c-sd-3","static-dynamic","ox","정적 할당 배열은 범위를 벗어나면 메모리가 자동으로 해제된다.",True)
C("c-cb-1","class-basic","ox","생성자와 소멸자는 객체가 생성·삭제될 때 자동으로 호출된다.",True)
C("c-cb-2","class-basic","mc","생성자에서 멤버 변수를 초기화하지 않으면?",1,
  choices=["컴파일 오류","쓰레기 값(garbage)을 가져서 위험·불안정","자동으로 0이 됨","소멸자가 호출 안 됨"])
C("c-op-1","obj-pointer","mc","Rectangle *foo; Rectangle obj(3,4); 일 때 foo가 obj를 가리키게 하는 문장은?",2,
  choices=["foo = obj;","*foo = obj;","foo = &obj;","foo = new obj;"])
C("c-op-2","obj-pointer","mc","bar = new Rectangle(5,6); 일 때 넓이를 호출하는 올바른 식은?",1,
  choices=["bar.area()","bar->area()","&bar.area()","*bar->area()"])
C("c-op-3","obj-pointer","blank","baz = new Rectangle[2]; 이면 기본 생성자(width=1, height=1)가 (a) 번 불리고, baz[0].area()의 값은 (b) 이다. 해제는 (c) baz; 로 한다.",
  ["2","1","delete[]"], accept=[["2","두","two"],["1","one"],["delete[]","delete []"]])
C("c-op-4","obj-pointer","ox","배열 원소 baz[0]은 객체이므로 baz[0].area()처럼 점(.)으로 멤버에 접근한다.",True)
C("c-fs-1","fstream","blank","ofstream: write on files / (a): read from files / (b): read and write from/to files",
  ["ifstream","fstream"], accept=[["ifstream"],["fstream"]])
C("c-fs-2","fstream","mc","파일이 제대로 열렸는지 확인하는 함수는?",0,
  choices=["is_open()","eof()","tellg()","open_ok()"])
C("c-fs-3","fstream","mc","스트림 상태 함수 중 '파일 끝에 도달했으면 true'인 것은?",2,
  choices=["bad()","fail()","eof()","good()"])
C("c-om-1","open-modes","blank","ios::app means all output operations are performed at the (a) of the file, appending the content. ios::(b) means if the file already exists, its previous content is deleted and replaced.",
  ["end","trunc"], accept=[["end","the end","끝"],["trunc","ios::trunc"]])
C("c-om-2","open-modes","mc","ofstream의 기본 열기 모드는?",0,
  choices=["ios::out","ios::in","ios::in | ios::out","ios::app"])
C("c-om-3","open-modes","mc","ios::ate의 뜻은?",3,
  choices=["바이너리 모드","모든 출력을 끝에 덧붙임","기존 내용 삭제","초기 위치를 파일 끝으로"])
C("c-om-4","open-modes","blank","열기 모드 플래그 여러 개는 비트 (a) 연산자로 결합한다. 예) ios::out (b) ios::binary",
  ["OR","|"], accept=[["or","bitwise or","|"],["|"]])
C("c-st-1","seek-tell","blank","파일 크기 구하기: begin = myfile.(a); myfile.seekg(0, ios::(b)); end = myfile.tellg(); size = end − begin",
  ["tellg()","end"], accept=[["tellg()","tellg"],["end"]])
C("c-st-2","seek-tell","mc","get(읽기) 위치를 바꾸는 함수는?",1,
  choices=["tellg","seekg","seekp","tellp"])
C("c-st-3","seek-tell","mc","seekg(offset, direction)에서 '현재 위치부터'를 뜻하는 direction은?",1,
  choices=["ios::beg","ios::cur","ios::end","ios::now"])
C("c-bin-1","binary","mc","바이너리 파일 전체를 메모리로 읽을 때 'ios::ate로 연 직후 tellg()'가 주는 값은?",2,
  choices=["0","현재 줄 번호","파일 크기","파일 이름 길이"])
C("c-bin-2","binary","ox","바이너리 파일을 복사할 때 getline으로 한 줄씩 읽어 쓰면 된다.",False,
  explain="read/write로 바이트 블록을 통째로. getline은 텍스트용이라 바이너리가 깨짐(기출 감점).")
C("c-bin-3","binary","blank","바이너리 입출력 함수: file.(a)(memblock, size); out.(b)(memblock, size); 여기서 memblock의 타입은 char* 이다.",
  ["read","write"], accept=[["read"],["write"]])
C("c-bin-4","binary","mc","ios::ate로 열고 크기를 얻은 뒤, read 전에 해야 하는 것은?",0,
  choices=["seekg(0, ios::beg)로 처음으로 되감기","close()","seekp(0, ios::end)","clear()"])
