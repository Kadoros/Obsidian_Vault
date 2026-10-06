---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: 함수와 데이터 검증
level: 표준
topic: "함수 + validation check (IGCSE 빈출)"
---
## Problem 1: Validation Check

This is one of the most common 'data validation' algorithms in IGCSE exams. Create a function that checks if the user's input age falls within the secondary school age range (11 to 18 years old).

- **Function Name:** `validate_age`
    
- **Parameter (Input):** `age` (integer)
    
- **Logic:** Return `True` if the age is between 11 and 18 (inclusive). Otherwise, return `False`.
    
- **Test Code:**
    
    ```
    result1 = validate_age(15)
    print("Age 15 test (Should be True):", result1)
    
    result2 = validate_age(20)
    print("Age 20 test (Should be False):", result2)
    ```
    

## Problem 2: IGCSE Grade Converter (Calculation & If-else)

Create a function that takes a student's score and converts it into an IGCSE alphabetical grade.

- **Function Name:** `get_grade`
    
- **Parameter (Input):** `score` (integer)
    
- **Logic:**
    
    - 80 or above: Return `"A"`
        
    - 60 to 79: Return `"B"`
        
    - 40 to 59: Return `"C"`
        
    - Below 40: Return `"U"` (Unclassified)
        
- **Test Code:**
    
    ```
    my_grade = get_grade(75)
    print("The grade for 75 is:", my_grade) # Should output "B"
    ```
    

## Problem 3: 1D Array Iteration and Counting

Create a function that counts the total number of students who passed (scored 50 or above) from a given list of student exam scores.

- **Function Name:** `count_passes`
    
- **Parameter (Input):** `score_list` (a list containing integers)
    
- **Logic:**
    
    1. Initialize a variable (e.g., `count`) to 0 to store the number of passes.
        
    2. Use a `for` loop to iterate through each score in the list.
        
    3. If the score is 50 or above, increment the pass count by 1.
        
    4. After the loop finishes, `return` the final pass count.
        
- **Test Code:**
    
    ```
    class_scores = [45, 80, 50, 30, 95, 62]
    pass_count = count_passes(class_scores)
    print("Number of passes:", pass_count) # Should output 4
    ```
    

## Problem 4: String Manipulation Algorithm 

이 문제는 눈으로만 보고  푸는 방법을 생각해 보세요 
Create a function that takes a single word as input and counts the total number of vowels (a, e, i, o, u) in that word. This is a fundamental problem in computer science.

- **Function Name:** `count_vowels`
    
- **Parameter (Input):** `word` (string)
    
- **Logic:**
    
    1. Initialize a variable to 0 to store the vowel count.
        
    2. Use a `for` loop to check each letter in the string.
        
    3. If the letter is 'a', 'e', 'i', 'o', or 'u', increment the count by 1.
        
    4. Return the final vowel count.
        
- **Test Code:**
    
    ```
    vowel_count = count_vowels("computer")
    print("Number of vowels in 'computer':", vowel_count) # Should output 3 (o, u, e)
    ```