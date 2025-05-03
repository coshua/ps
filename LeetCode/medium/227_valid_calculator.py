class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")

        # calculate multiplier and divisor first, using stack
        q = []
        num = ""
        for i in range(len(s)):
            if s[i] in ['+', '-', '*', '/'] or i == len(s) - 1:
                if i == len(s) - 1:
                    num += s[i]
                if len(q) >= 2 and q[-1] in ['/', '*']:
                    if q[-1] == '/':
                        q.pop()
                        q.append(int(q.pop()) // int(num))
                    elif q[-1] == '*':
                        q.pop()
                        q.append(int(q.pop()) * int(num))
                else:
                    q.append(num)
                q.append(s[i])
                num = ""
            else:
                num += s[i]
        ans = int(q[0])
        for i in range(len(q)):
            if q[i] == '+':
                ans += int(q[i + 1])
            elif q[i] == '-':
                ans -= int(q[i + 1])
        
        return ans
            

if __name__ == "__main__":
    solution = Solution()
    print(solution.calculate("2*3+4"))