class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        ans = -1000
        d = defaultdict(int)

        total = sum(nums)
        for n in nums:
            d[n] += 1

        for n in nums:
            rem = total - n
            d[n] -= 1
            if rem % 2 == 0 and d[rem // 2]:
                ans = max(ans, n)
            d[n] += 1
        
        return ans