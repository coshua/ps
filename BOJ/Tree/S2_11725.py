import sys 
from collections import deque
input = sys.stdin.readline

N = int(input())
m = {i: [] for i in range(1, N + 1)}
parent = [-1] * (N + 1)
v = [False] * (N + 1)
for _ in range(N - 1):
    a, b = map(int, input().split())
    m[a].append(b)
    m[b].append(a) 
q = deque()
q.append(1)
v[1] = True
while(q):
    i = q.popleft()
    for j in m[i]:
        if not v[j]:
            v[j] = True
            parent[j] = i
            q.append(j)
sys.stdout.write("\n".join(map(str, parent[2:])))