import sys
ip = sys.stdin.readline
import heapq

N, M = map(int, ip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, c = map(int, ip().split())
    graph[s].append((e, c))
    graph[e].append((s, c))

def dijkstra(start, store_list):
    visited = set()
    cost = [float('inf')] * (N + 1)
    cost[start] = 0
    closest_store = float('inf')
    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        acc_cost, idx = heapq.heappop(pq)
        visited.add(idx)
        for nxt, cur_cost in graph[idx]:
            if nxt not in visited:
                if cost[nxt] > acc_cost + cur_cost:
                    cost[nxt] = acc_cost + cur_cost
                    heapq.heappush(pq, (acc_cost + cur_cost, nxt))

    for num in store_list:
        closest_store = min(closest_store, cost[num])
    
    return closest_store
    

H, C = map(int, ip().split())
home_list = list(map(int, ip().split()))
target_list = list(map(int, ip().split()))

ans = 0
dist = float('inf')
for i in range(len(home_list)):
    cur_min = dijkstra(home_list[i], target_list)
    if cur_min < dist:
        ans = home_list[i]
        dist = cur_min
    elif cur_min == dist and home_list[i] < ans:
        ans = home_list[i]

print(ans)