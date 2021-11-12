class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        price_at_buy = prices[0]
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - price_at_buy)
            price_at_buy = min(price_at_buy, prices[i])
        
        return profit