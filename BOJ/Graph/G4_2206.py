from collections import deque
import sys 
input = sys.stdin.readline

R, C = map(int, input().split())
m = [list(map(int, input().strip())) for _ in range(R)]
v = [[[False] * C for _ in range(R)] for j in range(2)]

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

q = deque()
q.append((0, 0, 0))
v[0][0][0] = True
found = False
cnt = 1
while(q):
    tl = len(q)
    for _ in range(tl):
        y, x, k = q.popleft()
        if (y == R - 1 and x == C - 1):
            found = True
            print(cnt)
            break
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if (0<=ny<R and 0<=nx<C and not v[k][ny][nx] and m[ny][nx] == 0):
                q.append((ny, nx, k))
                v[k][ny][nx] = True
            if (k == 0 and 0<=ny<R and 0<=nx<C and not v[k][ny][nx] and m[ny][nx] == 1):
                q.append((ny, nx, k + 1))
                v[k][ny][nx] = True
    cnt += 1
    if found:
        break
if not found:
    print(-1)