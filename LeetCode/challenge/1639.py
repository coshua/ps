class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        ln = len(target)
        mod = 10**9 + 7
        d = [[0] * 26 for _ in range(len(words[0]))]
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)):
                d[j][ord(w[j]) - ord("a")] += 1

        dp = [[-1] * ln for _ in range(len(words[0]))]

        def getDP(wid, tid):
            if dp[wid][tid] == -1:
                prevsum = 0
                cur = d[wid][ord(target[tid]) - ord("a")]
                if cur == 0:
                    dp[wid][tid] = 0
                elif tid > 0:
                    for i in range(tid - 1, wid):
                        prevsum += getDP(i, tid - 1)
                    dp[wid][tid] = (prevsum * cur) % mod
                else:
                    dp[wid][tid] = cur
            return dp[wid][tid]

        ans = 0
        for i in range(ln - 1, len(words[0])):
            ans += getDP(i, ln - 1)
        ans %= mod
        return ans


sol = Solution()
print(sol.numWays(["acca", "bbbb", "caca"], "aba"))
