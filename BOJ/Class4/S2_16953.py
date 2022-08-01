import sys
from collections import deque
input = sys.stdin.readline
A, B = map(int, input().split())

q = deque()
q.append(A)
cnt = 1
visited = set(q)
found = False
while q:
    size = len(q)
    for _ in range(size):
        c = q.popleft()

        if c == B:
            print(cnt)
            found = True

        if c*10 + 1 <= B:
            q.append(c*10 + 1)
            visited.add(c*10 + 1)

        if c*2 <= B:
            q.append(c*2)
            visited.add(c*2)
    cnt += 1
if not found:
    print(-1)