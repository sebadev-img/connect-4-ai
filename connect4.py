import numpy as np

EMPTY = 0
NORTH_PIECE = 1
SOUTH_PIECE = 2

char_mapping = {' ': EMPTY, 'N': NORTH_PIECE, 'S': SOUTH_PIECE}

def create_board_from_string(string_board):
    string_rows = string_board.splitlines()
    board = np.array([[char_mapping[char] for char in row[1:-1]] for row in string_rows])
    flipped_board = board[::-1, :]
    return flipped_board

def get_row_count(board):
    return board.shape[0]

def get_column_count(board):
    return board.shape[1]

def get_piece_from_side(side):
    if side == "N":
        return NORTH_PIECE
    else: # side == "S"
        return SOUTH_PIECE

def is_valid_column_location(board, col):
    row_count = get_row_count(board)
    return board[row_count-1,col] == 0

def get_valid_column_locations(board):
    valid_locations = []
    column_count = get_column_count(board)
    for col in range(column_count):
        if is_valid_column_location(board,col):
            valid_locations.append(col)
    return valid_locations

def get_next_open_row(board,col):
    row_count = get_row_count(board)
    for row in range(row_count):
        if board[row][col] == 0:
            return row
        
def get_reverse_row(board,row):
    row_count = get_row_count(board)
    return (row_count -1) - row

def drop_piece(board,row,col,piece):
    board[row,col] = piece

def kill_row(board,row):
    row_count = get_row_count(board)
    if row_count > 6:
        return delete_row(board,row)
    else:
        return set_row_to_zero(board,row)        

def kill_column(board,column):
    column_count = get_column_count(board)
    if column_count > 7:
        return delete_column(board,column)
    else:
        return set_col_to_zero(board,column)

def delete_row(board,row):
    new_board = np.delete(board,row,axis=0)
    return new_board  

def delete_column(board,col): 
    new_board =np.delete(board,col,axis=1)
    return new_board    

def set_col_to_zero(board,col):  
    board[:,col] = 0
    return board    

def set_row_to_zero(board,row):
    board = np.delete(board, row, axis=0)
    row_of_zeros = np.zeros((1, board.shape[1]), dtype=board.dtype)
    board = np.vstack((board, row_of_zeros))
    return board

def get_not_empty_rows_index(board):
    rows_with_all_zeros = np.all(board == 0, axis=1)
    not_empty_rows = np.where(~rows_with_all_zeros)[0]
    return not_empty_rows

def get_not_empty_columns_index(board):
    columns_with_all_zeros = np.all(board == 0, axis=0)
    not_empty_columns = np.where(~columns_with_all_zeros)[0]
    return not_empty_columns
        
def is_winning_move(board,piece):
    row_count = get_row_count(board)
    column_count = get_column_count(board)            
    #Check horizontal if not empty
    not_empty_rows = get_not_empty_rows_index(board)
    if len(not_empty_rows > 0):
        for r in not_empty_rows:
            for c in range(column_count-3):
                if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                    return True
    #Check vertical if not empty
    not_empty_columns = get_not_empty_columns_index(board)
    if len(not_empty_columns) > 0:
        for c in not_empty_columns:
            for r in range(row_count-3):
                if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                    return True
    #Check diagonals if not empty row count > 3
    if len(not_empty_rows) > 3:
    #Check postivily sloped diagonal
        for c in range(column_count-3):
            for r in range(row_count-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True
        #Check negativily sloped diagonal
        for c in range(column_count-3):
            for r in range(3, row_count):
                if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                    return True
