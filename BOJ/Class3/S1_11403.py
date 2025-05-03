import sys
input = sys.stdin.readline

N = int(input())
p = [i for i in range(N + 1)]

def find(p, u):
    if p[u] != u:
        p[u] = find(p[u])
    return p[u]

for i in range(N):
    lst = list(map(int, input().split()))