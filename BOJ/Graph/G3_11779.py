import sys 
input = sys.stdin.readline
import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    v, u, w = map(int, input().split())
    graph[v].append((u, w))

S, E = map(int, input().split())

parent = [-1] * (N + 1)
cost = [float('inf')] * (N + 1)

parent[S] = S
pq = []
heapq.heappush(pq, (0, S))

visited = set()
while pq:
    cur_cost, cur_vertex = heapq.heappop(pq)
    visited.add(cur_vertex)

    if cur_vertex == E:
        print(cur_cost)
        lst = []
        temp = cur_vertex
        while parent[temp] != temp:
            lst.append(temp)
            temp = parent[temp]
        lst.append(S)
        print(len(lst))
        lst.reverse()
        print(*lst)
        break
    for e, c in graph[cur_vertex]:
        if e not in visited:
            old_cost = cost[e]
            new_cost = cur_cost + c
            if new_cost < old_cost:
                heapq.heappush(pq, (new_cost, e))
                cost[e] = new_cost
                parent[e] = cur_vertex