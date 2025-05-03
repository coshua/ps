import math


class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def compare(val, lst, target):
            ans = 0
            for n in lst:
                ans += math.floor(n / val)
                if ans >= target:
                    return True
            return False

        lo, hi = 1, 10**7
        while lo < hi:
            mid = (lo + hi) // 2
            if compare(mid, candies, k):
                lo = mid
            else:
                hi = mid - 1
        return lo - 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumCandies([1, 100, 1000], 1))
