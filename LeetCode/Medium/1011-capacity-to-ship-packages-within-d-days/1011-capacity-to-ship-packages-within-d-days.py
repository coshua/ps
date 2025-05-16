class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        

        def fit(cap):
            ans = 0
            cur = 0
            for w in weights:
                if cur + w > cap:
                    ans += 1
                    cur = 0
                cur += w
            if cur:
                ans += 1
            return ans
        lo, hi = max(weights), sum(weights)
        while lo <= hi:
            mid = (lo + hi) // 2
            # increase capacity
            if fit(mid) > days:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo
