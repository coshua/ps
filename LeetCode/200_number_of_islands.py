class Solution:
    def numIslands(self, grid):
        R = len(grid)
        C = len(grid[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        v = [[False for j in range(C)] for i in range(R)]
        cnt = 0

        def dfs(i, j, v):
            v[i][j] = True
            for dy, dx in dirs:
                ny, nx = i + dy, j + dx
                if 0 <= ny < R and 0 <= nx < C and grid[ny][nx] == '1' and not v[ny][nx]:
                    dfs(ny, nx, v)
        
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '1' and not v[i][j]:
                    dfs(i, j, v)
                    cnt += 1
        return cnt
