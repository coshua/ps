class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lo,hi = min(nums), max(nums)
        r = hi-lo+1
        cnt = [0] * (hi-lo+1)
        for n in nums:
            cnt[n-lo] += 1
        
        for i in range(r-1, -1,-1):
            if cnt[i] >= k:
                return i+lo
            k -= cnt[i]
        return -1