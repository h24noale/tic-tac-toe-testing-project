class Board:

    def __init__(self):

        self.grid = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def place_mark(self, row, col, symbol):

        if self.grid[row][col] == " ":
            self.grid[row][col] = symbol
            return True

        return False

    def check_winner(self):

        # Rader
        for row in self.grid:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        # Kolumner
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != " ":
                return self.grid[0][col]

        # Diagonaler
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != " ":
            return self.grid[0][0]

        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != " ":
            return self.grid[0][2]

        return None

    def check_draw(self):

        for row in self.grid:

            if " " in row:
                return False

        return self.check_winner() is None