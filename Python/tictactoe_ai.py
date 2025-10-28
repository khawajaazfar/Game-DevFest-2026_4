
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tic-Tac-Toe with an UNBEATABLE AI (minimax + pruning)
- Human vs AI (you are 'X' by default, AI is 'O')
- Robust input validation (row/col 1–3, empty cell only)
- Replay option after game ends
- Tiny self-check to ensure core functions behave as expected
Run: python3 tictactoe_ai.py
"""

from typing import List, Optional, Tuple

Board = List[List[str]]

HUMAN = "X"
AI = "O"
EMPTY = " "

def new_board() -> Board:
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def print_board(b: Board) -> None:
    print("\n   1   2   3")
    for i, row in enumerate(b, start=1):
        print(f"{i}  " + " | ".join(row))
        if i < 3:
            print("  ---+---+---")
    print()

def available_moves(b: Board) -> List[Tuple[int, int]]:
    return [(r, c) for r in range(3) for c in range(3) if b[r][c] == EMPTY]

def winner(b: Board) -> Optional[str]:
    lines = []
    # rows & cols
    lines.extend(b)
    lines.extend([[b[r][c] for r in range(3)] for c in range(3)])
    # diagonals
    lines.append([b[i][i] for i in range(3)])
    lines.append([b[i][2 - i] for i in range(3)])
    for line in lines:
        if line[0] != EMPTY and line.count(line[0]) == 3:
            return line[0]
    return None

def terminal(b: Board) -> bool:
    return winner(b) is not None or not available_moves(b)

def score(b: Board, depth: int) -> int:
    w = winner(b)
    if w == AI:
        return 10 - depth
    if w == HUMAN:
        return depth - 10
    return 0

def minimax(b: Board, depth: int, maximizing: bool, alpha: int, beta: int) -> Tuple[int, Optional[Tuple[int, int]]]:
    if terminal(b):
        return score(b, depth), None

    best_move: Optional[Tuple[int, int]] = None

    if maximizing:  # AI turn
        best_val = -10_000
        for (r, c) in available_moves(b):
            b[r][c] = AI
            val, _ = minimax(b, depth + 1, False, alpha, beta)
            b[r][c] = EMPTY
            if val > best_val:
                best_val, best_move = val, (r, c)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return best_val, best_move
    else:          # Human turn
        best_val = 10_000
        for (r, c) in available_moves(b):
            b[r][c] = HUMAN
            val, _ = minimax(b, depth + 1, True, alpha, beta)
            b[r][c] = EMPTY
            if val < best_val:
                best_val, best_move = val, (r, c)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return best_val, best_move

def ai_move(b: Board) -> Tuple[int, int]:
    _, move = minimax(b, 0, True, -10_000, 10_000)
    assert move is not None
    return move

def human_move(b: Board) -> Tuple[int, int]:
    while True:
        try:
            raw = input("Enter your move as row col (e.g., 1 3): ").strip()
            r_s, c_s = raw.split()
            r, c = int(r_s) - 1, int(c_s) - 1
            if r not in range(3) or c not in range(3):
                print("Row/Col must be 1..3. Try again.")
                continue
            if b[r][c] != EMPTY:
                print("That cell is occupied. Try again.")
                continue
            return r, c
        except ValueError:
            print("Invalid format. Example: 2 3")
        except KeyboardInterrupt:
            print("\nBye!")
            raise SystemExit

def game() -> None:
    print("You are 'X'. AI is 'O'. Good luck 🙂")
    b = new_board()
    print_board(b)

    # Optional: let user choose who goes first
    first = input("Go first? [Y/n]: ").strip().lower()
    human_turn = not (first == "n")

    while True:
        if human_turn:
            r, c = human_move(b)
            b[r][c] = HUMAN
        else:
            print("AI is thinking...")
            r, c = ai_move(b)
            b[r][c] = AI
        print_board(b)

        if terminal(b):
            w = winner(b)
            if w == HUMAN:
                print("You win! 🎉")
            elif w == AI:
                print("AI wins. Unlucky! 🤖")
            else:
                print("It's a draw. 🤝")
            # replay
            again = input("Play again? [y/N]: ").strip().lower()
            if again == "y":
                b = new_board()
                print_board(b)
                first = input("Go first? [Y/n]: ").strip().lower()
                human_turn = not (first == "n")
                continue
            else:
                break

        human_turn = not human_turn

def _self_check() -> None:
    # Simple sanity checks
    b = new_board()
    assert winner(b) is None
    b[0] = [AI, AI, AI]
    assert winner(b) == AI
    b = new_board()
    b[0][0] = HUMAN; b[1][1] = HUMAN; b[2][2] = HUMAN
    assert winner(b) == HUMAN
    print("Self-check OK.")

if __name__ == "__main__":
    _self_check()
    game()
