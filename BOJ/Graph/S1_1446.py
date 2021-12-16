import sys
import heapq
ip = sys.stdin.readline

N, D = map(int, ip().split())
cost  = [float('inf')] * (D + 1)

graph = [[] for _ in range(D + 1)]
for i in range(D):
    graph[i].append((i + 1, 1))

for _ in range(N):
    s, e, c = map(int, ip().split())
    if s <= D and e <= D:
        graph[s].append((e, c))

pq = []
cost[0] = 0

heapq.heappush(pq, (0, 0))

while pq:
    cur_cost, cur_dist = heapq.heappop(pq)

    if cur_dist == D:
        print(cur_cost)
        break
    for nxt_dist, c in graph[cur_dist]:
        if nxt_dist <= D and cost[nxt_dist] > cur_cost + c:
            heapq.heappush(pq, (cur_cost + c, nxt_dist))
            cost[nxt_dist] = cur_cost + c