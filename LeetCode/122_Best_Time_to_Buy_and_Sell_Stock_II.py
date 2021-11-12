class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        acumProfit = 0
        price_at_buy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] <= price_at_buy:
                price_at_buy = prices[i]
            else:
                acumProfit += prices[i] - price_at_buy
                price_at_buy = prices[i]
        
        return acumProfit