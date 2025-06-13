class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        s += '+'
        
        def calc(op, val, st):
            if op == '-':
                st.append(-val)
            elif op == '+':
                st.append(val)
            elif op == '*':
                st[-1] *= val
            elif op == '/':
                if val == 0:
                    return -1
                st[-1] =  int(st[-1] / val)
        def helper():
            st = []
            cur, op = 0, '+'
            nonlocal i
            while i < len(s):
                ch = s[i]
                if ch == '(':
                    i += 1
                    cur = helper()
                    continue
                elif ch in '+-/*':
                    calc(op, cur, st)
                    op = ch
                    cur = 0
                elif ch.isdigit():
                    cur = cur*10 + int(ch)
                elif ch == ')':
                    calc(op, cur, st)
                    i += 1
                    return sum(st)
                i += 1
            return sum(st)
        return helper()