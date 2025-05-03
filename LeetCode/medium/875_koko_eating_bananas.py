import math
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            mid = (lo + hi) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
                if time > h:
                    break
            
            if time > h:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo