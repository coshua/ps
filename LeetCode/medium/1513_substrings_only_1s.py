class Solution:
    def numSub(self, s: str) -> int:
        dp = [-1] * (len(s) + 1)
        dp[0] = 0
        def getDP(dp, i):
            if dp[i] == -1:
                dp[i] = getDP(dp, i - 1) + i
                dp[i] %= 10**9 + 7

            return dp[i]
        
        cnt = 0
        lst = s.split("0")
        for group in lst:
            cnt += getDP(dp, len(group))
        
        return cnt % (10**9 + 7)