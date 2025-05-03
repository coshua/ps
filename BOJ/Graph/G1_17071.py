A, B = map(int, input().split())

cache = [[False] * 500001 for _ in range(2)] 
# cache[i][0] means Subin could find her sister on every t % 2 == 0

def bfs(a, b):
    q = [a]
    q.append(a)
    cache[0][a] = True
    t = 0
    moveamount = 0
    while (q):
        if b > 500000:
            print(-1)
            return
        if cache[t % 2][b]:
            print(t)
            return
        lt = len(q)
        tmp = []
        for j in range(lt):
            c = q[j]
            for i in [c - 1, c + 1, c * 2]:
                if 0<=i<=500000 and not cache[(t + 1) % 2][i]:
                    cache[(t + 1) % 2][i] = True
                    tmp.append(i)
        q = tmp
        moveamount += 1
        b += moveamount
        t += 1

bfs(A, B)