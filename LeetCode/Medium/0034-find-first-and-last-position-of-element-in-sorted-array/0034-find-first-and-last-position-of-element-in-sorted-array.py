class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        lo, hi = 0, len(nums) - 1
        left = -1
        right = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                left = mid
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                right = mid
            if nums[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return [left,right]
        