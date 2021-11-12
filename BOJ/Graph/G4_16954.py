from collections import deque
m = []
walls = deque()
for i in range(8):
    row = list(map(str, input().strip()))
    m.append(row)
    for j in range(8):
        if (row[j] == '#'):
            walls.append((i, j))

cnt = 0
q = deque()
dirs = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1))
q.append((7, 0))
found = False
while(q):
    length = len(q)
    for _ in range(length):
        y, x = q.popleft()
        for dy, dx in dirs:
            ny = y + dy
            nx = x + dx

            if (0 <= ny < 8 and 0 <= nx < 8 and m[ny][nx] != '#'):
                if (ny == 0) or (ny > 0 and m[ny - 1][nx] != '#'):
                    q.append((ny, nx))
            

    wl = len(walls)
    for _ in range(wl):
        a, b = walls.pop()
        m[a][b] = '.'
        if (a <= 6):
            m[a + 1][b] = '#'
            walls.appendleft((a + 1, b))
    cnt += 1
    if (cnt > 7):
        found = True
        break

if found:
    print(1)
else:
    print(0)
    
