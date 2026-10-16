@unit U2 | C++ in Summary (Syntax · Pointers · File I/O) | C++ in Summary.pdf + static vs dynamic 토론 자료
@intro A summary of C++ syntax. What shows up directly on the exam: the three meanings of pointer `*` and `&`, static vs dynamic allocation, fill-in-the-blank on the Rectangle pointer code, and file I/O (open modes, tellg/seekg, copying a binary file). The file-copy code had to be written in full in both 2024 and 2025.

@lesson L2-1 | Compiling · I/O · string | C++ in Summary p.2–14

## Compiling and Standard I/O {#cpp-io}

- **Compiler**: converts high-level language code to machine language code. The C++ compiler generates an executable file (binary code) from C++ source code
  - `g++ -o TestProg TestProg.cpp` → `./TestProg`
- `#include <iostream>` (header file), `using namespace std;`. C code may be used in a C++ program
- **cout**: screen stream object (standard output). `cout << "Hello";` → prints the string Hello; `cout << Hello;` → prints the value of the variable Hello
- **cin**: keyboard stream object (standard input). `cin >> age;` → keyboard input goes into the variable (the arrow shows the direction of data flow)
- Formatting like printf: `std::format` (C++20), `std::print` (C++23)
```
double pi = 3.141592; int age = 21;
printf("pi=%7.2f , age=%d\n", pi, age);
cout << format("pi={:7.2f} , age={}\n", pi, age);   // pi=   3.14 , age=21
```

## Data Types · string · Control Structures · Functions · Arrays {#cpp-basics}

- Variable = a **named memory location** where a value is stored; must be declared before use
- char 1B, short 2B, int 4B (−2³¹ ~ 2³¹−1), float 4B, double 8B. Use unsigned for non-negative values only
- **string**: a standard library class. Unlike C-style strings (char*), string **automatically manages memory** and provides many convenient functions (length, find, substr, replace, insert, erase, c_str, stoi, stod, to_string)
- `getline(cin, str)`: reads a line of text
- for-loop execution order: (1) initialization → (2) condition → body → (3) increment → (2) → body → …
- break = exit the loop; continue = jump to the condition check of the next iteration
- Functions: local variables (including parameters) are created when the function is called and destroyed when it returns. Why use functions: remove repetition, reuse, top-down design, easier debugging, easier modification/extension, readability
- Array: a **fixed-size** collection of elements of the same type, stored contiguously in memory, fast random access `x[15]=3;`

@lesson L2-2 | Pointers · Dynamic Allocation · Static vs Dynamic | C++ in Summary p.23–24 + 토론 자료

## Pointers {#pointer}

- Pointer = a variable that stores a memory **address**. Its size is always 8 bytes (64-bit) / 4 bytes (32-bit)
```
int *xPtr, x;   // xPtr is a pointer, x is an int
x = 5;
xPtr = &x;      // xPtr points to x (value of xPtr = address of x)
*xPtr = 10;     // set the value pointed to by xPtr to 10 → x becomes 10
cout << x;      // 10
```
**Three meanings of `*`**: (i) multiplication (binary) `z=x*y;` (ii) the value pointed to (unary, the-value-of / dereference) `*x=5;` (iii) pointer type declaration `int *x;`
**Three meanings of `&`**: (i) bitwise AND (binary) `z=x&y;` (ii) address operator (unary, address-of) `x=&y;` (iii) reference type declaration `int& y=x;`

> Exam point: question type like the 2022 final "Meaning of '*' in line 2? '&' in line 3?". Be able to answer in English which meaning each line uses (pointer type declaration / reference type declaration / address-of / dereference / multiplication / bitwise AND).

## Dynamic Memory Allocation {#new-delete}

- "dynamic" means "**… occurs at run-time (execution-time)**"
- `malloc` in C ⇔ `new` in C++, `free` in C ⇔ `delete` in C++
```
int *x = new int[10];   // C: x = (int*)malloc(10*sizeof(int));
...
delete[] x;             // C: free(x);
```
- A single object: `delete p;`, an array: `delete[] p;`
- **Unlike Java, C++ requires you to free memory yourself** (no garbage collection)

> Exam point: 2019 blank "Dynamic memory allocation means memory allocation occurs at (run-time)".

## Static vs Dynamic Allocation (discussion handout) {#static-dynamic}

`int x[10];` (static) vs `int* y = new int[n];` (dynamic)

| | Advantages | Disadvantages |
|---|---|---|
| **Static** | simple and fast; memory is **deallocated automatically** (on the stack, when it goes out of scope) | size is fixed at **compile time** → cannot change while running (waste or shortage) |
| **Dynamic** | size can be decided at **run time** → uses exactly as much memory as needed | the programmer must **deallocate it manually (delete[])** → risk of **memory leak, dangling pointer** |

> Exam point: the 2023 essay came straight from this handout (advantages, disadvantages, reasons — 4 boxes). Key words = **compile time vs run time**, **automatic vs manual deallocation**.

@lesson L2-3 | C++ Class Basics · Pointers to Objects | C++ in Summary p.25–28

## class · Constructor · Destructor (summary) {#class-basic}

