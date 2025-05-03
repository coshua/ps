from collections import defaultdict
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        
        hq = []
        for ch in freq:
            heapq.heappush(hq, (freq[ch], ch))
        
        ans = ""

        while hq:
            cur = heapq.heappop(hq)
            ans += cur[1] * cur[0]
        return ans[::-1]