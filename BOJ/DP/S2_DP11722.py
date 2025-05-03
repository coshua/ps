n = int(input())

lst = list(map(int, input().split()))

dp = [1] * n


m = 1

for i in range(1, n):
    for j in range(i):
        if (lst[j] > lst[i]):
            dp[i] = max(dp[i], dp[j] + 1)
    m = max(m, dp[i])
print(dp)