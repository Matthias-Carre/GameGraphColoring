

#exemple de skelet de code pour l'exec
def is_TestConfig(grid,bob_move):
    #C'est juste un exemple de test
    #if alpha Alice play diagonal same value (if possible)

    #if bob_move.config != "a":
    if "a" != "a":
        return False
    return True
    
def solve_TestConfig(grid,bob_move):
    lx,ly,lc = bob_move
    
    print("resolve test config")
    return (lx+1,ly+1,lc)


#Bob joue dans j+1 ou j+2 de D 
# 1. Bob color sick => Alice color any j+1
# 2. Bob not color sick => Alice color sick with available color
def is_1Delta(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)

    if block.particular_config != "Delta":
        return False

    j = block.particular_config_j
    #Bob play in j+1 or j+2 of Delta
    print("x =",x,"j=",j)
    if x == j+1 or x == j+2:
        return True

    print("Bob in block D","j=",block.particular_config_j)
    return False

def solve_1Delta(grid,bob_move):
    x,y,color = bob_move
    j =  grid.blocks.block_at(x).particular_config_j
    
    if x == j+1 and y == 1 :
        print("Alice colore dans j+1 ")
    else:
        print("Alice colore sick")
        
def is_Delta_p_a(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)

    if block.particular_config != "Delta'":
        return False
    j = block.particular_config_j
    #Bob play in (1,j-1) or (0,j+1)
    print("DPA: Bob last move ",(x,y))
    print("DPA: check:",2,j-1,"or",1,j)
    print("Bob last move 2,j-1 ",(y,x) == (2,j-1), "or" "1,j",(y,x) == (1,j))
    print("j=",j)
    if ((y,x) == (2,j-1)) or ((y,x) == (1,j)):
        print("DELTRA P A")
        return True
    return False

def solve_Delta_p_a(grid,bob_move):

    print("Alice joue (2,j+1)")

def is_Delta_p_b(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)
    if block.particular_config != "Delta'":
        return False

    j = block.particular_config_j
    if ((y,x) == (2,j)):
        print("DELTRA P B")
        return True

def solve_Delta_p_b(grid,bob_move):
    
    print("Alice joue")
    
def is_Delta_p_c(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)
    if block.particular_config != "Delta'":
        return False
    j = block.particular_config_j

    if ((y,x) == (2,j+1)):
        print("DELTRA P C")
        return True

def solve_Delta_p_c(grid,bob_move):
    
    print("Alice joue")

def is_Delta_p_d(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)
    if block.particular_config != "Delta'":
        return False
    j = block.particular_config_j

    if ((y,x) == (1,j+2)):
        print("DELTRA P D")
        return True

def solve_Delta_p_d(grid,bob_move):
    
    print("Alice joue")

def is_Delta_p_e(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)

    if block.particular_config != "Delta'":
        return False
    j = block.particular_config_j
    if ((y,x) == (4,j+2)):
        print("DELTRA P E")
        return True
    
def solve_Delta_p_e(grid,bob_move):
    
    print("Alice joue")


def is_Delta_p_f(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)

    if block.particular_config != "Delta'":
        return False
    j = block.particular_config_j
    if ((y,x) == (2,j+2)):
        print("DELTRA P F")
        return True

def solve_Delta_p_f(grid,bob_move):
    
    print("Alice joue")

def is_Delta_p_2(grid,bob_move):
    x,y,color = bob_move
    block = grid.blocks.block_at(x)

    if block.particular_config != "Delta2'":
        return False
    
    return True

#Bob play in (j-2,j-1 or j) in Lambda or Lambda2
def is_Lambda_a(grid,bob_move):
    # 4,j-1 -> 3,j-1
    return False





