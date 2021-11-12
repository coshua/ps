import sys
from collections import deque 
input = sys.stdin.readline

N, P = list(map(int, input().split()))

link_cnt = [0] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(P):
    lst = list(map(int, input().split()))[1:]
    for i in range(len(lst) - 1):
        link_cnt[lst[i + 1]] += 1
        graph[lst[i]].append(lst[i + 1])

q = deque()

for i in range(1, N + 1):
    if link_cnt[i] == 0:
        q.append(i)

id = 0
ans = [0] * N
while(q):
    c = q.popleft()
    for item in graph[c]:
        link_cnt[item] -= 1
        if link_cnt[item] == 0:
            q.append(item)
    ans[id] = c
    id += 1

if id < N:
    print(0)
else:
    print('\n'.join(map(str, ans)))