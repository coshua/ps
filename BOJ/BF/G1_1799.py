import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
N = int(input())

m =[[[0] for i in range(N)] for j in range(N)]

for i in range(N):
    m[i] = list(map(int, input().split()))

def dfs(cnt, r, c):
    m[r][c] = -1
