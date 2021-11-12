n = int(input())

m = [list(map(str, input().strip())) for _ in range(n)]
v = [[False] * n for _ in range(n)]

dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt_default = 0
cnt_special = 0

def dfs_special(y, x, s):
    v[y][x] = True

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        if (ny >= 0 and nx >= 0 and ny < n and nx < n and not v[ny][nx]):
            if (s == 'B'):
                if (m[ny][nx] == 'B'):
                    dfs_special(ny, nx, s)
            else:
                if (m[ny][nx] != 'B'):
                    dfs_special(ny, nx, s)

def dfs_default(y, x, s):
    v[y][x] = True

    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx

        if (ny >= 0 and nx >= 0 and ny < n and nx < n and not v[ny][nx] and m[ny][nx] == s):
            dfs_default(ny, nx, s)
for i in range(n):
    for j in range(n):
        if (not v[i][j]):
            cnt_default += 1
            dfs_default(i, j, m[i][j])

v = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (not v[i][j]):
            cnt_special += 1
            dfs_special(i, j, m[i][j])

print(cnt_default, cnt_special, end = " ")