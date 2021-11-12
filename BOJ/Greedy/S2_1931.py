import sys
input = sys.stdin.readline

N = int(input())

m = [tuple(map(int, input().split())) for i in range(N)]

m.sort(key=lambda x:(x[1], x[0]))
print(m)
time = 0
cnt = 0
i = 0
while i < len(m):
    start, end = m[i]
    if start >= time:
        cnt += 1
        time = end
    else:
        i += 1
print(cnt)