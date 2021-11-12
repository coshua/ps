from collections import deque
import sys
sys.setrecursionlimit(10**9)
dp = [-1] * 3001
gp = [[] for _ in range(3001)]

N = int(input())

for _ in range(N):
    a, b = list(map(int, input().split()))

    gp[a].append(b)
    gp[b].append(a)
v = [False] * 3001
found = False
ans = []
def dfs(s, track):
    global found
    global ans
    v[s] = True
    if (found):
        return
    for i in gp[s]:
        if (len(track) >= 2 and i == track[0]):
            found = True
            track.append(s)
            ans = track
            return
        if (found):
            return
        if not v[i]:
            temp = track[:]
            temp.append(s)
            dfs(i, temp)
            v[i] = False

for i in range(1, N):
    if (found):
        break
    if (not found and len(gp[i]) > 1):
        dfs(i, [])

s = set(ans)
for i in s:
    dp[i] = 0
for i in range(1, N + 1):
    if (i in s):
        dp[i] = 0
    else:
        q = deque()
        cnt = 0
        cur = 1
        nxt = 0
        q.append(i)
        nv = [False] * 3001
        nv[i] = True
        while (q):
            a = q.popleft()
            if (dp[a] == 0):
                break
            for num in gp[a]:
                if (not nv[num]):
                    nv[num] = True
                    q.append(num)
                    nxt += 1
            cur -= 1
            if (cur == 0):
                cur = nxt
                nxt = 0
                cnt += 1
        dp[i] = cnt

for i in range(1, N + 1):
    print(dp[i], end = " ")
