M = 1000

# -1 은 자기 자신이 루트인 집합이다
parent = [-1] * 1001

def find(x):
    if parent[x] < 0:
        return x
    y = find(parent[x]) # flatten
    parent[x] = y
    return y

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y: return
    if (parent[x] <= parent[y]):
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y