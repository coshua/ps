class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        q = []
        for x, y in points:
            heapq.heappush(q, (-(x*x + y*y), x, y))
            if len(q)>k:
                heapq.heappop(q)
        
        return [[x,y] for _, x, y in q]