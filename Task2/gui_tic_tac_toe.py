import tkinter as tk
from tkinter import messagebox
import math

# Minimax-based AI
def minimax(brd, is_maximizing):
    winner = check_winner(brd)
    if winner == 'O':
        return 1
    elif winner == 'X':
        return -1
    elif ' ' not in brd:
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'O'
                score = minimax(brd, False)
                brd[i] = ' '
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if brd[i] == ' ':
                brd[i] = 'X'
                score = minimax(brd, True)
                brd[i] = ' '
                best_score = min(best_score, score)
        return best_score

# Get best move for AI
def get_best_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# Check for a winner
def check_winner(brd):
    win_combos = [(0,1,2),(3,4,5),(6,7,8),
                  (0,3,6),(1,4,7),(2,5,8),
                  (0,4,8),(2,4,6)]
    for i, j, k in win_combos:
        if brd[i] == brd[j] == brd[k] and brd[i] != ' ':
            return brd[i]
    return None

# Handle button click
def on_click(i):
    if board[i] == ' ' and not game_over[0]:
        board[i] = 'X'
        buttons[i]['text'] = 'X'
        winner = check_winner(board)
        if winner:
            end_game(f"You win! ({winner})")
            return
        elif ' ' not in board:
            end_game("It's a draw!")
            return

        # AI's turn
        ai_index = get_best_move()
        board[ai_index] = 'O'
        buttons[ai_index]['text'] = 'O'

        winner = check_winner(board)
        if winner:
            end_game(f"AI wins! ({winner})")
        elif ' ' not in board:
            end_game("It's a draw!")

# End game message
def end_game(msg):
    game_over[0] = True
    messagebox.showinfo("Game Over", msg)

# Reset game
def reset_game():
    for i in range(9):
        board[i] = ' '
        buttons[i]['text'] = ''
    game_over[0] = False

# Initialize GUI
window = tk.Tk()
window.title("Tic-Tac-Toe AI (Minimax)")
window.resizable(False, False)

frame = tk.Frame(window)
frame.pack()

board = [' ' for _ in range(9)]
buttons = []
game_over = [False]

# Create 3x3 grid of buttons
for i in range(9):
    btn = tk.Button(frame, text='', font=('Arial', 24), width=5, height=2,
                    command=lambda i=i: on_click(i))
    btn.grid(row=i//3, column=i%3)
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(window, text="Restart", font=('Arial', 14),
                      command=reset_game)
reset_btn.pack(pady=10)

window.mainloop()
