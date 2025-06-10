class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs =[[-1,0],[1,0],[0,1],[0,-1]]
        rsz, csz = len(grid), len(grid[0])
        v = set()
        def dfs(r,c):
            local = 0
            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if 0 <= nr < rsz and 0 <= nc < csz and (nr,nc) not in v and grid[nr][nc] == 1:
                    v.add((nr,nc))
                    local += dfs(nr,nc)
                if nr < 0 or nr == rsz or nc < 0 or nc == csz or grid[nr][nc] == 0:
                    local += 1

            return local
        for i in range(rsz):
            for j in range(csz):
                if grid[i][j] == 1:
                    v.add((i,j))
                    return dfs(i,j)
        return