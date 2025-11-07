#a block is a union of neighboring columns where each column has at least one colored cell
class Block:
    def __init__(self,grid):
        
        self.grid = grid
        self.columns = [] #list of columns in the block
        self.start_col = None
        self.end_col = None

        self.size = 0 #number of columns in the block

        self.is_safe = False
        self.is_sound = False
        self.is_sick = False

        self.configurations= ["a","b","g","d","p"] #alpha beta gamma delta pi
        self.right_configuration = None
        self.left_configuration = None

    #merge 2 blocks together 
    def merge(self,other_block):
        return

    #set the left and right configurations of the block
    def check_configurations(self):
        return
        

