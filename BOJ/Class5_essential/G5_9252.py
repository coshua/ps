import sys 
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
f = input().strip()
s = input().strip()

fl = len(f)
sl = len(s)
dp = [['*'] * sl for _ in range(fl)]

def LCS(a, b):
    if a < 0 or b < 0:
        return ''
    
    if dp[a][b] == '*':
        dp[a][b] = ''

        if f[a] == s[b]:
            dp[a][b] = LCS(a - 1, b - 1) + f[a]
        else:
            if len(LCS(a - 1, b)) > len(LCS(a, b - 1)):
                dp[a][b] = LCS(a - 1, b)
            else:
                dp[a][b] = LCS(a, b - 1)
        
    return dp[a][b]

LCS(fl - 1, sl - 1)
if len(dp[fl - 1][sl - 1]) == 0:
    print(0)
else:
    print(len(dp[fl - 1][sl - 1]))
    print(dp[fl - 1][sl - 1])
