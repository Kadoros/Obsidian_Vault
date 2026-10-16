---
tags:
  - tutoring
date: 2026-10-12
---
1. **Implement Pawn Promotion**
   - In the `moving` function, check if the moved piece is a Pawn (`P` or `p`).
   - If a White Pawn reaches row 7 (`targetRow == 7`), promote it to a Queen (`"Q"`).
   - If a Black Pawn reaches row 0 (`targetRow == 0`), promote it to a Queen (`"q"`).

2. **Refactor Display Rendering (DRY Principle)**
   - Create a reusable function: `render_display(Boards, DisplayBoards, valid_moves)`.
   - Move the duplicate rendering logic (copying `Boards` to `DisplayBoards`, plotting `"X"`, and calling `show_board`) into this new function.
   - Replace the repeated rendering blocks across all 6 piece functions with a call to `render_display`.

3. **Track and Display Captured Pieces**
   - Initialize two global lists: `white_captured = []` and `black_captured = []`.
   - In the `moving` function, check if `Boards[targetRow][targetCol]` contains an opponent piece (not `"."`) before overwriting it.
   - Append the captured piece to the appropriate team's list and print both lists below the board.