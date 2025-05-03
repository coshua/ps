import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
p = [i for i in range(V + 1)]

def find(p, u):
    if p[u] == u:
        return u
    p[u] = find(p, p[u])
    return p[u]

def union(p, u, v):
    pu, pv = find(p, u), find(p, v)
    if pu == pv:
        return False
    else:
        p[pu] = pv
        return True

for _ in range(E):
    u, v = map(int, input().split())
    union(p, u, v)

cnt = set()
for i in range(1, V + 1):
    group = find(p, i)
    cnt.add(group)

print(len(cnt))