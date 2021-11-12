N = int(input())

m = [[' '] * N for i in range(N)]

def draw(y, x):
    for i in range(3):
        m[y][x + i] = '*'
        m[y + 2][x + i] = '*'
    m[y + 1][x] = '*'
    m[y + 1][x + 2] = '*'

def dq(n, y, x):
    if n == 3:
        draw(y, x)
        return

    for i in range(3):
        dq(n / 3, y, int(x + i * (n / 3)))
        dq(n / 3, int(y + 2 * (n / 3)), int(x + i * (n / 3)))
    dq(n / 3, int(y + (n / 3)), x)
    dq(n / 3, int(y + (n / 3)), int(x + 2 * (n / 3)))

dq(N, 0, 0)
for i in range(N):
    print(''.join(m[i]))
