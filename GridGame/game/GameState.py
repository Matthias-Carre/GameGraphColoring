class GameState:
    def __init__(self, grid):
        self.grid = grid
        self.current_player = "A"  # "A" for Alice, "B" for Bob
        self.current_color = 0 
        self.grid_type = 0