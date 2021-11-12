from collections import deque

N = int(input())

M = [[0] * (N * 2) for _ in range(N)]
V = [[False] * N for _ in range(N)]
for i in range(N):
    if (i % 2 == 0):
        for j in range(N):
            a, b = list(map(int, input().split()))
            M[i][j * 2] = a
            M[i][j * 2 + 1] = b
    else:
        for j in range(N - 1):
            a, b = list(map(int, input().split()))
            M[i][j * 2 + 1] = a
            M[i][j * 2 + 2] = b

q = deque()
q.append([0, 0, [1]])
q.append([0, 1, [1]])
V[0][0] = True
tile = 1
cur = 2
nxt = 0

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
while(q):
    y, x, lst = q.popleft()
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        
        if (y % 2 == 0):
            if (x % 2 == 0):
                if (dx != 1 and 0 <= ny < N and 0 <= nx and not V[ny][nx]):
                    V[ny][nx] = True
                    temp = lst[:]
                    q.append((ny, nx))
                    q.append((ny, nx - 1))
