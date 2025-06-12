class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {}
        cur = 0

        for i, n in enumerate(nums):
            if n == 0:
                if i > 0 and nums[i-1] == 0:
                    return True
            cur = (cur+n)%k
            if cur == 0 and i > 0:
                return True
            if cur in d and i - d[cur] > 1:
                return True
            if cur not in d:
                d[cur] = i
        return False