- **class**: a data structure type that can contain member data and member functions. Defines a new data type
- **Constructor/destructor**: member functions that are **automatically called when an object is created/deleted**
  - A local object is deleted when the function returns → its destructor is called then. The destructor's name is `~ClassName`
  - If you don't write a constructor, the compiler generates an empty default constructor. Same for the destructor
  - Uninitialized member variables hold **garbage values** → dangerous and unstable. Initialize them in the constructor

## Pointers to Objects (Rectangle example) {#obj-pointer}

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
  foo = &obj;                    // assign an address
  bar = new Rectangle(5,6);      // dynamic creation: new returns an address
  baz = new Rectangle[2];        // array: default constructor called twice → each 1×1
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
- **Objects use `.`**, **pointers use `->`** (= `(*foo).area()`). The array element `baz[0]` is an object, so it uses `.`
- `foo = obj;` (wrong) → `foo = &obj;` (right). `bar.area()` (wrong) → `bar->area()` (right)

> Exam point: a variant of this code every year in 2025·2024·2023·2019·2017 (fill in the blanks, find 5 errors, write the output). Get `.`/`->`/`&`/`new`/`delete[]` exactly right line by line.

@lesson L2-4 | File I/O | C++ in Summary p.29–39

## File Stream Classes and open {#fstream}

- **ofstream**: stream class to write on files / **ifstream**: stream class to read from files / **fstream**: read and write from/to files (`#include <fstream>`)
- File processing order: **open → read/write → close**
- Decide when opening: text vs binary; for writing, **append vs truncate (overwrite)**; file position (automatic vs user-controlled)
- `myfile.open(filename, mode);` or via the constructor `ofstream myfile("example.txt");`
- Check that it opened: `if (myfile.is_open()) { ... }`; close: `myfile.close();`
- Write text: `myfile << "This is a line.\n";`; read: `while (getline(myfile, line)) cout << line << '\n';`
- State checks: `bad()` read/write failed, `fail()` bad + format error, `eof()` end of file, `good()` everything OK, `clear()` reset the flags

> Exam point: 2019 blank "ofstream: write on files / (ifstream): read from files / (fstream): read and write".

## File Open Modes {#open-modes}

| Flag | Meaning |
|---|---|
| `ios::in` | open for input (reading) |
| `ios::out` | open for output (writing) |
| `ios::binary` | open in binary mode |
| `ios::ate` | set the initial position at the **end of the file** (otherwise at the beginning) |
| `ios::app` | **all output operations are performed at the end of the file** → **appends** to the existing content |
| `ios::trunc` | if the file is opened for output and **already exists**, its previous content is **deleted** and replaced by the new content |

- Combine several with **bitwise OR `|`**: `myfile.open("example.bin", ios::out | ios::app | ios::binary);`
- **Default modes**: ofstream = `ios::out`, ifstream = `ios::in`, fstream = `ios::in | ios::out`
- Opening for writing erases the existing file and writes from the beginning (the professor warned about this several times)

> Exam point: 2023 blanks "ios::app means all output operations are performed at the (end)", "(ios::trunc) means if the file is opened for output and already (existing), its previous content is deleted". app also in 2019.

## File Position: tellg / seekg {#seek-tell}

- There is a separate **get position** (reading) and **put position** (writing)
- `tellg()` / `tellp()`: return the current get/put position
- `seekg(position)` / `seekp(position)`: move to an absolute position
- `seekg(offset, direction)`: `ios::beg` (from the beginning), `ios::cur` (from the current position), `ios::end` (from the end)

**Getting the file size (a blank every year)**
```
streampos begin, end;
ifstream myfile("example.bin", ios::binary);
begin = myfile.tellg();          // beginning position
myfile.seekg(0, ios::end);       // go to the end
end = myfile.tellg();            // end position
myfile.close();
cout << "size is: " << (end-begin) << " bytes.\n";
```

> Exam point: 2024·2023·2019 "Fill in the boxes to print the size". The three lines `begin = myfile.tellg();` → `myfile.seekg(0, ios::end);` → `end = myfile.tellg();`.

## Binary Files and File Copy {#binary}

- Text vs binary: writing 253 as text gives the characters '2','5','3' (3 bytes); as binary it is 11111101 (1 byte)
- Binary I/O uses `write(memory_block, size);` / `read(memory_block, size);` (memory_block is a `char*`)

**Reading a whole file (from the slides)**
```
ifstream file("example.bin", ios::in | ios::binary | ios::ate);
if (file.is_open()) {
    streampos size = file.tellg();     // because of ate, end position = file size
    char* memblock = new char[size];
    file.seekg(0, ios::beg);           // rewind to the beginning
    file.read(memblock, size);
    file.close();
    ...
    delete[] memblock;
}
```
**File copy (code writing in 2024·2025)**: the code above + `ofstream out("des.bin", ios::out | ios::binary); out.write(memblock, size); out.close();`

> Caution: copying line by line with getline corrupts a binary file and loses points (per past-exam answer notes). Memorize the order `ios::binary`, `ios::ate` → `tellg` → `seekg(0, ios::beg)` → `read` → `write` → `delete[]`.
