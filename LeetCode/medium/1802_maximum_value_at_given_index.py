class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi = 0, 10**9

        while lo < hi:
            index_val = (lo + hi) // 2
            prev = (index_val * (index_val + 1) / 2) - ((index_val - index - 1) * (index_val - index) / 2)
            nxt = (index_val * (index_val + 1) / 2) - ((index_val - (n - index) - 1) * (index_val - (n - index)) / 2)
            if prev + nxt - index_val == maxSum:
                return index_val
            elif prev + nxt - index_val > maxSum:
                hi = index_val - 1
            else:
                lo = index_val + 1

        return lo