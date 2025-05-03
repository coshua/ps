from collections import deque

A, B = map(int, input().split())

v = [False] * 100001

def bfs(a, b):
    t =  0
    q = deque()
    q.append(a)
    v[a]= True
    cur = 1
    nxt = 0
    while(q):
        c = q.popleft()
        if c == b:
            print(t)
            return
        if c * 2 <= 100000 and not v[c*2]:
            q.appendleft(c*2)
            v[c*2] = True
            cur += 1
        for i in [c-1, c+1]:
            if (0<=i<=100000 and not v[i]):
                v[i] = True
                q.append(i)
                nxt += 1
        cur -= 1
        if (cur == 0):
            cur = nxt
            nxt = 0
            t += 1

bfs(A, B)