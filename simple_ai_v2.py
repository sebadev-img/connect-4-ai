import simulation_system

def pick_best_move(board,piece):
    drop_col,drop_col_score = simulation_system.get_best_col_v2(board,piece)
    kill_row,kill_row_score = simulation_system.get_best_kill_row_v2(board,piece)
    kill_col,kill_col_score = simulation_system.get_best_kill_col_v2(board,piece)
    score_list = [drop_col_score,kill_row_score,kill_col_score]
    if max(score_list) == drop_col_score:
        return drop_col,None,None
    elif max(score_list) == kill_row_score:
        return None,kill_row,None
    else:
        return None,None,kill_col

def get_move(board,piece):
    return pick_best_move(board,piece)