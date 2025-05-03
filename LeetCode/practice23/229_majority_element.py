from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        d = defaultdict(int)
        s = set()

        for num in nums:
            d[num] += 1
            if d[num] > len(nums) / 3:
                s.add(num)
        
        return list(s)