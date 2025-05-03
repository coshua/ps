import sys 
input = sys.stdin.readline
n = int(input())

mn = [0] * 3
mx = [0] * 3
for _ in range(n):
    a, b, c = map(int, input().split())
    tempa = max(mx[0], mx[1]) + a
    tempb = max(max(mx[0], mx[1]), mx[2]) + b
    tempc = max(mx[1], mx[2]) + c
    mina = min(mn[0], mn[1]) + a
    minb = min(min(mn[0], mn[1]), mn[2]) + b
    minc = min(mn[1], mn[2]) + c
    mn = [mina, minb, minc]
    mx = [tempa, tempb, tempc]
print(max(mx), min(mn), end = " ")