class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        ans = []
        prev = 0
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > prev:
                ans.append(i)
                prev = heights[i]
        
        return ans[::-1]