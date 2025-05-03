import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    stickers = [[0] * N for _ in range(2)]
    stickers[0] = list(map(int, input().split()))
    stickers[1] = list(map(int, input().split()))

    dp = [[0] * (N + 1) for _ in range(2)]
    dp[0][1] = stickers[0][0]
    dp[1][1] = stickers[1][0]

    for i in range(2, N + 1):
        dp[0][i] = max(max(dp[0][i - 2], dp[1][i - 1]) + stickers[0][i - 1], dp[0][i - 1])
        dp[1][i] = max(max(dp[1][i - 2], dp[0][i - 1]) + stickers[1][i - 1], dp[1][i - 1])
    
    print(max(dp[0][N], dp[1][N]))
