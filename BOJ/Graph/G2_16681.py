import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M, CO_COST, CO_REWARD = map(int, input().split())
H = [0] + list(map(int, input().split()))
route = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    route[a].append((b, c))
    route[b].append((a, c))

# shortest way taking routes upside
def dijkstra(start):
    cost = [inf] * (N + 1)
    cost[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        acc_cost, cur_id = heapq.heappop(q)
        if acc_cost > cost[cur_id]:
            continue
        for nxt_id, cur_cost in route[cur_id]:
            if H[nxt_id] <= H[cur_id]:
                continue
            nxt_cost = cur_cost + acc_cost
            if nxt_cost < cost[nxt_id]:
                cost[nxt_id] = nxt_cost
                heapq.heappush(q, (nxt_cost, nxt_id))
    
    return cost

goingup = dijkstra(1)
goingdown = dijkstra(N)

maxreward = float('-inf')
for i in range(2, N):
    if goingup[i] != inf and goingdown[i] != inf:
        maxreward = max(maxreward, (CO_REWARD * H[i]) - CO_COST * (goingup[i] + goingdown[i]))

if maxreward == float('-inf'):
    print("Impossible")
else:
    print(maxreward)