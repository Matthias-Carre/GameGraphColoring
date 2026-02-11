
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

def is_1Delta(grid,bob_move):
    if bob_move.config != "D":
        return False
    if bob_move.x in [bob_move.j+1,bob_move.j+2] :
        return True
    return False

def solve_1Delta(grid,bob_move):
    j = bob_move.j
    sick_vertex_pos = (j + 1, 2) 
    
