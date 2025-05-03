import sys
input = sys.stdin.readline

S = input().strip()
T = input().strip()

# T에서 S로 추적한다. S 길이와 같아질 때까지 문자열 끝 문자를 검사한다.
# B가 뒤에 나온 경우는 지우고 뒤집는다.
# A가 뒤에 나온 경우는 지운다.

def op(t, length):
    while (len(t) > length):
        if (t[-1] == 'A'):
            t = t[:len(t) - 1]
        else:
            t = t[len(t) - 2::-1]
    return t

trimmed = op(T, len(S))
if trimmed == S:
    print(1)
else:
    print(0)