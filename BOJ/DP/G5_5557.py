import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

dp = [[0 for i in range(N - 1)] for j in range(21)]
dp[lst[0]][0] = 1

for j in range(1, N - 1):
    # 이번 차례에 더하거나 빼야하는 수
    add = lst[j]

    for i in range(21):
        add_nxt = i + add
        if add_nxt < 21:
            dp[add_nxt][j] += dp[i][j - 1]
        
        subtract_next = i - add
        if subtract_next >= 0:
            dp[subtract_next][j] += dp[i][j - 1]

print(dp[lst[N - 1]][N - 2])
