import sys
input = sys.stdin.readline

T = int(input())

dp = [[-1, -1] for _ in range(41)]
dp[0][0], dp[0][1] = 1, 0
dp[1][1], dp[1][0] = 1, 0

def getDP(n, cnt):
    if n <= 1:
        return dp[n][cnt]
    elif dp[n][cnt] == -1:
        dp[n][cnt] = getDP(n - 1, cnt) + getDP(n - 2, cnt)
    
    return dp[n][cnt]

for i in range(T):
    n = int(input())
    print(getDP(n, 0), getDP(n, 1))