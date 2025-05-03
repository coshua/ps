import sys
input = sys.stdin.readline
N, M = map(int, input().split())
s = set(list(map(int, input().split())))

arr = []
for ele in s:
    arr.append(ele)
arr.sort()

def backtrack(arr, ids, length):
    if len(ids) == length:
        res = []
        for id in ids:
            res.append(arr[id])
        print(*res)
        return
    
    start = 0 if not ids else ids[-1]
    for i in range(start, len(arr)):
        nxtids = ids[:]
        nxtids.append(i)
        backtrack(arr, nxtids, length)

backtrack(arr, [], M)

