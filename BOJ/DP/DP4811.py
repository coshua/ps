dp = [1, 1]

for i in range(2, 31):
    adp = 0
    for j in range(0, i):
        adp += dp[j] * dp[i - j - 1]
    dp.append(adp)

while(True):
    a = input()
    if (a == "0"):
        break
    print(dp[int(a)])