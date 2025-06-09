class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ansidx = 1
        numidx = 1
        while numidx < len(nums):
            # ignore duplicate
            if nums[numidx] != nums[numidx - 1]:
                nums[ansidx] = nums[numidx]
                ansidx += 1
            numidx += 1
        return ansidx