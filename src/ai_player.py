import random

class AIPlayer:

    def make_move(self, board):

        available_moves = []

        for row in range(3):
            for col in range(3):
                if board.grid[row][col] == " ":
                    available_moves.append((row, col))

        if not available_moves:
            return None

        return random.choice(available_moves)