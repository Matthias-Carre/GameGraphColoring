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

        self.particular_config = {} #dict to store node:config

        #self.pi_

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
    (ap = a' ...)
    """
    #check if the block is of type alpha
    # b=c != 0, a and c not doctors and if colored then a != c
    def is_alpha(self):
        a,b,c,d = self.columns[len(self.columns)-1]
        first = self.alpha_config(a,b,c,d)
        revers = self.alpha_config(d,c,b,a)
        if first or revers:
            #block of 1 is always left alpha
            self.left_configuration = "a"
            
        
        
    def alpha_config(self,a,b,c,d):
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
        
        #right side
        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        first = self.beta_config(b,c,cp)
        revers = self.beta_config(c,b,bp)
        if first or revers:
            self.right_configuration = "b"
        

        #left side
        a,b,c,d = self.columns[0]
        ap, bp, cp, dp = self.columns[1]
        first = self.beta_config(b,c,cp)
        revers = self.beta_config(c,b,bp)
        if first or revers:
            self.left_configuration = "b"


    def beta_config(self,b,c,cp):
        # b = cp and c=0
        if((b.value == cp.value and b.value !=0) and c.value == 0):
            return True

    #check if the block is of type gamma
    # a=d=bp != 0, b=c=cp = 0 and cp safe
    def is_gamma(self):
        if self.size <2:
            return False

        #right side
        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        first = self.gamma_config(a,b,c,d,ap,bp,cp,dp)
        revers = self.gamma_config(d,c,b,a,dp,cp,bp,ap)
        if first or revers:
            self.right_configuration = "g"
        
        #left side
        a,b,c,d = self.columns[0]
        ap, bp, cp, dp = self.columns[1]
        first = self.gamma_config(a,b,c,d,ap,bp,cp,dp)
        revers = self.gamma_config(d,c,b,a,dp,cp,bp,ap)
        if first or revers:
            self.left_configuration = "g"

        
    def gamma_config(self,a,b,c,d,ap,bp,cp,dp):
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

        #right side
        a,b,c,d = self.columns[len(self.columns)-1]
        ap, bp, cp, dp = self.columns[len(self.columns)-2]
        first = self.delta_config(a,c,bp)
        revers = self.delta_config(d,b,cp)
        if first or revers:
            self.right_configuration = "d"
        
        #left side
        d, c, b, a = self.columns[0]
        dp,cp,bp,ap = self.columns[1]
        first = self.delta_config(a,c,bp)
        revers = self.delta_config(d,b,cp)
        if revers or first:
            self.left_configuration = "d"

        


    def delta_config(self,a,c,bp):
        # a=bp !=0
        if(a.value == bp.value and a.value !=0):
            # c != a != 0
            if(c.value != a.value and c.value !=0):
                return True

    #particular case whene between two blocks
    # a==d, b==cd and c != a,b,0 and a != b and a,b,c != 0
    def is_pi(self):
        a,b,c,d = self.columns[len(self.columns)-1]

        if  self.end_col +2 < self.grid.width:
            cd = self.grid.get_cell(self.end_col +2,2)
            print("cd=",cd.value)
            if a.value == d.value and b.value == cd.value :
                print("Block: check pi")
                if c.value != a.value and c.value != b.value and c.value !=0 and a.value != b.value and a.value !=0 and b.value !=0:
                    self.right_configuration = "p"
                    return True
        return False
    
    # b_0 == a_2 == c_2 == d_0 != 0
    # c_1 != 0 
    # a_0,b_0,d_0,b_1,d_1 == 0 
    def is_Delta(self):
        if self.size <= 3:
            return False
        a_0,b_0,c_0,d_0 = self.columns[len(self.columns)-2]
        a_1,b_1,c_1,d_1 = self.columns[len(self.columns)-1]
        a_2,b_2,c_2,d_2 = self.columns[len(self.columns)]
        if(b_0.value == a_2.value and a_2.value == c_2.value and c_2.value == d_0.value and d_0.value !=0):
            if(c_1.value !=0):
                if(a_0.value == 0 and b_0.value == 0 and d_0.value == 0 and b_1.value == 0 and d_1.value == 0):
                    print("Block is Delta")
                    self.right_configuration = "D"

        return
    


    #set the left and right configurations of the block
    def check_configurations(self):
        self.left_configuration = None
        self.right_configuration = None

        if self.is_alpha():
            print("Block is alpha")
            self.right_configuration = "a"
        
        # if config is alpha and beta => beta
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

        
        #manage critical cases
        if self.is_Delta():
            print("Block is Delta")
            self.right_configuration = "D"
        
        

    def print_block(self):
        print(f"Block from column {self.start_col} to {self.end_col}, size: {self.size}")
        for i in range(4):
            for col in self.columns:
                cell = col[i]
                print(f"{cell.value} ", end="")
            print()
        print()

        print(f"Left configuration: {self.left_configuration}, Right configuration: {self.right_configuration}")

    
        
        

