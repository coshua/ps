class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        ln = len(bombs)
        mp = [[] for _ in range(ln)]

        for i in range(ln):
            x, y, r = bombs[i]
            for j in range(ln):
                if i == j:
                    continue
                nx, ny, nr = bombs[j]
                if ((nx - x) ** 2 + (ny - y) ** 2) ** 0.5 <= r:
                    mp[i].append(j)

        def detonate(i, mp):
            v = [0] * ln
            v[i] = 1
            q = [i]
            while q:
                sz = len(q)
                nq = []
                for _ in range(sz):
                    cur = q.pop()
                    for nxt in mp[cur]:
                        if not v[nxt]:
                            v[nxt] = 1
                            nq.append(nxt)
                q = nq

            return sum(v)

        ans = 0
        for i in range(ln):
            ans = max(ans, detonate(i, mp))

        return ans
