import sys
input = sys.stdin.readline

s = [0] * 21
T = int(input())
for i in range(T):
    op = input().split()
    if op[0] == "add":
        s[int(op[1])] = 1
    elif op[0] == "remove":
        s[int(op[1])] = 0
    elif op[0] == "check":
        print(s[int(op[1])])
    elif op[0] == "toggle":
        s[int(op[1])] ^= 1
    elif op[0] == "all":
        for i in range(21):
            s[i] = 1
    else:
        for i in range(21):
            s[i] = 0