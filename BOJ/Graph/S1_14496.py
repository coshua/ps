import sys
ip = sys.stdin.readline
import heapq

a, b = map(int, ip().split())
N, M = map(int, ip().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e = map(int, ip().split())
    graph[s].append(e)
    graph[e].append(s)

pq = []
cost = [float('inf')] * (N + 1)
cost[a] = 0

found = False
heapq.heappush(pq, (0, a))
while pq:
    cur_cost, cur_char = heapq.heappop(pq)
    if cur_char == b:
        print(cur_cost)
        found = True
        break
    for nxt_char in graph[cur_char]:
        if cur_cost + 1 < cost[nxt_char]:
            cost[nxt_char] = cur_cost + 1
            heapq.heappush(pq, (cur_cost + 1, nxt_char))

if not found:
    print(-1)