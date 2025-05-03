import sys 
input = sys.stdin.readline


N, T = list(map(int, input().split()))
times = [0] * N
scores = [0] * N

for i in range(N):
    a, b = list(map(int, input().split()))
    times[i] = a
    scores[i] = b

dp = [[-1 for j in range(T + 1)] for _ in range(N)]

def getDP(n, t):
    if (n < 0 or t < 0):
        return 0

    if (dp[n][t] == -1):
        if times[n] > t:
            dp[n][t] = getDP(n - 1, t)
        else:
            dp[n][t] = max(getDP(n - 1, t), getDP(n - 1, t - times[n]) + scores[n])

    return dp[n][t]

print(getDP(N - 1, T))
