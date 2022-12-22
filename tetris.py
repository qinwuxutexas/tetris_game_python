#!/usr/bin/env python

from tetrislib import *

prepare_terminal()

# This example code draws a T-shaped piece.
row = 2
board[row][5] = 1
board[row][6] = 1
board[row][7] = 1
board[row+1][6] = 1

draw_board()

# This code waits for input until the user hits a keystroke.
# get_input() returns one of "left", "up", "right", "down", "exit", or None
# (for all other keys).
while True:
    key = get_input()
    if key == "exit":
        break
    print(key)

