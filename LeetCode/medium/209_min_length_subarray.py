class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left, sm, ln = 0, 0, 0

        for i in range(len(nums)):
            sm += nums[i]
            
            while sm >= target and left <= i:
                if ln == 0:
                    ln = i - left + 1
                else:
                    ln = min(ln, i - left + 1)
                
                sm -= nums[left]
                left += 1

        return ln
