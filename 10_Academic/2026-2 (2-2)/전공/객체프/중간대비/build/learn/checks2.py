from cdsl import C

# ── U3 ──
C("c-rdd-1","rdd","mc","책임 주도 설계에서 한 객체 안의 책임들은?",1,
  choices=["서로 관련 없어야 함","서로 밀접하게 관련되어야 함","하나뿐이어야 함","다른 객체와 겹쳐야 함"])
C("c-rdd-2","rdd","ox","책임 주도 설계에서는 시스템이 수행할 활동(책임)을 시스템의 객체들에 분배한다.",True)
C("c-dp-1","dev-process","mc","개발 과정 9단계에서 CRC 카드를 쓰는 단계는?",2,
  choices=["1. Initial Description","2. Refine Specification","4. Identification of Components Responsibilities","8. Integration"])
C("c-dp-2","dev-process","mc","개발 과정 9단계에서 stub을 쓰는 단계는?",3,
  choices=["3. Identification of Components","5. Formalize the Interface","7. Implementing Components","8. Integration of Components"])
C("c-dp-3","dev-process","blank","개발 과정의 마지막 단계는 Maintenance & (a) 이고, 첫 단계는 Initial (b) (Specification) 이다.",
  ["Evolution","Description"], accept=[["evolution","진화"],["description"]])
C("c-sc-1","scenario","mc","IIKH의 모호한 초기 명세를 다듬는 주요 도구는?",0,
  choices=["시나리오 따라가기 (walking through scenarios)","UML 클래스 다이어그램","단위 테스트","stub"])
C("c-sc-2","scenario","blank","다른 저자들은 시나리오를 개발하는 과정을 (a) 라고 부른다.",
  ["use-cases"], accept=[["use-cases","use cases","use-case","use case","유스케이스"]])
C("c-sc-3","scenario","ox","시나리오를 따라갈 때는 이미 동작하는 응용이 있다고 가정하고 사용 방법을 따라가 본다.",True)
C("c-cmp-1","component","mc","좋은 구성요소(component)의 조건이 '아닌' 것은?",3,
  choices=["작고 잘 정의된 책임 집합","다른 구성요소와 상호작용 최소","책임을 연결할 수 있는 추상적 설계 단위","가능한 많은 책임을 가짐"])
C("c-cmp-2","component","ox","구성요소는 다른 구성요소와 가능한 많이 상호작용해야 한다.",False)
C("c-crc-1","crc","blank","CRC 카드의 C-R-C는 Component, (a), (b) 이다.",
  ["Responsibility","Collaborators"], accept=[["responsibility","responsibilities","책임"],["collaborators","collaborator","collaboration","협력자"]])
C("c-crc-2","crc","mc","IIKH의 Greeter 카드에서 협력자(Collaborators)는?",1,
  choices=["Recipe, Meal","Database Manager, Plan Manager","Date, Meal","없음"])
C("c-ik-1","iikh-components","mc","레시피 '하나'의 재료 목록을 유지하고 자기를 편집·표시·인쇄하는 IIKH 구성요소는?",2,
  choices=["Recipe Database","Planner","Recipe","Greeter"])
C("c-ik-2","iikh-components","mc","인원수를 설정하면 레시피를 자동 조절하고 한 끼 장보기 목록을 만드는 구성요소는?",0,
  choices=["Meal","Date","Recipe Database","Greeter"])
C("c-ik-3","iikh-components","blank","IIKH는 (a) 개의 SW 구성요소로 다 할 수 있고, 이 시점에 구성요소를 서로 다른 (b) 에게 나눠 개발시킬 수 있다.",
  ["6","programmers"], accept=[["6","six","여섯"],["programmers","programmer","프로그래머","개발자"]])
C("c-ik-4","iikh-components","ox","RecipeDB(Recipe Database)는 레시피 모음을 관리해서 탐색·검색·추가·편집을 허용한다.",True)
C("c-bs-1","behavior-state","mc","구성요소 안에 있는 모든 정보(데이터 값)를 뜻하는 것은?",1,
  choices=["Behavior","State","Interface","Responsibility"])
