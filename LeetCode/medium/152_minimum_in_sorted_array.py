class Solution:
    def findMin(self, nums: list[int]) -> int:
        lo, hi = 0, len(nums)
        # assume there is only one point that this array has been reversed
        minv = nums[0]
        while lo < hi:
            mid = (lo + hi) // 2
            # it is sorted, set min as nums[lo] and search through the next half
            if nums[lo] < nums[mid]:
                minv = min(minv, nums[lo])
                lo = mid + 1
            
            # it is reversed in one point within this range(lo ~ mid)
            else:
                minv = min(minv, nums[mid])
                hi = mid
        
        return minv

