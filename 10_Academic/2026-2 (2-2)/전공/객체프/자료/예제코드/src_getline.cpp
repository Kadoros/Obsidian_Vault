#include <iostream>
#include <string>
#include <sstream>
#include <fstream>
using namespace std;

int main() 
{
    cout << "[student_id] [name] [department] [age] [GPA(score)]\n";
    
    string student_id;
    string name;
    string dept;
    int age;
    double GPA;
    double GPA_total=0.0;
    string linestr;
    int count=0;


    while (getline(cin,linestr)) {
//  ifstream myfile("example.txt");
//  while (getline(myfile,linestr)) {
        if (linestr.empty()) break;
        istringstream iss(linestr); // istringstream treats a string as an input stream.
        iss >> student_id >> name >> dept >> age >> GPA ;
        cout << "student_id: " << student_id << "\n";
        cout << "name: " << name << "\n";
        cout << "department: " << dept << "\n";
        cout << "age: " << age << "\n";
        cout << "GPA(score): " << GPA << "\n";
        GPA_total += GPA;
        count++;
    }
//  myfile.close();
    cout << "GPA average: " << GPA_total/count << "\n";

    return 0;
}
