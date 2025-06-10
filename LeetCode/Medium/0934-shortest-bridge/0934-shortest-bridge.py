class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        v = set()
        edge = []
        rsz, csz = len(grid), len(grid[0])
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        def dfs(r, c, e):
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 1 and (nr,nc) not in v:
                    v.add((nr,nc))
                    dfs(nr,nc,e)
                if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 0 and (nr,nc) not in v:
                    v.add((nr,nc))
                    e.append((nr,nc))
        
        for i in range(rsz):
            for j in range(csz):
                if grid[i][j] == 1:
                    if len(v) == 0:
                        v.add((i,j))
                        dfs(i,j,edge)

        # now perform BFS to find another island with minimum steps
        steps = 1
        while edge:
            nxt = []
            for r, c in edge:
                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc
                    if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 1 and (nr,nc) not in v:
                        return steps
                    if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 0 and (nr,nc) not in v:
                        v.add((nr,nc))
                        nxt.append((nr,nc))
            edge=nxt
            steps += 1
        return -1