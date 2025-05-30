class Solution:

    def __init__(self, w: List[int]):
        self.total = sum(w)
        self.pre = []
        cur = 0
        for n in w:
            cur += n
            self.pre.append(cur)

    def pickIndex(self) -> int:
        idx= random.randint(1, self.total)
        ans = bisect.bisect_left(self.pre, idx)
        return ans
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()