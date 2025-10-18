from Grid import Grid

#ask the user for the size of the grid

def create_grid():
    height = int(input("Grid height: "))
    width = int(input("Grid width: "))

    grid = Grid(width, height)
    return grid
    
# return (x,y,color)
def turn_input(grid): 
    print(f'Enter x (between 1 and {grid.width})')
    x = int(input("x: "))-1
    print(f'Enter y (between 1 and {grid.height})')
    y = int(input("y: "))-1
    print(f'color (between 1 and 7)')
    color = int(input("color: "))

    return (x,y,color)
    #to do : check values and limits the number of colors

#game logic with turn and node/color
def play():
    grid = create_grid()
    grid.print_terminal()
    alice_turn = True # False = Bob, True = Alice

    while grid.as_proper_coloring():
        if alice_turn:
            print("Alice's turn")
        else:
            print("Bob's turn")
        (x,y,color) = turn_input(grid)
        grid.set_cell(x, y, color)
        grid.print_terminal()
        alice_turn = not alice_turn

if __name__ == "__main__":
    play()
