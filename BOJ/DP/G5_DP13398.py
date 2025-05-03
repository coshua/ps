n = int(input())

lst = list(map(int, input().split()))

dp = [[0, 0] for i in range(len(lst))]
dp[0][0] = lst[0]
m = -1000000000
for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + lst[i], lst[i])
    dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + lst[i])
    m = max(m, dp[i][0], dp[i][1])
print(m)


