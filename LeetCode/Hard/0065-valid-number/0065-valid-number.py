class Solution:
    def isNumber(self, s: str) -> bool:
        dot = False
        digit = False
        exp = False
        for i, ch in enumerate(s):
            if ch.isdigit():
                digit = True
            elif ch in ['+', '-']:
                if i > 0 and s[i-1] not in ['e','E']:
                    return False
            elif ch in ['e', 'E']:
                if exp or not digit:
                    return False
                digit = False
                exp = True
            elif ch == '.':
                if dot or exp:
                    return False
                dot = True
            else:
                return False
        return digit