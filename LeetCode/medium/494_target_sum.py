from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        d = defaultdict(int)

        for num in nums:
            for prev in d:
                d[prev + num] += 1
                d[prev - num] -= 1
        
        return d[target]