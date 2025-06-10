class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lo,hi = 0, 0
        v = set()

        ans = 0
        while hi < len(s):
            ch = s[hi]
            while ch in v:
                v.remove(s[lo])
                lo += 1
            v.add(ch)
            ans = max(ans, hi - lo + 1)
            hi += 1
        return ans