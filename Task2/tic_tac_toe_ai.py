import math

board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    for i in range(3):
        row = " | ".join(board[i*3:(i+1)*3])
        print(" " + row)
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(brd, player):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(brd[i] == brd[j] == brd[k] == player for i,j,k in win_combos)

def is_draw(brd):
    return ' ' not in brd

def get_available_moves(brd):
    return [i for i in range(9) if brd[i] == ' ']

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'O'):
        return 1
    if check_winner(brd, 'X'):
        return -1
    if is_draw(brd):
        return 0
    if is_maximizing:
        best_score = -math.inf
        for move in get_available_moves(brd):
            brd[move] = 'O'
            score = minimax(brd, depth + 1, False)
            brd[move] = ' '
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for move in get_available_moves(brd):
            brd[move] = 'X'
            score = minimax(brd, depth + 1, True)
            brd[move] = ' '
            best_score = min(best_score, score)
        return best_score

def ai_move():
    best_score = -math.inf
    best_move = None
    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    board[best_move] = 'O'

def human_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move! Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Please enter a valid number (1-9).")

def play_game():
    print("\n" * 10)
    print("Welcome to TIC-TAC-TOE")
    print("You are X | AI is O")
    print_board()

    while True:
        human_move()
        print("\n" * 10)
        print_board()
        if check_winner(board, 'X'):
            print("You win! Well played.")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        print("AI is thinking...")
        ai_move()
        print("\n" * 10)
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        if is_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
