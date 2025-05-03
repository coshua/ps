from collections import deque
n = int(input())
cnt = 0
q = deque()
def prime_list(n):
    sieve = [True] * (n + 1)

    m = int((n + 1) ** 0.5)

    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n + 1, i):
                sieve[j] = False
    
    return [i for i in range(2, n + 1) if sieve[i] == True]
div = prime_list(n)
print(div)
ln = len(div)
t, s = 0, 0
for i in range(ln):
    f = div[i]
    s += f
    while s > n and t < ln:
        s -= div[t]
        t += 1
    if s == n:
        cnt += 1
print(cnt)