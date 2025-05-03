class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        cnt = 1
        diff = 2001
        sub = 0

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                cnt += 1
                sub += cnt - 2

            else:
                diff = nums[i] - nums[i - 1]
                cnt = 2
        
        return sub
        