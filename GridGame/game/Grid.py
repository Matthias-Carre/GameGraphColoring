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
        self.last_moves = [] # (x,y,color)
        self.nodes = [[Cell(x, y, self.width, self.height,num_colors=num_colors) for y in range(width)] for x in range(height)]
        self.num_colors = num_colors
        self.blocks = []
        self.player = 0 #0 for Alice, 1 for Bob
        self.round = 1
        self.last_Bob_move = None # (x,y,color,past_config)        

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
        for neighbor in self.nodes[y][x].neighbors:
            if neighbor.value == value:
                return False

        if 0 <= x < self.width and 0 <= y < self.height:
            if value in self.nodes[y][x].color_options:
                if self.nodes[y][x].value == 0:
                    return True
        return False

    def get_col(self, col_index):
        if 0 <= col_index < self.width:
            return [self.nodes[row][col_index] for row in range(self.height)]
        else:
            raise IndexError("Column index out of bounds")

    def play_move(self,x,y,color):
        if not(self.is_move_valid(x,y,color)):
            print(f"Invalid move at ({x}, {y}) with color {color} by player {self.player}")
            return False
        
        
        
        self.nodes[y][x].value = color
        self.nodes[y][x].played_by = self.player
        self.nodes[y][x].round = self.round
        self.last_moves.append((x,y,color))

        self.update_neighbors(x,y,color)


    def update_neighbors(self,x,y,color):
        cell = self.nodes[y][x]
        for neighbor in cell.neighbors:
            if color in neighbor.color_options:
                neighbor.color_options.remove(color)
            neighbor.neighbors_to_color -= 1
            neighbor.update_cell()
            
    
    def roll_back_neighbors(self,x,y,color):
        cell = self.nodes[y][x]
        for neighbor in cell.neighbors:
            color_is_posible = True #check if we can restore the color option
            for neighbor2 in neighbor.neighbors:
                print(f"voisin2 value: {neighbor2.value}, color: {color}")
                if neighbor2.value == color:
                    color_is_posible = False
                    break
                
            if color_is_posible:
                neighbor.color_options.append(color)
            neighbor.neighbors_to_color += 1
            neighbor.update_cell()
            
            
    def get_cell(self, x, y): 
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.nodes[y][x]
        else:
            raise IndexError("Cell position out of bounds")
    
    #undo need to blank the last move, and restore the color options of the neighbors
    def undo_move(self):
        print("Undo:",self.last_moves[-1])
        if self.last_moves != []:
            x,y,color = self.last_moves.pop()
            self.nodes[y][x].value=0
            self.nodes[y][x].played_by = ""
            self.nodes[y][x].round = None
            #restore the color options of the neighbors
            self.roll_back_neighbors(x,y,color)
            return True
        return False
            
            
    