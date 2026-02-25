import tkinter as tk
from graphic.Draw import Draw

class Interface:
    def __init__(self,root,engine):
        self.root = root
        self.engine = engine
        self.grid = engine.grid
        self.canvas = None
        self.on_click = engine.on_click
        self.draw = None
        self.selected_color = engine.color_selected
        engine.on_update_callback = self.draw_grid
        


    
    def create_window(self):
        #remove previous widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        window_height = self.engine.window_height 
        window_width = self.engine.window_width

        if(window_height / window_width > self.grid.height/self.grid.width):
            ratio = window_width / self.grid.width
            
        else:
            ratio = window_height / self.grid.height
            

        #set the window size to match the gird of the graph
        #ratio = min(window_width / self.grid.width, window_height / self.grid.height)
        w = ratio * self.grid.width
        h = ratio * self.grid.height
        print(f"h={h}, ratio={ratio}, grid height={self.grid.height}, window height={window_height}")
        self.root.geometry(f'{int(w)}x{int(h)+250}')

        print(f"Window size: {int(w)}x{int(h)}, ratio: {ratio}")
        canvas = tk.Canvas(self.root, width=w, height=h, bg="white")
        self.canvas = canvas

        draw = Draw( window_width,window_height, self.grid,self.root,canvas)
        self.draw = draw

        draw.draw_window()
        self.draw_grid()
        #creation of the canvas and button/color selection
        canvas.bind("<Button-1>", self.on_click)
        self.engine.color_var_accessor = draw.color_selected

        self.draw_buttons()

        playing = True
        


    def get_draw(self):
        return self.draw
    
    #draw the grid
    def draw_grid(self):
        self.draw.draw_grid()
    
    #create and draw a button with text and command
    def draw_button(self, text, command):
        print("DrawButtonInterface")
        self.draw.draw_button(text, command)
        self.root.update()
    
    #draw all buttons needed for the game interface
    def draw_buttons(self):
        #self.draw_button("test",self.test_print())
        return 

    def test_print(self,msg=""):
        print("InterTestPrint:",msg)