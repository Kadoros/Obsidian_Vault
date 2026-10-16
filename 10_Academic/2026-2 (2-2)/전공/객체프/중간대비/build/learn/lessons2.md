@unit U2 | C++ in Summary (문법 · 포인터 · 파일 입출력) | C++ in Summary.pdf + static vs dynamic 토론 자료
@intro C++ 문법 요약. 시험에 직접 나오는 건 포인터 *·&의 세 가지 뜻, 동적 할당과 정적 할당 비교, Rectangle 포인터 코드 빈칸, 그리고 파일 입출력(open mode, tellg/seekg, 바이너리 파일 복사)이야. 파일 복사 코드는 2024·2025 연속으로 통째로 썼어.

@lesson L2-1 | 컴파일 · 입출력 · string | C++ in Summary p.2–14

## 컴파일과 표준 입출력 {#cpp-io}

- **컴파일러**: 고급 언어 코드 → 기계어. C++ 컴파일러는 소스 파일에서 실행 파일(binary)을 만든다
  - `g++ -o TestProg TestProg.cpp` → `./TestProg`
- `#include <iostream>` (header file), `using namespace std;`. C++ 프로그램에서 C 코드를 써도 된다
- **cout**: 화면 스트림 객체 (standard output). `cout << "Hello";` → 문자열 Hello 출력, `cout << Hello;` → 변수 Hello의 값 출력
- **cin**: 키보드 스트림 객체 (standard input). `cin >> age;` → 키보드 입력이 변수로 (화살표 방향이 데이터 흐름)
- 서식: printf와 비슷하게 `std::format` (C++20), `std::print` (C++23)
```
double pi = 3.141592; int age = 21;
printf("pi=%7.2f , age=%d\n", pi, age);
cout << format("pi={:7.2f} , age={}\n", pi, age);   // pi=   3.14 , age=21
```

## 자료형 · string · 제어문 · 함수 · 배열 {#cpp-basics}

- 변수 = 값이 저장되는 **이름 붙은 메모리 위치**, 사용 전에 선언
- char 1B, short 2B, int 4B (−2³¹ ~ 2³¹−1), float 4B, double 8B. 양수만이면 unsigned
- **string**: 표준 라이브러리 클래스. C 문자열(char*)과 달리 **메모리를 자동 관리**하고 편리한 함수 제공 (length, find, substr, replace, insert, erase, c_str, stoi, stod, to_string)
- `getline(cin, str)`: 한 줄 읽기
- for문 실행 순서: (1) 초기화 → (2) 조건 → body → (3) 증감 → (2) → body → …
- break = 루프 탈출, continue = 다음 반복의 조건 검사로
- 함수: 지역 변수(매개변수 포함)는 호출 때 생성, 반환 때 삭제. 쓰는 이유 = 반복 제거, 재사용, top-down, 디버그 쉬움, 수정·확장 쉬움, 가독성
- 배열: 같은 타입 원소의 **고정 크기** 모음, 메모리에 연속 저장, 빠른 임의 접근 `x[15]=3;`

@lesson L2-2 | 포인터 · 동적 할당 · 정적 vs 동적 | C++ in Summary p.23–24 + 토론 자료

## 포인터 {#pointer}

- 포인터 = 메모리 **주소**를 저장하는 변수. 크기는 항상 8바이트(64비트)/4바이트(32비트)
```
int *xPtr, x;   // xPtr은 포인터, x는 int
x = 5;
xPtr = &x;      // xPtr이 x를 가리킴 (xPtr의 값 = x의 주소)
*xPtr = 10;     // xPtr이 가리키는 값을 10으로 → x가 10
cout << x;      // 10
```
**`*`의 세 가지 뜻**: (i) 곱셈 (이항) `z=x*y;` (ii) 가리키는 값 (단항, the-value-of) `*x=5;` (iii) 포인터 타입 선언 `int *x;`
**`&`의 세 가지 뜻**: (i) 비트 AND (이항) `z=x&y;` (ii) 주소 연산자 (단항, address-of) `x=&y;` (iii) 참조 타입 선언 `int& y=x;`

> 시험 포인트: 2022 기말 "Meaning of '*' in line 2? '&' in line 3?" 같은 유형. 줄마다 어느 뜻인지 영어로 답할 수 있어야 해 (pointer type declaration / reference type declaration / address-of / dereference / multiplication / bitwise AND).

