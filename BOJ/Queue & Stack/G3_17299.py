import sys
from collections import defaultdict
input = sys.stdin.readline

dic = defaultdict(int)
n = int(input())
m = list(map(int, input().split()))
for i in m:
    dic[i] += 1
ans = [-1 for _ in range(n)]
st = []
for i in range(n):
    while (len(st) > 0 and dic[m[st[-1]]] < dic[m[i]]):
        c = st.pop()
        ans[c] = m[i]
    st.append(i)
for i in ans:
    sys.stdout.write(str(i) + " ")

