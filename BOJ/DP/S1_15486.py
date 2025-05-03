n = int(input())
comp = []
delay = []
for i in range(n):
    d, c = list(map(int, input().split()))
    comp.append(c)
    delay.append(d)

dp = [0] * (n + 1)

for i in range(n):
    if (delay[i] + i <= n):
        dp[i + delay[i]] = max(dp[i] + comp[i], dp[i + delay[i]])
    dp[i + 1] = max(dp[i + 1], dp[i])

print(dp[n])