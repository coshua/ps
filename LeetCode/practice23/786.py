import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        cnt = 0
        q = [(arr[0] / arr[len(arr) - 1], 0, len(arr) - 1)]
        v = set()

        while cnt < k:
            v, lo, hi = heapq.heappop(q)
            print(v, lo, hi)
            if hi - lo > 1:
                if (lo + 1, hi) not in v:
                    heapq.heappush(q, (arr[lo + 1] / arr[hi], lo + 1, hi))
                    v.add((lo + 1, hi))
                cur = arr[lo] / arr[hi - 1]
                if (lo, hi - 1) not in v:
                    heapq.heappush(q, (cur, lo, hi - 1))
                    v.add((lo, hi - 1))
            cnt += 1
        return [arr[lo], arr[hi]]


if __name__ == "__main__":
    sol = Solution()
    print(sol.kthSmallestPrimeFraction([1, 7, 23, 29, 47], 8))
