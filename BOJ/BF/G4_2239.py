import sys
input = sys.stdin.readline

m = []
index = []
for i in range(9):
    row = list(map(int, input().strip()))
    for j in range(9):
        if row[j] == 0:
            index.append((i, j))
    m.append(row)

def validate_section(num, r, c):
    s_i = (r // 3) * 3
    s_j = (c // 3) * 3
    for i in range(s_i, s_i + 3):
        for j in range(s_j, s_j + 3):
            if m[i][j] == num:
                return False
    return True

def validate_linear(num, r, c):
    for i in range(9):
        if m[r][i] == num:
            return False
        if m[i][c] == num:
            return False
    return True

def dfs(d):
    if d == len(index):
        for i in range(9):
            print(''.join(map(str, m[i])))
        exit()
    
    for k in range(1, 10):
        if (validate_section(k, index[d][0], index[d][1]) and 
                validate_linear(k, index[d][0], index[d][1])): 
            m[index[d][0]][index[d][1]] = k
            dfs(d + 1)
            m[index[d][0]][index[d][1]] = 0
dfs(0)
