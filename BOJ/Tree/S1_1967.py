import sys 
input = sys.stdin.readline
N = int(input())

tree = [[] for _ in range(N + 1)]
maxarr = [-1] * (N + 1)
maxDistance = 0
for _ in range(N - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))

def getmax(n):
    global maxDistance
    if n == -1:
        return 0
    if maxarr[n] == -1:
        first_c, second_c = -1, -1
        first_w, second_w = 0, 0
        if len(tree[n]) == 2:
            first_c, first_w = tree[n][0]
            second_c, second_w = tree[n][1]

        elif len(tree[n]) == 1:
            first_c, first_w = tree[n][0]

        first_w += getmax(first_c)
        second_w += getmax(second_c)

        maxarr[n] = max(first_w, second_w)
        maxDistance = max(maxDistance, first_w + second_w)
    
    return maxarr[n]

getmax(1)
print(maxDistance)
