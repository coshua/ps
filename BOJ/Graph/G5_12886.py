from collections import deque

A, B, C = map(int, input().split())
t = A + B + C
v = [[False] * t for i in range(t)]

def bfs(init):
    q = deque()
    q.append(init)
    while(q):
        x, y = q.popleft()
        z = t - x - y
        if (x == y == z):
            print(1)
            return
        
        for (a, b) in ((x, z), (x, y), (y, z)):
            if a < b:
                b -= a
                a += a
            elif a > b:
                a -= b
                b += b
            else:
                continue
            c = t - a - b
            X = min(a, b, c)
            Y = max(a, b, c)
            if not v[X][Y]:
                q.append((X, Y))
                v[X][Y] = True

    print(0)
    return
bfs((A, B))