n = int(input())

lst = [0 for i in range(n + 1)]

for i in range(n):
    if (i == n - 1):
        lst[i: i+2] =  list(map(int, input().split()))
    else:
        lst[i] = list(map(int, input().split()))[0]

lst = [lst[:] for i in range(n - 1)]
dp = [0] * (n)

