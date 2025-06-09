class MedianFinder:
    
    def __init__(self):
        self.lo = []
        self.hi = []

    def addNum(self, num: int) -> None:
        if not self.hi or num >= self.hi[0]:
            heapq.heappush(self.hi, num)
        else:
            heapq.heappush(self.lo, -num)
        
        if len(self.lo) > len(self.hi):
            heapq.heappush(self.hi, -heapq.heappop(self.lo))
        elif len(self.hi) > len(self.lo) + 1:
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) == len(self.hi):
            return (self.hi[0] - self.lo[0]) / 2
        else:
            return self.hi[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()