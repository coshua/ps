import math
class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        lo, hi = min(nums), max(nums)
        while lo <= hi:
            cur = 0
            mid = (lo + hi) // 2
            for num in nums:
                cur += math.ceil(num / mid)

            if cur > threshold:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo      