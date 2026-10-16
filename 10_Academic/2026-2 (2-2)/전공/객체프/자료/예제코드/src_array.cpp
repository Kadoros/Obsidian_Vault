#include <iostream>
using namespace std;

int main() {
    // 1. Standard Array
    int stackArray[3] = {10, 20, 30};

    // 2. Dynamic Memory Allocation
    int size;
    cout << "input size: ";
    cin >> size;
    int* heapArray = new int[size];

    // 3. Pointer Operations
    int* ptrToStack = stackArray; 

    // Populate the heap array using pointer offset notation
    cout << "enter " << size << " integers: \n";
    for (int i = 0; i < size; ++i) {
        cin >> heapArray[i];
    }

    // 4. Output Comparisons
    for (int i = 0; i < 3; ++i) {
        cout << "stackArray[" << i << "]=" << stackArray[i] 
             << " | *(ptrToStack+" << i << ")=" << *(ptrToStack + i) << "\n";
    }

    for (int i = 0; i < size; ++i) {
        cout << "*(heapArray+" << i << ")= " << *(heapArray + i)
                  << " | heapArray[" << i << "]=" << heapArray[i] << "\n";
    }

    // 5. Memory Cleanup
    // Only heap-allocated memory requires manual deletion.
    delete[] heapArray;

    return 0;
}
