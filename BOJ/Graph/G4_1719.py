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

def dijkstra(start):
    cost = [inf] * (N + 1)
    cost[start] = 0
    q = []
    parent = [-1] * (N + 1)
    parent[start] = start
    heapq.heappush(q, (0, start))
    while q:
        acc, id = heapq.heappop(q)
        if acc > cost[id]:
            continue
        for nxt, c in graph[id]:
            nxt_c = c + acc
            if nxt_c < cost[nxt]:
                cost[nxt] = nxt_c
                parent[nxt] = id
                heapq.heappush(q, (nxt_c, nxt))
    
    for i in range(1, N + 1):
        if i == start:
            print("-", end = " ")
        else:
            id = i
            while parent[id] != start:
                id = parent[id]
            print(id, end = " ")

for i in range(1, N + 1):
    dijkstra(i)
    print()