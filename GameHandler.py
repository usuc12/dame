from board import Board

class GameHandler:
    def __init__(self):
        self.current_player = 1
        self.selected = None
        self.white_count = 0
        self.black_count = 0

    def select(self, event, board):
        y, x = self.get_cell(event.x, event.y, board)
        self.selected = [x, y]

        board.draw_selected(x, y)

        for i in range(8 - x):
            newY, newX = self.get_cell(x + i, y + i, board)
            self.newSelected = [newX, newY]

        board.draw_selected(newX, newY)

    def controls(): return  

    def get_cell(self,x,y, board, cell=None):
        u = board.get_u()
        for i in range(board.get_n()):
            for j in range(board.get_n()):
                if x>=j+u*j and y>=i+u*i and x<=j+u*(j+1) and y<=i+u*(i+1):
                    cell = [i,j]
                    break
        return cell if cell else [-1,-1]

    def draw_diff(self): return


    def check_moves(self): return