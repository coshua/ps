from collections import deque
from sys import stdin

inp = list(map(int, input().split()))



def op():
    cnt = 0
    cur = 0
    nxt = 1
    dirs = ((-1, 0), (0, 1), (1, 0), (0, -1))
    q = deque()
    q.append((0, 0, 0))

    while(len(q) > 0):
        x, y, w = q.popleft()
