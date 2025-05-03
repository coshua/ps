import sys
input = lambda: sys.stdin.readline().strip()


R, C = list(map(int, input().split()))
m = [list(map(lambda x : ord(x) - 65, input())) for _ in range(R)]
ch = [0]*26
mx = 0
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def dfs(ans, i, j):
    global mx
    
    mx = max(mx, ans)
    for t in range(4):
        ny = i + dy[t]
        nx = j + dx[t]
        if (0 <= ny < R and 0 <= nx < C and ch[m[ny][nx]] == 0):
            ch[m[ny][nx]] = 1
            dfs(ans + 1, ny, nx)
            ch[m[ny][nx]] = 0
ch[m[0][0]] = 1
dfs(1, 0, 0)
print(mx)