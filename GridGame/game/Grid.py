#Grid class to handle the grid of the graph

from game.Cell import Cell
#from game.Block import Block

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
    def __init__(self, height, width, num_colors=4):
        self.width = width
        self.height = height
        self.last_move = [] # (x,y,color)
        self.nodes = [[Cell(x, y, self.width, self.height,num_colors=num_colors) for y in range(width)] for x in range(height)]
        self.num_colors = num_colors
        self.blocks = []

        #add neighbors to each cell
        for i in range(self.width):
            for j in range(self.height):
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    #check if we hit a border
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.nodes[j][i].neighbors.append(self.nodes[ny][nx])
                self.nodes[j][i].update_cell()

    def is_move_valid(self, x, y, value):
        if 0 <= x < self.width and 0 <= y < self.height:
            if value in self.nodes[y][x].color_options:
                if self.nodes[y][x].value == 0:
                    return True
        return False

    def play_move(self,x,y,color,player):
        if not(self.is_move_valid(x,y,color)):
            print(f"Invalid move at ({x}, {y}) with color {color} by player {player}")
            return False
        
        self.nodes[y][x].value = color
        self.nodes[y][x].played_by = player
        self.last_move = (x,y,color)

    def update_neighbors(self,x,y,color):
        cell = self.nodes[y][x]
        for neighbor in cell.neighbors:
            if color in neighbor.color_options:
                neighbor.color_options.remove(color)
            neighbor.update_cell()
            
    def get_cell(self, x, y): 
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.nodes[y][x]
        else:
            raise IndexError("Cell position out of bounds")
    