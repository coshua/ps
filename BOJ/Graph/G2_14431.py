import sys
input = sys.stdin.readline
import math
from collections import deque
inf = float('inf')
import heapq

maxdist = int(math.ceil(2 ** 0.5 * 6000))
primelst = [True] * (maxdist + 1)
m = int((maxdist + 1) ** 0.5)

for i in range(2, m + 1):
    if primelst[i] == True:
        for j in range(i * 2, maxdist + 1, i):
            primelst[j] = False

primenum = set([i for i in range(2, maxdist + 1) if primelst[i] == True])

def dist(x1, y1, x2, y2):
    temp = int(math.floor(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5))
    if temp in primenum:
        return -1
    return temp

coordlst = []
cost = [[inf] * 6001 for _ in range(6001)]
graph = [[[] for i in range(6001)] for j in range(6001)]
xs, ys, xt, yt = map(int, input().split())
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())
    x += 3000
    y += 3000
    for xn, yn in coordlst:
        temp = dist(x, y, xn, yn)
        if temp > -1:
            graph[xn][yn].append((temp, x, y))
            graph[x][y].append((temp, xn, yn))
    coordlst.append((x, y))

cost[xs][ys] = 0
q = []
heapq.heappush(q, (0, xs, ys))
while q:
    acc_cost, xc, yc = heapq.heappop()

    for cur_cost, xn, yn in graph[xc][yc]:
        nxt_cost = cur_cost + acc_cost
        if nxt_cost > cost[xn][yn]:
            continue
        cost[xn][yn] = nxt_cost
        heapq.heappush(q, (nxt_cost, xn, yn))

if cost[xt][yt] == inf:
    print(-1)
else:
    print(cost[xt][yt])
