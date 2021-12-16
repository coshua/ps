import sys
import heapq as h
input = sys.stdin.readline
inf = float('inf')

R, C = map(int, input().split())
forest =[[] for _ in range(R)]

start, end = (), ()
for i in range(R): 
    line = list(input().strip())
    if 'S' in line:
        start = (i, line.index('S'))
    if 'F' in line:
        end = (i, line.index('F'))
    forest[i] = line


def onedim(y, x):
    return y * C + x

dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

def dijkstra(start):
    cost = [(inf, inf)] * (C * R)
    cost[onedim(start[0], start[1])] = (0, 0)

    q = []
    h.heappush(q, ((0, 0), start))

    def closetog(y, x):
        if y == end[0] and x == end[1]:
            return False
        for dy, dx in dirs:
            ny, nx = dy + y, dx + x
            if 0 <= ny < R and 0 <= nx < C:
                if forest[ny][nx] == 'g':
                    return True
        return False

    while q:
        acc_cost, yx = h.heappop(q)
        y = yx[0]
        x = yx[1]
        if acc_cost > cost[onedim(y, x)]:
            continue
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C:
                cur_cost = (0, 0)
                if forest[ny][nx] == 'g':
                    cur_cost = (1, 0)
                elif closetog(ny, nx):
                    cur_cost = (0, 1)
                new_cost = (cur_cost[0] + acc_cost[0], cur_cost[1] + acc_cost[1])
                if new_cost < cost[onedim(ny, nx)]:
                    cost[onedim(ny, nx)] = new_cost
                    h.heappush(q, (new_cost, (ny, nx)))
    return cost

result = dijkstra(start)
print(result[onedim(end[0], end[1])][0], result[onedim(end[0], end[1])][1])