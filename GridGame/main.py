import tkinter as tk
from game.Grid import Grid
from graphic.Draw import Draw
from game.Engine import GameEngine
from graphic.Interface import Interface


def on_button_click(event):
    return

def create_game(root,width=9, height=9):
    grid = Grid(width, height, num_colors=4)

    engine = GameEngine(grid,root)
    #window = Interface(root,engine)
    #engine.window = window
    
    
    print("Game created with grid size:", width, "x", height)
    engine.run()




def main():
    root = tk.Tk()
    root.title("Lunch Menu")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)

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

    def submit():
        width = int(width_entry.get())
        height = int(height_entry.get())
        print(f"lunch with width: {width}, height: {height}")
        create_game(root,width, height)

    tk.Button(main_frame, text="Valider", command=submit).pack(pady=10)

    tk.mainloop()

if __name__ == "__main__":
    #selection menu
    #main()

    #pour les test passer direcetement a la grille
    create_game(tk.Tk())