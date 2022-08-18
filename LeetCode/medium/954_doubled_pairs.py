from collections import defaultdict
import heapq as hq
class Solution:
    def canReorderDoubled(self, arr: list[int]) -> bool:
        d = defaultdict(int)
        minq_neg = []
        minq = []
        for num in arr:
            d[num] += 1
            if num < 0:
                hq.heappush(minq_neg, -num)
            else:
                hq.heappush(minq, num)
        
        while minq:
            num = hq.heappop(minq)
            if d[num * 2] >= d[num]:
                d[num * 2] -= d[num]
                d[num] = 0
            else:
                return False
        while minq_neg:
            num = hq.heappop(minq_neg)
            if d[num * (-2)] >= d[-num]:
                d[num * (-2)] -= d[-num]
                d[-num] = 0
            else:
                return False
        return True