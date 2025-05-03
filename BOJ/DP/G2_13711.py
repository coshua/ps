from bisect import bisect_left
import sys 
input = sys.stdin.readline

N = int(input())
first_list = list(map(int, input().strip().split()))
sec_list = list(map(int, input().strip().split()))
occ = [-1] * (N + 1)

for id, item in enumerate(sec_list):
    occ[item] = id + 1

dp = []

for i in first_list:
    temp = occ[i]
    k = bisect_left(dp, temp)
    if (k >= len(dp)):
        dp.append(temp)
    else:
        dp[k] = temp
print(len(dp))