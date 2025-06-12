class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        sz = len(s)
        tz = len(t)

        # number of ways that construct t[:b] with s[:a]
        dp = [[-1] * sz for _ in range(tz)]

        def getdp(a, b):
            if b == 0 and s[a] == t[b]:
                return 1
            if a < b:
                return 0
            if s[a] != t[b]:
                return 0
            if dp[b][a] == -1:
                tmp = 0
                for i in range(a):
                    tmp += getdp(i, b-1)
                dp[b][a] = tmp
            return dp[b][a]
        ans = 0
        for i in range(sz):
            ans += getdp(i, tz-1)
        return ans