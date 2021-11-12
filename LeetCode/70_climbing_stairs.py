class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[0] = [1, 0]
        dp[1] = [1, 0]
        for i in range(2, n + 1):
            dp[i] = [dp[i - 1][0] + dp[i - 1][1], dp[i - 2][0] + dp[i - 2][1]]
        
        return sum(dp[n])

if __name__ == "__main__":
    solution = Solution()
    print(solution.climbStairs(5)) 