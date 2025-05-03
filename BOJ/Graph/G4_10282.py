import sys
input = sys.stdin.readline
import heapq

T = int(input())

def simulation():
    N, D, S = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(D):
        e, s, w = map(int, input().split())
        graph[s].append((e, w))
    
    time = [float('inf')] * (N + 1)
    time[S] = 0

    pq = []

    heapq.heappush(pq, (0, S))

    while pq:
        cur_time, cur_comp = heapq.heappop(pq)

        for nxt_comp, w in graph[cur_comp]:
            old_time = time[nxt_comp]
            new_time = cur_time + w
            if new_time < old_time:
                heapq.heappush(pq, (new_time, nxt_comp))
                time[nxt_comp] = new_time

    cnt = 0
    maxtime = 0
    for i in range(1, N + 1):
        if time[i] != float('inf'):
            cnt += 1
            maxtime = max(maxtime, time[i])

    print(cnt, maxtime)    

for _ in range(T):
    simulation()   
