import sys
input = sys.stdin.readline
import heapq

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    u, w, c = map(int, input().split())
    graph[u].append((w, c))
    graph[w].append((u, c))

v1, v2 = map(int, input().split())

def dijkstra(s):
    cost = [float('inf')] * (N + 1)
    cost[s] = 0
    pq = []
    heapq.heappush(pq, (0, s))
    visited = set()
    
    while pq:
        cur_cost, cur_vertex = heapq.heappop(pq)
        visited.add(cur_vertex)

        for e, c in graph[cur_vertex]:
            if e not in visited:
                old_cost = cost[e]
                new_cost = cur_cost + c
                if new_cost < old_cost:
                    cost[e] = new_cost
                    heapq.heappush(pq, (new_cost, e))
    
    return cost

fromstart = dijkstra(1)
fromv1 = dijkstra(v1)
fromv2 = dijkstra(v2)

mincost = min(fromstart[v1] + fromv1[v2] + fromv2[N], fromstart[v2] + fromv2[v1] + fromv1[N])
if mincost == float('inf'):
    print(-1)
else:
    print(mincost)