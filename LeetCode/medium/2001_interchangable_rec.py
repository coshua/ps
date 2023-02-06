from collections import defaultdict
class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        fcs = defaultdict(int)
        for rec in rectangles:
            fcs[rec[0]/rec[1]] += 1
        
        ans = 0

        for rec in rectangles:
            ans += fcs[rec[0]/rec[1]] - 1

        return ans // 2