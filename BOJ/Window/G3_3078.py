import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
K += 1
name_cnt_by_length = [0] * 21

ans = 0
q = deque()
for i in range(K):
    ln = len(input().strip())
    ans += name_cnt_by_length[ln]
    name_cnt_by_length[ln] += 1
    q.append(ln)

for i in range(K, N):
    ln = len(input().strip())
    name_out = q.popleft()
    name_cnt_by_length[name_out] -= 1
    ans += name_cnt_by_length[ln]
    name_cnt_by_length[ln] += 1
    q.append(ln)

print(ans)
