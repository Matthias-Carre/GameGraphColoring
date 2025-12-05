import tkinter as tk
import graphic.Draw as Draw
from game.Engine import GameEngine

def start_pvp():
    return

def treenGrid():
    return

def fournGrid():
    return

def main():
    root = tk.Tk()
    root.title("Lunch Menu")

    main_frame = tk.Frame(root)
    main_frame.pack(padx=20, pady=20)

    tk.Label(root, text="Choose your lunch option:").pack(pady=10)

    tk.Button(root, text="Solo Custom Grid", command=start_pvp).pack(pady=5)
    tk.Button(root, text="3n Grid", command=treenGrid).pack(pady=5)
    tk.Button(root, text="4n Grid", command=fournGrid).pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()