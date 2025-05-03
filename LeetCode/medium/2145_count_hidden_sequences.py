class Solution:
    def numberOfArrays(self, differences: list[int], lower: int, upper: int) -> int:
        cur, minv, maxv = 0, 0, 0
        for diff in differences:
            cur += diff
            minv = min(minv, cur)
            maxv = max(maxv, cur)
        
        offset = lower - minv

        return 0 if maxv + offset > upper else upper - (maxv + offset) + 1
