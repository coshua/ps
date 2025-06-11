class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        d=Counter(tasks)
        q=[]
        for elem in d:
            heapq.heappush(q, (0, -d[elem], d))
        time = 0
        while q:
            now, sz, ch = heapq.heappop(q)
            time = max(time, now)
            if sz < -1:
                heapq.heappush(q, (now + n + 1, sz+1, ch))
            time += 1
        return time