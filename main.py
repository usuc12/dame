import board
from GameHandler import *

board = board.Board(8, 80) 
gameHandler = GameHandler()

def onClick(event):
    gameHandler.select(event, board)

board.canvas.bind("<Button-1>", lambda event: onClick(event))

x = board.get_board()

board.canvas.mainloop()
