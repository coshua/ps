import sys 
input = sys.stdin.readline
import heapq

N =  int(input())

maze = [list(map(int, input().strip())) for _ in range(N)]
dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))

pq = []
heapq.heappush(pq, (maze[0][0] ^ 1, 0, 0))

cost = [float('inf')] * (N * N)
cost[0] = maze[0][0] ^ 1
while pq:
    print(len(pq))
    cur_cost, y, x = heapq.heappop(pq)
    if y == N - 1 and x == N - 1:
        print(cur_cost)
        break
    for dy, dx in dirs:
        ny, nx = dy + y, dx + x
        if 0 <= ny < N and 0 <= nx < N:
            old_cost = cost[ny * N + nx]
            new_cost = cur_cost + (maze[ny][nx] ^ 1)
            if new_cost < old_cost:
                heapq.heappush(pq, (new_cost, ny, nx))
                cost[ny * N + nx] = new_cost
            
