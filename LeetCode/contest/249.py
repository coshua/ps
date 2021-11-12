class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        dp = [[[0 for x in range(n)] for y in range(m)] for z in range(3)]
        dp[0][0][0] = 1
        dp[1][0][0] = 1
        dp[2][0][0] = 1
        for j in range(n):
            for i in range(m):
                for k in range(3):
                    c1 = (k + 1) % 3
                    c2 = (k + 2) % 3
                    if j > 0 and i > 0:
                        dp[k][i][j] = 4 * dp[k][i - 1][j - 1] + dp[c1][i - 1][j - 1] + dp[c2][i - 1][j - 1]
                    elif j > 0:
                        dp[k][i][j] = dp[c1][i][j - 1] + dp[c2][i][j - 1]
                    elif i > 0:
                        dp[k][i][j] = dp[c1][i - 1][j] + dp[c2][i - 1][j]
                    dp[k][i][j] %= 1000000007

        return 3 * dp[0][m - 1][n - 1] % 1000000007

if __name__ == "__main__":
    solution = Solution()
    print(solution.colorTheGrid(5, 5))