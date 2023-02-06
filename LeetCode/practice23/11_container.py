class Solution:
    def maxArea(self, height: list[int]) -> int:
        pl, pr = 0, len(height) - 1
        area = 0
        while pl < pr:
            area = max(area, (pr - pl) * min(height[pr], height[pl]))

            if height[pl] < height[pr]:
                pl += 1
            else:
                pr -= 1
        
        return area