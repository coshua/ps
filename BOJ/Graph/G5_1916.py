import sys
import heapq
input = sys.stdin.readline

N = int(input())
B = int(input())

neighbor = [[] for _ in range(N + 1)]

for _ in range(B):
    s, e, w, = map(int, input().split())
    neighbor[s].append((e, w))

start, target = map(int, input().split())

def dijkstra(start, target):

    visited = set()
    dist = [float('inf')] * (N + 1)
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        cur_dist, cur_vertex = heapq.heappop(pq)
        visited.add(cur_vertex)
        if cur_vertex == target:
            return cur_dist
        for nxt_vertex, weight in neighbor[cur_vertex]:
            if nxt_vertex not in visited:
                old_cost = dist[nxt_vertex]
                new_cost = cur_dist + weight

                if new_cost < old_cost:
                    dist[nxt_vertex] = new_cost
                    heapq.heappush(pq, (new_cost, nxt_vertex))

    
    return -1

print(dijkstra(start, target))
