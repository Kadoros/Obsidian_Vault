#include <iostream>
#include <fstream>
using namespace std;
int main() {
    ifstream in("src.bin", ios::in | ios::binary | ios::ate);
    if (!in.is_open()) { cout << "cannot open\n"; return 1; }
    streampos size = in.tellg();
    char* memblock = new char[size];
    in.seekg(0, ios::beg);
    in.read(memblock, size);
    in.close();
    ofstream out("des.bin", ios::out | ios::binary);
    out.write(memblock, size);
    out.close();
    delete[] memblock;
    streampos begin, end;
    ifstream myfile("des.bin", ios::binary);
    begin = myfile.tellg();
    myfile.seekg(0, ios::end);
    end = myfile.tellg();
    myfile.close();
    cout << "size: " << (end-begin) << " bytes\n";
    return 0;
}
