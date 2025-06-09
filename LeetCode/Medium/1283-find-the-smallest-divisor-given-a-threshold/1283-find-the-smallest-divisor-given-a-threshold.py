class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        lo, hi = 1, max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            rem = 0
            for num in nums:
                rem += math.ceil(num / mid)
            if rem <= threshold:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo