from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        cur = defaultdict(int)
        cnt = 0
        for ch in t:
            d[ch] += 1
            cnt += 1
        
        size = float('inf')
        ans = ""
        lo, hi = 0, 0
        while hi < len(s) and cnt > 0:
            if cur[s[hi]] < d[s[hi]]:
                cnt -= 1
            cur[s[hi]] += 1
            hi += 1
        
        while hi <= len(s) and lo < len(s):
            if hi - lo < size:
                ans = s[lo:hi]
            if cur[s[lo]] == d[s[lo]]:
                while hi <= len(s) and s[hi - 1] != s[lo]:
                    cur[s[hi - 1]] += 1
                    hi += 1
            cur[s[lo]] -= 1
            lo += 1
        
        return ans