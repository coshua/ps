class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dict = set(wordDict)
        dp = [300] * len(s)

        for i in range(len(s) + 1):
            for j in range(0, i):
                temp = s[j: i]
                if temp in dict:
                    if j > 0:
                        dp[i - 1] = min(dp[i - 1], min(dp[j - 1], j))
                    else:
                        dp[i - 1] = min(dp[i - 1], j)
                        
        return dp[-1] == 0

if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsandog", ["cats", "a", "ndog"]))