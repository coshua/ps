class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        q = [(grid[0][0], 0, 0)]
        dirs = [[-1,0],[1,0],[0,1],[0,-1]]

        time = 0
        rsz, csz = len(grid), len(grid[0])
        visited = set([(0,0)])
        while q:
            v, r, c = heapq.heappop(q)
            time = max(time, v)
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return time
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rsz and 0 <= nc < csz and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    heapq.heappush(q, (grid[nr][nc], nr, nc))
        return -1