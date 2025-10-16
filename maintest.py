import Grid
from PrintTerminal import PrintTerminal, Color

grid = Grid.Grid(5, 5)
grid.set_cell(0, 0, 1)

if __name__ == "__main__":
    PrintTerminal().print_terminal(grid)
    print(grid.as_proper_coloring())
    grid.set_cell(1, 0, 1)
    PrintTerminal().print_terminal(grid)
    print(grid.as_proper_coloring())
    