import sys
input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
cnt = [[-1] * N for _ in range(N)]
cnt[0][0] = 1
def getcnt(y, x):
    if cnt[y][x] == -1:
        acc = 0
        for i in range(y):
            if graph[i][x] == y - i:
                acc += getcnt(i, x)
        for j in range(x):
            if graph[y][j] == x - j:
                acc += getcnt(y, j)
        cnt[y][x] = acc
    return cnt[y][x]

print(getcnt(N - 1, N - 1))