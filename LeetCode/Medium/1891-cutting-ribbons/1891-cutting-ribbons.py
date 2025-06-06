class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        if sum(ribbons) < k:
            return 0
        
        lo, hi = 1, max(ribbons)

        def pos(lst, sz, k):
            cnt = 0
            for rib in lst:
                cnt += rib // sz
            return cnt >= k
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if pos(ribbons, mid, k):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo - 1