class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        sz = len(graph)
        path = [0]
        def backtrack(node):
            if node == sz-1:
                ans.append(path[:])
                return

            for nxt in graph[node]:
                path.append(nxt)
                backtrack(nxt)
                path.pop()
        backtrack(0)
        return ans
            