C("c-bs-2","behavior-state","ox","Recipe 인스턴스는 많지만 모두 같은 방식으로 행동하므로 그 행동은 Recipe 클래스에 공통이다.",True)
C("c-cc-1","coupling-cohesion","blank","(a) is the degree to which each program module relies on each one of the other modules. (b) is a measure of how strongly-related the responsibilities of a single module are.",
  ["Coupling","Cohesion"], accept=[["coupling","결합도"],["cohesion","응집도"]])
C("c-cc-2","coupling-cohesion","blank","Good design: (a) cohesion and (b) coupling. We want to (c) coupling.",
  ["high","low","minimize"], accept=[["high","tight","strong","높은"],["low","loose","weak","낮은"],["minimize","최소화"]])
C("c-cc-3","coupling-cohesion","mc","결합도가 높을 때의 문제는?",2,
  choices=["코드가 짧아짐","응집도가 자동으로 높아짐","한 모듈의 변경이 다른 모듈에 영향을 줘 유지보수·재사용이 어려움","컴파일이 빨라짐"])
C("c-cc-4","coupling-cohesion","ox","Coupling means the degree to which the ability to fulfill a certain responsibility depends upon the actions of another component, and it is desirable to maximize it.",False,
  explain="정의는 맞지만 결합도는 minimize.")
C("c-ii-1","interface-impl","mc","Two views of a software system에서 'text buffer, window pointer, ingredient list'는?",1,
  choices=["interface","implementation","scenario","collaborator"])
C("c-ii-2","interface-impl","blank","Information hiding is the (a) hiding of implementation details. The user of a software component need only know (b) it does, not how it does it.",
  ["purposeful","what"], accept=[["purposeful","intentional","의도적"],["what","무엇을"]])
C("c-pp-1","public-private","ox","Private view는 구성요소 안에서만 쓰는 특징(데이터 또는 행동)이다.",True)
C("c-pp-2","public-private","mc","다른 구성요소가 보고 쓸 수 있는 특징을 담는 관점은?",0,
  choices=["Public view","Private view","Internal view","Implementation view"])
C("c-nm-1","naming","mc","이름 선택 지침이 '아닌' 것은?",3,
  choices=["evocative","short","pronounceable","include digits for clarity (count1, count2)"])
C("c-nm-2","naming","blank","Names should be (a) in the context of the problem: the name should call to mind the meaning of the thing. Names should be (b) within the project.",
  ["evocative","consistent"], accept=[["evocative"],["consistent","일관"]])
C("c-nm-3","naming","ox","행동이 하나뿐인 구성요소는 함수로, 행동이 여러 개인 구성요소는 클래스로 만드는 게 쉽다.",True)
C("c-im-1","implement","mc","서브시스템을 개별적으로 검증(validate)하는 테스트는?",0,
  choices=["unit testing","integration testing","acceptance testing","stress testing"])
C("c-im-2","implement","ox","Design 단계에서는 각 구성요소의 자료구조를 설계하고 행동 설명을 알고리즘으로 바꾼다.",True)
C("c-stub-1","stub","blank","(a) is a simple dummy routine with no behavior or with very limited behavior, used as a temporary substitute for yet-to-be-developed components.",
  ["Stub"], accept=[["stub","a stub","stubs"]])
C("c-stub-2","stub","mc","'components are slowly integrated'의 뜻은?",1,
  choices=["천천히 코딩한다","구성요소를 한꺼번에가 아니라 하나(몇 개)씩 추가하며 테스트한다","통합을 마지막에 한 번에 한다","stub을 쓰지 않는다"])
C("c-stub-3","stub","ox","구성요소를 한꺼번에 통합하면 문제가 생겼을 때 어디서 생겼는지 찾기 어렵다.",True)
C("c-mt-1","maintenance","blank","Software maintenance: activities (a) to the delivery of the initial working version of the software system.",
  ["subsequent"], accept=[["subsequent","after","이후"]])
C("c-mt-2","maintenance","mc","흔한 설계 결함 중 '다른 구성요소의 데이터를 직접 수정'은 무엇을 위반하나?",2,
  choices=["코딩 규칙","상속","캡슐화 (encapsulation)","다형성"])
C("c-mt-3","maintenance","ox","좋은 설계는 변화가 불가피함을 인정하고 처음부터 그 변화에 대비한다.",True)

