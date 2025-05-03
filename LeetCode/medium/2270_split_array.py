class Solution:
    def waysToSplitArray(self, nums: list[int]) -> int:
        lf_sum, rt_sum = 0, sum(nums)
        cnt = 0

        for i in range(len(nums) - 1):
            lf_sum += nums[i]
            rt_sum -= nums[i]

            if lf_sum >= rt_sum:
                cnt += 1
        
        return cnt