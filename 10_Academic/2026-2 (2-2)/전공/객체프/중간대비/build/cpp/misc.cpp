#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
const unsigned int DEFAULT_SIZE = 256;
class TIntStack {
public:
    TIntStack(unsigned int stackSize = DEFAULT_SIZE);
    TIntStack(const TIntStack& that);
    ~TIntStack();
    bool Push(int thisValue);
    unsigned int getCount() const { return _count; }
private:
    int* _sp; unsigned int _count; unsigned int _size;
};
TIntStack::TIntStack(unsigned int stackSize) {
    _size = stackSize; _count = 0; _sp = new int[_size];
}
TIntStack::TIntStack(const TIntStack& that) {
    _size = that._size; _count = that._count; _sp = new int[_size];
    for (unsigned int i = 0; i < _count; i++) _sp[i] = that._sp[i];
}
TIntStack::~TIntStack() { delete[] _sp; }
bool TIntStack::Push(int thisValue) {
    if (_count >= _size) return false;
    _sp[_count++] = thisValue; return true;
}
class Complex {
private: double re, im;
public:
    Complex(double r, double i) : re(r), im(i) {}
    friend Complex operator-(Complex&, Complex&);
    friend Complex operator+(Complex&, Complex&);
    friend ostream& operator<<(ostream &o, const Complex &x);
};
Complex operator+(Complex& x, Complex& y) { return Complex(x.re + y.re, x.im + y.im); }
Complex operator-(Complex& x, Complex& y) { return Complex(x.re - y.re, x.im - y.im); }
ostream& operator<<(ostream &o, const Complex& x) {
    o << x.re;
    if (x.im > 0) o << "+" << x.im << "i";
    else if (x.im < 0) o << x.im << "i";
    return o;
}
class inf_int {
private:
    char* digits; unsigned int length; bool thesign;
public:
    inf_int();
    inf_int(int n);
    inf_int(const char* str);
    inf_int(const inf_int& x);
    ~inf_int() { delete[] digits; }
    friend bool operator==(const inf_int&, const inf_int&);
    friend bool operator>(const inf_int&, const inf_int&);
    friend bool operator<(const inf_int&, const inf_int&);
    friend ostream& operator<<(ostream&, const inf_int&);
};
inf_int::inf_int() {
    digits = new char[2]; digits[0] = '0'; digits[1] = '\0';
    length = 1; thesign = true;
}
inf_int::inf_int(int n) {
    char buf[100]; int i = 0;
    long long m = n;
    thesign = (m >= 0);
    if (m < 0) m = -m;
    do { buf[i++] = (char)('0' + m % 10); m /= 10; } while (m > 0);
    buf[i] = '\0';
    length = i;
    digits = new char[length + 1];
    strcpy(digits, buf);
}
inf_int::inf_int(const char* str) {
    thesign = true;
    if (str[0] == '-') { thesign = false; str++; }
    length = strlen(str);
    digits = new char[length + 1];
    for (unsigned int i = 0; i < length; i++) digits[i] = str[length - 1 - i];
    digits[length] = '\0';
}
inf_int::inf_int(const inf_int& x) {
    length = x.length; thesign = x.thesign;
    digits = new char[length + 1];
    strcpy(digits, x.digits);
}
bool operator==(const inf_int& x, const inf_int& y) {
    return x.thesign == y.thesign && x.length == y.length && strcmp(x.digits, y.digits) == 0;
}
bool operator>(const inf_int& x, const inf_int& y) {
    if (x.thesign != y.thesign) return x.thesign;           // positive > negative
    bool absGreater;                                         // |x| > |y| ?
    if (x.length != y.length) absGreater = x.length > y.length;
    else {
        int i = (int)x.length - 1;
        while (i >= 0 && x.digits[i] == y.digits[i]) i--;
        if (i < 0) return false;                             // equal
        absGreater = x.digits[i] > y.digits[i];
    }
    return x.thesign ? absGreater : !absGreater;
}
bool operator<(const inf_int& l, const inf_int& r) { return r > l; }
ostream& operator<<(ostream& o, const inf_int& x) {
    if (!x.thesign) o << '-';
    for (int i = (int)x.length - 1; i >= 0; i--) o << x.digits[i];
    return o;
}
int main() {
    TIntStack s(2); s.Push(1); s.Push(2); cout << s.Push(3) << " " << s.getCount() << "\n";
    TIntStack t(s); cout << t.getCount() << "\n";
    Complex a(3.2, 2.3), b(0, 4.6), c(3.2, 0);
    cout << a << " " << (a - b) << " " << c << " " << (a + b) << "\n";
    inf_int p(-123), q("-1200"), r(0), z, u(p);
    cout << p << " " << q << " " << r << " " << z << " " << u << "\n";
    cout << (p > q) << (q > p) << (r == z) << (p == u) << (p < r) << (inf_int(-2147483647-1)) << "\n";
}
