class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','') + '+'
        nums, cur, op = [], 0, '+'

        for c in s:
            if c.isdigit():
                cur = cur*10 + int(c)
            else:
                if op == '+':
                    nums.append(cur)
                elif op == '-':
                    nums.append(-cur)
                elif op == '*':
                    nums[-1] *= cur
                elif op == '/':
                    nums[-1] = int(nums[-1]/cur)
                op = c
                cur = 0
        return sum(nums)