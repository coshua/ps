import sys
input = sys.stdin.readline

N = int(input())

m = [[0] for i in range(N)]
f_col, s_col, t_col = 0, 0, 0
for i in range(N):
    m[i] = list(map(int, input().split()))

f_col = min(m[0][1] + m[N - 1][2], m[0][2] + m[N - 1][1])
s_col = min(m[0][0] + m[N - 1][2], m[0][2] + m[N - 1][0])
t_col = min(m[0][0] + m[N - 1][1], m[0][1] + m[N - 1][0])

if N == 2:
    print(min(min(f_col, s_col), t_col))
    sys.exit(0)

f_col += m[1][0]
s_col += m[1][1]
t_col += m[1][2]
for i in range(2, N - 1):
    f_nxt = m[i][0] + min(s_col, t_col)
    s_nxt = m[i][1] + min(f_col, t_col)
    t_nxt = m[i][2] + min(f_col, s_col)
    f_col = f_nxt
    s_col = s_nxt
    t_col = t_nxt

print(min(t_col, min(f_col, s_col)))