import tkinter as tk
from tkinter import messagebox

def is_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def on_click(row, col):
    global board
    if board[row][col] == ' ':
        board[row][col] = current_player.get()
        buttons[row][col].config(text=current_player.get())
        
        if check_winner(board, current_player.get()):
            messagebox.showinfo("Tic Tac Toe", f"Player {current_player.get()} wins!")
            reset_board()
        elif is_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        else:
            current_player.set('O' if current_player.get() == 'X' else 'X')

def reset_board():
    global board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text='')

def tic_tac_toe():
    global buttons, current_player, board
    root = tk.Tk()
    root.title("Tic Tac Toe")
    
    current_player = tk.StringVar(value='X')
    buttons = [[None for _ in range(3)] for _ in range(3)]
    board = [[' ' for _ in range(3)] for _ in range(3)]
    
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(root, text='', font='normal 20 bold', width=5, height=2,
                                          command=lambda row=row, col=col: on_click(row, col))
            buttons[row][col].grid(row=row, column=col)
    
    root.mainloop()

def check_winner(board, player):
    # Check rows, columns and diagonals for a win
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

tic_tac_toe()
