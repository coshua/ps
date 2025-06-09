class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        d=defaultdict(int)
        queries.sort()
        valid = 0 
        cnt = pnt = 0
        pq = []
        for i in range(len(nums)):
            while pnt < len(queries) and queries[pnt][0] <= i:
                heapq.heappush(pq, -queries[pnt][1])
                pnt += 1
            while valid < nums[i] and pq:
                cur = -heapq.heappop(pq)
                cnt += 1
                if cur >= i:
                    valid += 1
                d[cur] += 1
            if valid < nums[i]:
                return -1
            
            valid -= d[i]
        return len(queries) - cnt