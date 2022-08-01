import sys
input = sys.stdin.readline
A, B = map(int, input().split())

if B * 2 > A:
    B = A - B

ans = 1
for i in range(B):
    ans *= A
    A -= 1

div = 1
while B > 0:
    div *= B
    B -= 1

print(ans // div)