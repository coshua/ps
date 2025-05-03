class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [-1] * (k + maxPts)
        prob = 1 / maxPts
        dp[0] = 0

        def getDP(c, dp):
            if dp[c] == -1:
                if c <= maxPts:
                    dp[c] = prob
                else:
                    dp[c] = 0
                for i in range(max(0, c - maxPts), c):
                    dp[c] += getDP(i, dp) * prob
            return dp[c]

        ans = 0
        for i in range(k, min(n + 1, k - 1 + maxPts)):
            ans += getDP(i, dp)
        print(dp)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.new21Game(21, 17, 10))
