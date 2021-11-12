class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        for i in range(len(height)):
            for j in range(i):
                area = max(area, (i - j) * min(height[i], height[j]))
                if height[i] * (i - j) < area:
                    continue
        return area