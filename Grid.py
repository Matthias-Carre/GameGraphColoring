
class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.nodes = [[0 for _ in range(width)] for _ in range(height)]

    def set_cell(self, x, y, value): # give the value of the cell x,y
        if 0 <= x < self.width and 0 <= y < self.height:
            self.nodes[y][x] = value
        else:
            raise IndexError("Cell position out of bounds")

    def get_cell(self, x, y): # return the value of the cell x,y
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.nodes[y][x]
        else:
            raise IndexError("Cell position out of bounds")

    def display(self):
        for row in self.nodes:
            for cell in row:
                print(cell, end=' ')
            print()

    def as_proper_coloring(self): #check if the gird is a proper coloring
        for y in range(self.height-1):
            for x in range(self.width-1): # we check only the right and down neighbors
                current_color = self.get_cell(x,y)
                right_color = self.get_cell(x+1,y)
                down_color = self.get_cell(x,y+1)
                if ((current_color == right_color) or (current_color == down_color)) and current_color != 0:
                    return False

        return True

