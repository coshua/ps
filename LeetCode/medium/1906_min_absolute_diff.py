from collections import defaultdict
class Solution:
    def minDifference(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        numsSet = defaultdict(set)
        for i in range(len(nums)):
            numsSet[nums[i]].add(i)
        ans = []
        for query in queries:
            prev, cur = 0, 0
            
