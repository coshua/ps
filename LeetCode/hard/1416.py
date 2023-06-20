class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        dp = [0] * (len(s))
        mod = 10**9 + 7
        for i in range(len(s)):
            for j in range(max(0, i - len(str(k)) + 1), i + 1):
                wd = s[j : i + 1]
                if s[j] != "0" and int(wd) <= k:
                    if j > 0:
                        dp[i] += dp[j - 1]
                    else:
                        dp[i] += 1
                dp[i] %= mod
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfArrays("1327", 1000))
