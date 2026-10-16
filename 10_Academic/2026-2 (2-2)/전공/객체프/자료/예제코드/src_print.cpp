#include <iostream>
#include <cstdio>
#include <print>
#include <format>

using namespace std;

int main()
{
	double pi=3.141592;
	int age = 21;
	printf("pi=%7.2f , age=%d\n",pi,age);
	cout << format("pi={:7.2f} , age={}\n",pi,age);
	print("pi={:7.2f} , age={}\n",pi,age);

	return 0;
}