# ── U4 ──
C("c-ae-1","abs-encap","blank","Data encapsulation: implementation is encapsulated by the (a), and the only way to get to the implementation legally is through the (a). Information hiding: implementation is (b) from the user.",
  ["interface","hidden"], accept=[["interface","인터페이스"],["hidden","숨겨"]])
C("c-ae-2","abs-encap","mc","데이터 추상화를 한 문장으로 가장 잘 표현한 것은?",0,
  choices=["Separation of interface and implementation","Combining two classes","Hiding all members","Using inheritance"])
C("c-ae-3","abs-encap","ox","교수님은 data abstraction, data encapsulation, information hiding을 거의 같은 개념으로 보라고 했다.",True)
C("c-tv-1","two-views","blank","Interface: the outside, or (a) view, describes (b) an object does. Implementation: the inside view describes (c) it does.",
  ["service","what","how"], accept=[["service","서비스"],["what"],["how"]])
C("c-tv-2","two-views","ox","Service view는 객체가 어떻게 일을 수행하는지 알아야 객체를 특징지을 수 있다는 관점이다.",False,
  explain="반대. 어떻게 하는지 몰라도 제공하는 서비스로 객체를 특징짓는 능력.")
C("c-eb-1","encap-benefits","blank","Three benefits of data encapsulation: (a) of implementation (safety), (b) (understandability), and implementation (c).",
  ["protection","readability","independence"], accept=[["protection","보호"],["readability","가독성"],["independence","독립성"]])
C("c-eb-2","encap-benefits","mc","'A change in implementation should not affect the interface seen by the clients'는 어떤 이점인가?",2,
  choices=["Protection of implementation","Readability","Implementation independence","Reusability"])
C("c-eb-3","encap-benefits","mc","'Clients cannot directly access encapsulated data'는 어떤 이점인가?",0,
  choices=["Protection of implementation (safety)","Readability","Implementation independence","Efficiency"])
C("c-eb-4","encap-benefits","ox","Readability 이점: 인터페이스를 쓰는 클라이언트는 인터페이스 함수가 캡슐화된 정보를 어떻게 쓰는지 알 필요가 없다.",True)
C("c-mth-1","method","blank","A method has three parts: name, (a) (the combination of return type and argument types), and (b).",
  ["signature","body"], accept=[["signature","시그니처"],["body","몸체"]])
C("c-mth-2","method","ox","이름이 같은 메서드도 시그니처(인자 타입)가 다르면 구별된다.",True)
C("c-mth-3","method","mc","객체가 행동을 성공적으로 하려고 유지해야 하는 데이터(state)는 어디에 저장되나?",1,
  choices=["전역 변수","인스턴스 변수 (data member)","지역 변수","레지스터"])
C("c-mp-1","message-passing","blank","aGame.displayCard(aCard, 42, 27); 에서 aGame은 message (a), displayCard는 message (b), 괄호 안은 arguments이다.",
  ["receiver","selector"], accept=[["receiver","수신자"],["selector","선택자"]])
C("c-mp-2","message-passing","mc","메시지와 함수 호출의 차이로 옳은 것은?",1,
  choices=["메시지는 반환 값이 없다","메시지는 항상 어떤 객체(receiver)에게 주어지고, 응답 행동은 수신자가 결정한다","함수 호출은 객체에게만 할 수 있다","차이가 없다"])
C("c-avp-1","avoid-public","blank","Avoid data members in the public interface: (i) (a) (ii) precise control over the (b) of data members (iii) functional (c): you can later replace the data member with a computation.",
  ["consistency","accessibility","abstraction"], accept=[["consistency","일관성"],["accessibility","access","접근"],["abstraction","추상화"]])
C("c-avp-2","avoid-public","mc","클래스의 모든 멤버를 private으로 만들면 생기는 가장 심각한 문제는?",0,
  choices=["인터페이스가 없어서 클라이언트가 객체를 전혀 쓸 수 없다","캡슐화가 깨진다","컴파일러가 기본 생성자를 안 만든다","느려진다"])
C("c-avp-3","avoid-public","mc","모든 멤버를 public으로 만들면 생기는 문제는?",2,
  choices=["객체를 만들 수 없다","컴파일 오류","캡슐화가 없어서 클라이언트가 데이터를 직접 접근·훼손할 수 있다","소멸자가 안 불린다"])
