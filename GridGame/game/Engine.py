from game.Game_state import GameState


class GameEngine:
    def __init__(self,grid,Alice=None,Bob=None):
        self.window_width = 800
        self.window_height = 800
        self.grid = grid
        self.state = GameState(grid)
        self.Alice = Alice
        self.Bob = Bob
        self.on_click = self.on_click
        self.color_selected = 1

    def run(self):
        current_player = self.Alice
        move = current_player.get_move()
        if move is not None:
            x, y, color = move
            self.grid.play_cell(x, y, color, player=current_player.name)
            # Switch to the other player
            current_player = self.Bob if current_player == self.Alice else self.Alice


    def on_click(self,event):
        
        print("click",event)
        x = event.x
        y = event.y
        ratio = min(self.window_width / self.grid.width, self.window_height / self.grid.height)
        i = int(x // ratio)
        j = int(y // ratio)


        if (0 <= i) and (i < self.grid.width) and (0 <= j) and (j < self.grid.height) and (self.color_selected != -1):
            print(f'Button clicked at: {i}, {j},')
            if (self.grid.get_cell(i, j).get_value() == 0):
                
                self.change_node_color(self.grid, i, j, self.color_selected + 1)
                self.draw_grid()