import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dest = list(map(int, input().split()))

def dijkstra(start):
    cost = [inf] * (V + 1)
    cost[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        acc_cost, s = heapq.heappop(q)
        if acc_cost > cost[s]:
            continue
        for e, cur_cost in graph[s]:
            nxt_cost = cur_cost + acc_cost
            if nxt_cost < cost[e]:
                cost[e] = nxt_cost
                heapq.heappush(q, (nxt_cost, e))
    return cost

seller_time = [inf] * 10
seller_time[0] = 0
prev_point = dest[0]
acc_time = 0
for i in range(1, 10):
    temp = dijkstra(prev_point)
    if temp[dest[i]] == inf:
        seller_time[i] = inf
    else:
        seller_time[i] = temp[dest[i]] + acc_time
        acc_time = seller_time[i]
        prev_point = dest[i]

buyer_time = dijkstra(int(input()))

ans = inf
for i in range(10):
    if buyer_time[dest[i]] <= seller_time[i] and seller_time[i] != inf:
        ans = min(ans, dest[i])
if ans == inf:
    print(-1)
else:
    print(ans)