R, C = list(map(int, input().split()))

m = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    for j in range(C):
        a = 0
        if (i > 0):
            a = m[i - 1][j]
        b = 0
        if (j > 0):
            b = m[i][j - 1]
        c = 0
        if (i > 0 and j > 0):
            c = m[i - 1][j - 1]
        m[i][j] = max(a, max(b, c)) + m[i][j]

print(m[R - 1][C - 1])