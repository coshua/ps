import heapq as hq


class MedianFinder:
    def __init__(self):
        self.smq = []  # will hold smallest n // 2 (n // 2 + 1 if total is odd) elements
        self.lgq = []  # will hold largest n // 2 elements

    def addNum(self, num: int) -> None:
        if not self.smq:
            self.smq.append(-num)
            return
        if len(self.smq) == len(self.lgq):
            if num <= self.lgq[0]:
                hq.heappush(self.smq, -num)
            else:
                hq.heappush(self.lgq, num)
                hq.heappush(self.smq, -hq.heappop(self.lgq))
        else:
            if num >= -self.smq[0]:
                hq.heappush(self.lgq, num)
            else:
                hq.heappush(self.smq, -num)
                hq.heappush(self.lgq, -hq.heappop(self.smq))

    def findMedian(self) -> float:
        if len(self.smq) == len(self.lgq):
            return (-self.smq[0] + self.lgq[0]) / 2
        else:
            return -float(self.smq[0])
