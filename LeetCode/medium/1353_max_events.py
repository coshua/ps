import heapq
class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort()
        q = []

        attended = 0
        day = 1
        pointer = 0

        while pointer < len(events):
            while pointer < len(events) and events[pointer][0] <= day:
                heapq.heappush(q, events[pointer][1])
                pointer += 1
            
            while q and q[0] < day:
                heapq.heappop(q)
            
            if q:
                heapq.heappop(q)
                attended += 1

            day += 1
        
        while q:
            if q[0] < day:
                heapq.heappop(q)
            else:
                heapq.heappop(q)
                day += 1
                attended += 1

        return attended