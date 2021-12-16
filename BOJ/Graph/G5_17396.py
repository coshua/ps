import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M = map(int, input().split())
accessible = list(map(int, input().split()))
accessible[-1] = 0

road = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    road[a].append((b, t))
    road[b].append((a, t))
pq = []
heapq.heappush(pq, (0, 0))
cost = [inf for _ in range(N)]
cost[0] = 0

while pq:
    acc_cost, cur_vtx = heapq.heappop(pq)
    if cost[cur_vtx] < acc_cost:
        continue
    for nxt_vtx, cur_cost in road[cur_vtx]:
        new_cost = cur_cost + acc_cost
        if new_cost < cost[nxt_vtx] and accessible[nxt_vtx] == 0:
            cost[nxt_vtx] = new_cost
            heapq.heappush(pq, (new_cost, nxt_vtx))

result = cost[-1]
print(result if result < inf else -1)