from collections import defaultdict
class RangeFreqQuery:
    d = defaultdict(list)
    def __init__(self, arr: List[int]):
        for i in range(len(arr)):
            self.d[arr[i]].append(i)
        print(d)
    def bsupper(self, lst, i):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] <= i:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def bslower(self, lst, i):
        lo, hi = 0, len(lst)
        while lo < hi:
            mid = (lo + hi) // 2
            if lst[mid] >= i:
                hi = mid
            else:
                lo = mid + 1
        return lo
    
    def query(self, left: int, right: int, value: int) -> int:
        return self.bsupper(self.d[value], right) - self.bslower(self.d[value], left)
if __name__ == "__main__":
    sol = RangeFreqQuery([1, 1, 1, 2, 2])