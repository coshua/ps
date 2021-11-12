from collections import deque
import sys
n = int(input())

v = [False for i in range(n + 1)]

q = deque()
q.append((n, [n]))
cnt = 0
ans = []
while (q):
    ln = len(q)
    for _ in range(ln):
        c, lst = q.popleft()
        if c == 1:
            print(cnt)
            sys.stdout.write(' '.join(map(str, lst)))
            sys.exit(0)   
        if c % 3 == 0 and not v[c // 3]:
            tmp = lst[:]
            v[c // 3] = True
            tmp.append(c // 3)
            q.append((c // 3, tmp))
        if c % 2 == 0 and not v[c // 2]:
            v[c // 2] = True
            tmp = lst[:]
            tmp.append(c // 2)
            q.append((c // 2, tmp))
        if not v[c - 1]:
            v[c - 1] = True
            tmp = lst[:]
            tmp.append(c - 1)
            q.append((c - 1, tmp))
    cnt += 1