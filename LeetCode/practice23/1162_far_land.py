class Solution:
    def maxDistance(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dist = [[-1] * m for _ in range(m)]
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        q = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist[i][j] = 0
        
        if len(q) == 0 or len(q) == n * m:
            return -1
        
        ans = 0
        while q:
            nq = []
            while q:
                r, c = q.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < m and dist[nr][nc] == -1:
                        dist[nr][nc] = dist[r][c] + 1
                        ans = dist[r][c] + 1
                        nq.append((nr, nc))
            q = nq

        return ans