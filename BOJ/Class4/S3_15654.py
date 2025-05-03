import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sys.setrecursionlimit(10**5)

arr.sort()

def backtrack(arr, ids):
    if len(ids) == M:
        for id in ids:
            sys.stdout.write(str(arr[id]) + " ")
        print()
        return
    
    for i in range(N):
        if i not in ids:
            nxtids = ids[:]
            nxtids.append(i)
            backtrack(arr, nxtids)
    
    return

backtrack(arr, [])