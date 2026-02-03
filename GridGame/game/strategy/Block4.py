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

        self.flip_config_right = None #store the block fliped to match configurations (can be same as self)
        self.flip_config_left = None #store the block for the left config but flip it at right

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

        
        if revers:
            self.flip_config_left = self.flip_horizontal()
            self.left_configuration = "a"
            
        if first:
            #block of 1 is always left alpha
            self.flip_config_left = self
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
        
        #create fliped right
        if revers:
            self.flip_config_right = self.flip_horizontal()
            self.right_configuration = "b"

        if first:
            self.flip_config_right = self
            self.right_configuration = "b"
        

        #left side
        a,b,c,d = self.columns[0]
        ap, bp, cp, dp = self.columns[1]
        first = self.beta_config(b,c,cp)
        revers = self.beta_config(c,b,bp)


        #create fliped horison vertic left
        if revers:
            self.flip_config_left = self.flip_vertical()
            fliped = self.flip_config_left
            self.flip_config_left = fliped.flip_horizontal()
            self.left_configuration = "b"

        #create vertic fliped  
        if first:
            self.flip_config_left = self.flip_vertical()
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

        if revers:
            self.flip_config_right = self.flip_horizontal()
            self.right_configuration = "g"


        if first:
            self.flip_config_right = self
            self.right_configuration = "g"
        
        #left side
        a,b,c,d = self.columns[0]
        ap, bp, cp, dp = self.columns[1]
        first = self.gamma_config(a,b,c,d,ap,bp,cp,dp)
        revers = self.gamma_config(d,c,b,a,dp,cp,bp,ap)

        
        if revers:
            self.flip_config_left = self.flip_vertical()
            fliped = self.flip_config_left
            self.flip_config_left = fliped.flip_horizontal()
            self.left_configuration = "g"

        if first:
            self.flip_config_left = self.flip_vertical()
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

        
        if revers:
            self.flip_config_right = self.flip_horizontal()
            self.right_configuration = "d"

        if first:
            self.flip_config_right = self
            self.right_configuration = "d"
        
        #left side
        d, c, b, a = self.columns[0]
        dp,cp,bp,ap = self.columns[1]
        first = self.delta_config(a,c,bp)
        revers = self.delta_config(d,b,cp)
        
        if revers:
            self.flip_config_left = self.flip_vertical()
            fliped = self.flip_config_left
            self.flip_config_left = fliped.flip_horizontal()
            self.left_configuration = "d"

        if first:
            self.flip_config_left = self.flip_vertical()
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
        #right side
        

        if  self.end_col +2 < self.grid.width:

            a,b,c,d = self.columns[len(self.columns)-1]
            cd = self.grid.get_cell(self.end_col +2,2)

            if self.pi_config(a,b,c,d,cd):
                self.right_configuration = "p"
                self.flip_config_right = self
            

            d, c, b, a = self.columns[len(self.columns)-1]
            cd = self.grid.get_cell(self.end_col +2,1)
            if self.pi_config(a,b,c,d,cd):
                self.right_configuration = "p"
                self.flip_config_right = self.flip_horizontal()
        
        #left side
        if self.start_col -2 >= 0:

            a,b,c,d = self.columns[0]
            cd = self.grid.get_cell(self.start_col -2,2)
            print(f"Pi config A cd={cd.value}, a={a.value},b={b.value},c={c.value},d={d.value}")

            if self.pi_config(a,b,c,d,cd):
                self.left_configuration = "p"
                self.flip_config_left = self.flip_vertical()
            

            d, c, b, a = self.columns[0]
            cd = self.grid.get_cell(self.start_col -2,1)
            print("Pi config B:",cd.value)
            if self.pi_config(a,b,c,d,cd):
                self.left_configuration = "p"
                fliped = self.flip_vertical()
                self.flip_config_left = fliped.flip_horizontal()

    def pi_config(self,a,b,c,d,cd):
        # a==d, b==cd and c != a,b,0 and a != b and a,b,c != 0
        if a.value == d.value and b.value == cd.value :
            if c.value != a.value and c.value != b.value and c.value !=0 and a.value != b.value and a.value !=0 and b.value !=0:
                return True
        
        return False
    


    # b_0 == a_2 == c_2 == d_0 != 0
    # c_1 != 0 
    # a_0,b_0,d_0,b_1,d_1 == 0 
    def is_Delta(self):

        """
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
        """
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

        print("RIGHT config:")
        self.print_block(self.flip_config_right)
        print("LEFT config:")
        self.print_block(self.flip_config_left)
        
    #flip the block on horizontal axis 
    #goal is to apply same strategy after fliping (creating a new block object pointing to same cells)
    def flip_horizontal(self):
        flipped_block = Block(self.grid)
        flipped_block.start_col = self.start_col
        flipped_block.end_col = self.end_col
        flipped_block.size = self.size
        flipped_block.is_safe = self.is_safe
        flipped_block.is_sound = self.is_sound
        flipped_block.is_sick = self.is_sick

        #flip each column
        for col in self.columns:
            a,b,c,d = col
            flipped_col = [d,c,b,a]
            flipped_block.columns.append(flipped_col)

        #flip configurations
        flipped_block.left_configuration = self.left_configuration
        flipped_block.right_configuration = self.right_configuration
        return flipped_block
        
    def flip_vertical(self):
        flipped_block = Block(self.grid)
        flipped_block.start_col = self.start_col
        flipped_block.end_col = self.end_col
        flipped_block.size = self.size
        flipped_block.is_safe = self.is_safe
        flipped_block.is_sound = self.is_sound
        flipped_block.is_sick = self.is_sick

        #flip columns order
        for i in range(self.size-1,-1,-1):
            col = self.columns[i]
            flipped_block.columns.append(col)

        return flipped_block



    def print_block(self,block=None):
        if block == None:
            block = self

        print(f"Block from column {block.start_col} to {block.end_col}, size: {block.size}")
        for i in range(4):
            for col in block.columns:
                cell = col[i]
                print(f"{cell.value} ", end="")
            print()
        print()

