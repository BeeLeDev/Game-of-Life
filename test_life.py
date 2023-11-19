import unittest
from life import *

class TestLife(unittest.TestCase):
    def test_dead(self):
        board_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        expected_state = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        self.assertEqual(next_board_state(board_state), expected_state)

    def test_underpopulation(self):
        board_state = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0],
        ]
        expected_state = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0],
        ]
        self.assertEqual(next_board_state(board_state), expected_state)
    
    def test_overpopulation(self):
        board_state = [
            [1, 1, 1],
            [1, 0, 1],
            [0, 0, 0],
        ]
        expected_state = [
            [1, 0, 1],
            [1, 0, 1],
            [0, 0, 0],
        ]
        self.assertEqual(next_board_state(board_state), expected_state)

    def test_reproduction(self):
        board_state = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        expected_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0],
        ]
        self.assertEqual(next_board_state(board_state), expected_state)

if __name__ == "__main__":
    unittest.main()