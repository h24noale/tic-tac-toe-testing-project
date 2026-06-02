import io
from unittest.mock import Mock, patch
from src.board import Board
from src.cli_wrapper import CLI_Wrapper


def test_cli_invalid_input_then_valid_move():

    board = Board()
    board.grid = [
        ["X", "X", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    game_engine = Mock()
    game = CLI_Wrapper(game_engine, board)

    with patch("builtins.input", side_effect=["bad", "bad", "0", "2"]), patch("sys.stdout", new=io.StringIO()) as fake_out:
        game.start_game()

    output = fake_out.getvalue()

    assert "Invalid input" in output
    assert board.grid[0][2] == "X"
    assert "X wins!" in output
    game_engine.play_turn.assert_not_called()


def test_cli_position_taken_retries():

    board = Board()
    board.grid = [
        ["X", " ", "X"],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    game_engine = Mock()
    game = CLI_Wrapper(game_engine, board)

    with patch("builtins.input", side_effect=["0", "0", "0", "1"]), patch("sys.stdout", new=io.StringIO()) as fake_out:
        game.start_game()

    output = fake_out.getvalue()

    assert "That position is already taken." in output
    assert board.grid[0][1] == "X"
    assert "X wins!" in output
    game_engine.play_turn.assert_not_called()


def test_cli_ai_wins_after_player_move():

    board = Board()
    board.grid = [
        ["O", "X", " "],
        ["O", "X", " "],
        [" ", " ", " "]
    ]

    def ai_winning_move():
        board.place_mark(2, 0, "O")

    game_engine = Mock()
    game_engine.play_turn.side_effect = ai_winning_move
    game = CLI_Wrapper(game_engine, board)

    with patch("builtins.input", side_effect=["2", "2"]), patch("sys.stdout", new=io.StringIO()) as fake_out:
        game.start_game()

    output = fake_out.getvalue()

    assert board.grid[2][0] == "O"
    assert "O wins!" in output
    game_engine.play_turn.assert_called_once()
