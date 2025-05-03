import sys
input = sys.stdin.readline

N, T = map(int, input().split())
v = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

m = [[0 for i in range(10001)] for j in range(N + 1)]

for i in range(1, N + 1):
    for j in range(0, c[i]):
        m[i][j] = m[i - 1][j]
    for j in range(c[i], 10001):
        m[i][j] = max(m[i - 1][j], m[i - 1][j - c[i]] + v[i])
        if m[i][j] >= T:
            break

for c in range(10001):
    for r in range(N + 1):
        if m[r][c] >= T:
            print(c)
            sys.exit(0)
