import sys 
input = sys.stdin.readline

N = int(input())
op = input().strip()

mx = [10] * N
mn = [-10] * N
for i in range(1, N + 1):
    c = op[int(-i * (i + 1) / 2)]
    if c == '0':
        mx[i - 1] = 0
        mn[i - 1] = 0
    elif c == '-':
        mx[i - 1] = -1
        mn[i - 1] = -10
    else:
        mx[i - 1] = 10
        mn[i - 1] = 1
    
def dfs(arr, depth):
    if depth > N:
        arr.reverse()
        sys.stdout.write(" ".join(map(str, arr)))
        exit()
    fromrange = mn[depth - 1]
    torange = mx[depth - 1]
    if op[int(-depth * (depth + 1) / 2) + 1] == '-':
        if len(arr) > 0 and arr[-1] > 0:
            torange = -arr[-1] - 1
    elif op[int(-depth * (depth + 1) / 2) + 1] == '+':
        if len(arr) > 0 and arr[-1] < 0:
            fromrange = -arr[-1] + 1
    elif op[int(-depth * (depth + 1) / 2) + 1] == '0':
        if len(arr) > 0 and arr[-1] == 0:
            torange = arr[-1]
            fromrange = arr[-1]
    for a in range(fromrange, torange + 1):
        temp = arr[:]
        sm = a
        able = True
        id = depth
        for b in range(int(-depth * (depth + 1) / 2 + 1), int(-(depth - 1) * depth / 2)):
            sm += arr[(id - 2)]
            id -= 1
            if (sm > 0 and op[b] != '+'):
                able = False
                break
            elif (sm < 0 and op[b] != '-'):
                able = False
                break
            elif (sm == 0 and op[b] != '0'):
                able = False
                break
        if able:
            temp.append(a)
            dfs(temp, depth + 1)

dfs([], 1)