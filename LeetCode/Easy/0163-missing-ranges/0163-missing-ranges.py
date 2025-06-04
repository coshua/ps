class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        if not nums:
            return [[lower, upper]]
        
        if lower < nums[0]:
            ans.append([lower, nums[0]-1])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                continue
            ans.append([nums[i-1]+1, nums[i]-1])
        
        if nums[-1] < upper:
            ans.append([nums[-1] + 1, upper])
        return ans