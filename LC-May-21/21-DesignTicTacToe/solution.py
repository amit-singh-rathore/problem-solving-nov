class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.a_row = [n] * n
        self.a_col = [n] * n
        self.a_se_d = n
        self.a_sw_d = n

        self.b_row = [n] * n
        self.b_col = [n] * n
        self.b_se_d = n
        self.b_sw_d = n
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            self.a_row[row] -= 1
            self.a_col[col] -= 1
            if row == col: self.a_se_d -= 1
            if row == len(self.a_row) - col - 1: self.a_sw_d -= 1
        if player == 2:
            self.b_row[row] -= 1
            self.b_col[col] -= 1
            if row == col: self.b_se_d -= 1
            if row == len(self.b_row) - col - 1: self.b_sw_d -= 1
        if min(self.a_row[row], self.a_col[col], self.a_se_d, self.a_sw_d) == 0:
            return 1
        if min(self.b_row[row], self.b_col[col], self.b_se_d, self.b_sw_d) == 0:
            return 2
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)