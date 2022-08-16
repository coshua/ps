import math
class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        lo, hi = 1, 10000000
        minspeed = float('inf')
        while hi >= lo:
            mid = (hi + lo) // 2
            timetook = 0
            for i in range(len(dist) - 1):
                timetook += math.ceil(dist[i] / mid)
            timetook += dist[-1] / mid
            if timetook <= hour:
                minspeed = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        if minspeed == float('inf'):
            return -1
        else:
            return minspeed