from game.Alice.strategy_4 import *
from game.Alice.strategy_random import *

class Alice:
    def __init__(self,grid):
        self.grid = grid
        self.strategy = []
        self.load_strategy()

    '''
    On a besoin:
     - du dernier move de Bob 
     - dans quel config on ce trouve
     - la situation de la case avant le move de Bob
    
    '''

    def load_strategy(self):

        if self.grid.height == 4:
            self.strategy = [
                (is_TestConfig,solve_TestConfig)
            ]
        else:
            self.strategy = [
                (is_any,random_move)
            ]


    #return (x,y,color) of the move that Alice wants to play
    def next_move(self):
        if self.grid.player != 0:
            print("Not Alice's turn")
            return None
        print("Alice move")

        # react to Bob's last move
        
        #first move
        if(self.grid.round == 1):
            return (0,1,1)
        
        for is_case, solve_case in self.strategy:
            if is_case(self.grid,self.grid.last_Bob_move):
                return solve_case(self.grid,self.grid.last_Bob_move)

        #case test:
        if is_TestConfig(self.grid,self.grid.last_Bob_move):
            return solve_TestConfig(self.grid,self.grid.last_Bob_move)
       

        #CASE 1: in block/border d/j,j-1 of L,L2,L',L'2/j-2 of L,L'/j-2 of L2,L'2 if j-3 not empty

        #case 1D

        #case 1D'

        #case 1L

        #case 1L'

        #case 1-doc

        #case 1g-doc

        #case 1-safe
        #!!!

        #Case 2: In Border not in D,L,L'

        #case 2d

        #case 2afgFree

        #case 2b

        #case 2g

        #case 2a

        #case 2a'


        #Case 3: empty col not in j-1 of L,L2,L',L'2

        #case 3new

        #case 3pi

        #case 3d

        #case 3aF

        #case 3bF

        #case 3gF

        #case 3g

        #case 3b

        #case 3a

    #cases:

    '''
    def handle_case_1D():
        bob_move = self.grid.last_Bob_move
        self.case_1D(bob_move)
    '''


    #color j+1 or j+2 of D => 
    #1. bob color sick => Alice color any j+1
    #2. bob not color sick => Alice color sick with available color
    def case_1D(self,bob_move):
        if bob_move.past_state == 'sick':
            #alice colors any j+1
            pass
        else:
            #alice colors sick with available color
            pass

    #color in D' or D'2 =>
    #1. D'
    def case_1D_p(self,bob_move):
        #if config D'
        if bob_move.config == 'Dp':
            #if bob color v(2,j-1) or v(3,j) => v(2,j+1)
            if bob_move.pos == None:#x,y:
                pass
            #if bob color v(2,j) => v(1,j+1)

            #if bob color v(2,j+1) => v(1,j+1)

            #if bob color v(3,j+2) => v(2,j+1)

            #if bob color v(4,j+2) => v(3,j+2)

            #if bob color v(2,j+2) => v(3,j+2)

            #for D'2

        pass

        


