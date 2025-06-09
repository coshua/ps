class Solution:
    def maxArea(self, height: list[int]) -> int:
        pl, pr = 0, len(height) - 1
        ans = 0
        while pl < pr:
            ans = max(ans, (pr - pl) * (min(height[pl], height[pr])))
            if height[pl] < height[pr]:
                pl += 1
            else:
                pr -= 1
        return ans