from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        ln = len(grid)

        q = deque()
        if grid[0][0] == 0:
            q.append((0, 0))
        
        dir = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
        nxt = 0
        curq = 1
        step = 1
        while q:
            curR, curC = q.popleft()
            if curR == ln - 1 and curC == ln - 1:
                return step
            for dr, dc in dir:
                nr, nc = curR + dr, curC + dc
                if 0 <= nr < ln and 0 <= nc < ln and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    nxt += 1
                    q.append((nr, nc))
            curq -= 1

            if curq == 0:
                step += 1
                curq = nxt
                nxt = 0

        return -1
        