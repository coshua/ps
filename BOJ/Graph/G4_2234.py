C, R = map(int, input().split())

V = [[-1] * C for _ in range(R)]

m = []
for _ in range(R):
    row = list(map(int, input().split()))
    m.append(row)

cnt = 0
w = (1, 2, 4, 8)
dirs = ((0, -1), (-1, 0), (0, 1), (1, 0))

size = 0
maxroom = 0
cnt = 0
sizelist = []
def dfs(i, j):
    global size
    global maxroom
    V[i][j] = cnt
    size += 1
    maxroom = max(size, maxroom)
    sizelist[cnt] += 1
    for d in range(4):
        # 벽 뚫려있을 때 탐색
        ni = i + dirs[d][0]
        nj = j + dirs[d][1]
        if (m[i][j] & w[d] == 0 and V[ni][nj] == -1):
            dfs(ni, nj)

for i in range(R):
    for j in range(C):
        if (V[i][j] == -1):
            size = 0
            
            sizelist.append(0)
            dfs(i, j)
            cnt+= 1

twinroom = 0
print(cnt)
print(maxroom)
for i in range(R):
    for j in range(C):
        for d in range(4):
            ni = i + dirs[d][0]
            nj = j + dirs[d][1]
            if (m[i][j] & w[d] != 0 and 0 <= ni < R and 0 <= nj < C):
                if (V[i][j] != V[ni][nj]):
                    twinroom = max(twinroom, sizelist[V[i][j]] + sizelist[V[ni][nj]])

print(twinroom)
