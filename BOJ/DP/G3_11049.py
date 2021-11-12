import sys 
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
N = int(input())

dic = defaultdict(int)

init = [0] * (N - 1)

for i in range(N):
    if i == N - 1:
        init += list(map(int, input().split()))
    else:
        init[i] = list(map(int, input().split()))[0]

def multiply(lst):
    ln = len(lst)
    if ln == 2:
        return
    for i in range(1, ln - 1):
        amnt = lst[i - 1] * lst[i] * lst[i + 1]
        temp = lst[:i] + lst[i + 1:]
        temp = tuple(temp)
        if dic[temp] == 0:
            dic[temp] = dic[lst] + amnt
        else:
            dic[temp] = min(dic[temp], dic[lst] + amnt)
        multiply(temp)

multiply(tuple(init))

print(dic[(init[0], init[N])])
