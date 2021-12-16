import sys
import heapq
input = sys.stdin.readline
inf = float('inf')

N, M, R = map(int, input().split())
reward = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    cost = [inf] * (N + 1)
    q = []
    cost[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        acc_cost, id = heapq.heappop(q)
        if acc_cost > cost[id]:
            continue
        for nid, cur_cost in graph[id]:
            if cur_cost + acc_cost < cost[nid]:
                cost[nid] = cur_cost + acc_cost
                heapq.heappush(q, (cur_cost + acc_cost, nid))
    ans = 0
    for i in range(N + 1):
        if cost[i] <= M:
            ans += reward[i]
    
    return ans

maxitem = 0
for i in range(1, N + 1):
    maxitem = max(maxitem, dijkstra(i))

print(maxitem)