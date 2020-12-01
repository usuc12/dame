class Figur:
    def __init__(self,player,coords):
        self.Dame = False
        self.player1 = player
        self.coords = coords

    def get_D(self): return self.Dame
    def set_D(self,Dame): self.Dame = Dame
    def get_coords(self): return self.coords
    def set_coords(self,c): self.coords = coords
    def get_player1(self): return self.player1
