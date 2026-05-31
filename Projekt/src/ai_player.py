import random

class AIPlayer:

    def make_move(self, board):

        available_moves = []

        for row in range(3):
            for col in range(3):

                if board.grid[row][col] == " ":
                    available_moves.append((row, col))

        return random.choice(available_moves)