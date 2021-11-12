import sys
input = sys.stdin.readline

R, C = map(int, input().split())

m = [list(input().strip()) for j in range(R)]

v = [[False] * C for _ in range(R)]
safezone = 0

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def search(r, c, q):
    global safezone
    if m[r][c] == 'U':
        d = dirs[0]
    elif m[r][c] == 'D':
        d = dirs[1]
    elif m[r][c] == 'L':
        d = dirs[2]
    else:
        d = dirs[3]

    v[r][c] = True
    if v[r + d[0]][c + d[1]]:
        if (r + d[0], c + d[1]) in q:
            safezone += 1
        return
    else:
        q.append((r, c))
        search(r + d[0], c + d[1], q)

for i in range(R):
    for j in range(C):
        if not v[i][j]:
            search(i, j, [])
print(safezone)