class GameEngine:
    def __init__(self,grid,Alice,Bob):
        self.grid = grid
        self.state = GameState(grid)
        self.Alice = Alice
        self.Bob = Bob

    def run(self):
        