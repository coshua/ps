import sys 
input = sys.stdin.readline
N, M = map(int, input().split())
    
def find(i):
    if parent[i] < 0:
        return i
    else:
        j = find(parent[i])
        parent[i] = j
        return j
def union(x, y):
    x = find(x)
    y = find(y)
    if (x == y):
        return
    if (parent[x] <= parent[y]):
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y
q = [0] * M

id = list(map(int, input().split()))[1:]

parent = [-1] * (N + 1)

for i in range(len(id) - 1):
    union(id[i], id[i + 1])

for i in range(M):
    lst = list(map(int, input().split()))[1:]
    q[i] = lst
    for j in range(0, len(lst) - 1):
        a = lst[j]
        b = lst[j + 1]
        union(a, b)

root = id[0] if id else -1
cnt = 0
if root == -1:
    print(len(q))
else:
    for i in q:
        same = False
        for c in i:
            if find(c) == find(root):
                same = True
                break
        if not same:
            cnt += 1
    print(cnt)
