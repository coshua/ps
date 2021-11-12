import heapq
from collections import defaultdict

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        duplicate = set()
        sortedQueue = []

        for num in nums:
            if num not in duplicate:
                duplicate.add(num)
                heapq.heappush(sortedQueue, num)
        
        twoSum = defaultdict(list)

        for i in range(len(sortedQueue)):
            for j in range(i + 1, len(sortedQueue)):
                twoSum[sortedQueue[i] + sortedQueue[j]].append([sortedQueue[i], sortedQueue[j]])

        

        