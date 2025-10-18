#Grid class to handle the grid of the graph

#possible colors:
class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    ENDC = '\033[0m'
    dictionary = {0:"WHITE", 1:"RED", 2:"GREEN", 3:"YELLOW", 4:"BLUE", 5:"MAGENTA", 6:"CYAN", 7:"WHITE"}

class Grid:
    #for now grid is defined as an matrix of cells with colors represented by integers
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.last_move = None # (x,y,color)
        self.nodes = [[0 for _ in range(width)] for _ in range(height)]

    # give the value/color of the cell x,y
    def set_cell(self, x, y, value): 
        if 0 <= x < self.width and 0 <= y < self.height:
            self.nodes[y][x] = value
            self.last_move = (x, y, value)
        else:
            raise IndexError("Cell position out of bounds")

    # return the value of the cell x,y
    def get_cell(self, x, y): 
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.nodes[y][x]
        else:
            raise IndexError("Cell position out of bounds")


    #check if the gird is a proper coloring
    def as_proper_coloring(self): 
        for y in range(self.height-1):
            for x in range(self.width-1): # we check only the right and down neighbors
                current_color = self.get_cell(x,y)
                right_color = self.get_cell(x+1,y)
                down_color = self.get_cell(x,y+1)
                if ((current_color == right_color) or (current_color == down_color)) and current_color != 0:
                    return False

        return True

    #take as input the coordinates of a cell and return the coordinates of a neighbor with the same color, or True if none
    def same_color_neighbors(self, x, y):
        for y in range(self.height-1):
            for x in range(self.width-1): # we check only the right and down neighbors
                current_color = self.get_cell(x,y)
                right_color = self.get_cell(x+1,y)
                down_color = self.get_cell(x,y+1)
                if current_color == 0:
                    return (-1,-1)
                if (current_color == right_color):
                    return (x+1, y)
                if (current_color == down_color):
                    return (x, y+1)

        return True

    #undo the last move on the grid (only one for now)
    def undo_last_move(self):
        if self.last_move:
            x, y, _ = self.last_move
            self.set_cell(x, y, 0)
            self.last_move = None
        else:
            print("No move to undo")

    #print the grid in terminal with colors
    def print_terminal(self):
        for row in self.nodes:
            for cell in row:
                color = Color.dictionary.get(cell)
                print(f"{Color.__dict__[color]}⬤{Color.ENDC}", end=' ')
            print()

