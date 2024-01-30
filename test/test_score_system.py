import sys
sys.path.append('..')
import unittest
import score_system
import numpy as np

class TestScoreSystem(unittest.TestCase):

    def setUp(self):
        # Set up any resources needed for the tests
        self.BOARD = np.array([[0,0,1,1,1,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0],
                               [0,0,0,0,0,0,0]]) 

    def test_evaluate_window_4_score(self):
        window = [1,1,0,0]
        piece = 1
        result = score_system.evaluate_window_4_score(window,piece)
        self.assertEqual(result, 2)

    def test_evaluate_window_5_score(self):
        window = [1,1,1,2,1]
        piece = 1
        col_count = 7
        is_horizontal = False
        is_vertical = True
        result = score_system.evaluate_window_5_score(window,piece,col_count,is_horizontal,is_vertical)
        self.assertEqual(result, 20)

    def test_get_window_4_score(self):
        board = self.BOARD
        piece = 1
        result = score_system.get_window_4_score(board,piece)
        self.assertEqual(result, 17)
    
    def test_get_window_5_score(self):
        board = self.BOARD
        piece = 1
        result = score_system.get_window_5_score(board,piece)
        self.assertEqual(result, 24)
    
    def test_get_board_score(self):
        board = self.BOARD
        piece = 1
        result = score_system.get_board_score(board,piece)
        self.assertEqual(result, 17)
    
    def test_get_full_board_score(self):
        board = self.BOARD
        piece = 1
        result = score_system.get_full_board_score(board,piece)
        self.assertEqual(result, 41)

    def test_get_row_score(self):
        row_array = [0,1,1,0,0,0,0]
        column_count = 7
        piece = 1
        result = score_system.get_row_score(row_array,column_count,piece)
        self.assertEqual(result, 4)

    def test_get_col_score(self):
        col_array = [1,1,0,0,0,0]
        row_count = 6
        piece = 1
        result = score_system.get_col_score(col_array,row_count,piece)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()