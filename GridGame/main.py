import tkinter as tk
from game.Grid import Grid
from graphic.Draw import Draw
from game.Engine import GameEngine
from graphic.Interface import Interface
from game.Bob.bob import Bob
from game.Alice.alice import Alice


def on_button_click(event):
    return


def create_game(root,width=15, height=4,num_colors=4):
    #grid = Grid(width, height, num_colors=4)
    
    #for the cas of the paper
    #grid = Grid(3,16,4)
    grid = Grid(height, width, num_colors)

    engine = GameEngine(grid,root,Alice=Alice(grid),Bob=Bob(grid))
  
    
    print("Game created with grid size:", width, "x", height)
    engine.run()




def main():
    # Create the main window
    root = tk.Tk()
    root.title("Lunch Menu")
    
    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)

    # parameters selection
    tk.Label(root, text="Choose your lunch option:").pack(pady=10)

    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)
    tk.Label(main_frame, text="Largeur de la grille:").pack(pady=5)
    width_entry = tk.Entry(main_frame)
    width_entry.pack(pady=5)

    tk.Label(main_frame, text="Hauteur de la grille:").pack(pady=5)
    height_entry = tk.Entry(main_frame)
    height_entry.pack(pady=5)

    tk.Label(main_frame, text="Nombre de couleurs").pack(pady=5)
    color_entry = tk.Entry(main_frame)
    color_entry.pack(pady=5)

    # Submit button
    def submit():
        width = int(width_entry.get())
        height = int(height_entry.get())
        num_colors = int(color_entry.get())
        print(f"lunch with width: {width}, height: {height}")
        create_game(root,width, height, num_colors)

    tk.Button(main_frame, text="Valider", command=submit).pack(pady=10)

    tk.mainloop()

if __name__ == "__main__":
    #selection des parametres
    #main()

    #Commenter au dessus et decommenter en dessous pour passer la selection des parametres
    create_game(tk.Tk(),width=5, height=5, num_colors=4)