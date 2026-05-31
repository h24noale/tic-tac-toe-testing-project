class CLI_Wrapper:

    def __init__(self, game_engine, board):

        self.game_engine = game_engine
        self.board = board

    def display_board(self):

        print("\n")

        for row in self.board.grid:

            print(" | ".join(row))
            print("-" * 9)

    def start_game(self):

        print("Welcome to Tic Tac Toe!")

        while True:

            self.display_board()

            # Spelarens drag
            try:

                row = int(input("Choose row (0-2): "))
                col = int(input("Choose column (0-2): "))

            except ValueError:

                print("Invalid input. Please enter numbers.")
                continue

            # Försöker placera spelarens symbol
            if not self.board.place_mark(row, col, "X"):

                print("That position is already taken.")
                continue

            # Kollar om spelaren vann
            winner = self.board.check_winner()

            if winner:

                self.display_board()
                print(f"{winner} wins!")
                break

            # AI:s tur
            self.game_engine.play_turn()

            # Kollar om AI vann
            winner = self.board.check_winner()

            if winner:

                self.display_board()
                print(f"{winner} wins!")
                break

            # Kollar draw
            if self.board.check_draw():

                self.display_board()
                print("It's a draw!")
                break