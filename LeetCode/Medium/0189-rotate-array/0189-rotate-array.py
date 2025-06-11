class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def creverse(lst, lo, hi):
            while lo < hi:
                lst[lo], lst[hi] = lst[hi], lst[lo]
                lo += 1
                hi -= 1
        
        creverse(nums, 0, len(nums)-1)
        creverse(nums, 0, k-1)
        creverse(nums, k, len(nums)-1)

