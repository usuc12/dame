from board import Board

class GameHandler:
    def __init__(self):
        self.current_player = 1
        self.selected = None
        self.white_count = 0
        self.black_count = 0

    def select(self, event, board):
        board.delete_selected()
        y, x = self.get_cell(event.x, event.y, board)
        self.selected = [x, y]

        b = board.get_board()

        #for i in range(x, 0, -1):                                               #check for all adjacent positions behind the piece \
        #    if x - i >= 0 and y - i >= 0 or x + i <= 7 and y + i <= 7:
        #        #print(x - i, y - i)
        #        all_selected.append([x-i,y-i])
        #for i in range(8 - x):                                                  #check for all adjacent postions before the piece \
        #    if x - i >= 0 and y - i >= 0 or x + i <= 7 and y + i <= 7:
        #        #print(x + i, y + i)
        #        all_selected.append([x+i, y+i])
        #for i in range(x, -1, -1):
        #    if y + i >= 0 and y + i <= 7:
        #        #print(x - i, y + i)
        #        all_selected.append([x-i,y+i])
        #for i in range(1, y + 1):
        #    if x + i >= 0 and x + i <= 7:
        #        #print(x + i, y - i)
        #        all_selected.append([x+i,y-i])
        #
        #for arr in all_selected:
        #    board.draw_selected(arr[0], arr[1])                #vlt später nützzlich

        possible_moves = [[x,y]]

        board_arr = board.get_board()
        
        
        try:
            if board_arr[y][x] != 0:
                
                if board_arr[y-1][x-1] == 0 and board_arr[y][x].get_player1() == True:       #ist frei links oben und ist spieler 1
                    possible_moves.append([x-1, y-1])
                
                if board_arr[y+1][x-1] == 0 and board_arr[y][x].get_player1() == False:
                    possible_moves.append([x-1,y+1])

                if board_arr[y-1][x+1] == 0 and board_arr[y][x].get_player1() == True:       #ist frei rechts oben und ist spieler 1
                    possible_moves.append([x+1, y-1])
                
                if board_arr[y+1][x+1] == 0 and board_arr[y][x].get_player1() == False:
                    possible_moves.append([x+1, y+1])
                
        except: pass

        for coords in possible_moves:
            board.draw_selected(coords[0], coords[1])
        
        
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