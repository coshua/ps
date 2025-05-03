import heapq
import math
#retry
class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        used = 0
        hq = []
        used_each = [0] * len(quantities)
        for i in range(len(quantities)):
            heapq.heappush(hq, [-quantities[i], i])
            used += 1
            used_each[i] += 1
        
        while used < n:
            stored, id = heapq.heappop(hq)
            stored = math.ceil(quantities[id] / (used_each[id] + 1))
            used_each[id] += 1
            used += 1
            heapq.heappush(hq, [-stored, id])
        
        return -heapq.heappop(hq)[0]

