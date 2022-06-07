#took hours

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        s = 0
        e = 10
        mid = math.ceil((s + e) // 2)
        while s < e :
            if x >= mid * mid:
                s = mid
            else:
                e = mid - 1
            
            mid = math.ceil((s + e) / 2)
            print(s, e, mid)
        return mid

if __name__ == "__main__":
    sol = Solution()
    print(sol.mySqrt(1024))