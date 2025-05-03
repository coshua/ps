class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        mat = [[0] * n for _ in range(n)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r, c, dir = 0, 0, 0
        num = 1
        while num <= n * n:
            mat[r][c] = num
            nr, nc = r + dirs[dir][0], c + dirs[dir][1]
            if nr < n and nc < n and mat[nr][nc] == 0:
                r, c = nr, nc
            else:
                dir = (dir + 1) % 4
                r, c = r + dirs[dir][0], c + dirs[dir][1]
            num += 1
        
        return mat