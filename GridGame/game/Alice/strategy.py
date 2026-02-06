


def is_1Delta(grid,bob_move):
    if bob_move.config != "D":
        return False
    if bob_move.x in [bob_move.j+1,bob_move.j+2] :
        return True
    return False

def solve_1Delta(grid,bob_move):
    j = bob_move.j
    sick_vertex_pos = (j + 1, 2) 
