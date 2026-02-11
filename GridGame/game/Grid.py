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
        self.nodes = [[Cell(x, y, self ,num_colors=num_colors) for y in range(width)] for x in range(height)]
                
        self.last_moves = [] # (x,y,color)
        self.previous_changes = [] #list of list on changes for each move
        self.num_colors = num_colors
        self.blocks = []
        self.player = 0 #0 for Alice, 1 for Bob
        self.round = 1
        self.last_Bob_move = None # (x,y,color,past_config)        

        #add neighbors to each cell
        self.init_state()

        self.history = []

    def init_state(self):
        for i in range(self.width):
            for j in range(self.height):
                self.nodes[j][i].neighbors = self.neighborhood(self.nodes[j][i])

                #add the starting status of each cell
                self.nodes[j][i].check_safe_cell()
        for i in range(self.width):
            for j in range(self.height):
                self.nodes[j][i].check_sound_cell()

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

    #joue le coup color en x y et update la grille 
    def play_move(self, x, y, color):
        if not self.is_move_valid(x, y, color):
            print(f"Invalid move at ({x}, {y})")
            return False
        
        #save pour undo
        self.last_Bob_move = (x,y,color)
        self.save_zone_snapshot(x, y, distance=2)

        #applique le coup
        target = self.nodes[y][x]
        target.value = color
        target.played_by = self.player
        target.round = self.round
        target.update_cell()
        
        self.last_moves.append((x,y,color))
        self.update_neighbors(x,y,color)

        return True

    def update_neighbors(self,x,y,color):
        cell = self.nodes[y][x]
        for neighbor in cell.neighbors:
            if color in neighbor.color_options:
                #self.add_to_previous_changes([neighbor.clone_cell()])

                neighbor.color_options.remove(color)
            neighbor.neighbors_to_color -= 1
            affected_cells = neighbor.update_cell()
            self.add_to_previous_changes(affected_cells)
        return 
    
            
    #utiliser dans la premier version de undo
    def roll_back_neighbors(self,x,y,color):
        cell = self.nodes[y][x]
        for neighbor in cell.neighbors:
            
            #check if we can restore the color option
            color_is_posible = True 
            for neighbor2 in neighbor.neighbors:
                #print(f"voisin2 value: {neighbor2.value}, color: {color}")
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
    
    """
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
    """
    #undo version avec zone de sauvegarde
    def undo_move(self):
        if not self.history:
            print("Rien à annuler")
            return False

        #recup de la save
        patch = self.history.pop()

        #restoration 
        for (x, y), state in patch.items():
            self.nodes[y][x].restore_state(state, self)
        
        if self.last_moves:
            self.last_moves.pop()
        
        return True

    #add changed nodes to the last list of previous changes
    def add_to_previous_changes(self,changed_nodes):
        for node in changed_nodes:
            if self.previous_changes == [] or not(self.is_present(node,self.previous_changes[-1])):
                self.previous_changes[-1].append(node)


    #return true if node is in list 
    def is_present(self,node,list):
        for n in list:
            if n.x == node.x and n.y == node.y:
                return True
        return False
    

    def neighborhood(self,cell):
        i = cell.y
        j = cell.x
        neighborhood = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  
        for dx, dy in directions:
            nx, ny = i + dx, j + dy
            #check if we hit a border
            if 0 <= nx < self.width and 0 <= ny < self.height:
                neighborhood.append(self.nodes[ny][nx])
        return neighborhood
    
    #test d'une autre logique de save, on garde une zone autour du coup jouer 
    # on grade les co des elements voisin pour les restorer apres sans garder les objets 
    def save_zone_snapshot(self, center_x, center_y, distance=2):
        
        patch = {}
        
        # Calcul des bornes pour ne pas sortir de la grille
        min_x = max(0, center_x - distance)
        max_x = min(self.width, center_x + distance + 1)
        min_y = max(0, center_y - distance)
        max_y = min(self.height, center_y + distance + 1)

        # On boucle sur la zone carrée
        for y in range(min_y, max_y):
            for x in range(min_x, max_x):
                # On sauvegarde l'état AVANT modif
                patch[(x, y)] = self.nodes[y][x].get_state()
        
        self.history.append(patch)