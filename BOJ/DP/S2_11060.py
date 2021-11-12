n = int(input())

m = list(map(int, input().split()))
cnt = 0
id = 0
able = False
while (True):
    if (id >= n - 1):
        able = True
        break
    if (id + m[id] >= n - 1):
        cnt += 1
        able = True
        break
    plus = 0
    mid = id
    for i in range(id + 1, id + m[id] + 1):
        if (m[i] == 0):
            continue
        temp = i - id + m[i]
        if (temp > plus):
            plus = temp
            mid = i
    if (plus == 0):
        break
    id = mid
    cnt += 1
if not able:
    print(-1)
else:
    print(cnt)
