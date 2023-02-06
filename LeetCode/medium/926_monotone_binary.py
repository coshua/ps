class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        following_0 = 0
        preceded_1 = 0

        min_change = float('inf')
        for i in range(len(s)):
            if s[i] == '0':
                following_0 += 1
        
        for i in range(len(s)):
            min_change = min(min_change, following_0 + preceded_1)
            if s[i] == '0':
                following_0 -= 1
            else:
                preceded_1 += 1
        
        # last iterate
        min_change = min(min_change, following_0 + preceded_1)
        return min_change