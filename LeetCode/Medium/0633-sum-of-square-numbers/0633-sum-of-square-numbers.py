class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(int(math.sqrt(c))+1):
            rem = c-i*i
            if rem == int(math.sqrt(rem))**2:
                return True
        return False