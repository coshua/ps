class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, suf = [0] * len(nums), [0] * len(nums)
        pre[0] = nums[0]
        suf[-1] = nums[-1]
        sz = len(nums)
        for i in range(1, sz):
            pre[i] = pre[i-1] * nums[i]
        for i in range(sz-2, -1, -1):
            suf[i] = suf[i+1] * nums[i]
        
        ans = [0] * sz
        ans[0] = suf[1]
        ans[-1] = pre[-2]
        for i in range(1, sz-1):
            ans[i] = pre[i-1] * suf[i+1]
        return ans
