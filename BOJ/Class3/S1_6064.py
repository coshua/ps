import sys
input = sys.stdin.readline

def calc_year(m, n, x, y):
    if m > n:
        m, n, x, y = n, m, y, x
    
    dif = y - x
    year = 1
    s_m, s_n = 1, 1
    while s_n - s_m != dif:
        s_n += m
        year += m
        if s_n > n:
            s_n -= n
        if s_n == 1:
            break
    if s_n - s_m == dif:
        print(s_m, s_n, dif)
        print(year + x - 1)
    else:
        print(-1)

T = int(input())
for i in range(T):
    m, n, x, y = map(int, input().split())
    calc_year(m, n, x, y)