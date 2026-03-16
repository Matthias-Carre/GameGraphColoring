"""
Every case of the paper
Note: in the paper line are from down to up starting from 1
Here we consider up to down starting from 0
"""

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


"""
Case 3: Bob colors empty column
"""

# Bob play in col j with j-1,j and j+1 empty 
def is_3_new(grid,bob_move):
    x,y,color = bob_move
    #previous and next column
    list = [(x-1,0),(x-1,1),(x-1,2),(x-1,3),(x+1,0),(x+1,1),(x+1,2),(x+1,3),(x,0),(x,1),(x,2),(x,3)]
    list.remove((x,y))
    if same_value_grid(grid,list):
        print("Case 3-new")
        return True
    return False

# Alice answer in col j with |a-b| = 2 with c
def solve_3_new(grid,bob_move):
    print("Case 3-new: Alice color v_b,j with |a-b| = 2 with c")
    x,y,color = bob_move
    if y == 0 or y == 1:
        return (x,y+2,color)
    elif y == 2 or y == 3:
        return (x,y-2,color)


def is_3_pi(grid,bob_move):
    if grid.bob_play_on_config["config"] == "p":
        print("Is 3 pi")
        return True
    return False

def solve_3_pi(grid,bob_move):
    #normalize bob move:
    x,y,color = bob_move
    is_h_flip = grid.bob_play_on_config["is_hori_flipped"]
    is_v_flip = grid.bob_play_on_config["is_vert_flipped"]
    

    #fix j is full line of 3_pi is right or left
    j = x+1 if is_v_flip else x-1 

    #bob 2,j+1 => alice 1,j+1
    print("3Pi: Bob last move ",(x,y))
    print("3Pi: in :",grid.bob_play_on_config["config"])
    print("3Pi: Bob normalized move: ",get_norm_pos(grid,x,y,j,is_h_flip,is_v_flip))
    print("3Pi: check j+2, 2:",get_norm_cell(grid,2,2,j,is_h_flip,is_v_flip).value)
    print("3Pi: flip h and v: ",is_h_flip, is_v_flip)
    dx,ny = get_norm_pos(grid,x,y,j,is_h_flip,is_v_flip)

    if(ny == 2):
        col = get_norm_cell(grid,1,1,j,is_h_flip,is_v_flip).color_options
        print("3Pi color option: ", col)
        rx,ry = get_real_pos(grid,1,1,j,is_h_flip,is_v_flip)
        print("3Pi real pos: ",rx,ry)
        return (rx,ry,col[0])
    if(ny == 1):
        col = get_norm_cell(grid,1,2,j,is_h_flip,is_v_flip).color_options
        rx,ry = get_real_pos(grid,1,2,j,is_h_flip,is_v_flip)
        return (rx,ry,col[0])
    
    #bob 3,j+1 cw c' or c'' => alice 1,j+1 cw available 
    if(ny == 3):
        #cell c'
        col_cell_1 = get_norm_cell(grid,0,1,j,is_h_flip,is_v_flip)
        #cell c''
        col_cell_2 = get_norm_cell(grid,0,2,j,is_h_flip,is_v_flip)
        #color v3,j+1 w c' or c''
        if color == col_cell_1.value or color == col_cell_2.value:
            c = get_norm_cell(grid,dx,1,j,is_h_flip,is_v_flip).color_options
            rx,ry = get_real_pos(grid,dx,1,j,is_h_flip,is_v_flip)
            return (rx,ry,c[0])
        #bob 3,j+1 cw w => if 1,j+2 != w => alice 1,j+1 cw w else 1,j+1 cw c''
        if color != get_norm_cell(grid,dx+1,1,j,is_h_flip,is_v_flip).value:
            rx,ry = get_real_pos(grid,dx,1,j,is_h_flip,is_v_flip)
            return (rx,ry,color)
        else:
            #get the value of c'' (j,2)
            cell = get_norm_cell(grid,dx,2,j,is_h_flip,is_v_flip)
            #A FINIR
    

    if (ny == 0):
        #if 0,j+1 = c' => 2,j+1 available 
        #if 0,j+1 =  w => 2,j+1 w
        #if 0,j+1 = c'' => if 1,j+2 c'' => 2,j+1 aviable
        
        #if 0,j+1 = c'' => if 1,j+2 c or w => 2,j+1 same
        #if 0,j+1 = c' => if 1,j+2 0 => 1,j+1 w

        return

    """
    
    print("strat: ",color, grid.get_cell(x,1).value, grid.get_cell(x,2).value)
    if y == 3:
        if color == grid.get_cell(x-1,2).value or color == grid.get_cell(x+1,2).value:
            c = grid.get_cell(x,1).color_options
            #print("3Pi color option: ", c)
            return (x,1,c[0])
        
        #bob 3,j+1 cw w => if 1,j+2 != w => alice 1,j+1 cw w else 1,j+1 cw c''
        if color != grid.get_cell(x+1,1).value:
            return (x,1,color)
        else:
            #get the value of c''

            return (x,1,grid.get_cell(x-1,2).value)

    return
    """

def is_3_delta(grid,bob_move):
    #bob coor in col adjacent to border of config delta
    #idea: Alice will color to obtain alpha beta gamma or delta or merge
    return

def solve_3_delta(grid,bob_move):
    #Case 3d1
    #bob 3,j+1 y if 1,j+2 != y => alice 1,j+1 w y
    #bob 3,j+1 y if 1,j+2 = y => 0,j+1 w y

    #Case 3d2
    #bob 3,j+1 c != y => alice 1,j+1 c or y

    #Case 3d3
    #bob 2,j+1 c != y if j+2 not empty => alice 1,j+1 available
    #bob 2,j+1 c != y if j+2 empty if 1,j+3 != c => alice 1,j+2 c 







"""
input: list of (j,x) coordinates
return true if all the cells in the list have the same value
"""
def same_value_grid(grid,list):
    (j,x) = list[0]
    first_value = grid.get_cell(j,x).value
    for j,x in list: 
        if grid.get_cell(j,x).value != first_value: 
            return False
    return True

"""
input: grid, dx, y, j, is_hori_flipped, is_vert_flipped
    dx is just the position relative to j
return: the cell at (x,y) on this context

"""
def get_norm_cell(grid,dx,y,j,hori,verti):

    if hori and verti:
        print("strategy: dx,y,j , nx,ny ",dx,y,j,2*j-dx,grid.height-1-y)
        return grid.get_cell(j-dx,grid.height-1-y)
    elif hori:
        return grid.get_cell(j+dx,grid.height-1-y)
    elif verti:
        return grid.get_cell(j-dx,y)
    else:
        return grid.get_cell(j+dx,y)

"""
input: grid, x, y, j, is_hori_flipped, is_verti_flipped
return: the coordinates of (x,y) on the normalized context
x will be the position relative to j
idea: bob move is translate to his position after normalization
"""
def get_norm_pos(grid,x,y,j,hori,verti):
    dx_norm = j-x if verti else x-j
    y_norm = grid.height-1-y if hori else y 

    return (dx_norm,y_norm)

"""
input: grid, x, y, j, is_hori_flipped, is_verti_flipped
output: the coordinates of (x,y) in the real grid
"""
def get_real_pos(grid,dx,y,j,hori,verti):
    x_real = j - dx if verti else j+dx
    y_real = grid.height-1-y if hori else y 

    return (x_real,y_real)