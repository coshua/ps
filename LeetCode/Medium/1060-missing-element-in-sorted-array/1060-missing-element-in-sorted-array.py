class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        prev = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            # interval
            interval = cur - prev - 1
            if k > interval:
                k -= interval
            else:
                return prev + k  
            prev = cur
        return prev + k