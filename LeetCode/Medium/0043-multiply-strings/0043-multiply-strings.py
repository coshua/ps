class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        sz1 = len(num1)
        sz2=len(num2)
        for i in range(sz1-1, -1, -1):
            ch1 = num1[i]
            up = sz1-i-1
            for j in range(sz2-1, -1, -1):
                ch2 = num2[j]
                ans += ((ord(ch2) - ord('0')) * (ord(ch1)-ord('0'))) * (10 ** up)
                up += 1
        
        return str(ans)