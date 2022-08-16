class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        recent_buy = prices[0]
        recent_sell = -1
        profit = 0
        accum = 0

        for i in range(1, len(prices)):
            if prices[i] - recent_buy - fee > profit:
                profit = prices[i] - recent_buy - fee
                recent_sell = prices[i]
            
            if prices[i] + fee < recent_sell:
                recent_buy = prices[i]
                accum += profit
                profit = 0
                recent_sell = -1

            if prices[i] < recent_buy:
                recent_buy = prices[i]
        
        return accum + profit

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([4, 5, 2, 4, 3, 1, 2, 5, 4], 1))