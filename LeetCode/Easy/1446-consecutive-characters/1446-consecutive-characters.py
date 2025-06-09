class Solution:
    def maxPower(self, s: str) -> int:
        prev = 0
        ans = 0
        s += " "
        for i, ch in enumerate(s):
            if ch != s[prev]:
                ans = max(ans, i - prev)
                prev = i
        return ans