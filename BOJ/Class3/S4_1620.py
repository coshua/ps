import sys
input = sys.stdin.readline

N, M = map(int, input().split())

d = {}
for i in range(N):
    pokemon = input().strip()
    d[i + 1] = pokemon
    d[pokemon] = i + 1

for i in range(M):
    call = input().rstrip()
    if call.isdigit():
        print(d[int(call)])
    else:
        print(d[call])