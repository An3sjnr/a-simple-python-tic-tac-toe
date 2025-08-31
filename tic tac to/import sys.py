import sys
import os
import time
# Tic Tac To in Python (no gui)
board = [" " for _ in range(9)]

#  all winning combinations 
WIN_COMBINATIONS = [
    (0, 1, 2),  # top row
    (3, 4, 5),  # middle row
    (6, 7, 8),  # bottom row
    (0, 3, 6),  # left column
    (1, 4, 7),  # middle column
    (2, 5, 8),  # right column
    (0, 4, 8),  # diagonal top-left to bottom-right
    (2, 4, 6)   # diagonal top-right to bottom-left
]
def display_board ():
    os.system('cls')
   # sys.stdout.flush
    sys.stdout.write(f" {board[0]} | {board[1]} | {board[2]} \n --+---+-- \n {board[3]} | {board[4]} | {board[5]} \n --+---+-- \n {board[6]} | {board[7]} | {board[8]} \n")


def check_winner(player):
    for a, b, c in WIN_COMBINATIONS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def play_game():
    current_player = "X"
    for turn in range(9):
        display_board()
        move = int(input(f"Player {current_player}, choose a spot (0-8): "))
        if board[move] != " ":
            print("That spot is taken! Try again.")
            time.sleep(1)
            continue
        board[move] = current_player
        
        if check_winner(current_player):
            display_board()
            print(f" Player {current_player} wins!")
            return
        current_player = "O" if current_player == "X" else "X"
    
    display_board()
    print("It's a tie!")

play_game()

