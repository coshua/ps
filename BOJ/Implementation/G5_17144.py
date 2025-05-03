import sys 
input = sys.stdin.readline

R, C, T = map(int, input().split())

m = [[0] * C for _ in range(R)]
cleaner = []

for i in range(R):
    row = list(map(int, input().split()))
    m[i] = row
    for j in range(C):
        if row[j] == -1:
            cleaner.append((i, j))
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
def spread():
    q = []
    for i in range(R):
        for j in range(C):
            if (m[i][j] > 4):
                part = m[i][j] // 5
                cnt = 0
                for dy, dx in dirs:
                    ny = i + dy
                    nx = j + dx
                    if (0<=ny<R and 0<=nx<C and m[ny][nx] != -1):
                        q.append((ny, nx, part))
                        cnt += 1
                q.append((i, j, -part * cnt))
    for y, x, a in q:
        m[y][x] += a

def soak():
    c = cleaner[0][1]
    r = cleaner[0][0]
    while (r >= 1):
        m[r][c] = m[r - 1][c]
        if r == cleaner[0][0]:
            m[r][c] = -1
        r -= 1
    while (c < C - 1):
        m[r][c] = m[r][c + 1]
        c += 1
    while (r < cleaner[0][0]):
        m[r][c] = m[r + 1][c]
        r += 1
    while (c >= 1):
        m[r][c] = m[r][c - 1]
        if c == 1:
            m[r][c] = 0
        c -= 1
    
    c = cleaner[1][1]
    r = cleaner[1][0]
    while (r < R - 1):
        m[r][c] = m[r + 1][c]
        if r == cleaner[1][0]:
            m[r][c] = -1
        r += 1
    while (c < C - 1):
        m[r][c] = m[r][c + 1]
        c += 1
    while (r > cleaner[1][0]):
        m[r][c] = m[r - 1][c]
        r -= 1
    while (c >= 1):
        m[r][c] = m[r][c - 1]
        if c == 1:
            m[r][c] = 0
        c -= 1

def count():
    cnt = 0
    for i in range(R):
        for j in range(C):
            if (m[i][j] > 0):
                cnt += m[i][j]
    return cnt

for _ in range(T):
    spread()
    soak()

print(count())