

class Alice:
    def __init__(self,grid):
        self.grid = grid

    def next_move(self):
        if self.grid.player != 0:
            print("Not Alice's turn")
            return None
        print("Alice move")