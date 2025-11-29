from Grid import Grid
import tkinter as tk
from Visual4n import Visual

as_played = False
visu=None

def on_button_click(event):
    visu.on_button_click(event)
    root.update()


def bob_turns(grid):
    print("Bob turns")
    grid.set_cell(1, 1, 1)

def main(r):
    global grid, root, canvas, visu
    grid = Grid(4, 12, num_colors=4)
    root = r
    for widget in root.winfo_children():
        widget.destroy()
    root.title("Graph Coloring Game")

    window_size = 1800
    #set the window size to match the gird of the graph
    ratio = min(window_size / grid.width, window_size / grid.height)
    w = ratio * grid.width
    h = ratio * grid.height
    root.geometry(f'{int(w)}x{int(h)+150}')
    canvas = tk.Canvas(root, width=w, height=h, bg="white")

    #creation of the canvas and button/color selection
    canvas.bind("<Button-1>", on_button_click)

    playing = True
    visu = Visual(window_size, window_size, grid,root,canvas)
    visu.draw_window()
    
    root.mainloop()


if __name__ == "__main__":
    grid = Grid(4, 12, num_colors=4)
    root = tk.Tk()
    root.title("Graph Coloring Game")

    window_size = 1800
    #set the window size to match the gird of the graph
    ratio = min(window_size / grid.width, window_size / grid.height)
    w = ratio * grid.width
    h = ratio * grid.height
    root.geometry(f'{int(w)}x{int(h)+150}')
    canvas = tk.Canvas(root, width=w, height=h, bg="white")

    #creation of the canvas and button/color selection
    canvas.bind("<Button-1>", on_button_click)

    playing = True
    visu = Visual(window_size, window_size, grid,root,canvas)
    visu.draw_window()
    
    root.mainloop()


