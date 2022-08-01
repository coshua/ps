import sys
input = sys.stdin.readline
given = input().strip()
bomb = list(input().strip())
size = len(bomb)

arr = []
for i in range(len(given)):
    arr.append(given[i])

    if arr[-1] == bomb[-1]:

        if len(arr) - size >= 0 and arr[len(arr) - size:] == bomb[:]:
            
            arr = arr[:len(arr) - size]
    
if not arr:
    print("FRULA")
else:
    print(''.join(arr))