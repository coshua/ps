class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        sz = 0
        ans = 0
        for ch in s:
            if ch == '(':
                sz += 1
            else:
                if sz == 0:
                    # add opening bracket
                    ans += 1 
                else:
                    # or close correspond
                    sz -= 1
        return ans + sz