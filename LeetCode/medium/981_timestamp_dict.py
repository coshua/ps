from collections import defaultdict
class TimeMap:
    dic = None
    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        lo, hi = 0, len(self.dic) - 1
        ans = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if self.dic[key][mid][0] > timestamp:
                hi = mid - 1
            else:
                ans = self.dic[key][mid][1]
                lo = mid + 1
        
        return ans