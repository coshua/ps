import bisect


class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        # lower bound binary search
        def bs(lst, target):
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if lst[mid] <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return hi

        lst = [[] for i in range(2)]
        ans = 0

        for i in range(len(heights)):
            pos = bs(lst[0], heights[i])
            if pos > 0:
                ans = max(ans, (i + 1 - lst[1][pos - 1]) * lst[0][pos - 1])
            if pos < len(lst[0]):
                ans = max(ans, (i + 1 - lst[1][pos]) * heights[i])
            ans = max(ans, heights[i])

            if lst[0] and lst[0][-1] == heights[i]:
                continue
            elif not lst[0] or (lst[0] and heights[i] > lst[0][-1]):
                lst[0].append(heights[i])
                lst[1].append(i)
            else:
                while pos + 1 < len(lst[0]):
                    lst[0].pop()
                    lst[1].pop()
                lst[0][-1] = heights[i]
            print(lst, ans)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([1, 2, 3, 4, 5]))
