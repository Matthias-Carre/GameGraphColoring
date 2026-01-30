import tkinter as tk
from tkinter import Toplevel, simpledialog

global root
#create button to choses between soloCustom, 3n, 4n grid
def start_solo_custom():
    import main_graphic
    main_graphic.main()

def treenGrid():
    import size3n
    size3n.main(root)

def fournGrid():
    import size4n
    size4n.main(root)


def start_pvp():
    


    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)
    tk.Label(main_frame, text="Largeur de la grille:").pack(pady=5)
    width_entry = tk.Entry(main_frame)
    width_entry.pack(pady=5)

    tk.Label(main_frame, text="Hauteur de la grille:").pack(pady=5)
    height_entry = tk.Entry(main_frame)
    height_entry.pack(pady=5)

    tk.Button(main_frame, text="Valider", command=submit).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Lunch Menu")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)

    tk.Label(root, text="Choose your lunch option:").pack(pady=10)

    tk.Button(root, text="Solo Custom Grid", command=start_pvp).pack(pady=5)
    tk.Button(root, text="3n Grid", command=treenGrid).pack(pady=5)
    tk.Button(root, text="4n Grid", command=fournGrid).pack(pady=5)

    root.mainloop()