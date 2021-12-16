import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
plates = [0] * N

for i in range(N):
    plates[i] = int(input().strip())

sushi = [0] * (D + 1)
sushi[C] = float('inf')

cnt = 1

for i in range(K):
    if sushi[plates[i]] == 0:
        cnt += 1
    sushi[plates[i]] += 1

ans = cnt

for i in range(K, N + K - 1):
    #take off a plate
    if sushi[plates[i - K]] == 1:
        cnt -= 1
    sushi[plates[i - K]] -= 1

    #get next plate
    if sushi[plates[i % N]] == 0:
        cnt += 1
    sushi[plates[i % N]] += 1

    ans = max(ans, cnt)

print(ans)