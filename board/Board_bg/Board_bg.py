import tkinter as tk

class Figur:
    def __init__(self,player1,coords):
        self.dame = False
        self.coords = coords
        self.player1 = player1
    def get_d(self): return self.dame
    def set_d(self,dame): self.dame = dame
    def get_coords(self): return self.coords
    def set_coords(self,coords): self.coords = coords
    def get_player1(self): return self.player1

class Board:
    def __init__(self,n,u):
        self.n,self.u,self.board,self.s = n,u,[[0]*n for i in range(n)],[]
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window,width=n+n*u,height=n+n*u,bg="#f3f3f3",highlightthickness=0,cursor="hand1")
        self.canvas.pack()
        img = tk.PhotoImage(file="bg.png").subsample(2)
        self.canvas.create_image(0,0,image=img,anchor=tk.NW)
        for i in range(n):
            for j in range(n):
                if (i+j)%2==1:
                    if i<(n/2-1): self.board[i][j] = Figur(False,[i,j])
                    if i>(n/2): self.board[i][j] = Figur(True,[i,j])
        self.draw_board()
        self.canvas.mainloop()

    def draw_board(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j]: self.canvas.create_oval(j+self.u*j,i+self.u*i,j+self.u*(j+1),i+self.u*(i+1),fill="#333D79" if self.board[i][j].get_player1() else "#A13941",outline="#333D79" if self.board[i][j].get_player1() else "#A13941")

x = Board(8,80)