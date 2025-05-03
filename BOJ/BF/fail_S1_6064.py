import sys 
input = sys.stdin.readline

T = int(input())
ans = [0] * T

for i in range(T):
    M, N, x, y = list(map(int, input().split()))
    if (M > N):
        t = M
        M = N
        N = t
        t = x
        x = y
        y = t
    a = 1
    found = False
    dif = x - y
    ix, iy = 1, 1
    cnt = 1
    while (cnt < M * N):
        cnt += M
        iy = (iy + M) % N
        if iy == 0:
            iy = N
        if (ix == 1 and iy == 1):
            break
    if (ix - iy == dif):
        found = True
        ans[i] = cnt + x - ix
    if not found:
        ans[i] = -1
    

sys.stdout.write("\n".join((map(str, ans))))