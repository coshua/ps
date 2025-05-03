import sys
input = sys.stdin.readline

N = int(input())
trains = list(map(int, input().split()))
window = int(input())

dp = [[-1 for i in range(N + 1)] for j in range(3)]

sum_trains = [0] * (N - window + 1)
sm = 0
for i in range(window):
    sm += trains[i]

sum_trains[0] = sm
for i in range(1, N - window + 1):
    sm -= trains[i - 1]
    sm += trains[i + window - 1]
    sum_trains[i] = sm

for i in range(0, N + 1 - window):
    # 현재 인덱스에서 첫번째 열차가 시작되는 경우
    dp[0][i + window] = max(sum_trains[i], dp[0][i + window - 1])
    
    # 현재 인덱스에서 두번째 열차가 시작되는 경우
    if dp[0][i] > -1:
        dp[1][i + window] = max(dp[0][i] + sum_trains[i], dp[1][i + window - 1])

    # 현재 인덱스에서 세번째 열차가 시작되는 경우
    if dp[1][i] > -1:
        dp[2][i + window] = max(dp[1][i] + sum_trains[i], dp[2][i + window - 1])

print(dp[2][N])