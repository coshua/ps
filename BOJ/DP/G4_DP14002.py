n = int(input())

track = [[] for i in range(n)]

lst = list(map(int, input().split()))
dp = [0 for i in range(n)]
dp[0] = 1
for i in range(n):
    cnt = 1
    idx = -1
    for j in range(i):
        if(lst[j] < lst[i]):
            if (dp[j] + 1 > cnt):
                cnt = dp[j] + 1
                idx = j
    dp[i] = cnt
    if (idx > -1):
        track[i] = track[idx][:]
        track[i].append(lst[idx])

maxidx = 0
maxlt = 1
for i, item in enumerate(dp):
    if (item > maxlt):
        maxidx = i
        maxlt = item
track[maxidx].append(lst[maxidx])

print(maxlt)
for i in track[maxidx]:
    print(i, end = " ")