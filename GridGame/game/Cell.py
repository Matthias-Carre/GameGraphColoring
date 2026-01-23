class Cell:
    def __init__(self, x, y, grid_width, grid_height,num_colors=4, value=0):
        self.x = x
        self.y = y
        self.grid_width = grid_width
        self.grid_height = grid_height

        #used to track rounds in advanced strategies
        self.round=None

        self.value = value #color value, 0 if uncolored

        self.any_color = False #used to show x on cell

        self.neighbors = [] #values of the colors of neighboring cells
        self.neighbors_color = self.neighbors_colors()
        self.neighbors_to_color = self.number_of_neighbors() #number of neighbors yet to be colored
        self.color_options = [i for i in range(1,num_colors+1)] #remaining color options

        self.played_by = None #0 or 1 for Alice or Bob

        self.is_safe = False
        self.is_sound = False
        self.is_color_critical = False
        self.is_uncolorable = False

        self.doctors = []
        self.patients = []

    #return the colors of the neighboring cells
    def neighbors_colors(self):
        colors = []
        for neighbor in self.neighbors:
            if neighbor.get_value() != 0:
                colors.append(neighbor.get_value())
        return colors


    #check and update the status of the cell
    def update_cell(self):
        
        #check if its critical
        if len(self.color_options) == 1:
            print(f"Cell at ({self.x}, {self.y}) is color critical")
            self.is_color_critical = True

        #check if its safe
        #is colorred OR #N <= 3 OR 2 neighbors colored with same color
        #OR 3 neighbors colored with 3 colors but the 4th is neighbor to the last color
        if len(self.color_options) == 0:
            self.is_safe = True
        if self.value != 0 or len(self.neighbors) < 4 or len(self.neighbors_colors()) - len(set(self.neighbors_colors())) > 0 :
            self.is_safe = True
            #print(f"Cell at ({self.x}, {self.y}) is safe")
        if len(self.neighbors) == 4 and len(set(self.neighbors_colors())) == 3:
            missing_color = self.color_options[0] if len(self.color_options) > 1 else []
            print(f"Cell at ({self.x}, {self.y}) is check uncolored neighbor")
            uncolored_neighbor = self.get_uncolored_neighbor()
            if uncolored_neighbor is not None:
                if missing_color in uncolored_neighbor.neighbors_colors():
                    self.is_safe = True
                    print(f"Cell at ({self.x}, {self.y}) is safe by neighbor colors")

        
        #check if no color options left
        if len(self.color_options) == 0:
            self.is_uncolorable = True
            print(f"Cell at ({self.x}, {self.y}) has no color options left")

    #to simplify the detection of safe cells
    def number_of_neighbors(self):
        #at minimum border cells have 2 neighbors
        result = 2
        #not in the x borders
        if not (self.x == 0 or self.x ==  self.grid_width -1):
            result += 1

        #not in the y borders
        if not (self.y == 0 or self.y ==  self.grid_height -1):
            result += 1
        return result

    #change the value of the cell
    def set_value(self, value, player="A"):
        self.value = value
        self.played_by = player

    def get_value(self):
        return self.value

    def get_player(self):
        return self.played_by

    def is_doctor(self):
        return len(self.patients) > 0

    def get_uncolored_neighbor(self):
        for neighbor in self.neighbors:
            if neighbor.get_value() == 0:
                return neighbor
        return None
    #return the status safe/sound/color_critical/doctor/patient

    def get_status(self):
        if self.is_safe:
            return "safe"
        if self.is_sound:
            return "sound"
        return "o"
    
    #debug/analysis print (with right click)
    def print_cell_informations(self):
        print(f"Cell ({self.x}, {self.y}):")
        print(f"  Value: {self.value}")
        print(f"  Played by: {self.played_by}")
        print(f"  Neighbors: {[(n.x, n.y) for n in self.neighbors]}")
        print(f"  Neighbors colors: {self.neighbors_colors()}")
        print(f"  Neighbors to color: {self.neighbors_to_color}")
        print(f"  Color options: {self.color_options}")
        print(f"  Is safe: {self.is_safe}")
        print(f"  Is sound: {self.is_sound}")
        print(f"  Is color critical: {self.is_color_critical}")
        print(f"  Is uncolorable: {self.is_uncolorable}")
        print(f"  Doctors: {[(d.x, d.y) for d in self.doctors]}")
        print(f"  Patients: {[(p.x, p.y) for p in self.patients]}")
        