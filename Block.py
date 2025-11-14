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


    def is_alpha(self):
    
    def is_beta(self):

    def is_gamma(self):
    
    def is_delta(self):

    #particular case whene between two blocks
    def is_pi(self):
        
        return
    #set the left and right configurations of the block
    def check_configurations(self):
        a,b,c,d = self.columns[0]
        #beta
        
        
        #alpha
        
        if(a==c or b==d ):
            self.left_configuration = "a"


    def print_block(self):
        print(f"Block from column {self.start_col} to {self.end_col}, size: {self.size}")
        for col in self.columns:
            for cell in col:
                print(f"{cell.value} ", end="\n")
            print()


        
        

