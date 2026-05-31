import unittest
from src.board import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_place_mark(self):
        self.assertTrue(self.board.place_mark(0, 0, "X"))
        self.assertEqual(self.board.grid[0][0], "X")
        self.assertFalse(self.board.place_mark(0, 0, "O"))

    def test_check_winner_row(self):
        self.board.grid = [
            ["X", "X", "X"],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_check_winner_column(self):
        self.board.grid = [
            ["O", " ", " "],
            ["O", " ", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(self.board.check_winner(), "O")

    def test_check_winner_diagonal(self):
        self.board.grid = [
            ["X", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.board.check_winner(), "X")

    def test_check_draw(self):
        self.board.grid = [
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ]
        self.assertTrue(self.board.check_draw())