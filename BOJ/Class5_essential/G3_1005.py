import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for test in range(T):
    N, K = map(int, input().split())
    time = list(map(int, input().split()))

    cnt_enter_link = [0] * (N)
    graph = [[] for _ in range(N)]
    dp_build_time = [0] * (N)

    for _ in range(K):
        a, b = map(int, input().split())
        graph[a - 1].append(b - 1)
        cnt_enter_link[b - 1] += 1

    q = deque()
    for i in range(N):
        if cnt_enter_link[i] == 0:
            q.append(i)
    w = int(input()) - 1
    while(q):
        c = q.popleft()
        if c == w:
            print(dp_build_time[c] + time[c])
        for i in graph[c]:
            cnt_enter_link[i] -= 1
            dp_build_time[i] = max(dp_build_time[i], dp_build_time[c] + time[c])
            if cnt_enter_link[i] == 0:
                q.append(i)
