class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        lo, hi = 1, totalTrips * min(time)
        mintime = hi
        while lo <= hi:
            mid = (lo + hi) // 2
            total_trip = 0
            for each in time:
                total_trip += mid // each
            if total_trip >= totalTrips:
                mintime = mid
                hi = mid - 1
            else:
                lo = mid + 1
            
        return mintime