import connect4
import score_system
import random

def get_best_col(board,piece):
    valid_locations = connect4.get_valid_column_locations(board)
    best_score = -100000
    best_col = random.choice(valid_locations)
    for col in valid_locations:
        row = connect4.get_next_open_row(board,col)
        temp_board = board.copy()
        connect4.drop_piece(temp_board,row,col,piece)
        score = score_system.get_board_score(temp_board,piece)
        if (score > best_score):
            best_score = score
            best_col = col
    return best_col,best_score

def get_best_kill_row(board,piece):
    row_count = connect4.get_row_count(board)
    best_score = -100000
    best_kill_row = random.randint(0,row_count-1)
    for row in range(row_count):
        temp_board = board.copy()
        temp_board = connect4.kill_row(temp_board,row) 
        score = score_system.get_board_score(temp_board,piece)
        if (score > best_score):
            best_score = score
            best_kill_row = row
    return best_kill_row,best_score

def get_best_kill_col(board,piece):
    column_count = connect4.get_column_count(board)
    best_score = -100000
    best_kill_col = random.randint(0,column_count-1)
    for col in range(column_count):
        temp_board = board.copy()
        temp_board = connect4.kill_column(temp_board,col)
        score = score_system.get_board_score(temp_board,piece)
        if (score > best_score):
            best_score = score
            best_kill_col = col
    return best_kill_col,best_score