import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
parent = [-1] * (N + 1)
q = []
heapq.heappush(q, (0, 1))
cost = [inf] * (N + 1)
cost[1] = 0
parent[1] = 1
printed = set()
while q:
    acc_cost, comp = heapq.heappop(q)
    if acc_cost > cost[comp]:
        continue
    for n_comp, cur_cost in graph[comp]:
        n_cost = cur_cost + acc_cost
        if n_cost < cost[n_comp]:
            cost[n_comp] = n_cost
            parent[n_comp] = comp
            heapq.heappush(q, (n_cost, n_comp))

for i in range(1, N + 1):
    while parent[i] != i:
        a = parent[i] if parent[i] < i else i
        b = i if parent[i] < i else parent[i]
        if (a, b) not in printed:
            printed.add((a, b))
        i = parent[i]

print(len(printed))
for a, b in printed:
    print(a, b)