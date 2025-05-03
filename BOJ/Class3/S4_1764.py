import sys
from collections import defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())

cnt = 0
d = defaultdict(int)
for i in range(N):
    d[input().strip()] += 1
for j in range(M):
    s = input().strip()
    d[s] += 1
    cnt += 1 if d[s] == 2 else 0

print(cnt)
d = sorted(d.items())

for i in range(len(d)):
    if d[i][1] == 2:
        print(d[i][0])