lst = [[0 for i in range(200)] for j in range(201)]

for i in range(201):
    for j in range(200):
        if (i == 0 or j == 0):
            lst[i][j] = 1
        else:
            for k in range(i + 1):
                lst[i][j] += lst[k][j - 1]
            lst[i][j] %= 1000000000

inp = list(map(int, input().split()))
print(lst[inp[0]][inp[1] - 1])