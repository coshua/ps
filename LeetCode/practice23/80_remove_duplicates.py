class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p = 0
        for i in range(len(nums)):
            if p < 2 or nums[p - 2] != nums[i]:
                nums[p] = nums[i]
                p += 1
        
        return p