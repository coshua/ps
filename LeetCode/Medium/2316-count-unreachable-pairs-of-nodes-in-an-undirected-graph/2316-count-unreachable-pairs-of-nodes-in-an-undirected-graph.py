class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        # find islands
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        v = [False] * n

        ans = 0

        def bfs(node, v, g):
            q = deque([node])
            v[node] = True
            cnt = 1
            while q:
                sz = len(q)
                for _ in range(sz):
                    cur = q.pop()
                    for nxt in g[cur]:
                        if not v[nxt]:
                            v[nxt] = True
                            q.appendleft(nxt)
                            cnt += 1
            return cnt
        remaining = n
        for i in range(n):
            if not v[i]:
                num_nodes = bfs(i, v, graph)
                remaining -= num_nodes
                ans += num_nodes * remaining
        
        return ans