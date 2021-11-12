import sys
input = sys.stdin.readline
S = input().strip()

cnt_A, cnt_B, cnt_C = 0, 0, 0
for i in S:
    if i == 'A':
        cnt_A += 1
    elif i == 'B':
        cnt_B += 1
    else:
        cnt_C += 1

