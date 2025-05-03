import heapq as hq
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = min(nums)
        cnt = 0
        for num in nums:
            cnt += num - m
        
        return cnt