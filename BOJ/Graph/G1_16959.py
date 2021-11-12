from collections import deque

cnt = 0
N = int(input())

M = []
global id
id = []
for i in range(N):
    row = list(map(int, input().split()))
    M.append(row)
    for j in range(N):
        if row[j] == 1:
            id = [i, j]

global q
q = deque()
q.append((id[0], id[1], 0))
q.append((id[0], id[1], 1))
q.append((id[0], id[1], 2))
def bfs(sid, target):
    global id
    global q
    found = False
    cnt = 0
    v = [[[False] * 3 for _ in range(N)] for j in range(N)]
    for iy, ix, ic in q:
        v[iy][ix][ic] = True
    # 0, 1, 2 means knight, bishop, look respectively
    lst = []
    while(q):
        leng = len(q)
        for _ in range(leng):
            y, x, c = q.popleft()
            if (int(M[y][x]) == target):
                lst.append((y, x, c))
                found = True
            
            if (c == 0):
                dirs = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2))
                for dy, dx in dirs:
                    ny = y + dy
                    nx = x + dx

                    if (0 <= ny < N and 0 <= nx < N and not v[ny][nx][0]):
                        v[ny][nx][0] = True
                        q.append((ny, nx, 0))
                
                for i in range(1, 3):
                    if not v[y][x][i]:
                        q.append((y, x, i))
                        v[y][x][i] = True
            elif (c == 1):
                dirs = ((-1, -1), (-1, 1), (1, -1), (1, 1))
                for dy, dx in dirs:
                    ny = y + dy
                    nx = x + dx
                    while (0 <= ny < N and 0 <= nx < N):
                        if not v[ny][nx][1]:
                            q.append((ny, nx, 1))
                            v[ny][nx][1] = True
                        ny += dy
                        nx += dx
                if not v[y][x][0]:
                    q.append((y, x, 0))
                    v[y][x][0] = True
                if not v[y][x][2]:
                    q.append((y, x, 2))
                    v[y][x][2] = True
            else:
                dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
                for dy, dx in dirs:
                    ny = y + dy
                    nx = x + dx
                    while (0 <= ny < N and 0 <= nx < N):
                        if not v[ny][nx][2]:
                            q.append((ny, nx, 2))
                            v[ny][nx][2] = True
                        ny += dy
                        nx += dx
                if not v[y][x][0]:
                    q.append((y, x, 0))
                    v[y][x][0] = True
                if not v[y][x][1]:
                    q.append((y, x, 1))
                    v[y][x][1] = True
            

        if found:
            q.clear()
            for next in lst:
                q.append(next)
            return cnt
        cnt += 1
    return [(-1, -1, -1)]

for target in range(2, N * N + 1):
    n = bfs(id, target)
    cnt += n
print(cnt)