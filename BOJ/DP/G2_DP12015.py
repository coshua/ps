# 원리 완벽히 이해하지 못함

from bisect import bisect_left

dp = []

n = int(input())

lst = list(map(int, input().split()))

for i in lst:
    k = bisect_left(dp, i)
    if (k >= len(dp)):
        dp.append(i)
    else:
        dp[k] = i
print(len(dp))