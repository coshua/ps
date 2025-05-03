from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        holding = 0
        d = defaultdict(int)
        ans = 0

        lo, hi = 0, 0

        while hi < len(fruits):
            ans = max(ans, hi - lo)
            d[fruits[hi]] += 1
            # if basket needs to be empty
            if d[fruits[hi]] == 1:
                while holding == 2:
                    d[fruits[lo]] -= 1
                    if d[fruits[lo]] == 0:
                        holding -= 1
                    lo += 1
                holding += 1
            hi += 1
        ans = max(ans, hi - lo)
        return ans