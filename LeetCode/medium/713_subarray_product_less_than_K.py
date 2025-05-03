class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        product = 1
        ln = 0
        cnt = 0

        for i in range(len(nums)):
            product *= nums[i]
            ln += 1
            
            if product >= k:
                idx = i - ln + 1
                while idx <= i and product >= k:
                    product //= nums[idx]
                    idx += 1
                    ln -= 1
            cnt += ln

        return cnt 
            
        