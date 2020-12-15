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