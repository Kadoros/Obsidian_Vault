#include <iostream>
using namespace std;
class Rect {
public:
     int w,h;
     Rect(int x, int y): w(x), h(y) { cout << "c1\n"; }
     Rect(const Rect& x) { w=x.w; h=x.h; cout << "c2\n"; }
     int area() { return w*h; }
};
void func(Rect obj, int y) {
     cout << "f3\n";
     obj.h = y;
}
int main() {
    Rect a(5,6);
    Rect *b, *c;
    b = &a;
    c = new Rect(7,8);
    func(a,9);
    Rect d(a);
    b->w = 9;
    cout << "======="<< endl;
    cout << a.area() << endl;
    cout << b->area() << endl;
    cout << c->area() << endl;
    cout << d.area() << endl;
    delete c;
    return 0;
}
