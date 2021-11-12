# Graph mush Directed Acyclic
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

# Count how many edge directing to this vertex
cnt_enter_link = [0] * (N + 1)

# Store child components of each vertex
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    cnt_enter_link[b] += 1

q = deque()
for i in range(1, N + 1):
    if cnt_enter_link[i] == 0:
        q.append(i)
while(q):
    c = q.popleft()
    sys.stdout.write(str(c) + " ")
    for a in graph[c]:
        cnt_enter_link[a] -= 1
        if (cnt_enter_link[a]) == 0:
            q.append(a)