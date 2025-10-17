import tkinter as tk
from Grid import Grid

colors = ["Red", "Green", "Blue", "purple"]
color_selected = -1 # given by the radio button

def on_button_click(event):
    x = event.x
    y = event.y
    ratio = min(800 / grid.width, 800 / grid.height)
    i = int(x // ratio)
    j = int(y // ratio)
    
    if (0 <= i) and (i < grid.width) and (0 <= j) and (j < grid.height) and (color_selected.get() != -1):
        print(f'Button clicked at: {i}, {j}') 
        if (grid.get_cell(i, j) == 0):
            change_node_color(grid, i, j, color_selected.get() + 1)
            draw_grid(grid)


def draw_rectangle(x, y, width, height, color):#draw rectangle form x,y to x+width,y+height
    canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")

def draw_circle(x, y, radius, color):#draw circle centered in x,y with radius
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")
    canvas.create_oval(x - radius/1.5, y - radius/1.5, x + radius/1.5, y + radius/1.5, fill="white", outline="")

def undo_last_move():
    grid.undo_last_move()
    draw_grid(grid)

def change_node_color(grid, x, y, color):
    grid.set_cell(x, y, color)


def draw_grid(grid):#draw the grid with circles of colors of the nodes
    ratio = min(800 / grid.width, 800 / grid.height)

    for i in range(grid.width):
        for j in range(grid.height):
            x = i * ratio
            y = j * ratio
            color = grid.get_cell(i, j)
            draw_circle(x + ratio / 2, y + ratio / 2, ratio / 2 - 5, colors[color - 1] if color > 0 else "black")

def draw_color_selection():
    for i, color in enumerate(colors):
        tk.Radiobutton(root, text=color, value=i,variable=color_selected, fg=color).pack(anchor="w")
    tk.Button(root, text="Undo Last Move", command=undo_last_move).pack()


if __name__=="__main__":

    grid = Grid(5, 5)


    root = tk.Tk()
    root.title("Graph Coloring Game")
    
    #set the window size to match the gird of the graph
    ratio = min(800 / grid.width, 800 / grid.height)
    w = ratio * grid.width
    h = ratio * grid.height
    root.geometry(f'{int(w)}x{int(h)+150}')
    canvas = tk.Canvas(root, width=w, height=h, bg="white")

    canvas.bind("<Button-1>", on_button_click)
    color_selected = tk.IntVar(value=-1)  
    
    canvas.pack()
    
    draw_grid(grid)
    draw_color_selection()

    root.mainloop()