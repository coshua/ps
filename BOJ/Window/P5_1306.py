import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
K = K * 2 - 1

arr = list(map(int, input().split()))

q = deque()
ans = []
for i in range(K):
    while q and arr[i] > arr[q[-1]]:
        q.pop()
    q.append(i)

ans.append(arr[q[0]])
for i in range(K, N):
    while q and q[0] <= i - K:
        q.popleft()
    
    while q and arr[i] > arr[q[-1]]:
        q.pop()
    q.append(i)
    ans.append(arr[q[0]])

print(*ans)