C("c-avp-4","avoid-public","ox","데이터 멤버를 public에 두는 것은 문법적으로 오류다.",False,
  explain="문법적으로는 문제없지만 OOP 관점에서 좋지 않다.")
C("c-gs-1","getter-setter","mc","getter(accessor)를 쓰는 이유가 '아닌' 것은?",3,
  choices=["데이터를 read-only로 만듦","데이터에 접근할 수 있음을 더 잘 문서화","나중에 접근 방식을 바꾸기 쉬움","데이터를 public으로 만들기 위해"])
C("c-gs-2","getter-setter","ox","setter(mutator)는 getter보다 덜 흔하다.",True)
C("c-as-1","assert","blank","assert(e): if e is true, just (a); if e is false, the program is (b) with an error message. Its purpose is to make programs more (c).",
  ["continue","stopped","reliable"], accept=[["continue","continues","계속"],["stopped","stops","terminated","aborted","멈춤"],["reliable","신뢰"]])
C("c-as-2","assert","mc","assert(x = 3); 의 동작은?",2,
  choices=["x가 3인지 검사","항상 실패","x에 3을 대입하고 3은 참이므로 항상 통과","컴파일 오류"])
C("c-as-3","assert","blank","Class (a): conditions that must always be true inside an object.",
  ["invariant"], accept=[["invariant","invariants","불변식"]])
C("c-vis-1","visibility","mc","private 멤버에 접근할 수 있는 것은?",1,
  choices=["모든 클라이언트","그 클래스의 멤버 함수","main 함수","같은 파일의 모든 함수"])
C("c-vis-2","visibility","ox","상속이 없으면 protected는 private과 같다.",True)
C("c-vis-3","visibility","mc","PlayingCard에서 color를 데이터 멤버로 저장하지 않는 이유는?",3,
  choices=["private이라서","상수라서","enum이라서","suit 값에서 계산할 수 있어서"])
C("c-ctor-1","constructor","blank","A constructor is automatically called when (a) is created, has the same (b) as the class, and has no (c) type.",
  ["an object","name","return"], accept=[["an object","object","a new object","객체"],["name","이름"],["return","반환"]])
C("c-ctor-2","constructor","mc","멤버 초기화자(member initializer)를 쓴 생성자는?",1,
  choices=["PlayingCard(Suits is, int ir) { suit = is; }","PlayingCard(Suits is, int ir) : suitValue(is), rankValue(ir) { faceUp = true; }","PlayingCard::init(is, ir);","void PlayingCard(Suits is)"])
C("c-ctor-3","constructor","ox","생성자는 여러 개 있을 수 있다(매개변수가 다르면).",True)
C("c-dc-1","default-ctor","blank","In C++, if we do not declare any constructor in a class, (a) generates (b).",
  ["the compiler","a default constructor"], accept=[["the compiler","compiler","컴파일러"],["a default constructor","default constructor","기본 생성자"]])
C("c-dc-2","default-ctor","ox","생성자를 하나라도 직접 만들면 컴파일러는 기본 생성자를 자동으로 만들지 않는다.",True)
C("c-dc-3","default-ctor","mc","소멸자에 대한 설명으로 옳은 것은?",2,
  choices=["여러 개 있을 수 있다","반환 타입이 void다","~클래스이름()이고 객체가 삭제될 때 자동 호출된다","직접 호출해야만 실행된다"])
C("c-cw-1","copy-when","mc","복사 생성자가 호출되지 '않는' 문장은?",3,
  choices=["Person r(p);","Person p = q;","f(p);  // 값 매개변수","p = q;  // 이미 있는 객체"])
C("c-cw-2","copy-when","blank","A copy constructor is called whenever a new object is created from (a) object with the same type. 선언: Person(const Person& p)",
  ["an existing"], accept=[["an existing","existing","기존"]])
C("c-cw-3","copy-when","mc","p = q; 는 무엇으로 해석되나?",1,
  choices=["Person p(q);","p.operator=(q);","복사 생성자","소멸자 후 생성자"])
