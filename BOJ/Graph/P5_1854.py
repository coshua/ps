import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M, K = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

cost = [[] for _ in range(N + 1)]
heapq.heappush(cost[1], 0)
q = []
heapq.heappush(q, (0, 1))
while q:
    acc_cost, cur_city = heapq.heappop(q)
    for nxt_city, nxt_cost in graph[cur_city]:
        if len(cost[nxt_city]) < K:
            heapq.heappush(cost[nxt_city], -(acc_cost + nxt_cost))
            heapq.heappush(q, (nxt_cost + acc_cost, nxt_city))
        elif -cost[nxt_city][0] > acc_cost + nxt_cost:
            heapq.heappop(cost[nxt_city])
            heapq.heappush(cost[nxt_city], -(acc_cost + nxt_cost))
            heapq.heappush(q, (nxt_cost + acc_cost, nxt_city))

for i in range(1, N + 1):
    if len(cost[i]) < K:
        print(-1)
    else:
        print(-heapq.heappop(cost[i]))