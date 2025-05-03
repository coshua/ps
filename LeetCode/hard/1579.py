class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: list[list[int]]) -> int:
        pathsType3Taken = set()
        graph = [[] for i in range(n + 1)]
        for type, u, v in edges:
            graph[u].append((v, type))
            graph[v].append((u, type))

        v = [[0] * (n + 1) for _ in range(2)]

        # iterate routes for Alice
        q = [1]
        v[0][1] = 1
        while q:
            ln = len(q)
            nq = []
            for _ in range(ln):
                c = q.pop()
                for nxt, type in graph[c]:
                    if not v[0][nxt] and type in (1, 3):
                        nq.append((nxt))
                        v[0][nxt] = 1
                    if type == 3:
                        pathsType3Taken.add((type, min(c, nxt), max(c, nxt)))
            q = nq

        commonRoutes = 0

        q = [1]
        v[1][1] = 1
        while q:
            ln = len(q)
            nq = []
            for _ in range(ln):
                c = q.pop()
                for nxt, type in graph[c]:
                    if not v[1][nxt] and type in (2, 3):
                        nq.append((nxt))
                        v[1][nxt] = 1
                    if type == 3:
                        tup = (type, min(c, nxt), max(c, nxt))
                        if tup in pathsType3Taken:
                            commonRoutes += 1
                q = nq

        for i in range(1, n + 1):
            if not (v[0][i] and v[1][i]):
                return -1
        return len(edges) - ((n - 1) * 2 - commonRoutes)
