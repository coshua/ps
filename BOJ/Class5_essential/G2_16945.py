import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)
R, C = map(int, input().split())

m = [[int(x) for x in input().strip()] for j in range(R)]

for i in range(R):
    for j in range(C):
        if m[i][j] == 1:
            m[i][j] = -1
dirs = ((-1, 0), (1, 0), (0, 1), (0, - 1))

def dfs(i, j):
    m[i][j] = -2
    q.append((i, j))

    for dy, dx in dirs:
        ny, nx = i + dy, j + dx
        if 0 <= ny < R and 0 <= nx < C and m[ny][nx] == 0:
            dfs(ny, nx)

changed = {} # y, x, id which would become 0 later
id = 0
for i in range(R):
    for j in range(C):
        if m[i][j] == 0:
            q = []
            dfs(i, j)
            num = len(q)
            for y, x in q:
                m[y][x] = num
                changed[(y, x)] = id
            id += 1    

print(m)

# contains pairs of (y, x, m[y][x]) which would update at the end
update = []
for i in range(R):
    for j in range(C):
        if m[i][j] == -1:
            cnt = 1
            v = []
            for dy, dx in dirs:
                ny, nx = i + dy, j + dx
                if 0 <= ny < R and 0 <= nx < C and m[ny][nx] > 0 and changed[(ny, nx)] not in v:
                    cnt += m[ny][nx]
                    v.append(changed[(ny, nx)])
            update.append((i, j, cnt % 10))

for y, x in changed:
    m[y][x] = 0

for i, j, cnt in update:
    m[i][j] = cnt 

for i in range(R):
    sys.stdout.write(''.join(map(str, m[i])) + '\n')