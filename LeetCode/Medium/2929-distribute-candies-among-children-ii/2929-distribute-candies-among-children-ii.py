class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        def dist2(c):
            ans = limit - max(abs(limit-c), 0) + 1
            return ans if ans >= 0 else 0
        
        ans = 0
        for i in range(min(n,limit)+1):
            ans += dist2(n-i)
        return ans