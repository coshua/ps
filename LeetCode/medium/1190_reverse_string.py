class Solution:
    def reverseParentheses(self, s: str) -> str:
        sp, ep = 0, len(s) - 1
        while sp < ep:
            while sp < ep and s[sp] != '(':
                sp += 1
            while sp < ep and s[ep] != ')':
                ep -= 1
            
            s = s[:sp] + s[sp + 1: ep: -1] + s[ep + 1:]
            print(s)
        
        return s
