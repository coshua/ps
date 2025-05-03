import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

acc = 0
for i in range(K):
    acc += arr[i]

ans = acc
for i in range(K, N):
    acc = acc - arr[i - K] + arr[i]
    ans = max(ans, acc)

print(ans)