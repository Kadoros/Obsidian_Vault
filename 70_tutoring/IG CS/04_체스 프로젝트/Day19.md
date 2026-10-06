---
tags:
  - tutoring
course: Cambridge IGCSE Computer Science
unit: 체스 프로젝트
level: 심화
topic: "valid_moves 리스트로 이동 로직 재구성"
---
1. **Finalize Rook and Update the `moving` Function**
   - Clear the move list at the beginning of path generation using `valid_moves.clear()` to prevent duplicate coordinates.
   - In the `moving` function, change the condition from `if Boards[targetRow][targetCol] == "X":` to `if [targetRow, targetCol] in valid_moves:`.
   - Remove the nested loops that erase `"X"` from `Boards`, as `"X"` is no longer written to the actual board.

2. **Refactor Knight (N), King (K), and Pawn (P)**
   - In `show_N_path`, `show_K_path`, and `show_P_paths`, replace every instance of `Boards[...] = "X"` with `valid_moves.append(...)`.
   - Update each function to copy `Boards` into `DisplayBoards`, plot `"X"` onto `DisplayBoards` using `valid_moves`, and render using `show_board(DisplayBoards)`.

3. **Verify the Bug Fix (Piece Persistence Test)**
   - Place a piece adjacent to an opponent piece so an `"X"` appears over the opponent piece.
   - Choose a different valid square to move instead of capturing that piece.
   - Confirm that the uncaptured piece remains on the board and does not disappear.