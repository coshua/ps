from collections import deque

N, S, M = list(map(int, input().split()))

m = list(map(int, input().split()))

v = [[False] * 1001 for _ in range(100)]

q = deque()
q.append(S)
for i in range(N):
    length = len(q)
    for _ in range(length):
        s = q.popleft()
        if (s + m[i] <= M and not v[i][s + m[i]]):
            q.append(s + m[i])
            v[i][s + m[i]] = True
        if (0 <= s - m[i] <= M and not v[i][s - m[i]]):
            q.append(s - m[i])
            v[i][s - m[i]] = True

if (len(q) == 0):
    print(-1)
else:
    print(max(q))