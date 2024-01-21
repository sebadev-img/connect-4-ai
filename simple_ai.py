import simulation_system

def pick_best_move(board,piece):
    best_col = simulation_system.get_best_col(board,piece)[0]
    return best_col

def get_move(board,piece):
    return pick_best_move(board,piece)