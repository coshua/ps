import sys
input = sys.stdin.readline

N, M = map(int, input().split())
d = {}

for i in range(N):
    a, b = input().split()
    d[a] = b

for i in range(M):
    sys.stdout.write(d[input().strip()] + "\n")