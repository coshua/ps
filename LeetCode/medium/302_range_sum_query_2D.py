class NumMatrix:
    mat = None
    def __init__(self, matrix: list[list[int]]):
        self.mat = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(len(matrix)):
            self.mat[r][0] = matrix[r][0]
            for c in range(1, len(matrix[0])):
                self.mat[r][c] = self.mat[r][c - 1] + matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        blk = 0
        for r in range(row1, row2 + 1):
            blk += self.mat[r][col2]
            blk -= self.mat[r][col1 - 1] if col1 > 0 else 0
        return blk


if __name__ == "__main__":
    sol = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])
    print(sol.sumRegion(1, 2, 2, 4))