import sys
input = sys.stdin.readline

N = int(input())

dp = [[] for i in range(N + 1)]
dp[0] = [1]
for i in range(0, N):
    dp[i + 1].append(1)
    for j in range(len(dp[i]) - 1):
        dp[i + 1].append(dp[i][j] + dp[i][j + 1])
    dp[i + 1].append(1)

print(sum(dp[N]))

