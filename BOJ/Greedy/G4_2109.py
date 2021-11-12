import sys
input = sys.stdin.readline

N = int(input())

m = [tuple(map(int, input().split())) for i in range(N)]

m.sort(key=lambda x:(x[1], -x[0]))

crt = 1
reward = 0
for pay, day in m:
    if day < crt:
        continue
    reward += pay
    crt += 1
print(reward)
print(crt)