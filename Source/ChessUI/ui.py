from tkinter import *
from tkinter import ttk
import os
import sys
import logging

# Unicodes for the pieces
pieces = [
    # White
    '\u2654',  # King ♔ 0
    '\u2655',  # Queen ♕ 1
    '\u2656',  # Rook ♖ 2
    '\u2657',  # Bishop ♗ 3
    '\u2658',  # Knight ♘ 4
    '\u2659',  # Pawn ♙ 5

    # Black
    '\u265A',  # King ♚ 6
    '\u265B',  # Queen ♛ 7
    '\u265C',  # Rook ♜ 8
    '\u265D',  # Bishop ♝ 9
    '\u265E',  # Knight ♞ 10
    '\u265F',  # Pawn ♟ 11
    
    # Empty String
    '' #12
]

# Initial Config
board_config = [
    [2, 4, 3, 0, 1, 3, 4, 2],
    [5]*8,
    [12]*8,
    [12]*8,
    [12]*8,
    [12]*8,
    [11]*8,
    [8, 10, 9, 6, 7, 9, 10, 8],
] 

class ChessUI:
    def __init__(self):
        logging.info("UI Constructor")
        self.create_board()
    
    def create_board(self):
        self.root = Tk()
        self.root.config(background='#1e1e1e')
        self.big_frame = ttk.Frame(self.root)
        self.big_frame.pack()
        #create the 64 tiles
        self.tiles = [[] for i in range(8)]
        for i in range(8):
            for j in range(8):
                tile = Label(self.big_frame, 
                                 background= '#2bc24b' if (i+j)%2 else '#daf095', 
                                 text='\u265E', 
                                 font=('Arial', 25), 
                                 #foreground='White', 
                                 width=6,
                                 height=3,
                                 relief='solid')
                tile.grid(row=i, column=j)
                self.tiles[i].append(tile)
        self.update_config(self.tiles, board_config)
        self.root.mainloop()
    
    def update_config(self, tiles, config):
        for i in range(8):
            for j in range(8):
                tiles[i][j].config(text = pieces[config[i][j]])