import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    T = int(input())
    A = int(input())
    a = [int(x) for x in input().split()]
    B = int(input())
    b = [int(x) for x in input().split()]

    d = defaultdict(int)
    for i in range(len(a)):
        s = 0
        for j in range(i, len(a)):
            s += a[j]
            d[s] += 1

    cnt = 0
    for i in range(len(b)):
        s = 0
        for j in range(i, len(b)):
            s += b[j]
            if T - s in d:
                cnt += d[T - s]

    print(cnt)

if __name__ == '__main__':
    solve()