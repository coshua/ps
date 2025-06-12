class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 0 2 1 1 0
        # 0 2 2     
        # 0 first
        pnt = 0
        sz = len(nums)
        for i in range(sz):
            c = nums[i]
            if c == 0:
                nums[pnt], nums[i] = nums[i], nums[pnt]
                pnt += 1
        for i in range(pnt, sz):
            if nums[i] == 1:
                nums[pnt], nums[i] = nums[i], nums[pnt]
                pnt += 1
            