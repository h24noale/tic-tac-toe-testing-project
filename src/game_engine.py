class GameEngine:

    def __init__(self, board, ai_player):

        self.board = board
        self.ai_player = ai_player

    def play_turn(self):

        move = self.ai_player.make_move(self.board)

        if move is None:
            return False

        row, col = move
        self.board.place_mark(row, col, "O")
        return True
    
    def make_ai_move(self):

        move = self.ai_player.make_move(self.board)

        if move is not None:
            row, col = move
            self.board.place_mark(row, col, "O")
            return True

        return False