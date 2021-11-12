N = int(input())

dp = [[0 for i in range(2)] for j in range(N)]
dp[0][0] = 1
dp[0][1] = 0
copied = 1
for i in range(1, N):
    if i >= 3:
        if dp[i - 3][0] + dp[i - 2][1] >= dp[i - 1][0] + copied:
            dp[i][0] = dp[i - 3][0] + dp[i - 2][1]
            copied = dp[i - 2][1]
        else:
            dp[i][0] = dp[i - 1][0] + copied
    else:
        dp[i][0] = dp[i - 1][0] + 1
    dp[i][1] = dp[i - 1][0]
print(dp[N - 1][0])