T = int(input())

for i in range(T):
    n = int(input())
    lst = [0, 0]
    lst[0] = list(map(int, input().split()))
    lst[1] = list(map(int, input().split()))
    dp = [[0 for i in range(n)] for j in range(3)]
    dp[1][0] = lst[1][0]
    dp[0][0] = lst[0][0]
    m = 0
    for j in range(1, n):
        dp[2][j] = max(max(dp[0][j-1], dp[1][j-1]), dp[2][j-1])
        dp[0][j] = max(max(dp[1][j-1] + lst[0][j], dp[2][j-1] + lst[0][j]), dp[0][j-1])
        dp[1][j] = max(max(dp[0][j-1] + lst[1][j], dp[2][j-1] + lst[1][j]), dp[1][j-1])
    m = max(dp[1][j], dp[0][j])
    print(m)
    
