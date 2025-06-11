class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.d = {}
    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.arr.append(val)
        self.d[val] = len(self.arr)-1
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            del self.d[val]
            last = self.arr.pop()
            if idx < len(self.arr):
                self.arr[idx] = last
                self.d[self.arr[idx]] = idx
            return True
        return False

    def getRandom(self) -> int:
        idx = random.randint(0, len(self.arr)-1)
        return self.arr[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()