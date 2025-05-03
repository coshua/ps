import sys
input = sys.stdin.readline

R, C = map(int, input().split())

origin = [list(map(int, input().strip())) for j in range(R)]

destin = [list(map(int, input().strip())) for j in range(R)]

def flip(i, j):
    if (i + 2 >= R or j + 2 >= C):
        return
    for r in range(3):
        for c in range(3):
            origin[i + r][j + c] ^= 1
f_cnt = 0
for i in range(R):
    for j in range(C):
        if origin[i][j] != destin[i][j]:
            flip(i, j)
            f_cnt += 1

def has_same_element():
    for i in range(R):
        for j in range(C):
            if origin[i][j] != destin[i][j]:
                return False
    return True

if has_same_element():
    print(f_cnt)
else:
    print(-1)