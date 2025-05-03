class Solution:
    def maxTaxiEarnings(self, n: int, rides: list[list[int]]) -> int:
        rides.sort(reverse=True)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = max(dp[i], dp[i - 1])
            while rides and rides[-1][0] == i:
                s, e, t = rides.pop()
                dp[e] = max(dp[e], dp[s] + e - s + t)
        
        return dp[n]