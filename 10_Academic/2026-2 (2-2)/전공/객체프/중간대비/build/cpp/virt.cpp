#include <iostream>
using namespace std;
class B { public: B() { z=-2; } B(int z_val) : z(z_val) {} virtual int get_val() { return (z-1); }; int gv2() { return (z-2); } private: int z; };
class D1 : public B { public: D1() { x=0; } D1(int x_val): x(x_val) {} int get_val() { return x; }; private: int x; };
class D2 : public B { public: D2() { y=0; } D2(int y_val): y(y_val) {} virtual int gv2() { return y*y; }; private: int y; };
int main(){ B Zero(0); D1 Two(2); D2 Four(4); B* A[3]; A[0]=&Zero; A[1]=&Two; A[2]=&Four;
cout << "0 : " << A[0]->get_val() << endl; cout << "1 : " << A[0]->gv2() << endl; cout << "2 : " << A[1]->get_val() << endl; cout << "3 : " << A[2]->gv2() << endl; }
