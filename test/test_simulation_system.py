import sys
sys.path.append('..')
import unittest
import simulation_system
import numpy as np


class TestSimulationSystem(unittest.TestCase):

    def setUp(self):
        # Set up any resources needed for the tests
        self.BOARD = np.array([[]])

    def test_get_best_col(self):
        board = np.array([[0,0,1,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_col(board,piece)[0]
        self.assertEqual(result, 2)
    
    def test_get_best_kill_row(self):
        board = np.array([[0,0,1,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,2,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_kill_row(board,piece)[0]
        self.assertEqual(result, 2)

    def test_get_best_kill_col(self):
        board = np.array([[0,0,1,1,1,2,1,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_kill_col(board,piece)[0]
        self.assertEqual(result, 5)

    def test_get_best_col_v2(self):
        board = np.array([[0,0,1,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,1,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_col_v2(board,piece)[0]
        self.assertEqual(result, 2)

    def test_get_best_kill_row_v2(self):
        board = np.array([[0,0,0,1,2,0,2],
                          [0,0,0,1,0,2,0],
                          [0,0,0,1,0,0,0],
                          [0,0,0,2,0,0,0],
                          [0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_kill_row_v2(board,piece)[0]
        self.assertEqual(result, 3)

    def test_get_best_kill_col_v2(self):
        board = np.array([[0,0,1,1,1,2,1,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],
                          [0,0,0,0,0,0,0,0],])
        piece = 1
        result = simulation_system.get_best_kill_col_v2(board,piece)[0]
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()