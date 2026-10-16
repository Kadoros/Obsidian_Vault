/*
* The Original Source Code written by Krellor
*/

#include <iostream>
#include <cstdio>
#include <cmath>

using std::cout;
using std::cin;
using std::endl;
using std::ostream;
using std::istream;

class complex
{
    public:
        complex();
        complex(double a, double b); //a = real, b = imaginary.
        double get_real();
        double get_imag();
        double get_abs(); //uses pythagerom theorem to find distance from origin
        friend complex operator+(const complex& num1, const complex& num2);
        friend complex operator-(const complex& num1, const complex& num2);
        friend complex operator*(const complex& num1, const complex& num2);
        void operator+=(const complex& num);
        void operator-=(const complex& num);
        void operator*=(const complex& num);
        friend ostream& operator<<(ostream &output, complex &num);
        ~complex();
        
    private:
        double real;
        double imag;

};

complex::complex()
{
    real = 0;
    imag = 0;
}

complex::complex(double a, double b)
{
    real = a;
    imag = b;
}

double complex::get_real()
{
    return real;
}

double complex::get_imag()
{
    return imag;
}

double complex::get_abs() 
{
    return (double)sqrt(pow(real,2) + pow(imag,2));
}

complex operator+(const complex& num1,const complex& num2)
{
    complex temp;
    temp.imag = num1.imag + num2.imag;
    temp.real = num1.real + num2.real;

    return temp;
}

complex operator-(const complex& num1,const complex& num2)
{
    complex temp;
    temp.imag = num1.imag - num2.imag;
    temp.real = num1.real - num2.real;

    return temp;
}

complex operator*(const complex& num1,const complex& num2)
{
    complex temp;
    double w = 0, x = 0, y = 0, z = 0;
    
    w = num1.real * num2.real; //  \                                                                                        /
    x = num1.real * num2.imag; //   \    these four operations FOIL the two complex numbers. w is real, x & y are imaginary,
    y = num1.imag * num2.real; //   /    and z will be real once the i^2 is converted to -1.  The if statement handles the -1.
    z = num1.imag * num2.imag; //  /

    if(z > 0)
    {
        temp.real = w - z;
    }
    else
    {
        temp.real = w + z;
    }
    temp.imag = x + y;
    
    return temp;
}

void complex::operator+=(const complex& num)
{
    this->imag = this->imag + num.imag;
    this->real = this->real + num.real;
    
}

void complex::operator-=(const complex& num)
{
    this->imag = this->imag - num.imag;
    this->real = this->real - num.real;
}

void complex::operator*=(const complex& num)
{
    double w = 0, x = 0, y = 0, z = 0;
    
    w = this->real * num.real; //  \                                                                                        /
    x = this->real * num.imag; //   \    these four operations FOIL the two complex numbers. w is real, x & y are imaginary,
    y = this->imag * num.real; //   /    and z will be real once the i^2 is converted to -1.  The if statement handles the -1.
    z = this->imag * num.imag; //  /

    if(z > 0)
    {
        this->real = w - z;
    }
    else
    {
        this->real = w + z;
    }
    this->imag = x + y;
}

ostream& operator<<(ostream &output, complex &num)
{
    output << "y = " << num.real << " + " << num.imag << "i" << endl;

    return output;
}

complex::~complex()
{
}


int main(void)
{
    complex x1(2, 3), y1(4, 6);
    double hold_abs = 0;
    
    cout << "Complex number 1: "<< x1;
    cout << "Complex number 2: "<<  y1;

    x1 = x1 + y1;
    x1 += y1;
    x1 = x1 - y1;
    x1 -= y1;
    x1 = y1 * x1;
    x1 *= y1;
    
    hold_abs = x1.get_abs();
    hold_abs = x1.get_imag();
    hold_abs = x1.get_real();

    cout << hold_abs << endl;
    cout << x1;
    
    return 0;
}

