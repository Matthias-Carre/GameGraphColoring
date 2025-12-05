#Grid class to handle the grid of the graph

from Cell import Cell
from Block import Block

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
                return True
        return False

    def set_cell(self, x, y, value): 

        print(f"Lastmove: {self.last_move}")
        if 0 <= x < self.width and 0 <= y < self.height:
            self.nodes[y][x].set_value(value)
            if value != 0:
                self.last_move.append((x, y, value))
        else:
            raise IndexError("Cell position out of bounds")
    
    def update_grid(self):
        for row in self.nodes:
            for cell in row:
                cell.update_cell()

    def update_neighbors(self, x, y,value):
        #print(f"2THdebug update neighbors of ({x},{y}) with value {value}")
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            #check if we hit a border
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighbor_cell = self.get_cell(nx, ny)
                
                neighbor_cell.neighbors_to_color -= 1

                #remove the color from the options
                if value in neighbor_cell.color_options:
                    neighbor_cell.color_options.remove(value)
        return


    #play as "player" (A or B) the cell at x,y with color "value"
    def play_cell(self, x, y, value, player):
        if not self.is_move_valid(x, y, value):
            print(f"Move at ({x},{y}) with value {value} is not valid")
            return False
        if 0 <= x < self.width and 0 <= y < self.height:
            self.nodes[y][x].set_value(value)
            #update the neighboring cells
            if self.width == 4:
                self.update_neighbors(x, y, value)
                self.update_grid()
            self.nodes[y][x].played_by = player
            if value != 0:
                self.last_move.append((x, y, value))
            if self.width ==4:
                self.update_blocks(x,y)
            return True
        return False


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

    #function to update neighbors when undoing a move
    def undo_update(self, x, y,value):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            neighbor_cell = self.get_cell(nx, ny)
            neighbor_cell.neighbors_to_color += 1

            if value not in neighbor_cell.color_options:
                neighbor_cell.color_options.append(value)
        return

    #undo the last move on the grid (only one for now)
    def undo_last_move(self):
        print(f"Lastmove: {self.last_move}")
        if self.last_move:
            x, y, value = self.last_move.pop()
            print(f"Undoing move at: {x}, {y}")
            self.nodes[y][x].set_value(0,player=None)
            
            self.undo_update(x, y, value)
            self.update_grid()
        else:
            print("No move to undo")

    #print the grid in terminal with colors
    def print_terminal(self):
        for row in self.nodes:
            for cell in row:
                color = Color.dictionary.get(cell)
                print(f"{Color.__dict__[color]}⬤{Color.ENDC}", end=' ')
            print()

    #return list of critical cells
    def get_critical_cells(self):
        critical_cells = []
        for y in range(self.height):
            for x in range(self.width):
                cell = self.get_cell(x, y)
                if cell.is_color_critical:
                    critical_cells.append(cell)
        return critical_cells

    #return the first uncolored neighbor of (x,y)
    def get_uncolored_neighbor(self, cell):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            ny, nx = cell.x + dx, cell.y + dy
            print(f"Checking neighbor at ({nx}, {ny}),{self.width},{self.height}")
            #check if we hit a border
            if 0 <= nx < self.width and 0 <= ny < self.height:
                print(f"Checking neighbor at ({nx}, {ny})")
                neighbor_cell = self.get_cell(nx, ny)
                if neighbor_cell.get_value() == 0:
                    
                    return neighbor_cell

        return None

    #create/update or merge blocks after a move at (x,y)
    def update_blocks(self,x,y):
        block = self.block_at(x)
        #if no block we create it/add the column to the neighboring block
        if block == None:
            block_left = self.block_at(x-1)
            block_right = self.block_at(x+1)

            if(block_left):
                block_left.end_col = x
                block_left.size += 1
                block_left.columns.append([self.get_cell(x, row) for row in range(self.height)])
                #merge 2 blocks
                if(block_right):
                    block_left.end_col = block_right.end_col
                    block_left.size += block_right.size
                    block_left.columns.extend(block_right.columns)
                    self.blocks.remove(block_right)
                    
                block_left.check_configurations()
                block_left.print_block()
                return
                      
            if(block_right):
                block_right.start_col = x
                block_right.size += 1
                block_right.columns.insert(0,[self.get_cell(x, row) for row in range(self.height)])
                block_right.check_configurations()
                block_right.print_block()
                
                return
            #create new block
            block = Block(self)
            block.start_col = x
            block.end_col = x
            block.size = 1
            block.columns.append([self.get_cell(x, row) for row in range(self.height)])
            self.blocks.append(block)

        block.check_configurations()
        block.print_block()
        return

    # return block at x if it exists
    def block_at(self, x):
        for block in self.blocks:
            if block.start_col <= x <= block.end_col:
                return block
        return None
    
    