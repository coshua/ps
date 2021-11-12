R, C = list(map(int, input().split()))

m = [list(input().strip()) for _ in range(R)]
v = [[False] * C for _ in range(R)]
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

cnt = 0
starty = 0
startx = 0
found = False
def dfs(i, j, k, si, sj):
    global cnt
    global found
    cnt += 1
    if (found):
        return
    for y, x in dirs:
        ny = i + y
        nx = j + x
        if (ny == si and nx == sj and k >= 4 and not found and m[i][j] == m[ny][nx]):
            found = True
            return
        if (0 <= ny < R and 0 <= nx < C and not v[ny][nx] and m[i][j] == m[ny][nx]):
            v[ny][nx] = True
            dfs(ny, nx, k + 1, si, sj)
            v[ny][nx] = False

for i in range(R):
    for j in range(C):
        starty = i
        startx = j
        cnt = 0
        v[i][j] = True
        dfs(i, j, 1, i, j)
if not found:
    print("No")
else:
    print("Yes")