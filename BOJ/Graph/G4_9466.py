import sys
from collections import deque
input = sys.stdin.readline
T = int(input())

def solve(lst):
    n = len(lst)
    v = [False] * n
    cnt_prev_link = [0] * n
    for i in range(n):
        to = lst[i] - 1 # we use 0-base indexing
        cnt_prev_link[to] += 1
    cycle = [0] * n
    for i in range(n):
        if not v[i]:
            c = i
            temp_v = set()
            temp_v.add(c)
            nxt = lst[c] - 1
            while (not v[nxt]):
                if nxt in temp_v: # cycle found
                    while (cycle[nxt] == 0):
                        cycle[nxt] = 1
                        nxt = lst[nxt] - 1
                    break
                temp_v.add(nxt)
                nxt = lst[nxt] - 1
            for a in temp_v:
                v[a] = True
    print(cycle.count(0))

for _ in range(T):
    N = int(input())
    solve(list(map(int, input().split())))