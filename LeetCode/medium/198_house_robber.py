class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [[0 for j in range(len(nums))] for i in range(2)]

        dp[0][0] = nums[0]

        for i in range(1, len(nums)):
            dp[0][i] = dp[1][i - 1] + nums[i]  
            dp[1][i] = max(dp[1][i - 1], dp[0][i - 1])
        
        return max(dp[0][len(nums) - 1], dp[1][len(nums) - 1])