import sys 
input = sys.stdin.readline

T = int(input())

dp = [0] * 2501

dp[0] = 1
dp[1] = 1

for i in range(2, 2501):
    for j in range(0, i):
        dp[i] += (dp[j] * dp[i - j - 1]) % 1000000007
        dp[i] %= 1000000007

dp[0] = 0
for i in range(T):
    c = int(input())
    print(0 if c % 2 == 1 else dp[int(c / 2)])