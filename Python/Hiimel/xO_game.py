import tkinter as tk
from tkinter import messagebox

def check_win(board, player):
    """Checks if a player has won in any row, column, or diagonal."""
    for i in range(5):
        if all(board[i][j] == player for j in range(5)) or \
           all(board[j][i] == player for j in range(5)):
            return True
    if all(board[i][i] == player for i in range(5)) or \
       all(board[i][4-i] == player for i in range(5)):
        return True
    return False

def check_tie(board):
    """Checks if the board is full (a tie)."""
    return all(board[i][j] != "-" for i in range(5) for j in range(5))

def available_moves(board):
    """Returns a list of all available moves (empty cells) on the board."""
    moves = []
    for i in range(5):
        for j in range(5):
            if board[i][j] == "-":
                moves.append((i, j))
    return moves

def evaluate_board(board, player):
    """Evaluates the board for the given player (positive for their advantage)."""
    # Weights for different winning possibilities (can be adjusted for strategy)
    WIN_SCORE = 10
    FORK_SCORE = 5
    THREAT_SCORE = 1

    # Count potential wins and threats for both players
    my_wins = 0
    opponent_wins = 0
    my_threats = 0
    opponent_threats = 0

    # Check rows, columns, and diagonals for potential wins (3 in a row)
    for i in range(5):
        row_wins = sum(1 for cell in board[i] if cell == player)
        col_wins = sum(1 for cell in (board[j][i] for j in range(5)) if cell == player)
        diag_wins1 = sum(1 for cell in (board[j][j] for j in range(5)) if cell == player)
        diag_wins2 = sum(1 for cell in (board[j][4 - j] for j in range(5)) if cell == player)
        opponent_row_wins = sum(1 for cell in board[i] if cell == (opponent(player)))
        opponent_col_wins = sum(1 for cell in (board[j][i] for j in range(5)) if cell == (opponent(player)))
        opponent_diag_wins1 = sum(1 for cell in (board[j][j] for j in range(5)) if cell == (opponent(player)))
        opponent_diag_wins2 = sum(1 for cell in (board[j][4 - j] for j in range(5)) if cell == (opponent(player)))

        # Check for winning lines (3 in a row)
        if row_wins == 3:
            my_wins += 1
        elif opponent_row_wins == 3:
            opponent_wins += 1

        if col_wins == 3:
            my_wins += 1
        elif opponent_col_wins == 3:
            opponent_wins += 1

        if diag_wins1 == 3:
            my_wins += 1
        elif opponent_diag_wins1 == 3:
            opponent_wins += 1

        if diag_wins2 == 3:
            my_wins += 1
        elif opponent_diag_wins2 == 3:
            opponent_wins += 1

        # Check for forks (potential winning lines with two empty cells)
        if row_wins == 2 and sum(1 for cell in board[i] if cell == "-") == 2:
            my_threats += FORK_SCORE
        elif opponent_row_wins == 2 and sum(1 for cell in board[i] if cell == "-") == 2:
            opponent_threats += FORK_SCORE

        if col_wins == 2 and sum(1 for cell in (board[j][i] for j in range(5)) if cell == "-") == 2:
            my_threats += FOR
