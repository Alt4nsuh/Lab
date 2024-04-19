import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    for i in range(5):
        if all(board[i][j] == player for j in range(5)) or \
           all(board[j][i] == player for j in range(5)):
            return True
    if all(board[i][i] == player for i in range(5)) or \
       all(board[i][4-i] == player for i in range(5)):
        return True
    return False

def check_tie(board):
    return all(board[i][j] != "-" for i in range(5) for j in range(5))

def minimax(board, depth, maximizing_player):
    if check_win(board, "X"):
        return -1
    elif check_win(board, "O"):
        return 1
    elif check_tie(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(5):
            for j in range(5):
                if board[i][j] == "-":
                    board[i][j] = "O"
                    eval_score = minimax(board, depth + 1, False)
                    board[i][j] = "-"
                    max_eval = max(max_eval, eval_score)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(5):
            for j in range(5):
                if board[i][j] == "-":
                    board[i][j] = "X"
                    eval_score = minimax(board, depth + 1, True)
                    board[i][j] = "-"
                    min_eval = min(min_eval, eval_score)
        return min_eval

def computer_move(board):
    best_eval = float("-inf")
    best_move = None
    for i in range(5):
        for j in range(5):
            if board[i][j] == "-":
                board[i][j] = "O"
                eval_score = minimax(board, 0, False)
                board[i][j] = "-"
                if eval_score > best_eval:
                    best_eval = eval_score
                    best_move = (i, j)
    return best_move

def player_move(row, col):
    global currentPlayer
    if board[row][col] == "-":
        board[row][col] = currentPlayer
        button_texts[row][col].set(currentPlayer)
        if check_win(board, currentPlayer):
            messagebox.showinfo("Game Over", f"{currentPlayer} wins!")
            reset_board()
        elif check_tie(board):
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_board()
        else:
            currentPlayer = "O" if currentPlayer == "X" else "X"
            if currentPlayer == "O":
                row, col = computer_move(board)
                player_move(row, col)

def reset_board():
    global board, currentPlayer
    board = [["-" for _ in range(5)] for _ in range(5)]
    currentPlayer = "X"
    for i in range(5):
        for j in range(5):
            button_texts[i][j].set("-")

def create_button(row, col):
    text_var = tk.StringVar()
    text_var.set("-")
    button_texts[row][col] = text_var
    button = tk.Button(root, textvariable=text_var, font=("Arial", 20), width=5, height=2,
                       command=lambda: player_move(row, col))
    button.grid(row=row, column=col, padx=5, pady=5)

root = tk.Tk()
root.title("Tic Tac Toe")

board = [["-" for _ in range(5)] for _ in range(5)]
currentPlayer = "X"
button_texts = [[None for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        create_button(i, j)

root.mainloop()
