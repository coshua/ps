import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

R, C = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
routes = [[-1] * C for _ in range(R)]
routes[0][0] = 1
dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
def get_route(y, x):
    if routes[y][x] == -1:
        acc = 0
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < R and 0 <= nx < C and graph[ny][nx] > graph[y][x]:
                acc += get_route(ny, nx)
        routes[y][x] = acc
    return routes[y][x]

print(get_route(R - 1, C - 1))