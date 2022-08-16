from collections import defaultdict
class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        d = defaultdict(int)        
        for num in nums:
            d[num] += 1
        op = 0
        for num in nums:
            if num == k / 2:
                op += d[num] // 2
                d[num] -= (d[num] // 2) * 2
            elif d[k - num] > 0 and d[num] > 0:
                inc = min(d[k - num], d[num])
                op += inc
                d[k - num] -= inc
                d[num] -= inc
        return op
