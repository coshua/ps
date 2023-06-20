import math


class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        lo, hi = 1, max(quantities)

        def compare(val, lst):
            ans = 0
            for i in lst:
                ans += math.ceil(i / val)
                if ans > n:
                    return False
            return True

        while lo < hi:
            mid = (lo + hi) // 2
            if compare:
                hi = mid
            else:
                lo = mid + 1
