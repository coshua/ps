class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        #assume len(s) < len(t)
        if len(s)>len(t):
            return self.isOneEditDistance(t, s)
        
        if len(t) == len(s):
            idx = 0
            while idx < len(t) and t[idx] == s[idx]:
                idx += 1
            if idx >= len(t):
                return False
            return t[:idx] + t[idx + 1:] == s[:idx] + s[idx + 1:]
        elif len(s) + 1 == len(t):
            idx = 0
            while idx < len(s) and s[idx] == t[idx]:
                idx += 1
            return s == t[:idx] + t[idx + 1:]
        return False