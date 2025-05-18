class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(lambda: defaultdict(float))

        sz = len(values)
        for i in range(sz):
            a, b = equations[i]
            v = values[i]

            graph[a][b] = v
            graph[b][a] = 1/v
        ans = []

        def bfs(s, e):
            if s not in graph:
                return -1.0
            q = deque([(s, 1.0)])
            v = set() 
            while q:
                sz = len(q)
                for _ in range(sz):
                    cur, val = q.pop()
                    if cur == e:
                        return val
                    for nxt in graph[cur]:
                        if nxt not in v:
                            v.add(nxt)
                            q.appendleft((nxt, val * graph[cur][nxt]))

            return -1.0
        for a, b in queries:
            ans.append(bfs(a, b))
        return ans