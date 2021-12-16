import sys
import heapq as h
input = sys.stdin.readline
inf = float('inf')

N, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
cost = [[inf] * (N) for _ in range(N)]

cost[0][0] = 0
visited = [[[0] * N for _ in range(N)] for _ in range(3)]
visited[0][0][0] = 1
q = []
h.heappush(q, (0, 0, (0, 0))) #cost, count left to eat grass, coords

while q:
    acc_cost, cur_cnt, yx = h.heappop(q)
    y, x = yx[0], yx[1]
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if 0 <= ny < N and 0 <= nx < N:
            cur_cost = T
            nxt_cnt = cur_cnt + 1
            if nxt_cnt == 3:
                cur_cost += graph[ny][nx]
                nxt_cnt = 0
            nxt_cost = acc_cost + cur_cost
            if nxt_cost < cost[ny][nx]:
                cost[ny][nx] = nxt_cost
                visited[nxt_cnt][ny][nx] = 1
                h.heappush(q, (nxt_cost, nxt_cnt, (ny, nx)))
            elif visited[nxt_cnt][ny][nx] == 0:
                visited[nxt_cnt][ny][nx] = 1
                h.heappush(q, (nxt_cost, nxt_cnt, (ny, nx)))
print(cost[N - 1][N - 1])