import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
print = sys.stdout.write

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def backtrack(arr, ids, length):
    if len(ids) == length:
        for id in ids:
            print(str(arr[id]) + " ")
        print("\n")
        return
    
    start = 0 if not ids else ids[-1]
    for i in range(start, len(arr)):
        nxtids = ids[:]
        nxtids.append(i)
        backtrack(arr, nxtids, length)
    
    return

backtrack(arr, [], M)