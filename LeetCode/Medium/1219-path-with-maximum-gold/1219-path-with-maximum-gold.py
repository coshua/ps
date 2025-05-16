class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        rsz = len(grid)
        csz = len(grid[0])
        def dfs(r, c, total):
            nonlocal ans
            ans = max(ans,total)
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc]:
                    tmp = grid[nr][nc]
                    nxt = total + grid[nr][nc]
                    grid[nr][nc] = 0
                    dfs(nr, nc, nxt)
                    grid[nr][nc] = tmp
        
        for i in range(rsz):
            for j in range(csz):
                if grid[i][j]:
                    tmp = grid[i][j]
                    grid[i][j] = 0
                    dfs(i, j, tmp)
                    grid[i][j] = tmp
        return ans