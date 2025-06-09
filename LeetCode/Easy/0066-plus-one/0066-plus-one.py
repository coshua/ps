class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = []
        carry = 1
        pnt = len(digits) - 1
        while carry:
            if pnt < 0:
                ans.append(1)
                carry = 0
            else:
                ans.append((digits[pnt] + carry) % 10)
                carry = (digits[pnt] + carry) // 10
                pnt -= 1
        while pnt >= 0:
            ans.append(digits[pnt])
            pnt -= 1
        ans.reverse()
        return ans