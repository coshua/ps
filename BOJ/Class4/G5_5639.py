import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

preorder = []

while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postTraverse(arr, root, lo, hi):
    s, e = -1, -1
    for i in range(lo, hi):
        if s == -1 and arr[i] < root:
            s = i
        if e == -1 and arr[i] > root:
            e = i
    if s != -1:
        postTraverse(arr, arr[s], s, e) if e > 0 else postTraverse(arr, arr[s], s, hi)
    if e != -1:
        postTraverse(arr, arr[e], e, hi)
    print(root)

postTraverse(preorder, preorder[0], 0, len(preorder))