C("c-shd-1","shallow-deep","mc","포인터 멤버를 가진 클래스에서 기본 복사 생성자를 쓰면 생기는 문제는?",0,
  choices=["얕은 복사로 두 객체가 같은 배열을 공유하고, 소멸 때 delete[]가 두 번 불린다","컴파일 오류","깊은 복사로 메모리가 낭비된다","복사 생성자가 호출 안 된다"])
C("c-shd-2","shallow-deep","blank","깊은 복사(deep copy) 복사 생성자는 (a) 로 새 메모리를 할당하고 원소를 하나씩 (b) 한다.",
  ["new","copy"], accept=[["new","new[]"],["copy","복사","copies"]])
C("c-shd-3","shallow-deep","ox","얕은 복사로 괜찮으면 복사 생성자를 직접 쓰지 마라.",True)
C("c-r3-1","rule-of-three","blank","If you need a copy constructor, you also need a (a) and (b).",
  ["destructor","operator="], accept=[["destructor","소멸자"],["operator=","assignment operator","operator =","대입 연산자"]])
C("c-r3-2","rule-of-three","mc","Project 2의 inf_int에 복사 생성자가 필요한 이유는?",1,
  choices=["static 멤버가 있어서","자릿수를 동적 할당한 포인터를 가져서 깊은 복사가 필요","const 멤버 함수가 있어서","friend 함수가 있어서"])
C("c-oc-1","object-creation","mc","PlayingCard* CardsPtr = new PlayingCard[100]; 을 해제하는 문장은?",2,
  choices=["delete CardsPtr;","free(CardsPtr);","delete [] CardsPtr;","CardsPtr = 0;"])
C("c-oc-2","object-creation","ox","지역 객체들은 만든 순서대로(먼저 만든 것부터) 소멸한다.",False,
  explain="만든 역순으로 소멸.")
C("c-ld-1","leak-dangling","blank","A pointer pointing to a memory location that has been deallocated (freed) is called a (a) pointer.",
  ["dangling"], accept=[["dangling","댕글링"]])
C("c-ld-2","leak-dangling","mc","memory leak의 뜻은?",0,
  choices=["동적 할당한 메모리를 해제하지 않아 다시 쓸 수 없게 되는 것","해제된 메모리를 가리키는 포인터","스택 오버플로","배열 범위 초과"])
C("c-ld-3","leak-dangling","ox","댕글링 포인터에 접근하면 정의되지 않은 동작(충돌, 다른 데이터 훼손)이 일어날 수 있다.",True)
C("c-stc-1","static-member","blank","Static members are used to represent the properties of (a). Static member variables can be accessed even if there is no (b).",
  ["the class","created object"], accept=[["the class","class","클래스"],["created object","object","objects","instance","created objects","객체"]])
C("c-stc-2","static-member","mc","static 멤버 함수가 할 수 '없는' 것은?",2,
  choices=["객체 없이 클래스이름::함수()로 호출됨","static 멤버 변수 접근","non-static 멤버 변수 접근","값 반환"])
C("c-stc-3","static-member","mc","File 예제에서 open_files가 static이 아니면?",1,
  choices=["컴파일 오류","객체마다 자기 open_files를 가져서 전체 File 객체 수를 셀 수 없다","모든 객체가 0을 공유","소멸자가 불리지 않는다"])
C("c-stc-4","static-member","blank","static 멤버 변수는 클래스 밖에서 정의·초기화한다: int (a)::open_files = 0;",
  ["File"], accept=[["file"]])
C("c-cf-1","const-fn","blank","(a) member function does not (b) any data members of the object on which it is called. This restriction is enforced by (c).",
  ["const","modify","the compiler"], accept=[["const"],["modify","change","수정"],["the compiler","compiler","컴파일러"]])
C("c-cf-2","const-fn","mc","const 멤버 함수의 올바른 선언은?",1,
  choices=["const int rank();","int rank() const;","int const rank;","int rank(const);"])
C("c-cf-3","const-fn","ox","const 멤버 함수는 클라이언트에게 해가 없다는 것(benign nature)을 보장해서 안전성과 가독성을 높인다.",True)
C("c-inl-1","inline","mc","inline 함수의 주 이점은?",0,
  choices=["함수 호출 오버헤드가 없어져 실행이 빠르다","코드 크기가 줄어든다","재귀가 가능하다","메모리 누수가 없다"])
