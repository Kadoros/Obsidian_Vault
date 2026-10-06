---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: 2D 배열
level: 심화
topic: "2D 배열 90° 회전 (pseudocode+Python)"
---
파이션 코드 작성 + pseudocode 작성

Challenge 1. 2D Array 90-Degree Clockwise Rotation

  

Scenario:

Given an N x N 2D array (e.g., 3 x 3), write pseudocode to rotate the matrix 90 degrees clockwise and store the result in a new array Rotated[1:N, 1:N].

  

Original Grid:

[1, 2, 3]

[4, 5, 6]

[7, 8, 9]

  

After 90-Degree Clockwise Rotation:

[7, 4, 1]

[8, 5, 2]

[9, 6, 3]

  

Task:

Write pseudocode using nested loops (FOR) to copy the values from Original[1:N, 1:N] to Rotated[1:N, 1:N] in rotated positions.

  

Challenge 2. Tic-Tac-Toe Win Checker

  

Scenario:

A 2D array Board[1:3, 1:3] stores the current state of a Tic-Tac-Toe game with characters 'X', 'O', or ' ' (empty).

The variable Player holds the current player's mark (e.g., 'X').

  

Task:

Write pseudocode to check if the Player has won the game.

The program must check:

  

1. All 3 horizontal rows
    
      
    
2. All 3 vertical columns
    
      
    
3. Both 2 diagonals
    
      
    

If a winning line of 3 identical player marks is found, output "Player Wins!" and set the variable IsWin <- TRUE.