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