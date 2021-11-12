import sys

input = sys.stdin.readline
# 노드의 개수와 간선(union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [-1] * (v + 1)
edges = []
result = 0

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


# 부모 테이블상에서, 부모를 자기 자신으로 초기화

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 오름차순 정렬하기 위해 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

edges.sort()
max_cost = 0
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(a) != find(b):
        union(a, b)
        if cost > max_cost:
            max_cost = cost
        result += cost
result -= max_cost
print(result)