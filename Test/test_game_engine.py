from unittest.mock import Mock
import unittest
from src.game_engine import GameEngine

def test_game_engine_initialization():

    board_mock = Mock()
    ai_player_mock = Mock()

    game_engine = GameEngine(board_mock, ai_player_mock)

    assert game_engine.board == board_mock
    assert game_engine.ai_player == ai_player_mock

def test_game_engine_make_ai_move():

    board_mock = Mock()
    ai_player_mock = Mock()

    ai_player_mock.make_move.return_value = (1, 1)

    game_engine = GameEngine(board_mock, ai_player_mock)

    game_engine.make_ai_move()

    ai_player_mock.make_move.assert_called_once_with(board_mock)
    board_mock.place_mark.assert_called_once_with(1, 1, "O")


def test_game_engine_play_turn_calls_ai_move():

    board_mock = Mock()
    ai_player_mock = Mock()

    ai_player_mock.make_move.return_value = (2, 0)

    game_engine = GameEngine(board_mock, ai_player_mock)

    result = game_engine.play_turn()

    ai_player_mock.make_move.assert_called_once_with(board_mock)
    board_mock.place_mark.assert_called_once_with(2, 0, "O")
    assert result is True


def test_game_engine_play_turn_returns_false_on_full_board():

    board_mock = Mock()
    ai_player_mock = Mock()

    ai_player_mock.make_move.return_value = None

    game_engine = GameEngine(board_mock, ai_player_mock)

    result = game_engine.play_turn()

    assert result is False
    board_mock.place_mark.assert_not_called()