import sys
import heapq
input = sys.stdin.readline

C, R = map(int, input().split())
room = [list(map(int, input().strip())) for _ in range(R)]

visited = set()
cost = [float('inf')] * (R * C)
cost[0] = 0

dir = ((-1, 0), (1, 0), (0, 1), (0, -1))

pq = []
heapq.heappush(pq, (cost[0], 0, 0))

while pq:
    cur_cost, y, x = heapq.heappop(pq)
    visited.add(y * C + x)
    if y == R - 1 and x == C - 1:
        print(cur_cost)
        break

    for dy, dx in dir:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            onedim_idx = C * ny + nx
            if onedim_idx not in visited:
                old_cost = cost[onedim_idx]
                new_cost = 0 if room[ny][nx] == 0 else 1
                new_cost += cur_cost
                if new_cost < old_cost:
                    heapq.heappush(pq, (new_cost, ny, nx))
                    cost[onedim_idx] = new_cost