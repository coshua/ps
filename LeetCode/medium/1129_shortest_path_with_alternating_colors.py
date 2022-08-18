from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = [[[] for i in range(n)] for color in range(2)]
        #graph[0] = red, graph[1] = blue
        v = set()
        for s, e in redEdges:
            graph[0][s].append(e)
        for s, e in blueEdges:
            graph[1][s].append(e)
        
        path = [-1] * n
        path[0] = 0

        q = deque([0])
        color = 0
        cnt = 0
        while q:
            it = len(q)
            for i in range(it):
                p = q.popleft()
                path[p] = cnt if path[p] == -1 else min(path[p], cnt)
                for e in graph[color][p]:
                    if (color, p, e) not in v:
                        q.append(e)
                        v.add((color, p, e))
            color ^= 1
            cnt += 1
        
        q = deque([0])
        color = 1
        cnt = 0
        v = set()
        while q:
            it = len(q)
            for i in range(it):
                p = q.popleft()
                path[p] = cnt if path[p] == -1 else min(path[p], cnt)
                for e in graph[color][p]:
                    if (color, p, e) not in v:
                        q.append(e)
                        v.add((color, p, e))
            color ^= 1
            cnt += 1
        
        print(path)
        return path

if __name__  == "__main__":
    sol = Solution()
    print(sol.shortestAlternatingPaths(5,
[[2,2],[0,4],[4,2],[4,3],[2,4],[0,0],[0,1],[2,3],[1,3]],
[[0,4],[1,0],[1,4],[0,0],[4,0]]))