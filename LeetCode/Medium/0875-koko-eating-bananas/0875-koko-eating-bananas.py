class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        while lo <= hi:
            cnt = 0
            mid =(lo+hi)//2
            for p in piles:
                cnt += math.ceil(p/mid)
            if cnt > h:
                lo = mid + 1
            else:
                hi = mid - 1
        return hi+1