import sys
input = sys.stdin.readline

N = int(input())
boxes = list(map(int, input().split()))
cnt = [0] * N
maxbox = 0
for i in range(N):
    for j in range(i):
        if boxes[i] > boxes[j]:
            cnt[i] = max(cnt[i], cnt[j] + 1)
        maxbox = max(maxbox, cnt[i])

print(maxbox + 1)