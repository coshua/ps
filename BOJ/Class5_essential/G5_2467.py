import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())

lst = list(map(int, input().split()))

l = 0
r = len(lst) - 1

smallest = sys.maxsize
id = ()

while (l < r):
    sum = lst[l] + lst[r]
    if abs(sum) < smallest:
        smallest = abs(sum)
        id = (lst[l], lst[r])
    if sum < 0:
        l += 1
    else:
        r -= 1

print(id[0], id[1], end = ' ')