import tkinter as tk
from tkinter import messagebox
import random


player_turn = "X"
board = [" " for _ in range(9)]

def check_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return board[i]

    # Check columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    if board[2] == board[4] == board[6] != " ":
        return board[2]

    if " " not in board:
        return "Tie"

    return None

def make_move(index):
    global player_turn
    if board[index] == " " and not check_winner():
        board[index] = player_turn
        buttons[index].config(text=player_turn, state="disabled", disabledforeground="black")
        winner = check_winner()
        if winner:
            if winner == "Tie":
                messagebox.showinfo("Tic Tac Toe", "It's a Tie!")
            else:
                messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        else:
            player_turn = "O" if player_turn == "X" else "X"
            if player_turn == "O" and not computer_player:
                status_label.config(text="Player O's turn")
            elif player_turn == "X" and computer_player:
                computer_move()

def computer_move():
    # Simple computer move: random empty spot
    empty_spots = [i for i, val in enumerate(board) if val == " "]
    if empty_spots:
        move_index = random.choice(empty_spots)
        make_move(move_index)

def reset_board():
    global player_turn, board
    player_turn = "X"
    board = [" " for _ in range(9)]
    for button in buttons:
        button.config(text=" ", state="active")
    if computer_player:
        computer_move()
    status_label.config(text="Player X's turn")

def toggle_computer():
    global computer_player
    computer_player = not computer_player
    reset_board()

# Create the main window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create buttons for the board
buttons = [tk.Button(root, text=" ", font=('normal', 16), width=5, height=2, command=lambda i=i: make_move(i)) for i in range(9)]
for i, button in enumerate(buttons):
    row = i // 3
    col = i % 3
    button.grid(row=row, column=col)
    button.config(bg="lightgray", activebackground="lightgray")

# Create a status label
status_label = tk.Label(root, text="Player X's turn", font=('normal', 14))
status_label.grid(row=3, column=0, columnspan=3)

# Create a button to toggle playing against the computer
computer_player = False
computer_button = tk.Button(root, text="Play against the computer", command=toggle_computer)
computer_button.grid(row=4, column=0, columnspan=3)

# Start the game
reset_board()

root.mainloop()
