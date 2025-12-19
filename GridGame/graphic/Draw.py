import tkinter as tk
from game.Engine import GameEngine

class Draw:
    def __init__(self, width, height, grid,root,canvas):
        self.width = width
        self.height = height
        self.grid = grid
        self.canvas = canvas
        self.colors = ["Red", "Green", "Blue","Purple"]
        self.color_selected = -1 # given by the radio button
        self.root = root
        self.turn = 0 #0 for Alice, 1 for Bob
        self.print_status = True

    def draw_text(self, x, y, text, color="black", font=("Arial", 12)):
        self.canvas.create_text(x, y, text=text, fill=color, font=font)

    #draw rectangle form x,y to x+width,y+height
    def draw_rectangle(self, x, y, width, height, color):
        self.canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")

    #draw circle centered in x,y with radius
    def draw_circle(self, x, y, radius, color):
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")
        self.canvas.create_oval(x - radius/1.5, y - radius/1.5, x + radius/1.5, y + radius/1.5, fill="white", outline="")

    def undo_last_move():
        return

    def bob_play():
        return
    
    def test_print(self):
        #print("color selected:", self.color_selected.get())
        return

    #draw the color selection radio buttons
    def draw_color_selection(self):

        color_frame = tk.Frame(self.root)
        color_frame.pack(anchor="w")
        

        radio_frame = tk.Frame(color_frame)
        radio_frame.pack(side="left")
        
        #color Slecetion
        for i, color in enumerate(self.colors):
            tk.Radiobutton(radio_frame, text=color, value=i, variable=self.color_selected, fg=color).pack(anchor="w")
        
        button_frame = tk.Frame(color_frame)
        button_frame.pack(side="left", padx=10)
        
        tk.Button(button_frame, text="random move", command=self.test_print).pack()
        
        # Other buttons below
        tk.Button(self.root, text="Undo Last Move", command=self.undo_last_move).pack()
        tk.Button(self.root, text="Bob Play", command=self.bob_play).pack()
        tk.Button(self.root, text="Test Print", command=self.test_print).pack()

    #draw the grid on the canvas
    def draw_grid(self):
        ratio = min(self.width / self.grid.width, self.height / self.grid.height)
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
                if(self.print_status):
                    self.draw_text(x + ratio / 2, y + ratio / 2 + 10, cell.get_status(), color="blue", font=("Arial", 8))

           
    def draw_window(self):

        #creation of the canvas and button/color selection
        self.color_selected = tk.IntVar(value=0)
        self.canvas.pack()
        self.draw_grid()
        self.draw_color_selection()
        
