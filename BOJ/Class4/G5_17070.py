import sys
input = sys.stdin.readline
N = int(input().strip())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1] * N for _ in range(N)] for i in range(3)]
dp[0][0][0], dp[1][0][0], dp[2][0][0], dp[0][0][1], dp[1][0][1], dp[2][0][1] = 0, 0, 0, 1, 0, 0

def getDP(d, i, j):
    if dp[d][i][j] == -1:
        res = 0
        if graph[i][j] == 0:
            if d == 0 and j > 0:
                if graph[i][j - 1] == 0:
                    res += getDP(0, i, j - 1) + getDP(2, i, j - 1)
            elif d == 1 and i > 0:
                if graph[i - 1][j] == 0:
                    res += getDP(1, i - 1, j)+ getDP(2, i - 1, j)
            elif d == 2 and i > 0 and j > 0:
                if graph[i][j - 1] + graph[i - 1][j] + graph[i - 1][j - 1] == 0:
                    res += getDP(0, i - 1, j - 1) + getDP(1, i - 1, j - 1) + getDP(2, i - 1, j - 1)
        dp[d][i][j] = res

    return dp[d][i][j]

ans = 0
for i in range(3):
    ans += getDP(i, N - 1, N - 1)

print(ans)
