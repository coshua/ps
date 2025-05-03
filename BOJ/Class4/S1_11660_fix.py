import sys
input = sys.stdin.readline
print = sys.stdout.write

N, T = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(N)]

# now graph[i][j] stores accumulation of sum(graph[i][0]...graph[i][j])
for i in range(N):
    acc = 0
    for j in range(N):
        acc += graph[i][j]
        graph[i][j] = acc

for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())

    acc = 0
    for i in range(x1 - 1, x2):
        acc += graph[i][y2 - 1]
        if y1 > 1:
            acc -= graph[i][y1 - 2]
    
    print(str(acc) + "\n")