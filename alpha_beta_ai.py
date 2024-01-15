import connect4
import math
import random

EMPTY = 0
NORTH_PIECE = 1
SOUTH_PIECE = 2

WINDOW_LENGTH = 4

def is_terminal_node(board):
    return connect4.is_winning_move(board,NORTH_PIECE) or connect4.is_winning_move(board,SOUTH_PIECE) or len(connect4.get_valid_column_locations(board)) == 0

def evaluate_window(window,piece):
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
        score -= 4
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
            score += evaluate_window(window,piece)
    #Score vertical
    for c in range(column_count):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(row_count-3):
            window = col_array[r:r+WINDOW_LENGTH]
            score += evaluate_window(window,piece)
    #Score positive sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window,piece)
    #Socre negative sloped diagonal
    for r in range(row_count-3):
        for c in range(column_count-3):
            window = [board[r+3-i][c+i] for i in range(WINDOW_LENGTH)]
            score += evaluate_window(window,piece)
    return score


def alpha_beta(board,depth,alpha,beta,maximizingPlayer,my_piece):
    if my_piece == NORTH_PIECE:
        opponent_piece = SOUTH_PIECE
    else:
        opponent_piece = NORTH_PIECE
    valid_locations = connect4.get_valid_column_locations(board)
    is_termial = is_terminal_node(board)
    if depth == 0 or is_termial:
        if is_termial:
            if connect4.is_winning_move(board,my_piece):
                return (None, 1000000)
            if connect4.is_winning_move(board, opponent_piece):
                return (None, -1000000)
            else: # Game over, no more pieces
                return (None, 0)
        else: #Depth is zero
            return (None, score_position(board,my_piece))
    if maximizingPlayer:
        value = -math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = connect4.get_next_open_row(board,col)
            temp_board = board.copy()
            connect4.drop_piece(temp_board,row,col,my_piece)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,False,my_piece)[1]
            if new_score > value:
                value = new_score
                best_col = col
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        return best_col,value
    else: #minPlayer
        value = math.inf
        best_col = random.choice(valid_locations)
        for col in valid_locations:
            row = connect4.get_next_open_row(board,col)
            temp_board = board.copy()
            connect4.drop_piece(temp_board,row,col,opponent_piece)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,True,my_piece)[1]
            if new_score < value:
                value = new_score
                best_col = col
            beta = min(beta,value)
            if alpha >= beta:
                break
        return  best_col,value

def get_move(board,my_piece):
    alpha = -math.inf
    beta = math.inf
    depth = 3
    return alpha_beta(board,depth,alpha,beta,True,my_piece)[0]