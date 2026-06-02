import io
from unittest.mock import Mock, patch
from src.board import Board
from src.cli_wrapper import CLI_Wrapper


def test_cli_player_wins_without_ai_move():

    board = Board()
    board.grid = [
        ["X", "X", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]
    game_engine = Mock()
    game = CLI_Wrapper(game_engine, board)

    with patch("builtins.input", side_effect=["0", "2"]), patch("sys.stdout", new=io.StringIO()) as fake_out:
        game.start_game()

    output = fake_out.getvalue()

    assert board.grid[0][2] == "X"
    assert "X wins!" in output
    game_engine.play_turn.assert_not_called()


def test_cli_draws_when_player_fills_last_cell():

    board = Board()
    board.grid = [
        ["X", "O", "X"],
        ["X", "O", "O"],
        ["O", "X", " "]
    ]
    game_engine = Mock()
    game = CLI_Wrapper(game_engine, board)

    with patch("builtins.input", side_effect=["2", "2"]), patch("sys.stdout", new=io.StringIO()) as fake_out:
        game.start_game()

    output = fake_out.getvalue()

    assert board.check_draw() is True
    assert "It's a draw!" in output
    game_engine.play_turn.assert_not_called()
