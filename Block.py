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

    """
    functions to check the type of block:
    Illustration of the columns:
    ap a 0
    bp b 0
    cp c 0
    dp d 0
    """
    #check if the block is of type alpha
    # b=c != 0, a and c not doctors and if colored then a != c
    def is_alpha(self):
        a,b,c,d = self.columns[len(self.columns)-1]
        # b=c != 0
        if( (b.value == d.value and b.value !=0)):
            #a and c not doctors
            if((not(a.is_doctor()) and not(c.is_doctor()))):
                #if a and c colored then a != c
                if(a.value != c.value or a.value ==0 or c.value==0):
                    return True
            
    #check if the block is of type beta
    # b = cp and c=0 
    def is_beta(self):
        if self.size <2:
            return False
        
        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        # b = cp and c=0
        if((b.value == cp.value and b.value !=0) and c.value == 0):
            return True

    #check if the block is of type gamma
    # a=d=bp != 0, b=c=cp = 0 and cp safe
    def is_gamma(self):
        if self.size <2:
            return False

        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        # a=d=bp != 0
        if((a.value == d.value and a.value == bp.value and a.value !=0)):
            # b=c=cp = 0
            if(b.value ==0 and c.value ==0 and cp.value ==0):
                #cp safe
                if(cp.is_safe):
                    return True
    
    #check if the block is of type delta
    # a=bp !=0 , c != a != 0
    def is_delta(self):
        if self.size <2:
            return False

        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        # a=bp !=0
        if(a.value == bp.value and a.value !=0):
            # c != a != 0
            if(c.value != a.value and c.value !=0):
                return True

    #particular case whene between two blocks
    def is_pi(self):
        return false


    #set the left and right configurations of the block
    def check_configurations(self):
        if self.is_alpha():
            print("Block is alpha")
            self.right_configuration = "a"
        if self.is_beta():
            print("Block is beta")
            self.right_configuration = "b"
        if self.is_gamma():
            print("Block is gamma")
            self.right_configuration = "g"
        if self.is_delta():
            print("Block is delta")
            self.right_configuration = "d"
        if self.is_pi():
            print("Block is pi")
            self.right_configuration = "p"


    def print_block(self):
        print(f"Block from column {self.start_col} to {self.end_col}, size: {self.size}")
        for col in self.columns:
            for cell in col:
                print(f"{cell.value} ", end="\n")
            print()


        
        

