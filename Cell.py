class Cell:
    def __init__(self, x, y, value=0):
        self.x = x
        self.y = y
        self.value = value
        self.neighbors = []
        self.posibilities = []
        self.is_safe = False
        self.is_sound = False
        self.doctors = []
        self.patients = []
        

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value