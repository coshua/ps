import sys 
from queue import PriorityQueue
input = sys.stdin.readline
N, M = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]
prev_link_cnt = [0] * (N + 1)

for _ in range(M):
    a, b = list(map(int, input().strip().split()))
    graph[a].append(b)
    prev_link_cnt[b] += 1

q = PriorityQueue()

for i in range(1, N + 1):
    if prev_link_cnt[i] == 0:
        q.put(i)

while(q.qsize() > 0):
    c = q.get()
    for item in graph[c]:
        prev_link_cnt[item] -= 1
        if prev_link_cnt[item] == 0:
            q.put(item)
    sys.stdout.write(str(c) + " ")