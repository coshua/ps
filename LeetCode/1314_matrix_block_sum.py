class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) ->list[list[int]]:
        r = len(mat)
        c = len(mat[0])
        dp = [[0] * c for _ in range(r)]

        def getColSum(row, col):
            temp = 0
            for i in range(max(0, row - k), min(r, row + k + 1)):
                temp += mat[i][col]
            return temp
        def getBlock(row, col):
            if dp[row][col] == 0:
                prevBlock = 0
                if row > 0:
                    prevBlock = getBlock(row - 1, col)
                    if row - k > 0:
                        prevBlock -= sum(mat[row - k - 1][max(0, col - k): min(c, col + k + 1)])
                    if row + k < r:
                        prevBlock += sum(mat[row + k][max(0, col - k): min(c, col + k + 1)])
                else:
                    prevBlock = getBlock(row, col - 1)
                    if col - k > 0:
                        prevBlock -= getColSum(row, col - k - 1)
                    if col + k < c:
                        prevBlock += getColSum(row, col + k)
                dp[row][col] = prevBlock

            return dp[row][col]
        temp = 0
        for i in range(min(k + 1, r)):
            temp += sum(mat[i][:min(k + 1, c)])
        dp[0][0] = temp
        for i in range(c):
            getBlock(r - 1, i)

        return(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9],[1,2,3]], 2))
