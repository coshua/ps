class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x:x[1])
        cur = 0
        q = [] # (end, num)
        for trip in trips:
            p, s, e = trip
            while q and q[0][0] <= s:
                _, past = heapq.heappop(q)
                cur -= past
            heapq.heappush(q, (e, p))
            cur += p
            if cur > capacity:
                return False
        return True