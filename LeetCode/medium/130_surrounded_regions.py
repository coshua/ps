from collections import deque
class Solution:
    def solve(self, board):
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        R = len(board)
        C = len(board[0])
        v =[[False for j in range(C)] for i in range(R)]
        def bfs(r, c, v, b):
            track = []
            v[r][c] = True
            track.append((r, c))
            q = deque()
            q.append((r, c))
            escape = False
            while(q):
                ln = len(q)
                for _ in range(ln):
                    cy, cx = q.popleft()
                    if cy == 0 or cy == R - 1 or cx == 0 or cx == C - 1:
                        escape = True
                    for dy, dx in dirs:
                        ny, nx = cy + dy, cx + dx
                        if 0 <= ny < R and 0 <= nx < C and not v[ny][nx] and b[ny][nx] == 'O':
                            q.append((ny, nx))
                            track.append((ny, nx))
                            v[ny][nx] = True
            if not escape:
                for y, x in track:
                    b[y][x] = 'X'
        for i in range(R):
            for j in range(C):
                if board[i][j] == 'O' and not v[i][j]:
                    bfs(i, j, v, board)
        print(board)

if __name__ == "__main__":
    solution = Solution()
    solution.solve(
[["O","O","O"],["O","O","O"],["O","O","O"]])