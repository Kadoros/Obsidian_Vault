#include <iostream>
using namespace std;

int main()
{
	int x=5;
	int* y;
	int& z=x;
	y=&x;
	int w=*y;
	x=9;
	z=*y*x;
	x++;
	z=x&*y;
	cout << x << " " << *y << " " << z << " " << w << endl;   // print the values
	return 0;
}
