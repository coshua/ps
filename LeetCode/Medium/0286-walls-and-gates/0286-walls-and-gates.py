class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        rsz = len(rooms)
        csz = len(rooms[0])
        q = deque()
        for i in range(rsz):
            for j in range(csz):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
        dirs = ((-1, 0,), (1, 0), (0, 1), (0, -1))
        while q:
            sz = len(q)
            for _ in range(sz):
                r, c, d = q.pop()
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rsz and 0 <= nc < csz and rooms[nr][nc] != -1 and d + 1 < rooms[nr][nc]:
                        q.appendleft((nr, nc, d+1))
                        rooms[nr][nc] = d + 1
        
        return