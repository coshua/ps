class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 1) sort by start time
        intervals.sort(key=lambda x: x[0])
        
        # 2) min-heap of end times
        heap = []
        # push the end time of the first meeting
        heapq.heappush(heap, intervals[0][1])
        
        for s, e in intervals[1:]:
            # if the earliest meeting has ended by s, free up that room
            if heap[0] <= s:
                heapq.heappop(heap)
            
            # allocate a room for the current meeting
            heapq.heappush(heap, e)
        
        # the heap size is the max number of concurrent rooms needed
        return len(heap)