import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sys.setrecursionlimit(10**5)

arr.sort()

ans = []

def backtrack(arr, ids):
    if len(ids) == M:
        cur = []
        for id in ids:
            cur.append(arr[id])
        
        if not ans or ans[-1] != cur:
            ans.append(cur)
        return
    
    for i in range(N):
        if i not in ids:
            nxtids = ids[:]
            nxtids.append(i)
            backtrack(arr, nxtids)
    
    return

initiated = set()
for i in range(N):
    if arr[i] not in initiated:
        backtrack(arr, [i])
    initiated.add(arr[i])

for lst in ans:
    print(*lst)