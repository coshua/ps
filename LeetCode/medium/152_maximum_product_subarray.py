class Solution:
    #O(n)
    def maxProduct(self, nums: list[int]) -> int:
        dp = [[0] * 2 for _ in range(len(nums))]
        result = nums[0]
        dp[0] = [0, nums[0]] if nums[0] > 0 else [nums[0], 0]
        # first column for max negative
        
        for i in range(1, len(nums)):
            if nums[i] == 0:
                if result < 0:
                    result = 0
                dp[i] = [0, 0]

            if nums[i] > 0:
                dp[i][1] = nums[i] if dp[i - 1][1] == 0 else dp[i - 1][1] * nums[i]
                dp[i][0] = dp[i - 1][0] * nums[i]
            
            else:
                dp[i][0] = nums[i] if dp[i - 1][1] == 0 else dp[i - 1][1] * nums[i]
                dp[i][1] = dp[i - 1][0] * nums[i]
            
            result = max(result, max(dp[i]))

        return result
    
    def maxP(self, nums: list[int]) -> int:
        curmax, curmin = [0, nums[0]] if nums[0] < 0 else [nums[0], 0]
        result = nums[0]
        for i in range(1, len(nums)):
            tempmax, tempmin = curmax, curmin
            if nums[i] < 0:
                tempmax = curmin * nums[i]
                tempmin = curmax * nums[i] if curmax > 0 else nums[i]
            elif nums[i] > 0:
                tempmax = curmax * nums[i] if curmax > 0 else nums[i]
                tempmin = curmin * nums[i]
            
            else:
                tempmax, tempmin = 0, 0

            curmax, curmin = tempmax, tempmin
            result = max(curmax, result)
        return result
            

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProduct([7, 1, -4, 3, 5, -1, 0]))