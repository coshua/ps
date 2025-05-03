import sys
sys.setrecursionlimit(10 ** 9)

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [-1] * 10001
        for i in range(1, 101):
            num = i * i
            dp[num] = 1
            # cnt = 2
            # num *= 2
            # while num < 10001:
            #     dp[num] = cnt
            #     cnt += 1
            #     num = i * i * cnt
        
        def getDP(n):
            if dp[n] == -1:
                minusage = n
                for i in range(1, n // 2 + 1):
                    minusage = min(minusage, getDP(i) + getDP(n - i))
                dp[n] = minusage
            return dp[n]
        getDP(n)
        print(dp[1:21])
        return getDP(n)

if __name__ == "__main__":
    solution = Solution()
    print(solution.numSquares(7168))