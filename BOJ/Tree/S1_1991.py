import sys 
input = sys.stdin.readline
N = int(input())
lchild = [-1] * 26
rchild = [-1] * 26
for _ in range(N):
    root, l, r = input().split()
    c = ord(root) - 65
    if l != '.':
        lchild[c] = ord(l) - 65
    if r != '.':
        rchild[c] = ord(r) - 65

def preorder(i):
    sys.stdout.write(chr(i + 65))
    if lchild[i] != -1:
        preorder(lchild[i])
    if rchild[i] != -1:
        preorder(rchild[i])

def inorder(i):
    if lchild[i] != -1:
        inorder(lchild[i])
    sys.stdout.write(chr(i + 65))
    if rchild[i] != -1:
        inorder(rchild[i])

def postorder(i):
    if lchild[i] != -1:
        postorder(lchild[i])
    if rchild[i] != -1:
        postorder(rchild[i])
    sys.stdout.write(chr(i + 65))
preorder(0)
sys.stdout.write('\n')
inorder(0)
sys.stdout.write('\n')
postorder(0)
