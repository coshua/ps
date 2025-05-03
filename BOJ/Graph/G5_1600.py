from collections import deque

K = int(input())
w, h = map(int, input().split())
m = [list(map(int, input().split())) for _ in range(h)]
v = [[[False]*(K+1) for _ in range(w)] for _ in range(h)]
q = deque()

onedirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
horsedirs = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))

q.append((0, 0, 0))
v[0][0][0] = True

nxt = 0
cnt = 0
cur = 1
found = False
while(q):
    y, x, k = q.popleft()

    if (y == h - 1 and x == w - 1):
        print(cnt)
        found = True
        break
    for dy, dx in onedirs:
        ny = y + dy
        nx = x + dx
        if (0 <= ny < h and 0 <= nx < w and m[ny][nx] == 0 and not v[ny][nx][k]):
            v[ny][nx][k] = True
            nxt += 1
            q.append((ny, nx, k))
    if (k < K):
        for dy, dx in horsedirs:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < h and 0 <= nx < w and m[ny][nx] == 0 and not v[ny][nx][k + 1]):
                v[ny][nx][k + 1] = True
                nxt += 1
                q.append((ny, nx, k + 1))
    
    cur -= 1
    if (cur == 0):
        cur = nxt
        nxt = 0
        cnt += 1

if not found:
    print(-1)