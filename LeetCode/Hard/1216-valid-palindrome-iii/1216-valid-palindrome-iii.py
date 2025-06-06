class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        dp = [[-1] * len(s) for _ in range(len(s))]
        
        def helper(s, lo, hi):
            if lo > hi :
                return 0 
            if dp[lo][hi] == -1:
                if s[lo] == s[hi]:
                    dp[lo][hi] = helper(s, lo + 1, hi - 1)
                else:
                    dp[lo][hi] = 1 + min(helper(s, lo, hi - 1), helper(s, lo + 1, hi))
            return dp[lo][hi]
        
        return helper(s, 0, len(s) - 1) <= k