class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum = 0
        ans = -float('inf')

        for n in nums:
            cum += n
            ans = max(ans, cum)
            if cum < 0:
                cum = 0
        return ans