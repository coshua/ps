class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(0, n):
                if j == 0:
                    dp[j] = 1
                else:
                    dp[j] += dp[j - 1]
        return dp[n - 1]
if __name__ == "__main__":
    solution = Solution()
    print(solution.uniquePaths(3, 7))