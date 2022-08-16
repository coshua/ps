class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        while (lo <= hi):
            mid = lo + (hi - lo) // 2
            if (mid == 0 or nums[mid - 1] < nums[mid]) and (mid == len(nums) - 1 or nums[mid + 1] < nums[mid]):
                return mid
            
            if mid > 0 and nums[mid - 1] > nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
if __name__ == "__main__":
    solution = Solution()
    print(solution.findPeakElement([1,2,1,3,5,6,4]))