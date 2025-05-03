n = int(input())

dp1x = [1, 1]
dp2x = [0, 0]

for i in range(2, n + 1):
    dp1x.append(dp1x[i - 1] + dp2x[i - 1])
    dp2x.append((dp1x[i - 2] + dp2x[i - 2]))

print((dp1x[n] + dp2x[n]) % 10007)
