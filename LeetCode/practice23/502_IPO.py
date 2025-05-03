import heapq as hq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        #Since the condition is to pick at most 'k' projects, only consider project which holds profit - capital > 0
        q = []
        # sort by capital needed
        cap_idx = list(zip(capital, profits))
        cap_idx.sort()
        
        cnt = 0
        pnt = 0

        while cnt < k:
            while pnt < len(profits) and cap_idx[pnt][0] <= w:
                hq.heappush(q, -cap_idx[pnt][1])
                pnt += 1
            if not q:
                break
            w += -hq.heappop(q)
            cnt += 1
        return w