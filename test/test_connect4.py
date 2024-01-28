import sys
sys.path.append('..')
import unittest
import connect4
import numpy as np

class TestConnect4(unittest.TestCase):

    def setUp(self):
        # Set up any resources needed for the tests
        self.STRING_BOARD = "|       |\n|       |\n|       |\n|   S   |\n|   NS  |\n| SNNNS |\n"
        self.BOARD = np.array([[0,2,1,1,1,2,0],
                               [0,0,0,1,2,0,0],
                               [0,0,0,2,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0]])    

    def test_create_board_from_string(self):
        string_board = self.STRING_BOARD
        result = connect4.create_board_from_string(string_board)
        self.assertTrue(np.array_equal(result, self.BOARD))

    def test_get_row_count(self):
        board = self.BOARD
        result = connect4.get_row_count(board)
        self.assertEqual(result,6) 

    def test_get_column_count(self):
        board = self.BOARD
        result = connect4.get_column_count(board)
        self.assertEqual(result,7)
    
    def test_get_piece_from_side(self):
        side = "N"
        result = connect4.get_piece_from_side(side)
        self.assertEqual(result,1)

    def test_is_valid_column_location(self):
        board = self.BOARD
        col = 0
        result = connect4.is_valid_column_location(board,col)
        self.assertEqual(result,True)
    
    def test_get_valid_column_locations(self):
        board = self.BOARD
        result = connect4.get_valid_column_locations(board)
        self.assertEqual(result,[0,1,2,3,4,5,6])

    def test_get_next_open_row(self):
        board = self.BOARD
        col = 0
        result = connect4.get_next_open_row(board,col)
        self.assertEqual(result,0)

    def test_get_reverse_row(self):
        board = self.BOARD
        row = 0
        result = connect4.get_reverse_row(board,row)
        self.assertEqual(result, 5)

    def test_drop_piece(self):
        board = self.BOARD
        temp_board = board
        new_board = np.array([[0,2,1,1,1,2,0],
                              [0,1,0,1,2,0,0],
                              [0,0,0,2,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]])
        row = 1
        col = 1
        piece = 1
        connect4.drop_piece(temp_board,row,col,piece)
        result = temp_board
        self.assertTrue(np.array_equal(result, new_board))
    
    def test_kill_row(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,1,2,0],
                              [0,0,0,2,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]])
        row = 1
        result = connect4.kill_row(board,row)
        self.assertTrue(np.array_equal(result, new_board))
    
    def test_kill_column(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,1,0,0],
                              [0,0,0,1,2,0,0],
                              [0,0,0,2,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]])
        column = 5
        result = connect4.kill_column(board,column)
        self.assertTrue(np.array_equal(result, new_board))
    
    def test_delete_row(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,1,2,0],
                              [0,0,0,1,2,0,0],
                              [0,0,0,2,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],])
        row = 5
        result = connect4.delete_row(board,row)
        self.assertTrue(np.array_equal(result, new_board))
    
    def test_delete_column(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,2,0],
                              [0,0,0,1,0,0],
                              [0,0,0,2,0,0],
                              [0,0,0,0,0,0],
                              [0,0,0,0,0,0],
                              [0,0,0,0,0,0]])
        col = 4
        result = connect4.delete_column(board,col)
        self.assertTrue(np.array_equal(result, new_board))

    def test_set_col_to_zero(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,0,2,0],
                              [0,0,0,1,0,0,0],
                              [0,0,0,2,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]])
        col = 4
        result = connect4.set_col_to_zero(board,col)
        self.assertTrue(np.array_equal(result, new_board))
    
    def test_set_row_to_zero(self):
        board = self.BOARD
        new_board = np.array([[0,2,1,1,1,2,0],
                              [0,0,0,1,2,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0],
                              [0,0,0,0,0,0,0]])
        row = 2
        result = connect4.set_row_to_zero(board,row)
        self.assertTrue(np.array_equal(result, new_board))

    def test_get_not_empty_rows_index(self):
        board = self.BOARD
        arr = np.array([0,1,2])
        result = connect4.get_not_empty_rows_index(board)
        self.assertTrue(np.array_equal(result, arr))

    def test_get_not_empty_columns_index(self):
        board = self.BOARD
        arr = np.array([1,2,3,4,5])
        result = connect4.get_not_empty_columns_index(board)
        self.assertTrue(np.array_equal(result, arr))

    def test_is_winning_move(self):
        board = self.BOARD
        piece = 1
        result = connect4.is_winning_move(board,piece)
        self.assertEqual(result,None)


if __name__ == '__main__':
    unittest.main()