import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [-1] * (N * N)
dp[0] = 0
def getdp(a):
    if a < 0:
        return sys.maxsize
    if dp[a] == -1:
        y = a // N
        x = a % N
        uppernum, leftnum = sys.maxsize, sys.maxsize
        if y - 1 >= 0:
            uppernum = getdp((y - 1) * N + x)
            if graph[y][x] >= graph[y - 1][x]:
                uppernum += graph[y][x] - graph[y - 1][x] + 1
        
        if x - 1 >= 0:
            leftnum = getdp(y * N + x - 1)
            if graph[y][x] >= graph[y][x - 1]:
                leftnum += graph[y][x] - graph[y][x - 1] + 1
        
        dp[a] = min(uppernum, leftnum)
    return dp[a]
print(getdp(N * N - 1))