class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        flipped = deque()
        ans = 0
        lo = -1
        for i, n in enumerate(nums):
            if n == 0:
                flipped.append(i)
            
            if len(flipped) > k:
                lo = flipped.popleft()
            ans = max(ans, i - lo)
        return ans