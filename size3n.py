from Grid import Grid
import tkinter as tk
from Visual import Visual

as_played = False
visu=None

def on_button_click(event):
    visu.on_button_click(event)
    root.update()
    print("After Alice's move")
    #test Bob move:
    grid.play_cell(1, 1, 1, player="B")
    visu.draw_grid()
    root.update()


def bob_turns(grid):
    print("Bob turns")
    grid.set_cell(1, 1, 1)

if __name__ == "__main__":
    grid = Grid(3, 10)
    root = tk.Tk()
    root.title("Graph Coloring Game")

    #set the window size to match the gird of the graph
    ratio = min(800 / grid.width, 800 / grid.height)
    w = ratio * grid.width
    h = ratio * grid.height
    root.geometry(f'{int(w)}x{int(h)+150}')
    canvas = tk.Canvas(root, width=w, height=h, bg="white")

    #creation of the canvas and button/color selection
    canvas.bind("<Button-1>", on_button_click)

    playing = True
    visu = Visual(800, 800, grid,root,canvas)
    visu.draw_window()
    
    root.mainloop()


