class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        #p1 has not removed an element, while p2 has removed one element and keep count
        p1, p2 = nums[0], 0
        res = 0
        for i in range(1, len(nums)):
            if nums[i] == 0:
                res = max(res, p2)
                p1, p2 = 0, p1
            else:
                p1, p2 = p1 + 1, p2 + 1
        
        res = max(res, p2)
        return res