

def as_color_critical(grid, Alice_move):
    
    #check if bob move is color critical
    lx,ly,lc = Alice_move
    print(f"Bob strategy 3 GET CELL {lx,ly} ")
    Alice_cell = grid.get_cell(lx,ly)
    print("check as color crit")
    for neighbor in Alice_cell.neighbors:
        if neighbor.is_color_critical:
            print("Bob strategy 3: as_color_critical True")
            return True
        
    return False

def winning_move(grid, Alice_move):
    #check if bob move is winning
    lx,ly,lc = Alice_move
    print(f"Bob strategy 3 GET CELL {lx,ly} ")
    Alice_cell = grid.get_cell(lx,ly)
    for neighbor in Alice_cell.neighbors:
        if neighbor.is_color_critical:
            empty_cells = neighbor.get_empty_neighbors()
            lc = neighbor.color_options[0]
    print(f"Bob strategy 3:{empty_cells[0]} ")
    return (empty_cells[0].y, empty_cells[0].x,lc) if empty_cells else None