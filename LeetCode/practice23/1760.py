import math


class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        def requiredMoreBags(maxval, lst, target):
            ans = 0
            for n in lst:
                ans += math.ceil(n / maxval) - 1
                if ans > target:
                    return True
            return False

        lo, hi = 1, 10**9

        while lo < hi:
            mid = (lo + hi) // 2
            if requiredMoreBags(mid, nums, maxOperations):
                lo = mid + 1
            else:
                hi = mid

        return lo


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumSize([2, 4, 8, 2], 3))
