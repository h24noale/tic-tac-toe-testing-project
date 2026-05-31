from src.board import Board
from src.ai_player import AIPlayer


def test_ai_returns_valid_move():

    board = Board()
    ai = AIPlayer()

    move = ai.make_move(board)

    assert move is not None


def test_ai_returns_free_position():

    board = Board()
    ai = AIPlayer()

    row, col = ai.make_move(board)

    assert board.grid[row][col] == " "


def test_ai_returns_none_on_full_board():

    board = Board()
    ai = AIPlayer()

    board.grid = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", "X"]
    ]

    assert ai.make_move(board) is None


def test_ai_returns_coordinates_inside_board():

    board = Board()
    ai = AIPlayer()

    row, col = ai.make_move(board)

    assert 0 <= row <= 2
    assert 0 <= col <= 2
   