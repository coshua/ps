class NumArray:

    def __init__(self, nums: List[int]):
        self.acc = [0] * (len(nums) + 1)
        self.acc[1] = nums[0]
        for i in range(1, len(nums)):
            self.acc[i+1] = self.acc[i] + nums[i]
        

    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right + 1] - self.acc[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)