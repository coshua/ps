import sys
from bisect import bisect_left
input = sys.stdin.readline

G = int(input())
P = int(input())

f = [-1] * (G + 1)

cnt = 0
s = [0] * P
for i in range(P):
    s[i] = int(input())
for i in range(P):
    target = s[i]
    prev = []
    while f[target] != -1:
        prev.append(target)
        target = f[target]
    if target == 0:
        break
    for a in prev:
        f[a] = target - 1
    f[target] = target - 1
print(len([i for i in f if i > -1]))

    