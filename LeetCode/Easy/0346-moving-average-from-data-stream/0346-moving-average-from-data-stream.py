class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.lst = deque()
        self.sum = 0.0

    def next(self, val: int) -> float:
        self.sum += val
        self.lst.append(val)
        if len(self.lst) > self.size:
            self.sum -= self.lst.popleft()
        return self.sum / len(self.lst)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)