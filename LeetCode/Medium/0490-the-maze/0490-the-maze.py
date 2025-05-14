class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        rsz, csz = len(maze), len(maze[0])
        v = [[False] * csz for _ in range(rsz)]
        q = deque([start])
        while q:
            ln = len(q)
            for _ in range(ln):
                r, c = q.pop()
                if [r, c] == destination:
                    return True
                for dr, dc in dirs:
                    nr, nc = r, c
                    # hit the wall
                    while 0 <= nr + dr < rsz and 0 <= nc + dc < csz and maze[nr + dr][nc + dc] == 0:
                        nr += dr
                        nc += dc
                    if not v[nr][nc]:
                        q.appendleft([nr, nc])
                        v[nr][nc] = True
                    
        
        return False