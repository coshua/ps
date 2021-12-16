import sys
input = sys.stdin.readline
import heapq
inf = float('inf')


def solve():
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())

    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        s, e, c = map(int, input().split())
        c *= 2
        if (s == H or s == G) and (e == H or e == G):
            c += 1
        graph[s].append((e, c))
        graph[e].append((s, c))
    
    targets = [0] * T
    for i in range(T):
        temp = int(input())
        targets[i] = temp
    cost = [inf] * (N + 1)
    parent = [-1] * (N + 1)
    cost[S] = 0
    parent[S] = S

    q = []
    heapq.heappush(q, (0, S))
    while q:
        acc_cost, id = heapq.heappop(q)
        if acc_cost > cost[id]:
            continue
        for nxt_id, cur_cost in graph[id]:
            nxt_cost = cur_cost + acc_cost
            if nxt_cost < cost[nxt_id]:
                cost[nxt_id] = nxt_cost
                parent[nxt_id] = id
                heapq.heappush(q, (nxt_cost, nxt_id))
    print(cost)
    ans = []
    targets.sort()
    for num in targets:
        if cost[num] != inf and cost[num] % 2 == 1:
            print(num, end = " ")
    print()

T = int(input())
for _ in range(T):
    solve()

