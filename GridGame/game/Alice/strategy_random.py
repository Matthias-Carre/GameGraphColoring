import random


def is_any(grid, bob_move):
    return True

def random_move(grid, bob_move):
    x = random.randint(0, grid.width - 1)
    y = random.randint(0, grid.height - 1)
    color = random.randint(1, 3)
    cell = grid.get_cell(x, y)
    while cell.value != 0 or color not in cell.color_options:
        x = random.randint(0, grid.width - 1)
        y = random.randint(0, grid.height - 1)
        color = random.randint(1, 3)
        cell = grid.get_cell(x, y)    
    return (x, y, color)
        