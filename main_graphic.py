import tkinter as tk
from Grid import Grid

colors = ["Red", "Green", "Blue", "purple"]
color_selected = -1

def on_button_click(event):
    #we get the name of the button clicked
    x = event.x
    y = event.y
    ratio = min(800 / grid.width, 800 / grid.height)
    i = int(x // ratio)
    j = int(y // ratio)
    if 0 <= i < grid.width and 0 <= j < grid.height and color_selected.get() != -1:
        change_node_color(grid, i, j, color_selected.get() + 1)
        draw_grid(grid)


def draw_rectangle(x, y, width, height, color):#draw rectangle form x,y to x+width,y+height
    canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline="")

def draw_circle(x, y, radius, color):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline="")
    canvas.create_oval(x - radius/1.5, y - radius/1.5, x + radius/1.5, y + radius/1.5, fill="white", outline="")

def change_node_color(grid, x, y, color):
    grid.set_cell(x, y, color)


def draw_grid(grid):
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


def update_display():
    canvas.delete("all")
    root.after(100, update_display)  # Schedule the next update in 100 ms



if __name__=="__main__":
    root = tk.Tk()
    root.title("Graph Coloring Game")
    root.geometry("1200x1000")
    root.bind("<Button-1>", on_button_click)

    canvas = tk.Canvas(root, width=800, height=800, bg="white")
    color_selected = tk.IntVar(value=-1)  
    
    canvas.pack()
    grid = Grid(10, 5)
    draw_grid(grid)
    draw_color_selection()

    root.mainloop()