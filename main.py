import board
from GameHandler import *

board = board.Board(8, 80) 
gameHandler = GameHandler()

board.canvas.bind("<Button-1>", lambda event: gameHandler.select(event, board))

x = board.get_board()

board.canvas.mainloop()
