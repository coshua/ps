class Solution:
    def rotate_by_line(self, matrix, n):
        for i in range(n, len(matrix) - n - 1):
            temp = matrix[i][n]
            matrix[i][n] = matrix[len(matrix) - n - 1][i]
            matrix[len(matrix) - n - 1][i] = matrix[len(matrix) - 1 - i][len(matrix) - n - 1]
            matrix[len(matrix) -1 - i][len(matrix) - n - 1] = matrix[n][len(matrix) - 1 - i]
            matrix[n][len(matrix) - 1 - i] = temp
        
    def rotate(self, matrix: list[list[int]]) -> None:
        leng = len(matrix) // 2
        for i in range(0, leng):
            self.rotate_by_line(matrix, i)