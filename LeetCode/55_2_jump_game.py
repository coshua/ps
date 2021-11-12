class Solution:
    def canJump(self, nums: list[int]) -> bool:
        pointer = 0
        maxi = nums[pointer]
        
        if maxi + 1 >= len(nums):
            return True

        while pointer < maxi:
            pointer += 1
            maxi = max(maxi, pointer + nums[pointer])
            if maxi + 1 >= len(nums):
                return True
        
        return False