C("c-inl-2","inline","mc","inline의 단점은?",2,
  choices=["느려짐","재사용 불가","코드 크기 증가 (code bloat), 특히 함수가 크거나 여러 곳에서 호출될 때","컴파일 불가"])
C("c-inl-3","inline","ox","inline이 이득인 상황은 몸체가 작거나(getter/setter) 아주 자주 호출되는 함수다.",True)
C("c-sdf-1","separate-def","mc","PlayingCard의 color()를 클래스 밖에서 정의하는 첫 줄은?",1,
  choices=["Colors color() {","PlayingCard::Colors PlayingCard::color() {","Colors PlayingCard.color() {","PlayingCard::color() {"])
C("c-sdf-2","separate-def","ox","클래스 밖에서 생성자를 정의할 때는 반환 타입 없이 TIntStack::TIntStack(...)으로 쓴다.",True)
C("c-fr-1","friend","blank","A (a) function of a class has the right to access the non-public members of the class. To make all member functions of ClassTwo friends of ClassOne: friend (b) ClassTwo;",
  ["friend","class"], accept=[["friend"],["class"]])
C("c-fr-2","friend","mc","비멤버 함수 int get_area(Rect c) { return c.width * c.height; } 가 컴파일 오류인 이유와 고치는 법은? (width, height는 private)",0,
  choices=["비멤버 함수가 private에 접근 → 클래스 안에 friend int get_area(Rect c); 추가","width가 int라서 → double로","c가 값 전달이라서 → 참조로","return이 없어서"])
C("c-fr-3","friend","ox","멤버 함수는 같은 클래스의 '다른 객체'의 private 멤버에도 접근할 수 있다.",True)
C("c-ref-1","reference","blank","A reference is an (a) for an object. It is frequently used for pass-by-(b).",
  ["alias","reference"], accept=[["alias","another name","별명"],["reference","참조"]])
C("c-ref-2","reference","blank","int x=5; int* y; int& z=x; y=&x; int w=*y; x=9; z=*y*x; x++; z=x&*y; cout << x << \" \" << *y << \" \" << z << \" \" << w; 의 출력: (a) (b) (c) (d)",
  ["82","82","82","5"], accept=[["82"],["82"],["82"],["5"]])
C("c-ref-3","reference","mc","double square(double &x) { return x *= x; } 에 foo = 10.0을 넘긴 뒤 foo의 값은?",2,
  choices=["10","20","100","변하지 않음 (복사본만 바뀜)"])
C("c-rvp-1","ref-vs-pointer","mc","참조와 포인터의 차이로 옳은 것은?",1,
  choices=["포인터는 반드시 실제 객체를 가리켜야 한다","참조는 반드시 실제 객체를 가리켜야 하고, 포인터는 NULL 같은 값도 가질 수 있다","참조는 NULL일 수 있다","차이가 없다"])
C("c-rvp-2","ref-vs-pointer","ox","printDouble(const double& rd)는 rd가 NULL인지 검사할 필요가 없다.",True)
C("c-pm-1","pass-modes","mc","void X::f(T& arg)에서 &가 void X::f(T arg)에 비해 갖는 두 목적은?",0,
  choices=["복사를 피함(효율), 함수가 원본을 바꿀 수 있음","원본을 못 바꾸게 함, 복사를 함","포인터로 바꿈, NULL 허용","재귀 허용, inline"])
C("c-pm-2","pass-modes","mc","void X::f(const T& arg)에서 const의 목적은?",2,
  choices=["복사를 강제","arg를 NULL로","복사는 피하면서 원본을 못 바꾸게 보장","arg를 static으로"])
C("c-pm-3","pass-modes","ox","읽기 전용 매개변수에는 const 없는 참조 전달(T&)을 쓰면 안 된다.",True)
C("c-pg-1","pass-guide","mc","큰 객체를 값으로 넘기면 오버헤드가 큰 이유는?",1,
  choices=["포인터가 NULL일 수 있어서","객체 전체가 매개변수로 복사되어 복사 생성자·메모리 할당·소멸자가 불려서","컴파일러가 inline을 못 해서","스택이 없어서"])
