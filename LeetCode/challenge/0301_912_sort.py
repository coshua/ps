class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) < 2:
            return nums
        
        merged = []
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        lo = hi = 0
        while lo < len(left) or hi < len(right):
            if lo == len(left):
                merged.append(right[hi])
                hi += 1
            elif hi == len(right) or left[lo] <= right[hi]:
                merged.append(left[lo])
                lo += 1
            else:
                merged.append(right[hi])
                hi += 1

        return merged