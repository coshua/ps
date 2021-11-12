import sys
L, C = list(map(int, input().split()))
s = input().split()
s = sorted(s)

v = ['a', 'e', 'i', 'o', 'u']

def rec(c, id):
    if id == len(s) and len(c) < L:
        return
    if len(c) == L:
        cnt = 0
        vowel = False
        for i in c:
            if i in v:
                vowel = True
        if not vowel:
            return
        for i in c:
            if i not in v:
                cnt += 1
        if cnt >= 2:
            sys.stdout.write(c + "\n")
        return
    else:
        rec(c + s[id], id + 1)
        rec(c, id + 1)

rec("", 0)