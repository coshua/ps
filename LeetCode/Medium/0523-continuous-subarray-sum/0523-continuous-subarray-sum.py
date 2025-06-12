class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0: -1}
        cur = 0

        for i, n in enumerate(nums):
            cur = (cur+n)%k
            if cur in d:
                if i - d[cur] > 1:
                    return True
            else:
                d[cur] = i
        return False