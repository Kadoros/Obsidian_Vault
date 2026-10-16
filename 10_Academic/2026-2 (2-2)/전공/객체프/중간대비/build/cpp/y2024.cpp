#include <iostream>
using namespace std;
class X {
public:
    int w,h;
    X() { w=0; h=0; cout << "c1\n"; }
    X(int a,int b) { w=a; h=b; cout << "c2\n"; }
    X(const X& x) { w=x.w; h=x.h; cout << "c3\n"; }
    ~X() { cout << "d\n"; }
};
void func(X obj, int a, int b) {
     cout << "f1 called!\n";
     obj.w = a; obj.h = b;
}
int main() {
    X a(5,6);
    X* b;
    b = &a;
    a.w = 2;
    func(a,7,8);
    X c(a);
    b->h = 9;
    c.w = 1;
    cout << "=========="<< endl;
    cout << a.w <<" "<< a.h << endl;
    cout << b->w <<" "<< b->h << endl;
    cout << c.w <<" "<< c.h << endl;
    return 0;
}
