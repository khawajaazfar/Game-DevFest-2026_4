def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    moves = 0
    print("Welcome to Tic-Tac-Toe!")
    
    while moves < 9:
        print_board(board)
        player = players[turn % 2]
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers 0-2.")
            continue
        
        board[row][col] = player
        moves += 1
        
        if check_winner(board, player):
            print_board(board)
            print(f"Congratulations! Player {player} wins!")
            break
        turn += 1
    else:
        print_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