C("c-pg-2","pass-guide","ox","기본 타입(int 등)이나 작은 객체는 값으로 넘기는 게 더 안전하다.",True)
C("c-pg-3","pass-guide","mc","참조로 넘기면 오버헤드가 아주 작은 이유는?",3,
  choices=["const라서","inline이라서","static이라서","주소(별명)만 넘기고 복사가 없어서"])
C("c-ms-1","memory-safe","mc","Writing memory safe classes 지침이 '아닌' 것은?",3,
  choices=["객체 복사를 피하라","const 참조 매개변수를 써라","초기에는 안전 먼저, 최적화는 나중에","초기 단계부터 트릭으로 최적화하라"])
C("c-ms-2","memory-safe","ox","클라이언트는 문서에 없는 클래스 세부에 의존하지 말고 인터페이스와 문서만 따라야 한다.",True)
C("c-rl-1","return-local","mc","int& h() { int k = 2; return k; } 의 문제는?",0,
  choices=["반환 후 사라지는 지역 변수의 참조를 반환 → 댕글링","값이 복사됨","컴파일이 안 됨이 항상 보장됨","문제 없음"])
C("c-rl-2","return-local","ox","int f() { int i = 2; return i; } 는 값을 복사해서 반환하므로 안전하다.",True)
C("c-cow-1","cow","blank","Copy-on-write: allocate new memory only when (a). Otherwise share the data, keeping a (b) count (use count).",
  ["writing","reference"], accept=[["writing","write","쓸 때"],["reference","use","참조"]])
C("c-cow-2","cow","mc","s, k, m이 \"ADD ONE TO COBOL\"을 공유(use_count=3)하다가 s.to_lower(); 하면?",2,
  choices=["셋 다 소문자가 됨","k, m만 새 메모리","s만 새 메모리(use_count=1), k와 m은 계속 공유(use_count=2)","use_count=0"])
C("c-ts-1","tintstack","mc","TIntStack 깊은 복사 생성자에 반드시 있어야 하는 것은?",1,
  choices=["_sp = that._sp;","_sp = new int[_size]; 후 원소를 for문으로 복사","delete[] that._sp;","static _count"])
C("c-ts-2","tintstack","blank","bool TIntStack::Push(int thisValue) { if (_count >= _size) return (a); _sp[_count++] = thisValue; return true; } 소멸자는 (b) _sp; 한다.",
  ["false","delete[]"], accept=[["false"],["delete[]","delete []"]])
C("c-ts-3","tintstack","mc","스택에 1, 3, 4를 차례로 push한 뒤 pop하면 나오는 순서는?",3,
  choices=["1, 3, 4","1, 4, 3","3, 4, 1","4, 3, 1"])
C("c-ts-4","tintstack","ox","TIntStack(unsigned int stackSize = DEFAULT_SIZE)처럼 기본 인자를 쓰면 TIntStack s; 로도 객체를 만들 수 있다.",True)

# ── U5 ──
C("c-oo-1","opover-basic","mc","멤버 함수 방식 연산자 오버로딩에서 이항 연산자의 왼쪽 피연산자는?",0,
  choices=["this로 암묵적으로 받음","첫 번째 매개변수","두 번째 매개변수","friend"])
C("c-oo-2","opover-basic","mc","비멤버 함수 방식 연산자가 private 데이터에 접근하려면?",2,
  choices=["public 멤버여야","static이어야","friend여야","inline이어야"])
C("c-oo-3","opover-basic","blank","멤버 방식: c = a + b; → c = a.(a)(b);  비멤버 방식: c = operator+((b), b);",
  ["operator+","a"], accept=[["operator+","operator +"],["a"]])
C("c-oo-4","opover-basic","ox","비멤버 함수 방식은 왼쪽 피연산자가 다른 클래스의 객체여도 된다.",True)
C("c-cx-1","opover-complex","blank","a = 1.2+3.4i, b = 5.6+7.8i일 때 a+b = (a), a−b = (b)",
  ["6.8+11.2i","-4.4-4.4i"], accept=[["6.8+11.2i"],["-4.4-4.4i","−4.4−4.4i"]])
C("c-cx-2","opover-complex","mc","Complex operator*의 실수부 계산은?",1,
  choices=["re*other.re + im*other.im","re*other.re - im*other.im","re*other.im + im*other.re","re + other.re"])
