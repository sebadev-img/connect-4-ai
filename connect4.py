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
        
def is_winning_move(board,piece):
    row_count = get_row_count(board)
    column_count = get_column_count(board)            
    #Check horizontal
    for c in range(column_count-3):
        for r in range(row_count):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    #Check vertical
    for c in range(column_count):
        for r in range(row_count-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
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
