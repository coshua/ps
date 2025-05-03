class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        ans = 0

        def bsright(lst, target):
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        asclst = []
        for n in nums:
            if asclst and asclst[-1] > n:
                break
            asclst.append(n)

        prev = -100000
        for i, n in enumerate(nums):
            if n < prev:
                idx = bsright(asclst, n)
                ans = i - idx + 1
                while len(asclst) > idx:
                    asclst.pop()
            else:
                prev = n

        return ans
