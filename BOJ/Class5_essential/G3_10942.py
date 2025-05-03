import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())
m = [0] + list(map(int, input().split()))

Q = int(input())

dp = [[-1 for j in range(N + 1)] for i in range(N + 1)]

def getDP(s, e):
    if dp[s][e] == -1:
        if s == e:
            dp[s][e] = 1
        elif s == e - 1:
            dp[s][e] = 1 if m[s] == m[e] else 0
        else:
            prev = getDP(s + 1, e - 1)
            if prev == 1:
                dp[s][e] = 1 if m[s] == m[e] else 0
            else:
                dp[s][e] = 0
    return dp[s][e]

ans = [0] * Q
for i in range(Q):
    s, e = map(int, input().strip().split())
    ans[i] = getDP(s, e)

sys.stdout.write('\n'.join(map(str, ans)))