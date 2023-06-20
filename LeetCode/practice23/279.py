class Solution:
    def numSquares(self, n: int) -> int:
        q = []
        for i in range(1, 101):
            q.append(i * i)

        leastsum = [0] * 10001

        arr = q[:]
        cnt = 1
        for c in q:
            leastsum[c] = 1
        while q:
            nq = []
            sz = len(q)
            for i in range(sz):
                for j in range(len(arr)):
                    nxt = q[i] + arr[j]
                    if nxt <= 10000 and not leastsum[nxt]:
                        nq.append(nxt)
                        leastsum[nxt] = cnt + 1
            q = nq
            cnt += 1

        return leastsum[n]


if __name__ == "__main__":
    solution = Solution()
    print(solution.numSquares(254))
