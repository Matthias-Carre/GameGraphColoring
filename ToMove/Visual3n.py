import tkinter as tk
class Visual:
    def __init__(self, width, height, grid,root,canvas):
        self.width = width
        self.height = height
        self.grid = grid
        self.canvas = canvas
        self.colors = ["Red", "Green", "Blue"]
        self.color_selected = -1 # given by the radio button
        self.root = root
        self.turn = 0 #0 for Alice, 1 for Bob

    def draw_text(self, x, y, text, color="black", font=("Arial", 12)):
        self.canvas.create_text(x, y, text=text, fill=color, font=font)

    #draw rectangle form x,y to x+width,y+height
    def draw_rectangle(self, x, y, width, height, color):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")

    #draw circle centered in x,y with radius
    def draw_circle(self, x, y, radius, color):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")
        self.canvas.create_oval(x - radius/1.5, y - radius/1.5, x + radius/1.5, y + radius/1.5, fill="white", outline="")

    #management of undo button
    def undo_last_move(self):
        self.grid.undo_last_move()
        self.draw_grid()

    #management of bob play button
    def bob_play(self):
        if self.turn == 0:
            print("It's Alice's turn!")
            return

        self.turn = 0
        critical_cells = self.grid.get_critical_cells()

        if critical_cells:
            cell = critical_cells[0]
            uncolored_neighbors = self.grid.get_uncolored_neighbor(cell)

            self.grid.play_cell(uncolored_neighbors.y, uncolored_neighbors.x, cell.color_options[0], player="B")
            self.draw_grid()

            return
        
        #check Alice last move (logic for 3xn grid)
        if self.grid.last_move:
            last_x, last_y, last_color = self.grid.last_move[-1]

            if last_y == 1:
                if(self.grid.get_cell(last_x + 1, last_y + 1).get_value() == 0):
                    self.grid.play_cell(last_x + 1 , last_y+1,last_color + 1, player="B")
                    print(f"Bob plays at: {last_x + 1}, {last_y + 1}")
                elif(self.grid.get_cell(last_x - 1, last_y + 1).get_value() == 0):
                    self.grid.play_cell(last_x - 1 , last_y+1,last_color + 1, player="B")
                    print(f"Bob plays at: {last_x - 1}, {last_y + 1}")

                self.draw_grid()
                return 
            if(last_y == 0):
                self.grid.play_cell(last_x + 1 , last_y+2,last_color, player="B")
                print(f"Bob plays at: {last_x + 1}, {last_y + 2}")
            #last_y == 2
            else:
                self.grid.play_cell(last_x + 1 , last_y-2,last_color, player="B")
                print(f"Bob plays at: {last_x + 1}, {last_y - 2}")
            self.draw_grid()


        
        return


            

    def change_node_color(self, grid, x, y, color):
        self.turn = 1
        self.grid.play_cell(x, y, color, player="A")
        self.draw_grid()

    def on_button_click(self,event):
        x = event.x
        y = event.y
        ratio = min(800 / self.grid.width, 800 / self.grid.height)
        i = int(x // ratio)
        j = int(y // ratio)

        #form bob we wait button click
        if(self.turn == 1):
            print("It's Bob's turn!")
            return

        if (0 <= i) and (i < self.grid.width) and (0 <= j) and (j < self.grid.height) and (self.color_selected.get() != -1):
            print(f'Button clicked at: {i}, {j},')
            if (self.grid.get_cell(i, j).get_value() == 0):
                self.change_node_color(self.grid, i, j, self.color_selected.get() + 1)
                self.draw_grid()

    def draw_color_selection(self):
        for i, color in enumerate(self.colors):
            tk.Radiobutton(self.root, text=color, value=i, variable=self.color_selected, fg=color).pack(anchor="w")
        tk.Button(self.root, text="Undo Last Move", command=self.undo_last_move).pack()
        tk.Button(self.root, text="Bob Play", command=self.bob_play).pack()

    def draw_grid(self):
        ratio = min(800 / self.grid.width, 800 / self.grid.height)
        for i in range(self.grid.width):
            for j in range(self.grid.height):
                x = i * ratio
                y = j * ratio
                cell = self.grid.get_cell(i, j)
                self.draw_circle(x + ratio / 2, y + ratio / 2, ratio / 2 - 5, self.colors[cell.get_value() - 1] if cell.get_value() > 0 else "black")
                player=cell.get_player()
                if(cell.is_uncolorable):
                    self.draw_text(x + ratio / 2, y + ratio / 2, "X", color="red", font=("Arial", 16))
                else:
                    self.draw_text(x + ratio / 2, y + ratio / 2, player, color="black", font=("Arial", 16))
                
                
    def draw_window(self):

        #creation of the canvas and button/color selection
        self.color_selected = tk.IntVar(value=-1)
        self.canvas.pack()
        self.draw_grid()
        self.draw_color_selection()
