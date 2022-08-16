class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        ans = 0
        for r in range(m):
            for c in range(n):
                matrix[r][c] = int(matrix[r][c])
                ans = max(ans, matrix[r][c])
                if r > 0 and c > 0 and matrix[r][c] == 1:
                    prevSquare = matrix[r - 1][c - 1]
                    allone = True
                    rowcnt, colcnt = 0, 0
                    for testingRow in range(r - 1, r - prevSquare - 1, -1):
                        if matrix[testingRow][c] == 0:
                            allone = False
                            break
                        rowcnt += 1
                    for testingCol in range(c - 1, c - prevSquare - 1, -1):
                        if matrix[r][testingCol] == 0:
                            allone = False
                            break
                        colcnt += 1
                    if allone:
                        matrix[r][c] = prevSquare + 1
                    else:
                        matrix[r][c] = max(min(colcnt, rowcnt) + 1, 1)
                    ans = max(ans, matrix[r][c] * matrix[r][c])
        print(matrix)
        return ans
if __name__ == "__main__":
    sol = Solution()
    print(sol.maximalSquare([["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]))
