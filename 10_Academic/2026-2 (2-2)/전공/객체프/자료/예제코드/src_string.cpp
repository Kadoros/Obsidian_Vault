#include <iostream>
#include <string>
using namespace std;

int main() {
    // 1. Creating strings
    string s1 = "Hello";
    string s2("World");
    string s3;                 // empty string

    // 2. Concatenation
    s3 = s1 + " " + s2;
    cout << s3 << endl;        // Hello World

    // 3. Length
    cout << "Length: " << s3.length() << endl;
    cout << "Size: " << s3.size() << endl;  // same as length()

    // 4. Accessing individual characters
    cout << s3[0] << endl;     // H
    cout << s3.at(1) << endl;  // e

    // 5. Modifying a character
    s3[0] = 'h';
    cout << s3 << endl;        // hello World

    // 6. Adding text
    s3 += "!";
    s3.append(" C++");
    cout << s3 << endl;        // hello World! C++

    // 7. Finding a substring
    size_t pos = s3.find("World");

    if (pos != string::npos)
        cout << "Found at index: " << pos << endl;

    // 8. Extracting a substring
    string sub = s3.substr(6, 5);
    cout << sub << endl;       // World

    // 9. Replacing part of a string
    s3.replace(6, 5, "C++");
    cout << s3 << endl;        // hello C++! C++

    // 10. Inserting text
    s3.insert(5, " beautiful");
    cout << s3 << endl;        // hello beautiful C++! C++

    // 11. Erasing part of a string
    s3.erase(5, 10);
    cout << s3 << endl;        // hello C++! C++

    // 12. String comparison
    string a = "apple";
    string b = "banana";

    if (a < b)
        cout << "apple comes before banana" << endl;

    if (a == "apple")
        cout << "a is apple" << endl;

    // 13. Checking whether a string is empty
    if (s3.empty())
        cout << "String is empty" << endl;

    // 14. Iterating through characters
    for (char c : s3)
        cout << c << ' ';
    cout << endl;

    // 15. C-style string when needed
    const char* p = s3.c_str();
    cout << p << endl;

    // 16. Numeric Conversions
    string doubleStr = "123.45";
    string intStr = "67";
    double dval = stod(doubleStr);   // String to double
    int ival = stoi(intStr);   // String to int
    string formatted1 = to_string(dval * 2); // Number to string
    string formatted2 = to_string(ival * 2); // Number to string
    cout << "conversion result: " << formatted1 << " , " << formatted2 << "\n";

    return 0;
}
