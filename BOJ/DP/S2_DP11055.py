n = int(input())

lst = list(map(int, input().split()))

dp = lst[:]

m = lst[0]
for i in range(1, n):
    for j in range(i):
        if (lst[i] > lst[j]):
            dp[i] = max(dp[i], dp[j] + lst[i])
    m = max(m, dp[i])
print(dp)
