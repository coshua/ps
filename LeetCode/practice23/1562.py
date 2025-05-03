from collections import defaultdict


class Solution:
    def findLatestStep(self, arr: list[int], m: int) -> int:
        p = [-1] * (len(arr) + 1)
        sz = [0] * (len(arr) + 1)
        d = defaultdict(int)
        ans = 0

        def getP(i, p):
            if p[i] != i:
                gp = getP(p[i], p)
                p[i] = gp
                return gp

            return i

        for i in range(len(arr)):
            cur = arr[i]
            p[cur] = cur
            sz[cur] = 1
            d[sz[cur]] += 1
            if cur - 1 > 0 and p[cur - 1] > 0:
                d[sz[cur]] -= 1
                sz[cur] += sz[getP(cur - 1, p)]
                d[sz[getP(cur - 1, p)]] -= 1
                p[getP(cur - 1, p)] = p[cur]
                d[sz[cur]] += 1
            if cur + 1 <= len(arr) and p[cur + 1] > 0:
                d[sz[cur]] -= 1
                sz[cur] += sz[getP(cur + 1, p)]
                d[sz[getP(cur + 1, p)]] -= 1
                p[getP(cur + 1, p)] = p[cur]
                d[sz[cur]] += 1
            if d[m]:
                ans = i + 1
            print(cur, sz[cur])
        return ans if ans else -1


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.findLatestStep(
            [7, 6, 11, 10, 3, 8, 1, 14, 9, 13, 16, 15, 5, 12, 17, 4, 2], 13
        )
    )
