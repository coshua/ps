import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = list(map(int, input().split()))
m = [[0] * N for _ in range(N)]

houseid = []
chickenid = []
for i in range(N):
    row = list(map(int, input().split()))
    m[i] = row
    for j in range(N):
        if row[j] == 1:
            houseid.append((i, j))
        elif row[j] == 2:
            chickenid.append((i, j))

min_distance = sys.maxsize
for i in combinations(chickenid, M):
    dist = 0
    for house in houseid:
        temp = float('inf')
        for j in range(M):
            temp = min(temp, abs(house[0] - i[j][0]) + abs(house[1] - i[j][1]))
        dist += temp
    min_distance = min(min_distance, dist)
print(min_distance)