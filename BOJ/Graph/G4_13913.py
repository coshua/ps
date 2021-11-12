from collections import deque
import sys
A, B = map(int, input().split())

v = [False] * 100001

def bfs(a, b):
    track = [-1] * 100001
    q = deque()
    q.append(a)
    track[a] = a
    v[a] = True
    t = 0
    while (q):
        lt = len(q)
        for _ in range(lt):
            c = q.popleft()
            if (c == b):
                print(t)
                tr = track[c]
                result = []
                result.append(c)
                while(tr != a):
                    result.append(tr)
                    tr = track[tr]
                result.append(tr)
                if (a == b):
                    result.pop()
                sys.stdout.write(' '.join(map(str, reversed(result))))
                return
            for i in [c - 1, c + 1, c * 2]:
                if 0<=i<=100000 and not v[i]:
                    v[i] = True
                    track[i] = c
                    q.append(i)
        t += 1
bfs(A, B)