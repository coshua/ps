import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
import heapq

V, E, X = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    cost = [float('inf')] * (V + 1)
    cost[start] = 0
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_cost, cur_vertex = heapq.heappop(pq)
        visited.add(cur_vertex)
        for e, t in graph[cur_vertex]:
            if e not in visited:
                old_cost = cost[e]
                new_cost = cur_cost + t
                if old_cost > new_cost:
                    heapq.heappush(pq, (new_cost, e))
                    cost[e] = new_cost

    return cost

cost = [-1] * (V + 1)
cost[X] = 0
visited = set()
def mincost(start):
    cost = [float('inf')] * (V + 1)
    cost[start] = 0
    visited = set()
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_cost, cur_vertex = heapq.heappop(pq)
        if cur_vertex == X:
            return cur_cost
        visited.add(cur_vertex)
        for e, t in graph[cur_vertex]:
            if e not in visited:
                old_cost = cost[e]
                new_cost = cur_cost + t
                if old_cost > new_cost:
                    heapq.heappush(pq, (new_cost, e))
                    cost[e] = new_cost

    return -1

oneway = [0] * (V + 1)
for i in range(1, V + 1):
    oneway[i] = mincost(i)

wayback = dijkstra(X)

maxcost = -1
for i in range(1, V + 1):
    maxcost = max(oneway[i] + wayback[i], maxcost)

print(maxcost)