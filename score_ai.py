import connect4
import random

EMPTY = 0
NORTH_PIECE = 1
SOUTH_PIECE = 2

WINDOW_LENGTH = 4

def evaluate_window_score(window,piece):
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
    if window.count(opponent) == 3 and window.count(EMPTY) == 1:
        score -= 80
    return score

def score_position(board,piece):
    row_count = connect4.get_row_count(board)
    column_count = connect4.get_column_count(board)
    score = 0
    #Score center
    center_array = [int(i) for i in list(board[:,column_count//2])]
    center_count = center_array.count(piece)
    score += center_count * 3
    #Score horizontal
    for r in range(row_count):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(column_count-3):
            window = row_array[c:c+WINDOW_LENGTH]
            score += evaluate_window_score(window,piece)
    #Score vertical
    for c in range(column_count):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(row_count-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window_score(window,piece)
    #Score positive sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window_score(window,piece)
    #Score negative sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window_score(window,piece)
    return score

def pick_best_move(board,piece):
    valid_locations = connect4.get_valid_column_locations(board)
    best_score = -10000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = connect4.get_next_open_row(board,col)
        temp_board = board.copy()
        connect4.drop_piece(temp_board,row,col,piece)
        score = score_position(temp_board,piece)
        if (score > best_score):
            best_score = score
            best_col = col
    return best_col

def get_move(board,piece):
    return pick_best_move(board,piece)