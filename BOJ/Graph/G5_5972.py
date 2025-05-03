import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [float('inf')] * (N + 1)
cost[1] = 0

graph =[[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

pq = [(0, 1)]
visited = set()

while pq:
    acc_cost, cur_id = heapq.heappop(pq)
    if cur_id == N:
        print(acc_cost)
        break
    visited.add(cur_id)
    for nxt_id, cur_cost in graph[cur_id]:
        if nxt_id not in visited:
            new_cost = cur_cost + acc_cost
            if new_cost < cost[nxt_id]:
                cost[nxt_id] = new_cost
                heapq.heappush(pq, (new_cost, nxt_id))
            