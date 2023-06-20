import heapq as hq
class Solution:
    def minimumDeviation(self, nums: list[int]) -> int:
        q = []
    
        mindiff = curmin = float('inf')
        for n in nums:
            if n % 2 == 1:
                hq.heappush(q, -n*2)
                curmin = min(curmin, n * 2)
            else:
                hq.heappush(q, -n)
                curmin = min(curmin, n)

        while q[0] % 2 == 0:
            curmax = -hq.heappop(q)
            mindiff = min(mindiff, curmax - curmin)
            curmax //= 2
            curmin = min(curmin, curmax)
            hq.heappush(q, -curmax)
        
        mindiff = min(mindiff, -q[0] - curmin)

        return mindiff