# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> None:
#        
#
#    def isTarget(self) -> bool:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        d = ["U", "R", "D", "L"]
        dirs = [[-1,0],[0,1],[1,0],[0,-1]]
        # build graph, feasibility check
        # graph is (r,c): list
        g = defaultdict(set)
        v = set([(0,0)])
        target = None
        def dfs(r, c):
            if master.isTarget():
                nonlocal target
                target = (r, c)
            for i in range(4):
                cd = d[i]
                dr, dc = dirs[i][0], dirs[i][1]
                nr, nc = r + dr, c + dc
                if master.canMove(cd):
                    g[(r,c)].add((nr, nc))
                    g[(nr,nc)].add((r,c))
                    if (nr, nc) not in v:
                        v.add((nr, nc))
                        master.move(cd)
                        dfs(nr, nc)
                        master.move(d[(i + 2) % 4])
        dfs(0, 0)
        if not target:
            return -1
        # perform bfs
        step = 0
        q = deque([(0, 0)])
        v = set([(0,0)])
        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.pop()
                if cur == target:
                    return step
                for nxt in g[cur]:
                    if nxt not in v:
                        v.add(nxt)
                        q.appendleft(nxt)
            step += 1
        # Should not reach here
        return