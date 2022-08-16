class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        if len(prices) == 1:
            return 0
        dp[0] = [-prices[0], 0]
        dp[1] = [-min(prices[0], prices[1]), max(dp[0][1], dp[0][0] + prices[1])]
        for i in range(2, len(prices)):
            dp[i] = [max(dp[i - 1][0], dp[i - 2][1] - prices[i]), max(dp[i - 1][1], dp[i - 1][0] + prices[i])]
    
        return dp[len(prices) - 1][1]
                