class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        rsz = len(grid)
        csz = len(grid[0])
        q = deque([(0, 0)]) if grid[0][0] == 0 else []
        steps = 1
        v = set()
        while q:
            sz = len(q)
            for _ in range(sz):
                r, c = q.pop()
                if r == rsz - 1 and c == csz - 1:
                    return steps
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rsz and 0 <= nc < csz and grid[nr][nc] == 0 and (nr,nc) not in v:
                        v.add((nr, nc))
                        q.appendleft((nr,nc))
            steps += 1
        return -1