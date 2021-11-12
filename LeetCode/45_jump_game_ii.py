class Solution:
    def jump(self, nums: list[int]) -> int:
        pointer = 0
        reach = nums[pointer]
        jump = 0
        if len(nums) == 1:
            return 0
        if reach + 1 >= len(nums):
            return 1
        
        while True:
            temp = reach
            while pointer < reach:
                pointer += 1
                if pointer + nums[pointer] > temp:
                    temp = pointer + nums[pointer]
            
            reach = temp
            jump += 1
            if reach + 1 >= len(nums):
                return jump + 1