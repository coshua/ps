import sys 
input = sys.stdin.readline

f = input().strip()
s = input().strip()
t = input().strip()

fl = len(f)
sl = len(s)
tl = len(t)

dp = [[[-1] * tl for i in range(sl)] for j in range(fl)]

def LCS(a, b, c):
    if a < 0 or b < 0 or c < 0:
        return 0
    
    if dp[a][b][c] == -1:
        dp[a][b][c] = 0

        if f[a] == s[b] == t[c]:
            dp[a][b][c] = LCS(a - 1, b - 1, c - 1) + 1
        else:
            dp[a][b][c] = max(max(LCS(a, b - 1, c), LCS(a - 1, b, c)), LCS(a, b, c - 1))
    
    return dp[a][b][c]

print(LCS(fl - 1, sl - 1, tl - 1))

