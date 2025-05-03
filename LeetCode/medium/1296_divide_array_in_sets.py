from collections import defaultdict
import heapq
class Solution:
    def isPossibleDivide(self, nums: list[int], k: int) -> bool:
        q = []
        d = defaultdict(int)
        for num in nums:
            heapq.heappush(q, num)
            d[num] += 1

        while q:
            num = heapq.heappop(q)
            if d[num] > 0:
                cnt = d[num]
                for i in range(k):
                    if d[num + i] < cnt:
                        return False
                    else:
                        d[num + i] -= cnt
        
        return True