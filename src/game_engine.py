class GameEngine:

    def __init__(self, board, ai_player):
        self.board = board
        self.ai_player = ai_player

    def play_turn(self):
        move = self.ai_player.make_move(self.board)

        if move is None:
            return

        row, col = move
        self.board.place_mark(row, col, "O")