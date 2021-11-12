class Solution:
    def setZeroes(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        row_to_be_zeroes = [0] * (R + 1)
        col_to_be_zeroes = [0] * (C + 1)

        for i, row in enumerate(matrix):
            for j, item in enumerate(row):
                if item == 0:
                    row_to_be_zeroes[i] = 1
                    col_to_be_zeroes[j] = 1
        
        for i in range(R):
            if row_to_be_zeroes[i] == 1:
                for j in range(C):
                    matrix[i][j] = 0
        for j in range(C):
            if col_to_be_zeroes[j] == 1:
                for i in range(R):
                    matrix[i][j] = 0
if __name__ == "__main__":
    solution = Solution()
    print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))