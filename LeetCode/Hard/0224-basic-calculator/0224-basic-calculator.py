class Solution:
    def calculate(self, s: str) -> int:
        def calc(op, p, n):
            if op == '+':
                return p + n
            elif op == '-':
                return p - n
            return p

        def helper(idx):
            local = 0
            op = "+"
            prev = 0

            while idx < len(s) and s[idx] != ')':
                if s[idx] == '(':
                    val, idx = helper(idx+1)
                    local = calc(op, local, val)
                elif s[idx] in ['+','-']:
                    local = calc(op, local, prev)
                    prev = 0
                    op = s[idx]
                    idx += 1
                elif s[idx].isdigit():
                    prev = prev*10 + int(s[idx])
                    idx += 1
                else:
                    idx += 1

            local = calc(op, local, prev)
            return local, idx+1
        
        ans, _ = helper(0)
        return ans