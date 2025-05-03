class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        dp = [[] for i in range(len(s))]

        for i in range(len(s)):
            for wd in wordDict:
                if i - len(wd) + 1 >= 0 and s[i - len(wd) + 1 : i + 1] == wd:
                    if i - len(wd) + 1 == 0:
                        dp[i].append(wd)
                    else:
                        for prevwd in dp[i - len(wd)]:
                            dp[i].append(prevwd + " " + wd)
        print(dp)
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
