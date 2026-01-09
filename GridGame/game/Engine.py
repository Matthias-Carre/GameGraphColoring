from game.GameState import GameState
from graphic.Interface import Interface


class GameEngine:
    def __init__(self,grid,root,Alice=None,Bob=None):
        self.window_width = 800
        self.window_height = 800
        self.grid = grid
        self.root = root
        self.state = GameState(grid)
        self.Alice = Alice
        self.Bob = Bob
        self.on_click = self.on_click
        self.color_selected = 1
        self.on_update_callback = None
        self.buttons={}
        self.window = Interface(root,self)

    def button_test():
        print("Test")

    def run(self):
        self.window.create_window()
        print("Engine")
        self.window.draw_button("Undo",self.undo)

        
        """
        current_player = self.Alice
        move = current_player.get_move()
        if move is not None:
            x, y, color = move
            self.grid.play_cell(x, y, color, player=current_player.name)
            # Switch to the other player
            current_player = self.Bob if current_player == self.Alice else self.Alice
        """

        self.root.mainloop()

    def on_click(self,event):
        
        print("click",event)
        x = event.x
        y = event.y
        ratio = min(self.window_width / self.grid.width, self.window_height / self.grid.height)
        i = int(x // ratio)
        j = int(y // ratio)

        if hasattr(self, 'color_var_accessor'):
            self.color_selected = self.color_var_accessor.get()
            print("color selected:", self.color_selected)

        if (0 <= i) and (i < self.grid.width) and (0 <= j) and (j < self.grid.height) and (self.color_selected != -1):
            print(f'Button clicked at: {i}, {j}, color: {self.color_selected}')
            if not(self.is_move_valid(i, j, self.color_selected + 1)):
                print("Invalid move")
                return
            
            if (self.grid.get_cell(i, j).get_value() == 0):
                self.change_node_color(self.grid, i, j, self.color_selected + 1)
                self.on_update_callback()
                if self.grid.player == 1:
                    self.grid.round += 1
                self.grid.player = 0 if self.grid.player == 1 else 1
                

    def undo(self):
        print("Undo last move")
        if(self.grid.undo_move()):
            self.on_update_callback()
            if self.grid.player == 0:
                self.grid.round -= 1
            self.grid.player = 0 if self.grid.player == 1 else 1
        return

    def change_node_color(self,grid, x, y, color):
        grid.play_move(x, y, color)
        return
    
    def draw_grid(self):
        self.window.draw_grid()


    def is_move_valid(self,x,y,color):
        return self.grid.is_move_valid(x,y,color)
    