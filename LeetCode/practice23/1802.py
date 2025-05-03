class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        lo, hi = 0, 10**9

        while lo < hi:
            mid = (lo + hi + 1) // 2
            s = (mid * (mid + 1) / 2) * 2 - mid
            if n - index < mid:
                if n - index + 1 == mid:
                    s -= 1
                else:
                    s -= (mid - n + index) * (mid - n + index + 1) / 2

            if index + 1 < mid:
                if index + 2 == mid:
                    s -= 1
                else:
                    s -= (mid - index - 1) * (mid - index) / 2
            print(mid, s)
            if s <= maxSum:
                lo = mid
            else:
                hi = mid - 1

        return lo


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxValue(4, 0, 4))
