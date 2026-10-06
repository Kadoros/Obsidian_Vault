---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: Python 기초 (입출력·조건·반복)
level: 기초
topic: "자료형·조건문 (환율, 영화표)"
---
1. [Data Types & Operations] Currency Converter
    

- Write a program that takes an integer input for US Dollars (USD) and converts it to Korean Won (KRW). (Exchange rate: 1 USD = 1400 KRW)
    
- Requirements: Receive the dollar amount from the user, multiply it by the exchange rate, and print the result in the format: "Result: [USD] dollars is [KRW] won."
    

2. [Conditionals] Movie Ticket Machine
    

- Write a program that calculates the movie ticket price based on age.
    
- Requirements: Receive the user's age as input. Use branching to set the price: Free (0 won) for under 10 years old, Student rate (8000 won) for 10 to under 20 years old, and Adult rate (15000 won) for 20 years and older. Print the final price.
    

3. [Loops] Smartphone Unlock
    

- Write a program that repeatedly asks for a password until the correct one is entered.
    
- Requirements: Use a predefined password variable and an infinite loop (`while True`). If the input matches, print "Unlocked!" and exit the loop (`break`). If it is incorrect, print "Please try again."
    

4. [Lists & Arrays] My Playlist
    

- Write a program to store and manage song titles using a list.
    
- Requirements: Create a list with 3 initial songs. Prompt the user for a new song and append it to the end of the list. Then, remove the second song (index 1) from the list. Finally, use a `for` loop to print the remaining songs in order.
    

5. [Arithmetic Operators] Vending Machine Change Calculator
    

- Write a program that takes the total change amount as input and calculates the minimum number of 500-won and 100-won coins needed.
    
- Requirements: Use the floor division operator (`//`) to find the number of 500-won coins, use the modulo operator (`%`) to find the remaining amount, and then calculate the number of 100-won coins. Print the count for each coin.
    

6. [Comparison & Logical Operators] Scholarship Evaluator
    

- Write a program that receives Python and English scores and evaluates whether the student is eligible for a scholarship, outputting `True` or `False`.
    
- Requirements: The scholarship condition is scoring 90 or above in Python AND 80 or above in English. Do not use `if` statements. Store the boolean result of the comparison and logical operations in a variable, and print it directly in the format: "Scholarship eligibility: [True/False]".