class Solution:
    def countSubstrings(self, s: str) -> int:
        sz = len(s)
        dp = [[-1] * sz for _ in range(sz)]
        def getdp(lo, hi):
            if lo > hi:
                return True
            if dp[lo][hi] == -1:
                if s[lo] != s[hi]:
                    dp[lo][hi] = False
                else:
                    dp[lo][hi] = getdp(lo + 1, hi - 1)
            return dp[lo][hi]
        
        ans = 0
        for i in range(sz):
            for j in range(i, sz):
                if getdp(i, j):
                    ans += 1
        return ans

            