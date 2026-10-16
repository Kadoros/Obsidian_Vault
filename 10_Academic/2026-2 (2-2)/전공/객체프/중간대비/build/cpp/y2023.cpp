#include <iostream>
using namespace std;
class X {
private:
   int w,h;
public:
   X() { cout << "c1 called\n"; }
   X(int a,int b) { w=a; h=b; cout << "c3 called\n"; }
   X(const X& x) { w=x.w; h=x.h; cout << "c5 called\n"; }
   ~X() { cout << "d called\n"; }
   friend int f1(X obj);
};
int f1(X obj)
{
    cout << "f1 called!\n";
    return obj.w*obj.h;
}
int main()
{
    int z;
    X a(5,6), b;
    X c = a;
    b = c;
    z = f1(b);
    cout << "area: " << z << "\n";
    return 0;
}
