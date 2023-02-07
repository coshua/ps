class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0] + [-1] * high

        def getDP(n):
            if dp[n] == -1:
                dp[n] = 0
                if n == one:
                    dp[n] += 1
                if n == zero:
                    dp[n] += 1
                if n - zero > 0:
                    dp[n] += getDP(n - zero)
                if n - one > 0:
                    dp[n] += getDP(n - one)
                dp[n] %= 10**9 + 7
            return dp[n]
        
        sm = 0
        for i in range(low, high + 1):
            sm += getDP(i)
        
        return sm % (10**9 + 7)