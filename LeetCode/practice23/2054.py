class Solution:
    def maxTwoEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda x: x[1])

        def bslower(lst, target):
            lo, hi = 0, len(lst)
            while lo < hi:
                mid = (lo + hi) // 2
                if lst[mid][0] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        ans = 0
        maxq = [[0, 0]]
        for s, e, v in events:
            id = bslower(maxq, s)
            ans = max(ans, maxq[id - 1][1] + v)
            if v > maxq[-1][-1]:
                if maxq[-1][0] == e:
                    maxq.pop()
                maxq.append([e, v])
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))
