class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        dp = []
        for i in range(1, rowIndex + 2):
            temp = [1] * i
            for j in range(1, i - 1):
                temp[j] = dp[-1][j] + dp[-1][j - 1]
            dp.append(temp)
        return dp[rowIndex]