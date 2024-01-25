import connect4

EMPTY = 0
NORTH_PIECE = 1
SOUTH_PIECE = 2

WINDOW_LENGTH_4 = 4
WINDOW_LENGTH_5 = 5

def evaluate_window_4_score(window,piece):
    if piece == NORTH_PIECE:
        opponent = SOUTH_PIECE
    else:
        opponent = NORTH_PIECE
    score = 0
    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(EMPTY) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(EMPTY) == 2:
        score += 2
    if window.count(opponent) == 4:
        score -= 10000
    elif window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 80
    return score

def evaluate_window_5_score(window,piece,col_count,is_horizontal,is_vertical):
    if piece == NORTH_PIECE:
        opponent = SOUTH_PIECE
    else:
        opponent = NORTH_PIECE
    score = 0
    if is_horizontal:
        if col_count > 7:
            if window.count(piece) == 4 and window.count(opponent) == 1:
                score += 20
            if window.count(opponent) == 4 and window.count(piece) == 1:
                score -= 80
        if window.count(piece) == 3 and window.count(EMPTY) == 2:
            score += 8
        if window.count(opponent) == 2 and window.count(EMPTY) == 3:
            if window[0] == EMPTY and window[-1] == EMPTY:
                score -= 80
    if is_vertical:
        if window.count(piece) == 4 and window.count(opponent) == 1:
            score += 20
        if window.count(opponent) == 4 and window.count(piece) == 1:
            score -= 80   
    return score

def get_window_4_score(board,piece):
    row_count = connect4.get_row_count(board)
    column_count = connect4.get_column_count(board)
    score = 0
    #Score center
    center_array = [int(i) for i in list(board[:,column_count//2])]
    center_count = center_array.count(piece)
    score += center_count * 3
    #Score horizontal
    not_empty_rows = connect4.get_not_empty_rows_index(board)
    if len(not_empty_rows) > 0:
        for r in not_empty_rows:
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(column_count-3):
                window = row_array[c:c+WINDOW_LENGTH_4]
                score += evaluate_window_4_score(window,piece)
    #Score vertical
    not_empty_columns = connect4.get_not_empty_columns_index(board)
    if len(not_empty_columns) > 0:
        for c in not_empty_columns:
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(row_count-3):
                window = col_array[r:r+WINDOW_LENGTH_4]
                score += evaluate_window_4_score(window,piece)
    #Score positive sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH_4)]
            score += evaluate_window_4_score(window,piece)
    #Score negative sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH_4)]
            score += evaluate_window_4_score(window,piece)
    return score

def get_window_5_score(board,piece):
    row_count = connect4.get_row_count(board)
    column_count = connect4.get_column_count(board)
    score = 0
    #Score horizontal
    not_empty_rows = connect4.get_not_empty_rows_index(board)
    if len(not_empty_rows) > 0:
        for r in not_empty_rows:
            row_array = [int(i) for i in list(board[r,:])]
            for c in range(column_count-4):
                window = row_array[c:c+WINDOW_LENGTH_5]
                score += evaluate_window_5_score(window,piece,column_count,True,False)
    #Score vertical
    not_empty_columns = connect4.get_not_empty_columns_index(board)
    if len(not_empty_columns) > 0:
        for c in not_empty_columns:
            col_array = [int(i) for i in list(board[:,c])]
            for r in range(row_count-4):
                window = col_array[r:r+WINDOW_LENGTH_5]
                score += evaluate_window_5_score(window,piece,column_count,False,True)
    return score


def get_board_score(board,piece):
    score = 0
    score += get_window_4_score(board,piece)
    return score

def get_full_board_score(board,piece):
    score = 0
    score += get_window_4_score(board,piece)
    score += get_window_5_score(board,piece)
    return score