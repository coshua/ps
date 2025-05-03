class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        chArr = [[0] * 26 for i in range(len(s))]
        chArr[0][ord(s[0]) - ord('a')] = 1
        for i in range(1, len(s)):
            for j in range(26):
                chArr[i][j] = chArr[i - 1][j]
            chArr[i][ord(s[i]) - ord('a')] += 1
        
        longest = 0

        for i in range(len(s) - 1, -1, -1):
            p = True
            