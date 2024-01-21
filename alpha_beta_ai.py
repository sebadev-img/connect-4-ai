import connect4
import score_system
import math
import random

EMPTY = 0
NORTH_PIECE = 1
SOUTH_PIECE = 2

WINDOW_LENGTH = 4

def is_terminal_node(board):
    return connect4.is_winning_move(board,NORTH_PIECE) or connect4.is_winning_move(board,SOUTH_PIECE) or len(connect4.get_valid_column_locations(board)) == 0

def simulate_drop_piece(board,depth,alpha,beta,my_piece,opponent_piece,best_col,value,is_my_turn):
    valid_locations = connect4.get_valid_column_locations(board)
    for col in valid_locations:
            row = connect4.get_next_open_row(board,col)
            temp_board = board.copy()
            if is_my_turn:
                connect4.drop_piece(temp_board,row,col,my_piece)
                new_score = alpha_beta(temp_board,depth-1,alpha,beta,False,my_piece)[3]
                if new_score > value:
                    value = new_score
                    best_col = col
                alpha = max(alpha,value)
                if alpha >= beta:
                    break
            else:
                connect4.drop_piece(temp_board,row,col,opponent_piece)
                new_score = alpha_beta(temp_board,depth-1,alpha,beta,True,my_piece)[3]
                if new_score < value:
                    value = new_score
                    best_col = col
                beta = min(beta,value)
                if alpha >= beta:
                    break                
    return best_col,value

def simulate_kill_row(board,depth,alpha,beta,my_piece,best_kill_row,value,is_my_turn):
    row_count = connect4.get_row_count(board)
    for row in range(row_count):
        temp_board = board.copy()
        if is_my_turn:
            temp_board = connect4.kill_row(temp_board,row)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,False,my_piece)[3]
            if new_score > value:
                    value = new_score
                    best_kill_row = row
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        else:
            temp_board = connect4.kill_row(temp_board,row)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,True,my_piece)[3]
            if new_score < value:
                    value = new_score
                    best_kill_row = row
            beta = min(beta,value)
            if alpha >= beta:
                break 
    return best_kill_row,value

def simulate_kill_col(board,depth,alpha,beta,my_piece,best_kill_col,value,is_my_turn):
    col_count = connect4.get_column_count(board)
    for col in range(col_count):
        temp_board = board.copy()
        if is_my_turn:
            temp_board = connect4.kill_col(temp_board,col)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,False,my_piece)[3]
            if new_score > value:
                    value = new_score
                    best_kill_col = col
            alpha = max(alpha,value)
            if alpha >= beta:
                break
        else:
            temp_board = connect4.kill_col(temp_board,col)
            new_score = alpha_beta(temp_board,depth-1,alpha,beta,True,my_piece)[3]
            if new_score < value:
                    value = new_score
                    best_kill_col = col
            beta = min(beta,value)
            if alpha >= beta:
                break   
    return best_kill_col,value


def alpha_beta(board,depth,alpha,beta,maximizingPlayer,my_piece):
    if my_piece == NORTH_PIECE:
        opponent_piece = SOUTH_PIECE
    else:
        opponent_piece = NORTH_PIECE    
    is_termial = is_terminal_node(board)
    if depth == 0 or is_termial:
        if is_termial:
            if connect4.is_winning_move(board,my_piece) and not connect4.is_winning_move(board,opponent_piece):
                return (None,None,None, 1000000)
            if connect4.is_winning_move(board, opponent_piece) and not connect4.is_winning_move(board,my_piece):
                return (None, -1000000)
            else: # Game over, no more pieces
                return (None, 0)
        else: #Depth is zero
            return (None,None,None, score_system.get_board_score(board,my_piece))
    if maximizingPlayer:
        value = -math.inf
        drop_col = None
        best_kill_row = None
        best_kill_col = None
        drop_col,drop_col_value = simulate_drop_piece(board,depth,alpha,beta,my_piece,opponent_piece,drop_col,value,is_my_turn=True)
        best_kill_row,best_kill_row_value = simulate_kill_row(board,depth,alpha,beta,my_piece,best_kill_row,value,is_my_turn=True)
        best_kill_col,best_kill_col_value = simulate_kill_col(board,depth,alpha,beta,my_piece,best_kill_col,value,is_my_turn=True)
        value_list = [drop_col_value,best_kill_row_value,best_kill_col_value]
        if max(value_list) == drop_col_value:
            return drop_col,None,None,drop_col_value
        elif max(value_list) == best_kill_row_value:
            return None,best_kill_row,None,best_kill_row_value
        else:
            return None,None,best_kill_col,best_kill_col_value
    else: #minPlayer
        value = math.inf
        drop_col = None
        best_kill_row = None
        best_kill_col = None
        drop_col,drop_col_value = simulate_drop_piece(board,depth,alpha,beta,my_piece,opponent_piece,drop_col,value,is_my_turn=False)
        best_kill_row,best_kill_row_value = simulate_kill_row(board,depth,alpha,beta,my_piece,best_kill_row,value,is_my_turn=False)
        best_kill_col,best_kill_col_value = simulate_kill_col(board,depth,alpha,beta,my_piece,best_kill_col,value,is_my_turn=False)
        value_list = [drop_col_value,best_kill_row_value,best_kill_col_value]
        if max(value_list) == drop_col_value:
            return drop_col,None,None,drop_col_value
        elif max(value_list) == best_kill_row_value:
            return None,best_kill_row,None,best_kill_row_value
        else:
            return None,None,best_kill_col,best_kill_col_value

def calculate_depth(board):
    row_count = connect4.get_row_count(board)
    column_count = connect4.get_column_count(board)
    if row_count <= 6 and column_count <= 7:
        return 6
    elif row_count <= 8 and column_count <= 9:
        return 5
    elif row_count <= 11 and column_count <= 12:
        return 4
    else:
        return 3

def get_move(board,my_piece):
    alpha = -math.inf
    beta = math.inf
    depth = calculate_depth(board)
    return alpha_beta(board,depth,alpha,beta,True,my_piece)