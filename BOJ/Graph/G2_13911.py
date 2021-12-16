import sys
input = sys.stdin.readline
import heapq
inf = float('inf')

V, E = map(int, input().split())
graph = [[] for _ in range(V + 3)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

M_NUM, M_MAX = map(int, input().split())
M_LIST = list(map(int, input().split()))
S_NUM, S_MAX = map(int, input().split())
S_LIST = list(map(int, input().split()))

S_SET = set(S_LIST)
M_SET = set(M_LIST)
for num in M_LIST:
    graph[V + 1].append((num, 0))

for num in S_LIST:
    graph[V + 2].append((num, 0))

def dijkstra(start):
    cost = [inf] * (V + 3)
    cost[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:
        acc_c, place = heapq.heappop(q)
        if acc_c > cost[place]:
            continue
        for nxt, cur_c in graph[place]:
            nxt_c = cur_c + acc_c
            if nxt_c < cost[nxt]:
                cost[nxt] = nxt_c
                heapq.heappush(q, (nxt_c, nxt))
    
    return cost

dist_from_mcdonalds = dijkstra(V + 1)
dist_from_startbucks = dijkstra(V + 2)
min_dist = inf
for i in range(1, V + 1):
    if dist_from_mcdonalds[i] <= M_MAX and dist_from_startbucks[i] <= S_MAX and i not in S_SET and i not in M_SET:
        min_dist = min(min_dist, dist_from_startbucks[i] + dist_from_mcdonalds[i])

print(min_dist if min_dist < inf else -1)