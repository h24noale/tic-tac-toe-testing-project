from unittest.main import main

from src.board import Board
from src.ai_player import AIPlayer
from src.game_engine import GameEngine
from src.cli_wrapper import CLI_Wrapper

board = Board()

ai_player = AIPlayer()

game_engine = GameEngine(board, ai_player)

game = CLI_Wrapper(game_engine, board)

game.start_game()

if __name__ == "__main__":
   main()