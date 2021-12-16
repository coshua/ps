import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

S, E = map(int, input().split())

q = []
cost = [inf] * (N + 1)
heapq.heappush(q, (0, S))
cost[S] = 0

while q:
    acc_cost, cur_id = heapq.heappop(q)
    if acc_cost > cost[cur_id]:
        continue
    for nxt_id, cur_cost in graph[cur_id]:
        new_cost = cur_cost + acc_cost
        if new_cost < cost[nxt_id]:
            cost[nxt_id] = new_cost
            heapq.heappush(q, (new_cost, nxt_id))

print(cost[E])