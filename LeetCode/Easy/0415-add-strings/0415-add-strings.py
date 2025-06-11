class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        carry = 0
        p1,p2 = len(num1)-1, len(num2)-1

        while p1 >= 0 and p2 >=0:
            cur = int(num1[p1]) + int(num2[p2]) + carry
            carry = cur // 10
            ans.append(cur%10)
            p1 -= 1
            p2 -= 1
        while p1 >= 0:
            cur = int(num1[p1]) + carry
            carry = cur // 10
            ans.append(cur%10)
            p1 -= 1
        while p2 >= 0:
            cur = int(num2[p2]) + carry
            carry = cur // 10
            ans.append(cur%10)
            p2 -= 1
        
        if carry:
            ans.append(1)
        
        return ''.join(list(map(str, ans)))[::-1]

