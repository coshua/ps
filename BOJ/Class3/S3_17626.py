import math
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

dp = [float('inf')] * 50001
for i in range(1, math.floor(math.sqrt(50000))):
    dp[i * i] = 1

def getDP(n):
    if dp[n] == float('inf'):
        for i in range(1, n // 2):
            dp[n] = min(dp[n], getDP(i) + getDP(n - i))
    return dp[n]

N = int(input())
print(getDP(N))