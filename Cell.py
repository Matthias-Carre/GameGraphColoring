class Cell:
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = []
        self.posibilities = []
        self.played_by = None #A or B for Alice of Bob
        self.is_safe = False
        self.is_sound = False
        self.doctors = []
        self.patients = []


    def set_value(self, value, player="A"):
        self.value = value
        self.played_by = player

    def get_value(self):
        return self.value

    def get_player(self):
        return self.played_by