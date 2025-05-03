import sys 
input = sys.stdin.readline
N, S = list(map(int, input().split()))
m = list(map(int, input().split()))

ans = sys.maxsize
prep = 0
postp = 0
s = 0

while (prep < N or postp < N):
    while postp < N and s < S:
        s += m[postp]
        postp += 1
    while prep < N and s >= S:
        s -= m[prep]
        prep += 1
    ans = min(ans, postp - prep + 1)
    if postp == N and s < S:
        break

if sum(m) < S:
    print(0)
else:
    print(ans)