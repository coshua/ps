import heapq as hq
class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        s, e = 0, 0
        m, n = nums[0], nums[0]
        ans = 1

