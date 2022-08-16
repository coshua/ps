class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        slen, plen = len(s), len(p)

        # if sum(window) == 0 it means anagram at current index.
        window = [0] * 26 

        for ch in p:
            window[ord(ch) - ord('a')] += 1

        ans = []
        # initial window
        for i in range(plen):
            window[ord(s[i]) - ord('a')] -= 1

        # it means anagram if diff == 0
        diff = 0
        for i in range(26):
            diff += abs(window[i])

        if diff == 0:
            ans.append(0)

        for i in range(1, slen - plen + 1):

            diff -= abs(window[ord(s[i - 1]) - ord('a')])
            diff -= abs(window[ord(s[i + plen - 1]) - ord('a')])
            window[ord(s[i - 1]) - ord('a')] += 1
            window[ord(s[i + plen - 1]) - ord('a')] -= 1

            diff += abs(window[ord(s[i - 1]) - ord('a')])
            diff += abs(window[ord(s[i + plen - 1]) - ord('a')])
            if diff == 0:
                ans.append(i)
        return ans

if __name__ == "__main__":
    sol = Solution()
    print(sol.findAnagrams("cbaebabacd",
"abc"))