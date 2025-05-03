class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * 20
        dp[0] = 1
        dp[1] = 1

        # left subtree having 0~n-1 while right having n-1~0
        for i in range(2, 20):
            sum = 0
            for j in range(0, i // 2):
                sum += dp[j] * dp[i - j - 1]
            sum *= 2
            if i % 2 == 1:
                sum += dp[i // 2] * dp[i // 2]
            dp[i] = sum
        return dp[n]
        

if __name__ == "__main__":
    sol = Solution()
    print(sol.numTrees(3))