## 동적 메모리 할당 {#new-delete}

- "dynamic" = **실행 시간(run-time, execution-time)에 일어난다**
- C의 `malloc` ⇔ C++의 `new`, C의 `free` ⇔ C++의 `delete`
```
int *x = new int[10];   // C: x = (int*)malloc(10*sizeof(int));
...
delete[] x;             // C: free(x);
```
- 객체 하나는 `delete p;`, 배열은 `delete[] p;`
- **Java와 달리 C++은 직접 해제**해야 함 (garbage collection 없음)

> 시험 포인트: 2019 빈칸 "Dynamic memory allocation means memory allocation occurs at (run-time)".

## 정적 할당 vs 동적 할당 (토론 자료) {#static-dynamic}

`int x[10];` (정적) vs `int* y = new int[n];` (동적)

| | 장점 | 단점 |
|---|---|---|
| **정적** | 간단하고 빠름, 메모리가 **자동으로 해제**됨 (스택, 범위를 벗어나면) | 크기가 **컴파일 시간**에 고정 → 실행 중 바꿀 수 없음 (낭비 또는 부족) |
| **동적** | 크기를 **실행 시간**에 정할 수 있음 → 메모리를 필요한 만큼 효율적으로 | 프로그래머가 **직접 해제(delete[])** 해야 함 → **memory leak, dangling pointer** 위험 |

> 시험 포인트: 2023 서술이 이 토론 자료 그대로 나옴 (장점·단점·이유 4칸). 핵심 단어 = **compile time vs run time**, **automatic vs manual deallocation**.

@lesson L2-3 | C++ class 기초 · 객체 포인터 | C++ in Summary p.25–28

## class · 생성자 · 소멸자 (요약) {#class-basic}

- **class**: 멤버 데이터와 멤버 함수를 담는 자료구조 타입. 새 데이터 타입을 정의
- **생성자/소멸자**: 객체가 **생성/삭제될 때 자동으로 호출**되는 멤버 함수
  - 지역 객체는 함수가 반환될 때 삭제 → 그때 소멸자 호출. 소멸자 이름은 `~클래스이름`
  - 생성자를 안 만들면 컴파일러가 빈 기본 생성자를 만듦. 소멸자도 마찬가지
  - 멤버 변수를 초기화하지 않으면 **쓰레기 값(garbage)** → 위험·불안정. 생성자에서 초기화해야 함

## 객체 포인터 (Rectangle 예제) {#obj-pointer}

```
class Rectangle {
  private:
    int width, height;
  public:
    Rectangle() { width=1; height=1; }
    Rectangle(int x, int y) : width(x), height(y) {}
    int area() { return width*height; }
};
int main() {
  Rectangle obj(3,4);
  Rectangle *foo, *bar, *baz;
  foo = &obj;                    // 주소 대입
  bar = new Rectangle(5,6);      // 동적 생성: new는 주소를 반환
  baz = new Rectangle[2];        // 배열: 기본 생성자 2번 → 각 1×1
  cout << "obj's area: "    << obj.area()    << '\n';   // 12
  cout << "*foo's area: "   << foo->area()   << '\n';   // 12
  cout << "*bar's area: "   << bar->area()   << '\n';   // 30
  cout << "baz[0]'s area: " << baz[0].area() << '\n';   // 1
  cout << "baz[1]'s area: " << baz[1].area() << '\n';   // 1
  delete bar;
  delete[] baz;
  return 0;
}
```
- **객체는 `.`**, **포인터는 `->`** (= `(*foo).area()`). 배열 원소 `baz[0]`은 객체라서 `.`
- `foo = obj;` (X) → `foo = &obj;` (O). `bar.area()` (X) → `bar->area()` (O)

> 시험 포인트: 2025·2024·2023·2019·2017 매년 이 코드의 변형 (빈칸 채우기, 오류 5개 찾기, 출력 쓰기). `.`/`->`/`&`/`new`/`delete[]`를 줄 단위로 정확히.

@lesson L2-4 | 파일 입출력 | C++ in Summary p.29–39

## 파일 스트림 클래스와 open {#fstream}

