import sys 
input = sys.stdin.readline

T = int(input())
m = [list(input().strip()) for _ in range(T)]
testm = [[[-1] * T for _ in range(T)] for j in range(2)]
mx = 0
dirs = ((0, 1), (1, 0)) # 0 to right, 1 to down
def dfs(dir, i, j):
    c = m[i][j]
    dx = dirs[dir][1]
    dy = dirs[dir][0]
    ti = i
    tj = j
    cnt = 0
    while (ti < T and tj < T and m[ti][tj] == c):
        cnt += 1
        ti += dy
        tj += dx
    if (dir == 0):
        if (T > ti - 1 >= 0 and 0 <= tj < T and m[ti - 1][tj] == c) or (0 <= ti + 1 < T and 0 <= tj < T and m[ti + 1][tj] == c):
            cnt += 1
            while (ti + dy < T and tj + dx < T and m[ti + dy][tj + dx] == c):
                cnt += 1
                ti += dy
                tj += dx
    if (dir == 1):
        if (T > tj - 1 >= 0 and 0 <= ti < T and m[ti][tj - j] == c) or (tj + 1 < T and 0 <= ti < T and m[ti][tj + 1] == c):
            cnt += 1
            while (ti + dy < T and tj + dx < T and m[ti + dy][tj + dx] == c):
                cnt += 1
                ti += dy
                tj += dx
    if (ti + dy < T and tj + dx < T and m[ti + dy][tj + dx] == c):
        cnt += 1
    testm[dir][i][j] = cnt
    return cnt
for i in range(T):
    for j in range(T):
        rm = dfs(0, i, j)
        dm = dfs(1, i, j)
        mx = max(mx, max(rm, dm))

print(mx)