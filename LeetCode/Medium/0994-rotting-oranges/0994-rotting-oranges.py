class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rsz, csz = len(grid), len(grid[0])
        
        q = []
        for i in range(rsz):
            for j in range(csz):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        steps = 0
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]
        if fresh == 0:
            return 0
        while q:
            nq = []
            sz =len(q)
            for _ in range(sz):
                r, c = q.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        nq.append((nr,nc))
                        fresh -= 1
            q = nq
            steps += 1

        return -1 if fresh > 0 else steps-1
