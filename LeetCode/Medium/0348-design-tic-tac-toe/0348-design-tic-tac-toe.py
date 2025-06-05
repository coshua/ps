class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        # rows[row] = -3 indicates player 1 put 3 stones in the row
        self.diag = 0
        self.anti_diag = 0
        self.sz = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.rows[row] += 1
            self.cols[col] += 1
            if row == col:
                self.diag += 1
            if row == abs(col - self.sz) -1:
                self.anti_diag += 1
            if self.sz in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
                return 1
        elif player == 2:
            self.rows[row] -= 1
            self.cols[col] -= 1
            if row == col:
                self.diag -= 1
            if row == abs(col - self.sz) -1:
                self.anti_diag -= 1
            if -self.sz in [self.rows[row], self.cols[col], self.diag, self.anti_diag]:
                return 2
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)