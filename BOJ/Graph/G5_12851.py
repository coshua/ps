from collections import deque

A, B = map(int, input().split())

v = [False] * 100001

def bfs(a, b):
    q = deque()
    q.append(a)
    v[a] = True
    t = 0
    cnt = 0
    while (q):
        lt = len(q)
        for _ in range(lt):
            c = q.popleft()
            v[c] = True
            if (c == b):
                cnt += 1
            for i in [c - 1, c + 1, c * 2]:
                if 0<=i<=100000 and not v[i]:
                    q.append(i)
        if cnt > 0:
            print(t)
            print(cnt)
            return
        t += 1
bfs(A, B)