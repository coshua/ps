from collections import deque
R, C = list(map(int, input().split()))

m = []

coin = []

for i in range(R):
    row = input().strip()
    m.append(row)
    for j in range(C):
        if (row[j] == 'o'):
            coin.append(i)
            coin.append(j)

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

v = [[[[False] * C for _ in range(R)] for i in range(C)] for j in range(R)]
v[coin[0]][coin[1]][coin[2]][coin[3]] = True

q = deque()
q.append((coin[0], coin[1], coin[2], coin[3]))
cnt = 1
cur = 1
nxt = 0
found = False
while (q):
    cfy, cfx, csy, csx = q.popleft()
    if (found):
        break
    for dy, dx in dirs:
        nfy = cfy + dy
        nfx = cfx + dx
        nsy = csy + dy
        nsx = csx + dx

        if (0 <= nsy < R and 0 <= nsx < C and m[nsy][nsx] == '#'):
            nsy -= dy
            nsx -= dx
        if (0 <= nfy < R and 0 <= nfx < C and m[nfy][nfx] == '#'):
            nfy -= dy
            nfx -= dx
        
        if (nfy < 0 or nfy >= R or nfx < 0 or nfx >= C):
            if (0 <= nsy < R and 0 <= nsx < C):
                found = True
                print(cnt)
                break
        if (nsy < 0 or nsy >= R or nsx < 0 or nsx >= C):
            if (0 <= nfy < R and 0 <= nfx < C):
                found = True
                print(cnt)
                break
        
        if ((nsy != nfy or nsx != nfx) 
                and (0 <= nfy < R and 0 <= nfx < C) 
                and (0 <= nsy < R and 0 <= nsx < C)
                and (not v[nfy][nfx][nsy][nsx])):
            v[nfy][nfx][nsy][nsx] = True
            q.append((nfy, nfx, nsy, nsx))
            nxt += 1
        
    cur -= 1
    if (cur == 0):
        cur = nxt
        nxt = 0
        cnt += 1
        if (cnt > 10):
            break

if (not found):
    print(-1)
# 겹치면 탐색 중단
# 동시에 떨어지면 탐색 중단
# 두개의 동전 위치 방문한 곳이면 탐색 중단


