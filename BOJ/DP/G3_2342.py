import sys
from collections import deque
input = sys.stdin.readline

move = list(map(int, input().split()))

if len(move) == 0:
    print(0)
    sys.exit(0)

def find_min(prev, r, c):
    m = 500000

    for i in range(5):
        if prev[i][c] > -1:
            # 왼발 움직이기
            # 출발점에서 왼발 움직이는 경우
            if i == 0:
                m = min(m, prev[i][c] + 2)
            # 움직일 필요 없는 경우
            elif i == r:
                m = min(m, prev[i][c] + 1)
            # 반대편으로 왼발 움직이는 경우
            elif abs(i - r) % 2 == 0:
                m = min(m, prev[i][c] + 4)
            # 인접 칸으로 왼발 움직이는 경우
            else:
                m = min(m, prev[i][c] + 3)

            # 오른발 움직이기
        if prev[r][i] > -1:
            if i == 0:
                m = min(m, prev[r][i] + 2)
            elif abs(i - c) % 2 == 0:
                m = min(m, prev[r][i] + 4)
            else:
                m = min(m, prev[r][i] + 3)
    return -1 if m == 500000 else m

def find_nxt_board(prev, m):
    nxt = [[-1 for i in range(5)] for j in range(5)]
    for i in range(5):
        nxt[m][i] = find_min(prev, m, i)
        nxt[i][m] = find_min(prev, i, m)
    return nxt

prev = [[-1 for i in range(5)] for j in range(5)]
prev[0][0] = 0
for i in range(len(move) - 1):
    nxt = find_nxt_board(prev, move[i])
    prev = nxt
ans = sys.maxsize
for i in range(5):
    for j in range(5):
        if prev[i][j] > -1:
            ans = min(ans, prev[i][j])
print(ans)