import simulation_system
import score_system
import connect4

NORTH_PIECE = 1
SOUTH_PIECE = 2

def pick_best_move(board,piece):
    drop_col,drop_col_score = simulation_system.get_best_col_v2(board,piece)
    kill_row,kill_row_score = simulation_system.get_best_kill_row_v2(board,piece)
    kill_col,kill_col_score = simulation_system.get_best_kill_col_v2(board,piece)
    score_list = [drop_col_score,kill_row_score,kill_col_score]
    if max(score_list) == drop_col_score:
        return drop_col,None,None
    elif max(score_list) == kill_row_score:
        if kill_row_score < 20:
            kill_row = get_best_row(board,piece,kill_row)
        return None,kill_row,None
    else:
        if kill_col_score < 20:
            kill_col = get_best_col(board,piece,kill_col)
        return None,None,kill_col
    

def get_best_row(board,piece,kill_row):
    if piece == NORTH_PIECE:
        opponent = SOUTH_PIECE
    else:
        opponent = NORTH_PIECE
    column_count = connect4.get_column_count(board)
    best_row = kill_row
    best_row_arr = [int(i) for i in list(board[kill_row,:])]
    not_empty_rows = connect4.get_not_empty_rows_index(board)
    for row in not_empty_rows:
        row_arr = [int(i) for i in list(board[row,:])]
        row_score = score_system.get_row_score(row_arr,column_count,piece)
        if row_score >= 0:
            if row_arr.count(opponent) > best_row_arr.count(opponent):
                best_row = row
                best_row_arr = row_arr
            elif row_arr.count(opponent) == best_row_arr.count(opponent):
                if row_arr.count(piece) < best_row_arr.count(piece):
                    best_row = row
                    best_row_arr = row_arr
    return best_row

def get_best_col(board,piece,kill_col):
    if piece == NORTH_PIECE:
        opponent = SOUTH_PIECE
    else:
        opponent = NORTH_PIECE
    row_count = connect4.get_row_count(board)
    best_col = kill_col
    best_col_arr = [int(i) for i in list(board[:,kill_col])]
    not_empty_columns = connect4.get_not_empty_columns_index(board)
    for col in not_empty_columns:
        col_arr =[int(i) for i in list(board[:,col])]
        col_score = score_system.get_col_score(col_arr,row_count,piece)
        if col_score >= 0:
            if col_arr.count(opponent) > best_col_arr.count(opponent):
                best_col = col
                best_col_arr = col_arr
            elif col_arr.count(opponent) == best_col_arr.count(opponent):
                if col_arr.count(piece) < best_col_arr.count(piece):
                    best_col = col
                    best_col_arr = col_arr
    return best_col
    

def get_move(board,piece):
    return pick_best_move(board,piece)