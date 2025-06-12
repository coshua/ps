class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        n = len(nums)
        ans = [-1] * n
        for i in range(n*2):
            idx = i % n
            c = nums[idx]
            while st and st[-1][0] < c:
                v, p = st.pop()
                ans[p] = c
            st.append((c, idx))
        return ans