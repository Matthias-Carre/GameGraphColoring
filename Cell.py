class Cell:
    def __init__(self, x, y, grid_width, grid_height,num_colors=4, value=0):
        self.x = x
        self.y = y
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.value = value #color value, 0 if uncolored

        self.neighbors = [] #values of the colors of neighboring cells
        self.neighbors_to_color = self.number_of_neighbors() #number of neighbors yet to be colored
        self.color_options = [i for i in range(1,num_colors+1)] #remaining color options

        self.played_by = None #A or B for Alice of Bob

        self.is_safe = False
        self.is_sound = False
        self.is_color_critical = False
        self.is_uncolorable = False

        self.doctors = []
        self.patients = []

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

    def set_value(self, value, player="A"):
        self.value = value
        self.played_by = player

    def get_value(self):
        return self.value

    def get_player(self):
        return self.played_by