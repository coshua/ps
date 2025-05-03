from collections import deque
from functools import total_ordering
N = int(input())

v = [[[False] * 61 for i in range(61)] for j in range(61)]

lst = list(map(int, input().split()))
if (len(lst) < 3):
    lst.append(0)

if (len(lst) < 3):
    lst.append(0)

q = deque()
lst.sort(reverse=True)
q.append(lst)

v[lst[0]][lst[1]][lst[2]] = True

cnt = 0
found = False
while(not found):
    ln = len(q)
    for _ in range(ln):
        x, y, z = q.popleft()
        if (x == 0 and y == 0 and z == 0):
            found = True
            break
        nx = 0 if x < 9 else x - 9
        ny = 0 if y < 3 else y - 3
        nz = 0 if z < 1 else z - 1
        tlst = [nx, ny, nz]
        tlst.sort(reverse=True)
        if not v[tlst[0]][tlst[1]][tlst[2]]:
            q.append(tlst)
            v[tlst[0]][tlst[1]][tlst[2]] = True
        ny = 0 if y < 1 else y - 1
        nz = 0 if z < 3 else z - 3
        tlst = [nx, ny, nz]
        tlst.sort(reverse=True)
        if not v[tlst[0]][tlst[1]][tlst[2]]:
            q.append(tlst)
            v[tlst[0]][tlst[1]][tlst[2]] = True
    if found:
        break
    cnt += 1
print(cnt)