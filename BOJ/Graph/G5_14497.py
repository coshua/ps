import sys
inf = float('inf')
import heapq
input = sys.stdin.readline

R, C = map(int, input().split())

y_s, x_s, y_e, x_e = map(int, input().split())
y_s, x_s, y_e, x_e = y_s - 1, x_s - 1, y_e - 1, x_e - 1
room = [list(map(int, input().replace("#", "1").replace("*", "0").strip())) for _ in range(R)]
cost = [inf] * (R * C)
cost[y_s * C + x_s] = 0

dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

q = []
heapq.heappush(q, (0, y_s, x_s))

while q:
    acc_cost, y, x = heapq.heappop(q)
    if acc_cost > cost[y * C + x]:
        continue
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if 0 <= ny < R and 0 <= nx < C:
            new_cost = acc_cost + room[ny][nx]
            if new_cost < cost[ny * C + nx]:
                cost[ny * C + nx] = new_cost
                heapq.heappush(q, (new_cost, ny, nx))

print(cost[y_e * C + x_e])