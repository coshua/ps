import sys
input = sys.stdin.readline
import heapq

N, M, K, X = map(int, input().split())
graph = [[]for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

pq = []
heapq.heappush(pq, (0, X))
dist = [float('inf')] * (N + 1)
dist[X] = 0
city_with_k_dist = []
visited = set()
while pq:
    cur_dist, cur_city = heapq.heappop(pq)
    visited.add(cur_city)
    if cur_dist == K:
        city_with_k_dist.append(cur_city)

    else:
        for nxt in graph[cur_city]:
            if nxt not in visited:
                old_dist = dist[nxt]
                new_dist = dist[cur_city] + 1
                if old_dist > new_dist:
                    heapq.heappush(pq, (new_dist, nxt))
                    dist[nxt] = new_dist

city_with_k_dist.sort()
if len(city_with_k_dist) == 0:
    print(-1)
else:
    print(*city_with_k_dist, sep="\n")