from collections import deque

m = []

R, C = map(int, input().split())

bid = []
rid = []
for i in range(R):
    row = list(input().strip())
    m.append(row)
    for j in range(C):
        if (m[i][j] == 'B'):
            bid = [i, j]
            m[i][j] = '.'
        if (m[i][j] == 'R'):
            rid = [i, j]
            m[i][j] = '.'

dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))
# 0, 1, 2, 3 for right, down, left, up
vr = [[False] * C for _ in range(R)]
vb = [[False] * C for _ in range(R)]
global current
global nxt
current = 1
nxt = 0

def bfs(iyr, ixr, iyb, ixb):
    cnt = 1
    global current
    global nxt
    qr = deque()
    qb = deque()

    qr.append((iyr, ixr))
    qb.append((iyb, ixb))
    vr[iyr][ixr] = True
    vb[iyb][ixb] = True

    while(qr):
        qlen = len(qr)
        for _ in range(qlen):
            yr, xr = qr.popleft()
            yb, xb = qb.popleft()

            # roll right-side ball first
            for dy, dx in dirs:
                n_yr = yr
                n_xr = xr

                n_yb = yb
                n_xb = xb
                while (True):
                    n_yr += dy
                    n_xr += dx
                    if (m[n_yr][n_xr] == 'O'):
                        break
                    if (m[n_yr][n_xr] == '#'):
                        n_yr -= dy
                        n_xr -= dx
                        break
                while (True):
                    n_yb += dy
                    n_xb += dx
                    if (m[n_yb][n_xb] == 'O'):
                        break
                    if (m[n_yb][n_xb] == '#'):
                        n_yb -= dy
                        n_xb -= dx
                        break

                if (m[n_yb][n_xb] == 'O'):
                    continue

                if (m[n_yr][n_xr] == 'O'):
                    return cnt      

                if (n_yb == n_yr and n_xb == n_xr):
                    if abs(n_yr - yr) + abs(n_xr - xr) > abs(n_yb - yb) + abs(n_xb - xb):
                        n_yr -= dy
                        n_xr -= dx
                    else:
                        n_xb -= dx
                        n_yb -= dy
                if (not vr[n_yr][n_xr] or not vb[n_yb][n_xb]):
                    qr.append((n_yr, n_xr))
                    qb.append((n_yb, n_xb))
                    vr[n_yr][n_xr] = True
                    vb[n_yb][n_xb] = True
                    nxt += 1
            
            
        cnt += 1
    return -1

print(bfs(rid[0], rid[1], bid[0], bid[1]))