class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if not s:
            return 0
        pnt = 0
        if s[0] in ['-', '+']:
            pnt += 1
        digits = 0
        negmax = 2**31
        posmax = 2**31-1
        while pnt < len(s) and s[pnt].isdigit():
            if s[0] == '-' and digits > negmax / 10:
                return -negmax
            if s[0] != '-' and digits > posmax / 10:
                return posmax
            digits = digits * 10 + int(s[pnt])
            pnt += 1
        if not digits:
            return 0
        
        if s[0] == '-':
            digits = max(-2**31, -digits)
        else:
            digits = min(2**31-1, digits)
        return digits