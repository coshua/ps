class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [-1]
        ans = 0
        sz = len(heights)
        for i in range(sz):
            cur = heights[i]
            while st[-1] != -1 and heights[st[-1]] >= cur:
                h = heights[st.pop()]
                w = i - st[-1] -1
                ans = max(ans, h*w)
            st.append(i)

        while st[-1] != -1:
            h = heights[st.pop()]
            w = sz - st[-1] - 1
            ans = max(ans, h*w)
        return ans