class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        lo, hi = 1, position[-1]

        def canDistribute(val, lst, m):
            cnt, pnt = 1, 1
            prev = 0
            while pnt < len(lst):
                while pnt < len(lst) and lst[pnt] - lst[prev] < val:
                    pnt += 1
                if pnt < len(lst) and lst[pnt] - lst[prev] >= val:
                    cnt += 1
                    prev = pnt
                    pnt += 1
                if cnt >= m:
                    return True
            return False

        while lo < hi:
            mid = (lo + hi) // 2
            if canDistribute(mid, position, m):
                lo = mid + 1
            else:
                hi = mid
            print(lo, hi)
        return lo - 1


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxDistance([79, 74, 57, 22], 4))
