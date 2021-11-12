dp = [[0 for i in range(1000)] for j in range(10)]

for i in range(10):
    for j in range(1000):
        if (i == 0):
            dp[i][j] = 1
        elif (j == 0):
            dp[i][j] = 1
        else:
            for k in range(i + 1):
                dp[i][j] += dp[k][j - 1]
                dp[i][j] %= 10007

n = int(input()) - 1
sum = 0
for i in range(10):
    sum += dp[i][n]
print(sum % 10007)