class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            n = -n
            x = 1/x
        
        sub = self.myPow(x, n//2)
        ans = sub * sub
        if n % 2:
            ans *= x
        return ans