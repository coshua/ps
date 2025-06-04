class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        lo, hi = 0, len(num) - 1
        while lo <= hi:
            l, r = num[lo], num[hi]
            if l == r and l in ['1', '8', '0']:
                lo += 1
                hi -= 1
                continue
            if l != r and ((l == '6' and r =='9') or (l =='9' and r=='6')):
                lo += 1
                hi -= 1
                continue
            return False
            lo += 1
            hi -= 1
        return True
