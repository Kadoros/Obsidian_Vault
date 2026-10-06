---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: Python 기초 (입출력·조건·반복)
level: 표준
topic: "중첩 for문 (플로이드 삼각형 등)"
---
## Task 1: Continuous Number Pattern (Floyd's Triangle)

Write a program using nested `for` loops to output a continuous number pattern known as Floyd's Triangle. **Note:** The numbers do not reset on each row. You will need a variable outside the loops to keep track of the current number to print.

Output required: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15

_Hint:_ 1. The outer loop controls the 5 rows. 2. The inner loop controls how many numbers are printed on the current row. 3. You must increase your tracking number by 1 every time you print it.

## Task 2: Unique Passcode Generator

A security system generates 3-letter passcodes using only the letters `"A"`, `"B"`, `"C"`, and `"D"`. However, a valid passcode cannot contain any repeating letters (e.g., "ABC" and "CDA" are valid, but "ABA", "BBD", or "CCC" are invalid).

Write a program using nested loops to generate and print all valid 3-letter passcodes. At the very end, print the total count of valid passcodes found.

- **Logic:**
    
    1. You will need three nested loops to select the first, second, and third letters.
        
    2. Inside the innermost loop, use an `if` statement to check if all three letters are different from each other.
        
    3. If they are all different, print the combination and add 1 to your total count.
        
- **Expected Output format:** ABC ABD ACB ACD ... Total valid passcodes: 24