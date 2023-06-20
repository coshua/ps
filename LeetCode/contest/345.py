class Solution:
    def countCompleteComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        ans = 0
        v = [0] * n

        def findConnectedDotsandEdges(dot, v, graph):
            edges = set()
            v[dot] = 1
            q = [dot]
            dots = set()
            dots.add(dot)
            while q:
                ln = len(q)
                nq = []
                for _ in range(ln):
                    cur = q.pop()
                    for nxt in graph[cur]:
                        if not v[nxt]:
                            nq.append(nxt)
                            v[nxt] = 1
                            dots.add(nxt)
                        pair = tuple(sorted([cur, nxt]))
                        edges.add(pair)
                q = nq
            return 1 if len(edges) == len(dots) * (len(dots) - 1) // 2 else 0

        for i in range(n):
            if not v[i]:
                ans += findConnectedDotsandEdges(i, v, graph)

        return ans


if __name__ == "__main__":
    solution = Solution()
    print(
        solution.maxMoves(
            [
                [187, 167, 209, 251, 152, 236, 263, 128, 135],
                [267, 249, 251, 285, 73, 204, 70, 207, 74],
                [189, 159, 235, 66, 84, 89, 153, 111, 189],
                [120, 81, 210, 7, 2, 231, 92, 128, 218],
                [193, 131, 244, 293, 284, 175, 226, 205, 245],
            ]
        )
    )
