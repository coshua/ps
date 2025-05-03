import sys
from collections import deque
input = sys.stdin.readline
R, C = map(int, input().split())
m = [[0] * C for _ in range(R)]

vindex = []
zcnt = 0
zindex = []
for i in range(R):
    row = list(map(int, input().split()))
    m[i] = row
    for j in range(C):
        if row[j] == 0:
            zcnt += 1
            zindex.append((i, j))
        elif (row[j] == 2):
            vindex.append((i, j))
zcnt -= 3
q = deque()
for y, x in vindex:
    q.append((y, x))

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs():
    cnt = 0
    q = deque()
    for y, x in vindex:
        q.append((y, x))

    v = [[False] * C for _ in range(R)]
    while(q):
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx
            if (0 <= ny < R and 0 <= nx < C and not v[ny][nx] and m[ny][nx] == 0):
                cnt += 1
                v[ny][nx] = True
                q.append((ny, nx))
    return cnt
mx = 0

for i in range(len(zindex)):
    for j in range(i + 1, len(zindex)):
        for k in range(j + 1, len(zindex)):
            for a in [i, j, k]:
                ty, tx = zindex[a]
                m[ty][tx] = 1
            mx = max(mx, zcnt - bfs())
            for a in [i, j, k]:
                ty, tx = zindex[a]
                m[ty][tx] = 0

print(mx)