class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        result = nums[0]
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
            result = max(result, nums[i])

        return result