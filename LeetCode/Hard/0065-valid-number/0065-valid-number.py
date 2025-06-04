class Solution:
    def isNumber(self, s: str) -> bool:
        dot = False
        digit = False
        if len(s) == 1 and not s[0].isdigit():
            return False
        for i, ch in enumerate(s):
            if ch in ['-','+'] and i > 0:
                return False
            if ch.isdigit():
                digit = True

            if ch == '.':
                if dot:
                    return False
                dot = True
            
            
            if ch == 'e' or ch == 'E':
                if not digit:
                    return False
                if i == len(s) - 1:
                    return False
                j = i + 1
                if s[j] in ['-','+']:
                    if j == len(s) - 1:
                        return False
                    j += 1
                while j < len(s):
                    if not s[j].isdigit():
                        return False
                    j += 1
                return True
                
            if not ch.isdigit() and ch not in ['-','+','.']:
                return False
        return digit