- **ofstream**: 파일에 쓰기 / **ifstream**: 파일에서 읽기 / **fstream**: 읽기·쓰기 둘 다 (`#include <fstream>`)
- 파일 처리 순서: **open → read/write → close**
- 열 때 정할 것: 텍스트 vs 바이너리, 쓰기라면 **추가(append) vs 덮어쓰기(truncate)**, 파일 위치(자동 vs 사용자 제어)
- `myfile.open(filename, mode);` 또는 생성자 `ofstream myfile("example.txt");`
- 열렸는지 확인 `if (myfile.is_open()) { ... }`, 닫기 `myfile.close();`
- 텍스트 쓰기 `myfile << "This is a line.\n";`, 읽기 `while (getline(myfile, line)) cout << line << '\n';`
- 상태 검사: `bad()` 읽기/쓰기 실패, `fail()` bad + 형식 오류, `eof()` 파일 끝, `good()` 다 괜찮음, `clear()` 플래그 초기화

> 시험 포인트: 2019 빈칸 "ofstream: write on files / (ifstream): read from files / (fstream): read and write".

## 파일 열기 모드 {#open-modes}

| 플래그 | 뜻 |
|---|---|
| `ios::in` | 입력(읽기)용으로 열기 |
| `ios::out` | 출력(쓰기)용으로 열기 |
| `ios::binary` | 바이너리 모드 |
| `ios::ate` | 초기 위치를 **파일 끝**으로 (안 쓰면 처음) |
| `ios::app` | **모든 출력을 파일 끝에** → 기존 내용에 **덧붙임(append)** |
| `ios::trunc` | 출력용으로 열 때 파일이 **이미 있으면** 기존 내용을 **지우고** 새 내용으로 |

- 여러 개는 **비트 OR `|`** 로 결합: `myfile.open("example.bin", ios::out | ios::app | ios::binary);`
- **기본 모드**: ofstream = `ios::out`, ifstream = `ios::in`, fstream = `ios::in | ios::out`
- 쓰기로 열면 기존 파일이 지워지고 처음부터 써짐 (교수님이 여러 번 경고)

> 시험 포인트: 2023 빈칸 "ios::app means all output operations are performed at the (end)", "(ios::trunc) means if the file is opened for output and already (existing), its previous content is deleted". 2019도 app.

## 파일 위치: tellg / seekg {#seek-tell}

- **get 위치**(읽기)와 **put 위치**(쓰기)가 따로 있다
- `tellg()` / `tellp()`: 현재 get/put 위치 반환
- `seekg(position)` / `seekp(position)`: 위치를 절대값으로 이동
- `seekg(offset, direction)`: `ios::beg` (처음부터), `ios::cur` (현재 위치부터), `ios::end` (끝부터)

**파일 크기 구하기 (매년 빈칸)**
```
streampos begin, end;
ifstream myfile("example.bin", ios::binary);
begin = myfile.tellg();          // 처음 위치
myfile.seekg(0, ios::end);       // 끝으로
end = myfile.tellg();            // 끝 위치
myfile.close();
cout << "size is: " << (end-begin) << " bytes.\n";
```

> 시험 포인트: 2024·2023·2019 "Fill in the boxes to print the size". `begin = myfile.tellg();` → `myfile.seekg(0, ios::end);` → `end = myfile.tellg();` 세 줄.

## 바이너리 파일과 파일 복사 {#binary}

- 텍스트 vs 바이너리: 253을 텍스트로 쓰면 문자 '2','5','3' (3바이트), 바이너리로 쓰면 11111101 (1바이트)
- 바이너리 입출력은 `write(memory_block, size);` / `read(memory_block, size);` (memory_block은 `char*`)

**파일 전체 읽기 (교안)**
```
ifstream file("example.bin", ios::in | ios::binary | ios::ate);
if (file.is_open()) {
    streampos size = file.tellg();     // ate라서 끝 위치 = 파일 크기
    char* memblock = new char[size];
    file.seekg(0, ios::beg);           // 처음으로 되감기
    file.read(memblock, size);
    file.close();
    ...
    delete[] memblock;
}
```
**파일 복사 (2024·2025 코드 작성)**: 위 코드 + `ofstream out("des.bin", ios::out | ios::binary); out.write(memblock, size); out.close();`

> 주의: getline으로 한 줄씩 복사하면 바이너리 파일이 깨지고 감점 (기출 해설). `ios::binary`, `ios::ate` → `tellg` → `seekg(0, ios::beg)` → `read` → `write` → `delete[]` 순서를 외워.
