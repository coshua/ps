import sys
input = sys.stdin.readline

N = int(input())

dp = [[0] * N for _ in range(2)]
dp[1][0] = 1
if N > 1:
    dp[0][1] = 1
    dp[1][1] = 1

for i in range(2, N):
    dp[0][i] = dp[0][i - 2] + dp[1][i - 2]
    dp[1][i] = dp[0][i - 1] + dp[1][i - 1]

prev = 0
M = int(input())
acc = 1
for _ in range(M):
    nxt = int(input())
    diff = nxt - prev - 1
    if diff > 0:
        cases = dp[0][diff - 1] + dp[1][diff - 1]
        acc *= cases
    prev = nxt

diff = N - prev
if diff > 0:
    cases = dp[0][diff - 1] + dp[1][diff - 1]
    acc *= cases
print(acc)