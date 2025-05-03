from collections import defaultdict
class Solution:
    def findLonely(self, nums: list[int]) -> list[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        ans = []
        for num, size in d.items():
            if size == 1 and not d.get(num - 1) and not d.get(num + 1):
                ans.append(num)
        
        return ans