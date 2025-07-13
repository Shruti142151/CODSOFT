import math

def init_board():
    return [" " for _ in range(9)]

def print_board(b):
    print("\nCurrent Board:")
    for i in range(3):
        row = " | ".join(b[i*3:(i+1)*3])
        print(f" {row} ")
        if i < 2:
            print("---+---+---")
    print()

def winner(b, player):
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    return any(all(b[i] == player for i in combo) for combo in combos)

def is_draw(b):
    return " " not in b

def minimax(board, depth, is_max):
    if winner(board, "O"):
        return 10 - depth
    if winner(board, "X"):
        return depth - 10
    if is_draw(board):
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best = max(score, best)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best = min(score, best)
        return best

def ai_move(board):
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"
    print("AI has made its move.\n")

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9 and board[move - 1] == " ":
                board[move - 1] = "X"
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number from 1 to 9.")

def play_game():
    board = init_board()
    print("\nWelcome to Tic-Tac-Toe AI 🤖")
    print("You are 'X' and AI is 'O'. Let's begin!")
    print_board(board)

    while True:
        player_move(board)
        print_board(board)

        if winner(board, "X"):
            print("🎉 You win!\n")
            break
        elif is_draw(board):
            print("It's a draw!\n")
            break

        ai_move(board)
        print_board(board)

        if winner(board, "O"):
            print("😢 AI wins. Better luck next time!\n")
            break
        elif is_draw(board):
            print("It's a draw!\n")
            break

if _name_ == "_main_":
    while True:
        play_game()
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("\nThanks for playing! Goodbye 👋")
            break
