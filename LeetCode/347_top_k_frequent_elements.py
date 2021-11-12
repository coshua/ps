import heapq as hq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]

        for key in d:
            buckets[d[key]].append(key)

        res = []
        id = len(nums)
        while (len(res) < k):
            if (len(buckets[id]) > 0):
                res += buckets[id]
            id -= 1
        
        return res

        

if __name__ == "__main__":
    solution = Solution()
    print(solution.topKFrequent([3,1,3,4,2], 2))