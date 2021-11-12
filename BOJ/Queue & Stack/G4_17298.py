import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))

st = []
ans = [-1] * n
for i in range(n):
    while len(st) > 0 and m[st[-1]] < m[i]:
        c = st.pop()
        ans[c] = m[i]
    st.append(i)
sys.output.write(" ".join(map(str, ans)))
# print(" ".join(map(str, ans)))
# for i in ans:
#    sys.stdout.write(str(i) + " ")