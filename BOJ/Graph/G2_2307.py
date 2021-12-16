import sys
import heapq
inf = float('inf')
input = sys.stdin.readline

N, M = map(int, input().split())
cost = [inf] * (N + 1)
cost[1] = 0
graph = [[] for _ in range(N + 1)]
roads = [] #ascending
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    roads.append((a, b))
parent = [-1] * (N + 1)
parent[1] = 1
q = []
heapq.heappush(q, (0, 1))
while q:
    acc, id = heapq.heappop(q)
    if acc > cost[id]:
        continue
    for nid, c in graph[id]:
        nc = c + acc
        if nc < cost[nid]:
            cost[nid] = nc
            parent[nid] = id
            heapq.heappush(q, (nc, nid))

idealcost = cost[N]

def remove(road):
    cost = [inf] * (N + 1)
    cost[1] = 0

    q = []
    heapq.heappush(q, (0, 1))
    while q:
        acc, id = heapq.heappop(q)
        if acc > cost[id]:
            continue
        for nid, c in graph[id]:
            if (id == road[0] or id == road[1]) and (nid == road[0] or nid == road[1]):
                continue
            nc = c + acc
            if nc < cost[nid]:
                cost[nid] = nc
                heapq.heappush(q, (nc, nid))
    
    return cost[N]

delay = 0
pnt = N
while parent[pnt] != pnt:
    cur_delay = remove((parent[pnt], pnt))
    delay = max(delay, cur_delay - idealcost)
    pnt = parent[pnt]

if delay == inf:
    print(-1)
else:
    print(delay)
