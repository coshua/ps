class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        d=defaultdict(int)

        for ch in s:
            d[ch] += 1
        q = []
        for key in d:
            heapq.heappush(q, (d[key], key))
        ans = 0
        while len(q) > k:
            ans += heapq.heappop(q)[0]
        
        return ans
