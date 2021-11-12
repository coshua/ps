from bisect import bisect_left
import sys 
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))

dp = []
id = [0] * n
for i in range(n):
    k = bisect_left(dp, lst[i])
    if k >= len(dp):
        dp.append(lst[i])
    else:
        dp[k] = lst[i]
    id[i] = k

print(len(dp))

ans = [0] * (len(dp))
idx = len(dp) - 1
for i in range(n - 1, -1, -1):
    if id[i] == idx:
        ans[idx] = lst[i]
        idx -= 1
print(' '.join(map(str, ans)))