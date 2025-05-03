from collections import deque
ip = list(map(int, input().split()))

m = [list(map(str,input().strip())) for j in range(ip[0])]

visited = [[False] * ip[1] for j in range(ip[0])]

lambs = 0
wolves = 0
dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs(y, x):
    q = [(y, x)]
    seclamb, secwolf = 0, 0
    while q:
        y, x = q.pop()
        if (m[y][x] == 'o'):
            seclamb += 1
        elif (m[y][x] == 'v'):
            secwolf += 1
        m[y][x] = '#'
       
        visited[y][x] = True
        for newx, newy in dirs:
            nx = x + newx
            ny = y + newy
            if (nx < 0 or ny < 0 or nx >= ip[1] or ny >= ip[0]):
                continue
            if (m[ny][nx] != '#'):
                q.append((ny, nx))
    if (seclamb > secwolf):
        secwolf = 0
    else:
        seclamb = 0
    return seclamb, secwolf


for i in range(ip[0]):
    for j in range(ip[1]):
        if (not visited[i][j] and m[i][j] != '#'):
            o, v = bfs(i, j)
            lambs += o
            wolves += v

print(lambs, wolves, end=" ")