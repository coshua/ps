class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur = 0
        hist = defaultdict(int)
        hist[0] = 1
        ans = 0
        for n in nums:
            cur += n
            ans += hist[cur - k]
            hist[cur] += 1
        
        return ans