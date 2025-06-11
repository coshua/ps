class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) -1
        if len(nums) == 1:
            return 0
        while lo <= hi:
            mid = (lo+hi)//2
            if (mid == 0 and nums[mid] > nums[mid+1]) or (mid == len(nums)-1 and nums[mid] > nums[mid-1]) or (nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]):
                return mid
            if mid+1 < len(nums) and nums[mid+1] > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1